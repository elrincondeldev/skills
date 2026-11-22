# Page sections and blueprints

Page-level building blocks, then how to combine them for different kinds of site. All use the role tokens; decorations come from [motifs.md](motifs.md). Breakpoints: 1060 px (tablet), 760 px (nav), 560 px (phone).

## Contents

- [Blueprints by page type](#blueprints-by-page-type)
- [Section header](#section-header)
- [Pill header](#pill-header)
- [Hero](#hero)
- [Page header](#page-header)
- [Split row](#split-row)
- [Card grid](#card-grid)
- [Ruled grid](#ruled-grid)
- [Pricing](#pricing)
- [Interlude](#interlude)
- [Flow](#flow)
- [Stats row](#stats-row)
- [Terminal](#terminal)
- [Footer](#footer)
- [App shell](#app-shell)

## Blueprints by page type

Starting points, not templates: drop, reorder and repeat sections to fit the content.

| Page type | Ornament | Sections |
| --- | --- | --- |
| Product or marketing landing | balanced–festive | pill header → hero → card grid → interlude → ruled grid → flow or stats → CTA band → footer |
| Restaurant, shop, studio, hotel | balanced | pill header → hero with photo → split rows (story, craft) → card grid (menu or products, with prices) → interlude → note with hours and address → footer |
| Portfolio | quiet–balanced | pill header → hero with name and one line → card grid of works (figures) → split row (about) → contact form → footer |
| Blog index / article | quiet | pill header → page header → card list or [prose](components.md#prose) → pager → footer |
| Docs | quiet | pill header → app shell with sidebar → prose with notes, tables and code → footer |
| App, dashboard, settings | quiet | app shell → page header → stats row, tables, forms, tabs; no ambient motion |
| Event or launch | festive | hero with date in brush numerals → stats (date, place, seats) → flow (schedule) → pricing (tickets) → FAQ → footer |

Ornament levels: **quiet** is grain, hairlines, numerals and kanji in eyebrows, no ambient loops. **Balanced** adds a hanko, brush underlines, an enso and one ambient loop. **Festive** adds the sun or moon, mist, falling particles and patterns, still at most two loops per viewport.

## Section header

```html
<header class="head center" data-reveal>
  <p class="eyebrow">
    <span class="numeral" aria-hidden="true">三</span>
    <span class="rule" aria-hidden="true"></span>
    <span>Features</span>
    <span class="kanji" lang="ja">特徴</span>
  </p>
  <h2>Built to stay out of <em>your way</em>.</h2>
  <p class="lede">Optional one- or two-sentence lede.</p>
</header>
```

```css
.head { display: flex; flex-direction: column; gap: 18px; max-width: 760px; margin-bottom: clamp(44px, 6vw, 72px); }
.head.center { align-items: center; margin-inline: auto; text-align: center; }
.eyebrow { display: inline-flex; align-items: center; gap: 12px; color: var(--ink-3); font-size: 0.82rem; letter-spacing: 0.16em; text-transform: uppercase; }
.eyebrow .numeral, .eyebrow .kanji { font-family: var(--font-brush); letter-spacing: 0; text-transform: none; }
.eyebrow .numeral { color: var(--accent); font-size: 1.5rem; line-height: 1; }
.eyebrow .kanji { color: var(--ink-2); font-size: 1.05rem; }
.eyebrow .rule { width: 28px; height: 1px; background: var(--hairline-strong); }
.head .lede { color: var(--ink-2); font-size: 1.1rem; }
```

Start-aligned (`.head` without `.center`) suits content and app pages.

## Pill header

Fixed, transparent at the top, a frosted pill after 24 px of scroll.

```html
<header class="site-header" data-header>
  <a class="brand" href="/"><!-- logo or hanko --><span class="wordmark">kumo</span></a>
  <nav class="links" aria-label="Main"><a href="#menu">Menu</a><a href="#story">Story</a></nav>
  <a class="btn btn-ink btn-sm" href="#book">Book</a>
</header>
<script>
  const header = document.querySelector("[data-header]");
  const update = () => header?.classList.toggle("is-scrolled", scrollY > 24);
  addEventListener("scroll", update, { passive: true });
  update();
</script>
```

```css
.site-header { position: fixed; inset: 14px var(--gutter) auto; z-index: 50; display: flex; align-items: center; gap: 20px; max-width: var(--max); margin: 0 auto; padding: 8px 10px 8px 14px; border: 1px solid transparent; border-radius: 999px; transition: background 0.5s var(--ease-out), border-color 0.5s var(--ease-out), box-shadow 0.5s var(--ease-out); }
.site-header.is-scrolled { background: var(--glass); border-color: var(--hairline); box-shadow: 0 16px 40px -28px rgb(var(--shadow-rgb) / 0.35); backdrop-filter: blur(16px) saturate(150%); -webkit-backdrop-filter: blur(16px) saturate(150%); }
.brand { display: flex; align-items: center; gap: 8px; text-decoration: none; }
.wordmark { font-family: var(--font-display); font-weight: 700; font-size: 1.3rem; letter-spacing: 0.02em; }
.links { display: flex; gap: 2px; margin-left: auto; }
.links a { padding: 6px 14px; border-radius: 999px; color: var(--ink-2); font-size: 0.93rem; text-decoration: none; transition: color 0.3s, background 0.3s; }
.links a:hover, .links a[aria-current] { color: var(--ink); background: var(--tint); }
.btn-sm { min-height: 36px; padding: 6px 16px; font-size: 0.93rem; }
@media (max-width: 760px) { .links { display: none; } .site-header > .btn { margin-left: auto; } }
```

Below 760 px, when the links matter (more than a landing's anchors), replace them with a menu button that opens a [dialog](components.md#dialog) listing them.

## Hero

Two columns (copy | visual) over a painted backdrop. Split the headline into words in markup so each rises on its own; give the accent word a brush stroke. The visual is whatever proves the promise: a product shot, a photo, a demo, an illustration.

```html
<section class="hero" id="top">
  <div class="backdrop" aria-hidden="true"><!-- sun, mist, vertical kanji, particles: see motifs.md --></div>
  <div class="container grid">
    <div class="copy">
      <p class="kicker"><!-- hanko --><span><span lang="ja">雲</span> · <i>kumo</i>, notes that float</span></p>
      <h1>
        <span class="word" style="--i:0"><span>Your</span></span>
        <span class="word" style="--i:1"><span>notes,</span></span>
        <span class="word accent" style="--i:2"><span>floating</span><!-- brush stroke --></span>
        <span class="word" style="--i:3"><span>above</span></span>
        <span class="word" style="--i:4"><span>it all.</span></span>
      </h1>
      <p class="lede">Two or three sentences in plain words.</p>
      <div class="cta"><a class="btn btn-ink" href="#start">Start free</a><a class="ink-link" href="#more">See how <span aria-hidden="true">↓</span></a></div>
      <ul class="facts"><li>No account needed</li><li>Works offline</li></ul>
    </div>
    <figure class="visual"><!-- visual --><figcaption>One line on what it shows.</figcaption></figure>
  </div>
</section>
```

```css
.hero { position: relative; isolation: isolate; padding-block: 140px 96px; min-height: 100svh; display: grid; align-items: center; overflow: clip; }
.backdrop { position: absolute; inset: 0; z-index: -1; background: radial-gradient(60% 50% at 85% 10%, var(--bloom-soft), transparent 70%), radial-gradient(50% 60% at 0% 100%, var(--mist), transparent 70%), linear-gradient(180deg, color-mix(in srgb, var(--card) 50%, var(--paper)), var(--paper)); }
.hero .grid { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.08fr); align-items: center; gap: clamp(40px, 6vw, 88px); }
.hero .copy { display: flex; flex-direction: column; gap: 28px; }
.kicker { display: inline-flex; align-items: center; gap: 14px; color: var(--ink-2); font-size: 0.95rem; animation: rise 1.2s var(--ease-out) both; }
.kicker [lang="ja"] { font-family: var(--font-display); color: var(--ink); }
.word { position: relative; display: inline-block; overflow: hidden; padding-bottom: 0.08em; margin-bottom: -0.08em; vertical-align: top; }
.word > span { display: inline-block; animation: word 1.3s var(--ease-out) both; animation-delay: calc(0.15s + var(--i) * 0.055s); }
@keyframes word { from { translate: 0 105%; rotate: 4deg; } }
.accent { overflow: visible; color: var(--accent); }
.accent > span { clip-path: inset(0 0 -0.2em 0); }
.hero .lede { max-width: 33em; color: var(--ink-2); font-size: 1.12rem; animation: rise 1.2s var(--ease-out) 0.7s both; }
.cta { display: flex; flex-wrap: wrap; align-items: center; gap: 16px 26px; animation: rise 1.2s var(--ease-out) 0.85s both; }
.facts { display: flex; flex-wrap: wrap; gap: 8px 24px; color: var(--ink-3); font-size: 0.9rem; animation: rise 1.2s var(--ease-out) 1s both; }
.facts li { display: flex; align-items: center; gap: 9px; }
.facts li::before { content: ""; width: 6px; height: 6px; border-radius: 50%; background: var(--leaf); }
.visual { min-width: 0; animation: float-in 1.6s var(--ease-out) 0.45s both; }
.visual img { display: block; width: 100%; border-radius: var(--radius); box-shadow: 0 0 0 8px var(--halo), var(--shadow-lift); }
.visual figcaption { margin-top: 18px; color: var(--ink-3); font-size: 0.85rem; text-align: center; }
@keyframes float-in { from { opacity: 0; translate: 0 40px; scale: 0.97; } }
@keyframes rise { from { opacity: 0; translate: 0 18px; } }
@media (max-width: 1060px) {
  .hero { padding-block: 130px 72px; min-height: 0; }
  .hero .grid { grid-template-columns: minmax(0, 1fr); }
  .hero .copy { align-items: center; text-align: center; }
  .cta, .facts { justify-content: center; }
  .visual { width: 100%; max-width: 720px; margin-inline: auto; }
}
```

A one-column variant (centered copy, visual below) suits portfolios and events.

## Page header

The hero's quiet sibling for inner pages, articles and app screens: eyebrow, title, lede, a hairline below.

```css
.page-head { display: grid; gap: 14px; padding-block: 140px 40px; border-bottom: 1px solid var(--hairline); }
.page-head h1 { font-size: clamp(2.1rem, 4vw, 3.2rem); }
.page-head p { max-width: 40em; color: var(--ink-2); }
```

## Split row

Text beside an image, alternating sides row by row, with a vertical kanji in the gutter. Good for story, craft, process.

```html
<div class="split" data-reveal>
  <figure><img src="…" alt="…" /></figure>
  <div class="text"><span class="side-kanji" lang="ja" aria-hidden="true">職人</span><h3>Made by hand</h3><p>…</p></div>
</div>
```

```css
.split { display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr); align-items: center; gap: clamp(32px, 6vw, 88px); }
.split + .split { margin-top: clamp(64px, 9vw, 120px); }
.split:nth-of-type(even) figure { order: 2; }
.split img { display: block; width: 100%; aspect-ratio: 4 / 3; object-fit: cover; border-radius: var(--radius); box-shadow: var(--shadow-soft); }
.split .text { position: relative; display: grid; gap: 14px; }
.split h3 { font-size: clamp(1.5rem, 2.6vw, 2rem); }
.split p { color: var(--ink-2); }
.side-kanji { position: absolute; top: 0; left: -2.2em; writing-mode: vertical-rl; font-family: var(--font-brush); font-size: 1.2rem; letter-spacing: 0.2em; color: var(--accent); opacity: 0.7; }
@media (max-width: 860px) { .split { grid-template-columns: minmax(0, 1fr); } .split:nth-of-type(even) figure { order: 0; } .side-kanji { display: none; } }
```

## Card grid

Raised paper cards for a handful of showcase items: features, menu dishes, products, works. 4 → 2 → 1 columns (use 3 for wider content). Optional vertical kanji in the corner and a round stage for an icon or illustration.

```html
<ul class="cards">
  <li data-reveal><article class="card">
    <span class="card-kanji" lang="ja" aria-hidden="true">抹茶</span>
    <span class="stage"><!-- icon or image --></span>
    <h3>Matcha</h3><p>One or two short sentences.</p>
  </article></li>
</ul>
```

```css
.cards { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 18px; }
.cards > li { display: flex; }
.card { flex: 1; position: relative; display: flex; flex-direction: column; align-items: center; gap: 10px; padding: 34px 22px 26px; border: 1px solid var(--hairline); border-radius: var(--radius); background: var(--card); box-shadow: var(--shadow-soft); text-align: center; transition: translate 0.7s var(--ease-out), box-shadow 0.7s var(--ease-out); }
.card:hover { translate: 0 -6px; box-shadow: var(--shadow-lift); }
.card h3 { font-size: 1.3rem; }
.card p { color: var(--ink-2); font-size: 0.94rem; line-height: 1.6; }
.card-kanji { position: absolute; top: 18px; right: 18px; writing-mode: vertical-rl; font-family: var(--font-brush); font-size: 1.05rem; color: var(--accent); opacity: 0.75; }
.stage { display: grid; place-items: center; width: 132px; aspect-ratio: 1; margin-bottom: 6px; border-radius: 50%; overflow: hidden; background: radial-gradient(circle, var(--night) 0 58%, transparent 59%), conic-gradient(from 200deg, var(--bloom), var(--accent-soft), var(--mist), var(--bloom)); box-shadow: inset 0 0 0 6px var(--card); transition: rotate 1.2s var(--ease-out); }
.card:hover .stage { rotate: 6deg; }
@media (max-width: 1060px) { .cards { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (max-width: 560px) { .cards { grid-template-columns: minmax(0, 1fr); } }
```

For photos, drop the stage and put the image at the top of the card, full width, with the card's top radius. For prices, add `<p class="price">¥1,200</p>` styled `font-family: var(--font-display); font-size: 1.2rem; color: var(--ink);`.

## Ruled grid

For longer lists, no cards: a grid divided by hairlines on a `--paper → --paper-deep → --paper` band; items lighten on hover.

```css
.band { background: linear-gradient(180deg, var(--paper), var(--paper-deep) 50%, var(--paper)); }
.ruled { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); border-top: 1px solid var(--hairline-strong); }
.ruled > li { display: flex; border-bottom: 1px solid var(--hairline-strong); }
.ruled > li:not(:nth-child(3n + 1)) { border-left: 1px solid var(--hairline-strong); }
.ruled article { flex: 1; display: flex; flex-direction: column; gap: 10px; padding: 34px 30px 38px; transition: background 0.6s var(--ease-out); }
.ruled article:hover { background: color-mix(in srgb, var(--card) 70%, transparent); }
.ruled p { color: var(--ink-2); font-size: 0.97rem; }
@media (max-width: 1060px) {
  .ruled { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .ruled > li:not(:nth-child(3n + 1)) { border-left: 0; }
  .ruled > li:nth-child(even) { border-left: 1px solid var(--hairline-strong); }
}
@media (max-width: 640px) {
  .ruled { grid-template-columns: minmax(0, 1fr); }
  .ruled > li:nth-child(even) { border-left: 0; }
  .ruled article { padding: 28px 4px 30px; }
}
```

## Pricing

Card grid with three columns; the recommended plan gets the accent border, a warm wash and a hanko reading おすすめ (recommended).

```css
.plans { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px; align-items: stretch; }
.plan { position: relative; display: flex; flex-direction: column; gap: 14px; padding: 34px 28px; border: 1px solid var(--hairline); border-radius: var(--radius); background: var(--card); box-shadow: var(--shadow-soft); }
.plan.featured { border-color: var(--accent-line); background: linear-gradient(180deg, color-mix(in srgb, var(--accent-soft) 35%, var(--card)), var(--card)); }
.plan .hanko { position: absolute; top: -14px; right: 22px; }
.plan .amount { font-family: var(--font-display); font-size: 2.6rem; font-weight: 600; line-height: 1; }
.plan .amount small { color: var(--ink-3); font-family: var(--font-body); font-size: 0.9rem; font-weight: 400; }
.plan ul { flex: 1; }
@media (max-width: 1060px) { .plans { grid-template-columns: minmax(0, 1fr); max-width: 480px; margin-inline: auto; } }
```

Put a monthly/yearly [tab](components.md#tabs) above, and use `.dots` for the plan's list.

## Interlude

A centered breath between sections: one big brush word inside an enso, a dictionary line, one sentence, a bloom wash. See [motifs.md](motifs.md#enso) for the enso.

```html
<section class="interlude" aria-labelledby="word">
  <div class="container inner">
    <div class="title" data-reveal><!-- enso svg --><h2 id="word" lang="ja">間</h2></div>
    <p class="reading" data-reveal><i>ma</i> · <span>noun</span> · the pause between things</p>
    <p class="text" data-reveal>One sentence tying the word to the site.</p>
  </div>
</section>
```

```css
.interlude { position: relative; isolation: isolate; overflow: hidden; padding-block: clamp(96px, 12vw, 150px); background: radial-gradient(70% 60% at 50% 100%, color-mix(in srgb, var(--bloom) 35%, transparent), transparent 70%), linear-gradient(180deg, var(--paper), var(--bloom-soft) 60%, var(--paper)); }
.interlude .inner { display: flex; flex-direction: column; align-items: center; text-align: center; }
.interlude .title { position: relative; display: grid; place-items: center; }
.interlude h2 { position: relative; font-family: var(--font-brush); font-weight: 400; font-size: clamp(4.5rem, 13vw, 9.5rem); line-height: 1.2; letter-spacing: 0.04em; padding-block: clamp(30px, 5vw, 60px); }
.reading { margin-top: 8px; font-family: var(--font-mono); font-size: 0.92rem; color: var(--accent-strong); }
.reading span { color: var(--ink-3); }
.interlude .text { max-width: 30em; margin-top: 16px; color: var(--ink-2); font-size: 1.15rem; }
```

## Flow

Steps or parts joined by dotted wires with accent packets travelling along them; the highlighted node gets the accent border. Use for "how it works", a process or a schedule. Goes vertical below 1060 px.

```html
<ol class="flow" data-reveal>
  <li class="node"><span class="tag">step 1</span><b>Choose</b><span class="text">…</span></li>
  <li class="wire" aria-hidden="true"><i></i><i></i><i></i></li>
  <li class="node main"><span class="tag">step 2</span><b>Brew</b><span class="text">…</span></li>
  <li class="wire" aria-hidden="true"><i></i><i></i><i></i></li>
  <li class="node"><span class="tag">step 3</span><b>Enjoy</b><span class="text">…</span></li>
</ol>
```

```css
.flow { display: grid; grid-template-columns: 1fr 96px 1.1fr 96px 1fr; align-items: center; }
.node { position: relative; display: flex; flex-direction: column; gap: 6px; padding: 30px 26px 26px; border: 1px solid var(--hairline-strong); border-radius: var(--radius); background: var(--card); box-shadow: var(--shadow-soft); }
.node.main { border-color: var(--accent-line); background: linear-gradient(180deg, color-mix(in srgb, var(--accent-soft) 40%, var(--card)), var(--card)); }
.node b { font-family: var(--font-display); font-size: 1.35rem; }
.node .text { color: var(--ink-2); font-size: 0.94rem; }
.node .tag { position: absolute; top: -12px; left: 20px; }
.node.main .tag { border-color: var(--accent-line); color: var(--accent-strong); }
.wire { position: relative; height: 2px; background: radial-gradient(circle, var(--hairline-strong) 1px, transparent 1.5px) 0 50% / 8px 2px repeat-x; }
.wire i { position: absolute; top: -3px; left: 0; width: 8px; height: 8px; border-radius: 50%; background: var(--accent); box-shadow: 0 0 0 4px var(--accent-glow); animation: packet 2.8s var(--ease-in-out) infinite; }
.wire i:nth-child(2) { animation-delay: 0.93s; }
.wire i:nth-child(3) { animation-delay: 1.86s; }
@keyframes packet { from { left: 0; opacity: 0; } 20%, 80% { opacity: 1; } to { left: calc(100% - 8px); opacity: 0; } }
@keyframes packet-down { from { top: 0; opacity: 0; } 20%, 80% { opacity: 1; } to { top: calc(100% - 8px); opacity: 0; } }
@media (max-width: 1060px) {
  .flow { grid-template-columns: minmax(0, 1fr); max-width: 480px; margin-inline: auto; }
  .wire { width: 2px; height: 56px; margin: 8px auto; background: radial-gradient(circle, var(--hairline-strong) 1px, transparent 1.5px) 50% 0 / 2px 8px repeat-y; }
  .wire i { top: 0; left: -3px; animation-name: packet-down; }
}
```

`.tag` comes from [components.md](components.md#tags-and-status).

## Stats row

```html
<dl class="stats" data-reveal><div><dt>1962</dt><dd>the year we opened</dd></div>…</dl>
```

```css
.stats { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); margin: 0; border-top: 1px solid var(--hairline-strong); }
.stats div { padding: 26px 22px 0; }
.stats div + div { border-left: 1px solid var(--hairline); }
.stats dt { font-family: var(--font-display); font-size: clamp(1.9rem, 3.4vw, 2.7rem); font-weight: 600; line-height: 1.1; }
.stats dd { margin: 6px 0 0; color: var(--ink-3); font-size: 0.92rem; }
@media (max-width: 1060px) { .stats { grid-template-columns: repeat(2, minmax(0, 1fr)); } .stats div:nth-child(3) { border-left: 0; } .stats div:nth-child(n + 3) { padding-top: 22px; } }
```

In dashboards, put each stat in a `.card` instead and add a `.status` line under the number.

## Terminal

For developer products only: the page's dark island, framed by a halo.

```html
<div class="terminal" data-reveal>
  <div class="bar"><span class="lights" aria-hidden="true"><i></i><i></i><i></i></span><span>~</span></div>
  <pre><code><span class="prompt">$ </span>npx your-tool init
<span class="ok">✓ ready</span>
<span class="dim">a quieter line</span></code></pre>
</div>
```

```css
.terminal { position: relative; border-radius: var(--radius); background: var(--night); color: var(--night-ink); overflow: hidden; box-shadow: 0 0 0 8px var(--halo), 0 50px 100px -50px rgb(var(--shadow-rgb) / 0.65); }
.terminal .bar { position: relative; display: flex; justify-content: center; align-items: center; height: 38px; border-bottom: 1px solid rgba(255, 255, 255, 0.06); color: var(--night-dim); font-size: 0.8rem; }
.lights { position: absolute; left: 16px; display: flex; gap: 6px; }
.lights i { width: 11px; height: 11px; border-radius: 50%; background: #ff5f57; }
.lights i:nth-child(2) { background: #febc2e; }
.lights i:nth-child(3) { background: #28c840; }
.terminal pre { margin: 0; min-height: 200px; padding: 24px; overflow-x: auto; font: 400 0.92rem/1.8 var(--font-mono); }
.terminal .prompt { color: var(--bloom); }
.terminal .ok { color: #9fd08a; }
.terminal .dim { color: var(--night-dim); }
@media (max-width: 560px) { .terminal pre { font-size: 0.78rem; padding: 18px 16px; } }
```

## Footer

Patterned ground (optionally with a procession of the site's own icons walking across it), a huge Mincho wordmark with vertical kanji and a hanko, underlined links, a muted line of small print.

```css
.footer { position: relative; margin-top: 40px; background: var(--paper-deep); }
.ground { height: 14px; border-top: 1px solid var(--hairline-strong); /* seigaiha edge, see motifs.md */ }
.footer .inner { display: flex; flex-direction: column; align-items: center; gap: 24px; padding-block: 64px 56px; text-align: center; }
.mark { position: relative; display: flex; align-items: center; gap: 18px; }
.footer .wordmark { font-family: var(--font-display); font-weight: 700; font-size: clamp(4rem, 12vw, 8.5rem); line-height: 1; letter-spacing: -0.03em; }
.mark .vertical-kanji { writing-mode: vertical-rl; font-family: var(--font-brush); font-size: clamp(1.1rem, 2.4vw, 1.7rem); letter-spacing: 0.2em; color: var(--ink-2); }
.mark .hanko { position: absolute; top: -6px; right: -46px; animation: none; }
.footer nav { display: flex; flex-wrap: wrap; justify-content: center; gap: 8px 26px; }
.smallprint { max-width: 560px; color: var(--ink-3); font-size: 0.82rem; }
@media (max-width: 560px) { .mark .hanko { display: none; } }
```

Footer links use `.ink-link`. For apps and docs, a single hairline row with the wordmark and links is enough.

## App shell

For dashboards, tools and docs: a quiet sidebar on paper-deep, content on paper, no ambient motion.

```css
.shell { display: grid; grid-template-columns: 248px minmax(0, 1fr); min-height: 100svh; }
.sidebar { position: sticky; top: 0; height: 100svh; display: flex; flex-direction: column; gap: 4px; padding: 24px 14px; border-right: 1px solid var(--hairline); background: var(--paper-deep); overflow-y: auto; }
.sidebar .group { margin: 18px 12px 6px; color: var(--ink-3); font-size: 0.75rem; letter-spacing: 0.14em; text-transform: uppercase; }
.sidebar a { display: flex; align-items: center; gap: 10px; padding: 7px 12px; border-radius: 10px; color: var(--ink-2); text-decoration: none; transition: background 0.3s, color 0.3s; }
.sidebar a:hover { background: var(--tint); color: var(--ink); }
.sidebar a[aria-current="page"] { background: var(--card); color: var(--ink); box-shadow: inset 2px 0 0 var(--accent), var(--shadow-soft); }
.main { padding: 32px clamp(20px, 4vw, 56px) 80px; }
@media (max-width: 860px) { .shell { grid-template-columns: minmax(0, 1fr); } .sidebar { position: static; height: auto; flex-direction: row; overflow-x: auto; border-right: 0; border-bottom: 1px solid var(--hairline); } .sidebar .group { display: none; } }
```

Use the start-aligned section header with its numeral and kanji as the page title, and the brand's hanko at the top of the sidebar.
