# UI components

Interface primitives for any page: apps, forms, docs, shops. Plain HTML and CSS on the role tokens from `assets/tokens.css`; port them to the project's component syntax.

## Contents

- [Buttons](#buttons)
- [Copy command](#copy-command)
- [Form fields](#form-fields)
- [Tags and status](#tags-and-status)
- [Tabs](#tabs)
- [Accordion](#accordion)
- [Table](#table)
- [Note (fusen)](#note-fusen)
- [Dialog](#dialog)
- [Pagination and breadcrumbs](#pagination-and-breadcrumbs)
- [Prose](#prose)

## Buttons

Pills. The primary action is ink on paper; use the accent fill only for the one action a page exists for (buy, book, confirm), at most once per view.

```html
<a class="btn btn-ink" href="…">Get started</a>
<button class="btn btn-line" type="button">Learn more</button>
<button class="btn btn-accent" type="submit">Reserve a table</button>
```

```css
.btn { display: inline-flex; align-items: center; justify-content: center; gap: 10px; min-height: 44px; padding: 10px 22px; border: 1px solid transparent; border-radius: 999px; font-weight: 500; text-decoration: none; cursor: pointer; transition: transform 0.5s var(--ease-out), box-shadow 0.5s var(--ease-out), background 0.3s, border-color 0.3s; }
.btn:hover { transform: translateY(-2px); }
.btn:active { transform: translateY(0) scale(0.98); }
.btn-ink { background: var(--ink); color: var(--paper); box-shadow: 0 18px 40px -18px rgb(var(--shadow-rgb) / 0.55); }
.btn-ink:hover { box-shadow: 0 26px 50px -20px rgb(var(--shadow-rgb) / 0.6); }
.btn-line { border-color: var(--hairline-strong); background: var(--card); color: var(--ink); }
.btn-line:hover { border-color: var(--ink-3); }
.btn-accent { background: var(--accent-strong); color: var(--accent-ink); box-shadow: 0 18px 40px -18px var(--accent-line); }
.btn:disabled { opacity: 0.45; pointer-events: none; }
```

For a quiet text action use `.ink-link`.

## Copy command

For developer products: the install command as the primary button. Clicking copies it and the hint flips to the accent.

```html
<button class="copy-cmd" type="button" data-copy="npx your-tool init" aria-label="Copy npx your-tool init">
  <span class="prompt" aria-hidden="true">$</span><code>npx your-tool init</code>
  <span class="hint" aria-live="polite">copy</span>
</button>
<script>
  for (const b of document.querySelectorAll("[data-copy]")) {
    b.addEventListener("click", async () => {
      await navigator.clipboard.writeText(b.dataset.copy);
      const hint = b.querySelector(".hint");
      b.classList.add("copied"); hint.textContent = "copied";
      setTimeout(() => { b.classList.remove("copied"); hint.textContent = "copy"; }, 1600);
    });
  }
</script>
```

```css
.copy-cmd { display: inline-flex; align-items: center; gap: 12px; padding: 14px 14px 14px 24px; border: 0; border-radius: 999px; background: var(--ink); color: var(--paper); font-family: var(--font-mono); font-size: 1rem; cursor: pointer; box-shadow: 0 18px 40px -18px rgb(var(--shadow-rgb) / 0.55); transition: transform 0.5s var(--ease-out), box-shadow 0.5s var(--ease-out); }
.copy-cmd:hover { transform: translateY(-2px); }
.copy-cmd .prompt { color: var(--bloom); }
.copy-cmd code { font-size: inherit; }
.copy-cmd .hint { padding: 4px 12px; border-radius: 999px; background: color-mix(in srgb, var(--paper) 14%, transparent); font-family: var(--font-body); font-size: 0.8rem; letter-spacing: 0.04em; transition: background 0.3s, color 0.3s; }
.copy-cmd.copied .hint { background: var(--accent-strong); color: var(--accent-ink); }
```

## Form fields

Soft paper fields with a hairline border, the accent for focus and errors, labels in `--ink-2`.

```html
<form class="form">
  <label class="field">
    <span class="label">Name</span>
    <input type="text" name="name" autocomplete="name" required />
  </label>
  <label class="field">
    <span class="label">Message</span>
    <textarea name="message" rows="4"></textarea>
    <span class="hint">We answer within two days.</span>
  </label>
  <label class="field is-invalid">
    <span class="label">Email</span>
    <input type="email" name="email" aria-describedby="email-error" aria-invalid="true" />
    <span class="error" id="email-error">Write an address like name@example.com.</span>
  </label>
  <label class="check"><input type="checkbox" /> Send me the seasonal letter</label>
  <button class="btn btn-ink" type="submit">Send</button>
</form>
```

```css
.form { display: grid; align-content: start; gap: 20px; max-width: 520px; }
.field { display: grid; gap: 6px; }
.label { color: var(--ink-2); font-size: 0.9rem; font-weight: 500; }
.field input, .field textarea, .field select { width: 100%; min-height: 46px; padding: 10px 16px; border: 1px solid var(--hairline-strong); border-radius: var(--radius-sm); background: var(--card); transition: border-color 0.3s, box-shadow 0.4s var(--ease-out); }
.field textarea { resize: vertical; line-height: 1.6; }
.field :is(input, textarea, select):focus { outline: none; border-color: var(--accent); box-shadow: 0 0 0 4px var(--accent-glow); }
.field ::placeholder { color: var(--ink-3); }
.hint { color: var(--ink-3); font-size: 0.85rem; }
.error { color: var(--accent-strong); font-size: 0.85rem; }
.is-invalid :is(input, textarea, select) { border-color: var(--accent-line); }
.check { display: flex; align-items: center; gap: 10px; color: var(--ink-2); }
.check input, .form input[type="radio"] { width: 18px; height: 18px; accent-color: var(--accent); }
```

## Tags and status

```html
<span class="tag">v2.1</span>
<span class="tag tag-accent">new</span>
<span class="status" data-tone="ok">Open today</span>
```

```css
.tag { display: inline-flex; align-items: center; padding: 1px 10px; border: 1px solid var(--hairline-strong); border-radius: 999px; background: var(--paper); color: var(--ink-3); font-family: var(--font-mono); font-size: 0.75rem; }
.tag-accent { border-color: var(--accent-line); color: var(--accent-strong); }
.status { display: inline-flex; align-items: center; gap: 8px; color: var(--ink-2); font-size: 0.9rem; }
.status::before { content: ""; width: 7px; height: 7px; border-radius: 50%; background: var(--ink-3); }
.status[data-tone="ok"]::before { background: var(--leaf); box-shadow: 0 0 0 4px var(--leaf-glow); }
.status[data-tone="warn"]::before { background: var(--gold); }
.status[data-tone="alert"]::before { background: var(--accent); box-shadow: 0 0 0 4px var(--accent-glow); }
```

## Tabs

A pill segmented control; the selected tab is ink. Wire `aria-selected` and arrow keys per the ARIA tabs pattern.

```html
<div class="tabs" role="tablist">
  <button role="tab" aria-selected="true">Monthly</button>
  <button role="tab" aria-selected="false">Yearly</button>
</div>
```

```css
.tabs { display: inline-flex; gap: 2px; padding: 4px; border: 1px solid var(--hairline); border-radius: 999px; background: var(--card); }
.tabs [role="tab"] { padding: 6px 16px; border: 0; border-radius: 999px; background: none; color: var(--ink-2); font-size: 0.93rem; cursor: pointer; transition: background 0.3s, color 0.3s; }
.tabs [role="tab"]:hover { background: var(--tint); color: var(--ink); }
.tabs [role="tab"][aria-selected="true"] { background: var(--ink); color: var(--paper); }
```

## Accordion

For FAQs. Hairline rules, a brush numeral per item, a plus that turns into a cross.

```html
<div class="faq">
  <details>
    <summary><span class="numeral" aria-hidden="true">一</span>Do you ship abroad?</summary>
    <p>Yes, to most countries, in five to ten days.</p>
  </details>
</div>
```

```css
.faq { max-width: 760px; margin-inline: auto; border-top: 1px solid var(--hairline-strong); }
.faq details { border-bottom: 1px solid var(--hairline-strong); }
.faq summary { display: flex; align-items: baseline; gap: 18px; padding: 22px 4px; font-family: var(--font-display); font-size: 1.2rem; font-weight: 600; cursor: pointer; list-style: none; }
.faq summary::-webkit-details-marker { display: none; }
.faq summary::after { content: "+"; margin-left: auto; color: var(--ink-3); font-family: var(--font-body); font-weight: 400; transition: rotate 0.5s var(--ease-out); }
.faq details[open] summary::after { rotate: 45deg; color: var(--accent); }
.faq .numeral { color: var(--accent); font-family: var(--font-brush); font-weight: 400; }
.faq details p { padding: 0 4px 24px 42px; color: var(--ink-2); }
```

## Table

```css
.table { width: 100%; border-collapse: collapse; font-size: 0.95rem; }
.table th { padding: 10px 14px; border-bottom: 1px solid var(--hairline-strong); color: var(--ink-3); font-size: 0.75rem; font-weight: 500; letter-spacing: 0.12em; text-align: left; text-transform: uppercase; }
.table td { padding: 14px; border-bottom: 1px solid var(--hairline); color: var(--ink-2); }
.table td:first-child { color: var(--ink); font-weight: 500; }
.table .num { font-family: var(--font-mono); font-variant-numeric: tabular-nums; text-align: right; }
.table tbody tr { transition: background 0.3s; }
.table tbody tr:hover { background: var(--tint); }
```

Wrap wide tables in a `div` with `overflow-x: auto` so the page never scrolls sideways.

## Note (fusen)

An aside on a slip of paper with a folded corner. Use for tips, warnings and editor's notes; set `data-tone="alert"` for warnings.

```html
<aside class="note"><b>Tip</b><p>Steep the leaves for two minutes, no more.</p></aside>
```

```css
.note { position: relative; display: grid; gap: 4px; padding: 18px 22px; border-radius: var(--radius-sm) 0 var(--radius-sm) var(--radius-sm); background: linear-gradient(225deg, transparent 14px, var(--paper-deep) 0); color: var(--ink-2); }
.note::before { content: ""; position: absolute; top: 0; right: 0; width: 20px; height: 20px; background: linear-gradient(225deg, transparent 50%, var(--hairline-strong) 0); border-bottom-left-radius: 4px; }
.note b { color: var(--ink); font-family: var(--font-display); }
.note[data-tone="alert"] { background: linear-gradient(225deg, transparent 14px, var(--accent-soft) 0); }
```

## Dialog

```css
dialog.sheet { width: min(520px, calc(100vw - 32px)); padding: 32px; border: 1px solid var(--hairline); border-radius: var(--radius); background: var(--card); color: var(--ink); box-shadow: var(--shadow-lift); }
dialog.sheet::backdrop { background: color-mix(in srgb, var(--paper) 60%, transparent); backdrop-filter: blur(8px); }
dialog.sheet[open] { animation: rise 0.6s var(--ease-out); }
@keyframes rise { from { opacity: 0; translate: 0 18px; } }
```

Close with a `.btn-line` and keep the primary action on the right.

## Pagination and breadcrumbs

```css
.pager { display: flex; justify-content: center; gap: 6px; }
.pager a { display: grid; place-items: center; min-width: 40px; height: 40px; border-radius: 999px; color: var(--ink-2); text-decoration: none; transition: background 0.3s; }
.pager a:hover { background: var(--tint); }
.pager [aria-current="page"] { background: var(--ink); color: var(--paper); }
.crumbs { display: flex; flex-wrap: wrap; gap: 8px; color: var(--ink-3); font-size: 0.88rem; }
.crumbs li + li::before { content: "·"; margin-right: 8px; }
.crumbs a { color: inherit; text-decoration: none; }
.crumbs a:hover { color: var(--ink); }
```

## Prose

Long-form text: articles, docs, menus with descriptions. A reading column, Mincho headings with a short accent rule, Japanese corner brackets on quotes, and ruby for readings.

```html
<article class="prose">
  <p class="meta">Essay · 8 min</p>
  <h1>On rest</h1>
  <p>Body text…</p>
  <h2>A place to perch</h2>
  <blockquote><p>The best work happens between the work.</p></blockquote>
  <p>The word <ruby>止<rt>と</rt></ruby>まり means…</p>
  <figure><img src="…" alt="…" /><figcaption>Caption.</figcaption></figure>
</article>
```

```css
.prose { max-width: var(--measure); margin-inline: auto; }
.prose > * + * { margin-top: 1.25em; }
.prose .meta { color: var(--ink-3); font-size: 0.85rem; letter-spacing: 0.12em; text-transform: uppercase; }
.prose h1 { margin-top: 0.3em; }
.prose h2 { margin-top: 2.2em; font-size: clamp(1.6rem, 3vw, 2.1rem); }
.prose h2::before { content: ""; display: block; width: 28px; height: 2px; margin-bottom: 18px; background: var(--accent); }
.prose h3 { margin-top: 1.8em; }
.prose p, .prose li { color: var(--ink-2); }
.prose a { color: var(--ink); text-decoration-color: var(--accent-line); text-underline-offset: 4px; }
.prose a:hover { text-decoration-color: var(--accent); }
.prose ul { padding-left: 0; }
.prose ul li { display: flex; gap: 12px; }
.prose ul li::before { content: ""; flex: none; width: 6px; height: 6px; margin-top: 0.75em; border-radius: 50%; background: var(--leaf); }
.prose blockquote { position: relative; padding: 8px 0 8px 40px; font-family: var(--font-display); font-size: 1.3rem; line-height: 1.6; }
.prose blockquote::before { content: "「"; position: absolute; left: 0; top: -2px; color: var(--accent); font-size: 1.8rem; }
.prose blockquote p { color: var(--ink); }
.prose rt { color: var(--ink-3); font-size: 0.55em; }
.prose figure img { width: 100%; border-radius: var(--radius); }
.prose figcaption { margin-top: 10px; color: var(--ink-3); font-size: 0.85rem; text-align: center; }
.prose pre { padding: 20px 22px; border-radius: var(--radius-sm); background: var(--night); color: var(--night-ink); overflow-x: auto; font: 400 0.9rem/1.7 var(--font-mono); }
.prose :not(pre) > code { padding: 2px 7px; border-radius: 6px; background: var(--tint); color: var(--ink); }
```
