#!/usr/bin/env python3
"""Checks text contrast for every palette in one or more CSS files.

Usage: python3 check-contrast.py tokens.css palettes.css [more.css ...]

The first `:root` block is the base palette. Every other block that sets `--paper` is a palette
that overrides the base. Only hex colors are checked. Exits 1 when any pair falls below its minimum.
"""
import re
import sys

# (foreground, background, minimum ratio, what it is for)
PAIRS = [
    ("--ink", "--paper", 7.0, "headings and body"),
    ("--ink-2", "--paper", 4.5, "secondary text"),
    ("--ink-2", "--card", 4.5, "secondary text on cards"),
    ("--ink-2", "--paper-deep", 4.5, "secondary text on deep bands"),
    ("--ink-3", "--paper", 4.5, "small meta text"),
    ("--ink-3", "--card", 4.5, "small meta text on cards"),
    ("--accent", "--paper", 3.0, "large accent text and icons"),
    ("--accent-strong", "--paper", 4.5, "small accent text"),
    ("--accent-strong", "--card", 4.5, "small accent text on cards"),
    ("--accent-ink", "--accent", 3.0, "seals and large text on accent fills"),
    ("--accent-ink", "--accent-strong", 4.5, "button text on accent fills"),
    ("--night-ink", "--night", 7.0, "terminal text"),
]


def luminance(hex_color):
    h = hex_color.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    channels = [int(h[i : i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def ratio(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def blocks(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    for selector, body in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
        tokens = dict(re.findall(r"(--[\w-]+)\s*:\s*(#[0-9a-fA-F]{3,6})\b", body))
        if tokens:
            yield " ".join(selector.split()), tokens


def main(paths):
    base, palettes = None, []
    for path in paths:
        for selector, tokens in blocks(open(path, encoding="utf-8").read()):
            if base is None and selector == ":root":
                base = tokens
            elif "--paper" in tokens:
                palettes.append((selector, tokens))
    if base is None:
        sys.exit("No :root block with hex tokens found.")

    failed = False
    for selector, tokens in [(":root", {})] + palettes:
        merged = {**base, **tokens}
        print(selector)
        for fg, bg, minimum, use in PAIRS:
            if fg not in merged or bg not in merged:
                continue
            r = ratio(merged[fg], merged[bg])
            ok = r >= minimum
            failed |= not ok
            print(f"  {'ok  ' if ok else 'FAIL'} {r:5.2f} ≥ {minimum:<4} {fg} on {bg} ({use})")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main(sys.argv[1:] or sys.exit(__doc__))
