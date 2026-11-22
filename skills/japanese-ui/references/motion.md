# Motion

Motion in this style is slow, soft and finishes early. It uses long durations on `--ease-out` (`cubic-bezier(0.16, 1, 0.3, 1)`), so most of the movement happens in the first third and the rest is settling. App screens and docs use only hover and focus transitions, and marketing pages add entrances and ambience.

## Timings

| Kind | Duration | Easing | Example |
| --- | --- | --- | --- |
| Color and background hovers | 0.3 s | default | nav links, table rows |
| Lifts, underlines, button hovers | 0.5–0.7 s | `--ease-out` | cards rise 6 px, `.ink-link` draws |
| Entrances and reveals | 1.1–1.3 s | `--ease-out` | `rise`, `word`, `[data-reveal]` |
| Slow drawings | 1.6–2.4 s | `--ease-out` | enso, hero visual floating in |
| Ambient loops | 9–34 s | `--ease-in-out` or linear | sun breathing, mist, particles |

## First-view choreography

Play the entrance once on load, staggered so the eye travels from top to bottom:

1. The kicker rises (0 s).
2. The headline words rise from below their line and untilt, `0.15 s + i × 0.055 s` each.
3. The visual floats in (0.45 s).
4. The lede (0.7 s), CTA (0.85 s) and facts (1 s) rise.
5. The brush stroke under the accent word draws (1 s), and the hanko presses in (1.1 s).

Use `animation-fill-mode: both` so elements stay hidden until their delay and keep their final state. On inner pages, apply only step 4 to the page header.

## Reveal on scroll

Each block below the first view uses `data-reveal`. It starts 28 px lower, transparent and blurred by 6 px, and settles over 1.1 s once 12 % of it is in view. `assets/reveal.js` sets `--stagger` for each sibling (capped at 6), so grid items arrive 90 ms apart. Listen for the `revealed` event to start a section's own animation, such as an enso stroke or a typing terminal.

The hidden states apply only under `.js`, so the page is complete without scripts. Skip `data-reveal` on content people come to work with (tables, forms, docs body), because it should be there at once.

## Hover

Hover moves things a little and slowly. Cards rise with `translate: 0 -6px` and `--shadow-lift`, and icons rise 4 px. Stages rotate 6° while their content counter-rotates. Buttons lift 2 px and press to `scale(0.98)` on `:active`. Links draw a 1 px accent underline from the left.

## Ambient loops

Balanced pages get at most one ambient loop and festive pages two per viewport, and quiet pages get none. Keep them decorative and `aria-hidden`. Give neighbors different durations or negative delays so they never move in lockstep.

## Reduced motion

The reset in `assets/tokens.css` cuts every animation and transition to near zero and shows `[data-reveal]` immediately. Also hide purely ambient layers (particles, processions) with `display: none` under `prefers-reduced-motion: reduce`, because a frozen petal looks like a stain.
