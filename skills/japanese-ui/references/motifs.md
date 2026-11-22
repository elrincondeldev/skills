# Motifs

The Japanese ornaments. Each one is decorative: mark it `aria-hidden="true"`, keep it behind or beside content, and use only as many as the page's ornament level allows (see [sections.md](sections.md#blueprints-by-page-type)).

## Contents

- [Hanko seal](#hanko-seal)
- [Brush stroke](#brush-stroke)
- [Enso](#enso)
- [Vertical text](#vertical-text)
- [Sun or moon, and mist](#sun-or-moon-and-mist)
- [Falling particles](#falling-particles)
- [Patterns](#patterns)

## Hanko seal

A rotated square seal in the accent, pressed in after the headline settles. Two to four kana or kanji of the brand, set vertically. Use beside the brand, the hero kicker, the footer wordmark, or as a "recommended" stamp.

```html
<span class="hanko" style="--size: 38px" aria-hidden="true"><span>くも</span></span>
```

```css
.hanko { display: inline-grid; place-items: center; flex: none; width: var(--size); height: var(--size); border-radius: 18%; background: var(--accent); color: var(--accent-ink); box-shadow: inset 0 0 0 2px color-mix(in srgb, var(--accent-ink) 85%, transparent), inset 0 0 0 4px var(--accent); font-family: var(--font-brush); font-size: calc(var(--size) * 0.3); line-height: 1; rotate: -4deg; animation: press 0.9s var(--ease-out) 1.1s both; }
.hanko span { writing-mode: vertical-rl; letter-spacing: -0.05em; }
@keyframes press { from { opacity: 0; scale: 1.8; rotate: -16deg; filter: blur(3px); } 60% { opacity: 1; scale: 0.94; filter: none; } to { scale: 1; rotate: -4deg; } }
```

Adjust `font-size` so the glyphs fill the seal: 0.3 × size fits three kana; use 0.42 for two, 0.6 for one.

## Brush stroke

A hand-drawn underline that paints itself under an accent word. Put it inside the word's `<span class="word accent">`.

```html
<svg class="brush" viewBox="0 0 200 20" preserveAspectRatio="none" aria-hidden="true"><path d="M3 13 C 40 6, 90 5, 130 9 S 185 14, 197 8" /></svg>
```

```css
.brush { position: absolute; left: -2%; bottom: -0.12em; width: 104%; height: 0.32em; overflow: visible; }
.brush path { fill: none; stroke: var(--accent); stroke-width: 5; stroke-linecap: round; opacity: 0.45; stroke-dasharray: 220; stroke-dashoffset: 220; animation: stroke 1.1s var(--ease-out) 1s forwards; }
@keyframes stroke { to { stroke-dashoffset: 0; } }
```

The same path, unanimated, works as a section divider: `width: 120px; height: 12px; margin: 0 auto;`.

## Enso

The open zen circle, drawn when its container is revealed. Place it behind a big word or a portrait.

```html
<svg class="enso" viewBox="0 0 200 200" aria-hidden="true"><path pathLength="1" d="M150 40 C 118 14, 58 18, 34 62 C 12 104, 36 160, 92 170 C 146 180, 184 140, 178 92 C 175 70, 166 56, 156 46" /></svg>
```

```css
.enso { position: absolute; width: clamp(240px, 34vw, 420px); overflow: visible; }
.enso path { fill: none; stroke: var(--accent); stroke-width: 9; stroke-linecap: round; opacity: 0.16; stroke-dasharray: 1; stroke-dashoffset: 1; transition: stroke-dashoffset 2.4s var(--ease-out) 0.3s; }
.is-revealed .enso path, html:not(.js) .enso path { stroke-dashoffset: 0; }
```

## Vertical text

Japanese set top to bottom (`writing-mode: vertical-rl`) in brush type. Use it as texture at very low opacity in a margin, or small and in the accent as a label in a card corner.

```css
.vertical { position: absolute; top: 130px; left: calc(var(--gutter) * 0.4); writing-mode: vertical-rl; font-family: var(--font-brush); font-size: clamp(2.6rem, 5vw, 4.2rem); letter-spacing: 0.3em; color: color-mix(in srgb, var(--ink) 6%, transparent); }
@media (max-width: 1060px) { .vertical { display: none; } }
```

## Sun or moon, and mist

A soft disc that breathes, and bands of mist (kasumi) drifting across a hero backdrop. In the `yoru` palette the sun tokens turn it into the moon.

```html
<span class="sun"></span><span class="mist mist-1"></span><span class="mist mist-2"></span>
```

```css
.sun { position: absolute; top: 9%; right: 12%; width: clamp(220px, 32vw, 460px); aspect-ratio: 1; border-radius: 50%; background: radial-gradient(circle at 38% 36%, var(--sun-1), var(--sun-2) 55%, var(--sun-3)); opacity: 0.55; filter: blur(1px); animation: breathe 9s var(--ease-in-out) infinite alternate; }
@keyframes breathe { to { scale: 1.04; opacity: 0.62; } }
.mist { position: absolute; left: -20%; width: 140%; height: 120px; border-radius: 50%; background: radial-gradient(closest-side, color-mix(in srgb, var(--card) 90%, transparent), transparent); filter: blur(8px); animation: drift 26s var(--ease-in-out) infinite alternate; }
.mist-1 { top: 34%; }
.mist-2 { top: 62%; animation-duration: 34s; animation-direction: alternate-reverse; opacity: 0.8; }
@keyframes drift { from { translate: -6% 0; } to { translate: 6% 0; } }
@media (max-width: 1060px) { .sun { top: 6%; right: -10%; } }
```

## Falling particles

Petals in spring, leaves in autumn, snow in winter, fireflies on summer nights. Generate them with `seeded()` from `assets/reveal.js` at build or render time, so positions are stable between server and client.

```js
const random = seeded(11);
const items = Array.from({ length: 16 }, () => ({
  left: random() * 100, size: 7 + random() * 7, fall: 14 + random() * 12,
  sway: 3 + random() * 3, delay: -random() * 26, alt: random() < 0.35,
}));
// <span class="fall petal" style="left:${left}%; --size:${size}px; --fall:${fall}s; --sway:${sway}s; --delay:${delay}s"><i class="${alt ? "alt" : ""}"></i></span>
```

```css
.particles { position: absolute; inset: 0; overflow: hidden; pointer-events: none; }
.fall { position: absolute; top: -24px; animation: fall var(--fall) linear var(--delay) infinite; }
.fall i { display: block; width: var(--size); height: calc(var(--size) * 0.72); animation: sway var(--sway) var(--ease-in-out) var(--delay) infinite alternate; }
@keyframes fall { to { translate: 0 calc(100vh + 48px); } }
@keyframes sway { from { transform: translateX(-28px) rotate(-30deg) rotateY(0deg); } to { transform: translateX(28px) rotate(40deg) rotateY(180deg); } }

/* Spring: sakura petals. */
.petal i { border-radius: 100% 0 100% 0; background: linear-gradient(135deg, #fff 0%, var(--bloom-pale) 70%); opacity: 0.85; }
.petal i.alt { background: linear-gradient(135deg, #fff 0%, var(--bloom) 70%); }
/* Autumn: leaves in persimmon and red. */
.leaf i { border-radius: 0 100% 0 100%; background: linear-gradient(135deg, var(--bloom), var(--accent)); opacity: 0.8; }
.leaf i.alt { background: linear-gradient(135deg, var(--gold), var(--bloom)); }
/* Winter: snow, round and slow; give it --fall 20–34 s. */
.snow i { height: var(--size); border-radius: 50%; background: radial-gradient(circle, #fff 40%, transparent 72%); opacity: 0.9; }
/* Summer night (yoru): fireflies rising and glowing. */
.firefly { top: auto; bottom: -12px; animation-name: rise-up; }
.firefly i { width: 5px; height: 5px; border-radius: 50%; background: var(--gold); box-shadow: 0 0 12px 3px color-mix(in srgb, var(--gold) 60%, transparent); animation: glow var(--sway) var(--ease-in-out) var(--delay) infinite alternate; }
@keyframes rise-up { to { translate: 0 calc(-100vh - 48px); } }
@keyframes glow { from { opacity: 0.15; transform: translateX(-12px); } to { opacity: 1; transform: translateX(12px); } }

@media (prefers-reduced-motion: reduce) { .particles { display: none; } }
```

## Patterns

Traditional wagara as CSS backgrounds. Use them in small doses: a footer edge, a band behind a quote, a card's top strip, the stage behind an image. Keep the line color faint (`--hairline-strong` or the `--deep` color at 10–15 %).

```css
/* Seigaiha edge: one row of wave arcs, for the ground under a footer or a band's edge. */
.seigaiha-edge { background: radial-gradient(circle at 50% 100%, transparent 40%, color-mix(in srgb, var(--deep) 14%, transparent) 41% 46%, transparent 47%) 0 0 / 28px 14px, var(--paper-deep); }

/* Seigaiha: full overlapping waves. */
.seigaiha {
  --a: var(--paper-deep); --b: color-mix(in srgb, var(--deep) 14%, var(--paper-deep));
  background-color: var(--a);
  background-image:
    radial-gradient(circle at 100% 150%, var(--a) 24%, var(--b) 24% 28%, var(--a) 28% 36%, var(--b) 36% 40%, transparent 40%),
    radial-gradient(circle at 0 150%, var(--a) 24%, var(--b) 24% 28%, var(--a) 28% 36%, var(--b) 36% 40%, transparent 40%),
    radial-gradient(circle at 50% 100%, var(--b) 10%, var(--a) 10% 23%, var(--b) 23% 30%, var(--a) 30% 43%, var(--b) 43% 50%, var(--a) 50% 63%, var(--b) 63% 71%, transparent 71%),
    radial-gradient(circle at 100% 50%, var(--b) 5%, var(--a) 5% 15%, var(--b) 15% 20%, var(--a) 20% 29%, var(--b) 29% 34%, var(--a) 34% 44%, var(--b) 44% 49%, transparent 49%),
    radial-gradient(circle at 0 50%, var(--b) 5%, var(--a) 5% 15%, var(--b) 15% 20%, var(--a) 20% 29%, var(--b) 29% 34%, var(--a) 34% 44%, var(--b) 44% 49%, transparent 49%);
  background-size: 80px 40px;
}

/* Ichimatsu: checkerboard. */
.ichimatsu { --c: var(--tint); background: conic-gradient(var(--c) 25%, transparent 0 50%, var(--c) 0 75%, transparent 0) 0 0 / 24px 24px; }

/* Shippo: interlocking circles. */
.shippo {
  --s: 40px; --r: calc(var(--s) * 0.7071); --c: var(--hairline-strong);
  background:
    radial-gradient(circle var(--r) at 0 0, transparent calc(var(--r) - 1.5px), var(--c) calc(var(--r) - 1.5px) var(--r), transparent var(--r)),
    radial-gradient(circle var(--r) at 100% 0, transparent calc(var(--r) - 1.5px), var(--c) calc(var(--r) - 1.5px) var(--r), transparent var(--r)),
    radial-gradient(circle var(--r) at 0 100%, transparent calc(var(--r) - 1.5px), var(--c) calc(var(--r) - 1.5px) var(--r), transparent var(--r)),
    radial-gradient(circle var(--r) at 100% 100%, transparent calc(var(--r) - 1.5px), var(--c) calc(var(--r) - 1.5px) var(--r), transparent var(--r));
  background-size: var(--s) var(--s);
}
```

Fade a pattern out toward content with a mask: `mask-image: linear-gradient(180deg, #000, transparent);`.
