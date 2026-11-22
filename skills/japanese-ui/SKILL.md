---
name: japanese-ui
description: Builds websites and web UIs in a calm Japanese aesthetic, with washi-paper and sumi-ink colors, one vermilion or seasonal accent, Mincho display type, brush-kanji numerals, hanko seals, enso circles, wagara patterns, seasonal palettes (spring, summer, autumn, winter, night) and slow ease-out motion. Works for any page type, such as landings, blogs, docs, shops, restaurants, portfolios, dashboards and forms. Use when the user asks for a Japanese-style, washi, zen or wabi-sabi website or component, wants a page "like Tomari", or wants to restyle an existing site with that look.
license: MIT
metadata:
  author: elrincondeldev
  version: "0.2.0"
---

# Japanese UI

A design system for building any website or web app in a quiet Japanese aesthetic, first worked out on the [Tomari site](https://github.com/elrincondeldev/tomari/tree/main/site). The site keeps its own content and structure and takes on this look: paper and ink, one accent, generous space, small Japanese details and motion that settles slowly. A good result reads as calm and crafted at first glance and shows its Japanese details on a second look. It works at 375 px, without JavaScript and with reduced motion.

## Principles

Let these guide every choice the recipes don't cover:

- **Ma (間), space as material.** Few elements per view, wide margins, sections that breathe (`.section` padding is 96–168 px).
- **Kanso (簡素), simplicity.** One idea per block. Hairlines instead of boxes, little chrome.
- **Shibui (渋い), restraint.** Paper and ink tones carry the page, and the accent is reserved for what matters most: the accent word in a headline, numerals, seals, focus rings, the active state and the single most important action.
- **Fukinsei (不均整), asymmetry.** Offset heroes, vertical kanji in a margin, a seal tilted −4°.
- **Wabi-sabi (侘寂), texture and imperfection.** Paper grain, hand-drawn brush strokes, an enso left open.

## The language

- **Color roles.** `--paper`, `--paper-deep` and `--card` for surfaces. `--ink`, `--ink-2` and `--ink-3` for text. `--accent` for large accents, `--accent-strong` for small accent text and accent fills. `--bloom`, `--leaf`, `--deep`, `--mist` and `--gold` appear only as soft washes and small dots. `--night` is the one dark island, used for code and terminals.
- **Type.** Shippori Mincho for headings, Zen Maru Gothic for body text (17 px / 1.75), Yuji Syuku brush type only for kanji and numerals, JetBrains Mono for code.
- **Shape.** Cards with a 22 px radius and a soft warm shadow. Pill-shaped buttons, nav, tabs and tags. A grain overlay on the whole page.
- **Japanese details.** A brush numeral (一 二 三 …) and a kanji name in each section eyebrow, decorative vertical text, a hanko seal by the brand, `lang="ja"` on every Japanese string.
- **Motion.** Slow (0.6–1.3 s) on `--ease-out`, staggered. Elements rise, unblur and press in. Ambient loops are slow and decorative.
- **Voice.** Short, warm, concrete copy. Each headline holds one idea with one `<em>` accent word, followed by a lede in `--ink-2`.

## 1. Read the target

Find the stack (plain HTML, Astro, React, Vue, Svelte…), where global CSS lives and how components are written. From the request or the existing site, establish the page type(s), the real content and the one thing a visitor should do or understand. When restyling an existing site, keep its content, structure and behavior, and change only its look.

Done when you know the stack, the files to write, the page type of each page and its list of sections.

## 2. Choose palette and ornament

1. **Palette.** Pick a season from [assets/palettes.css](assets/palettes.css) to match the brand's mood: `haru` (spring, vermilion and sakura, the default), `natsu` (summer, indigo and water), `aki` (autumn, maple and persimmon), `fuyu` (winter, crimson and snow), `yoru` (night, a dark theme) or `auto` (haru by day, yoru when the system is dark). For a brand color, copy the closest palette and change its accent and bloom tokens.
2. **Ornament level.** Choose quiet, balanced or festive from the blueprint table in [references/sections.md](references/sections.md#blueprints-by-page-type). Apps, docs and forms stay quiet, and marketing pages can go further.

Done when the palette and ornament level are chosen. When you made a custom palette, done also requires `python3 scripts/check-contrast.py assets/tokens.css <your-palette.css>` to pass.

## 3. Lay the foundation

1. Copy [assets/tokens.css](assets/tokens.css), and [assets/palettes.css](assets/palettes.css) when you use a palette other than haru, into the project's global styles. Set `data-palette` on `<html>`.
2. Load the fonts as in [assets/head.html](assets/head.html). The brush font is requested with `&text=` set to the exact glyphs the page uses, so it costs a few KB.
3. Copy [assets/reveal.js](assets/reveal.js) into the project and call its `revealOnScroll()` once from a module script at the end of `<body>`. The `js` class from the head script gates every hidden state, so the page stays complete without JavaScript.

Done when an empty page shows the palette's paper with grain, Mincho headings and Zen Maru body text.

## 4. Choose the Japanese words

Give each section a numeral and a kanji name, and give the brand a hanko text. Use only words you are certain of: [references/kanji.md](references/kanji.md) lists common ones. When nothing fits, ask the user or use the numeral alone. Add every glyph to the brush font request.

Done when every section has `{ numeral, kanji, label }` and every glyph is in the font request.

## 5. Compose the pages

Start from the blueprint for the page type, then build with:

- [references/sections.md](references/sections.md) for page-level blocks: headers, heroes, split rows, grids, pricing, interlude, flow, stats, footer and the app shell.
- [references/components.md](references/components.md) for UI primitives: buttons, forms, tags, tabs, accordion, table, note, dialog, pagination and prose.
- [references/motifs.md](references/motifs.md) for ornaments: hanko, brush stroke, enso, vertical text, sun or moon, particles and patterns.

Translate the recipes to the project's component syntax, and when a need isn't covered, design it from the principles and tokens. While composing:

- Wrap content in `.container` and each band in `.section`. Shift backgrounds with soft vertical gradients between `--paper`, `--paper-deep` and a bloom wash, not hard color blocks.
- Use only role tokens for color, so the palette can change in one place.
- Add `data-reveal` to repeated items so siblings stagger in.
- Mark decorations `aria-hidden="true"` and keep real content in the DOM as text.
- Place random decorations with `seeded()` so every render matches.

Done when every planned section exists with real content and no placeholder text.

## 6. Tune motion

Follow [references/motion.md](references/motion.md): entrance choreography for the first view, reveal on scroll below it, slow hover lifts, and no more ambient loops than the ornament level allows.

Done when the first view plays its entrance once, sections reveal as they scroll in, and with reduced motion the page is static and fully visible.

## 7. Check it

Open the pages in a browser (a preview tool or dev server) and check:

1. At 375, 768 and 1280 px there is no horizontal scroll, grids and heroes collapse cleanly, and nav and sidebars adapt.
2. The accent appears only on accents, text uses ink tokens, and the contrast script passes for the palettes in use.
3. Every interactive element shows the accent focus ring and is reachable by keyboard. Form errors are tied to their fields.
4. With JavaScript disabled, every `data-reveal` element is visible.
5. With reduced motion, particles are gone and nothing animates.
6. With `yoru` or `auto`, the dark theme has no leftover light surfaces or hard-coded colors.

Done when every check passes. Fix and re-check any that don't.
