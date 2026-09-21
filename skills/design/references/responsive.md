# Responsive

> **Diverges from upstream Hallmark: T6 port (2026-09-09).** This file has been
> extended with material ported from the upstream packages named in the design
> chain's v4 plan, sections 2.1 to 2.5. Every addition is traceable to a source
> file; where a port collided with a rule already in this file, the conflict is
> resolved in the text and the winner is named. Upstream is no longer the bar
> here, and `verify-design-system.py` records the divergence rather than
> treating it as drift.

Mobile-first. Content-driven breakpoints. No desktop-only interactions.

## Mobile — non-negotiable

Every Hallmark output must render flawlessly at **320 px, 375 px, 414 px, and 768 px** CSS-pixel widths. Eyeball each viewport before marking the output complete:

- No horizontal scroll (slop-test gate 34)
- No clickable text wrapping to two lines (gate 49)
- No image-bearing grid pushing the layout past viewport — use `minmax(0, 1fr)`, never bare `1fr`, on tracks containing images (gate 50)
- Root carries `overflow-x: clip` on both `html` and `body` — never `hidden` (gate 34)
- Display headers wrap inside long words via `overflow-wrap: anywhere; min-width: 0` (gate 51)
- Section heads collapse to one column on mobile across every theme variant — per-theme overrides need a matching mobile rule (gate 52)
- No scroll-jump on radio-tab clicks — radios in normal flow OR JS guard with `focus({ preventScroll: true })` (gate 53)

This is a hard floor, not a wish list. A page that fails any of these on any of those four widths is not done. The slop-test gates listed run automatically — keep this checklist near the screen while building.

## Principles

- Base styles are for the smallest viewport. `min-width` media queries add as you go up. Never `max-width` as the primary direction.
- Breakpoints are where the *content* breaks, not where a device sits. If the headline reflows awkwardly at 720px, that's a breakpoint — regardless of what the Tailwind defaults say.
- Use `pointer` and `hover` media queries instead of width to detect *interaction capability*.
- **Adaptation is not scaling.** The trap is treating a new context as the same design at a different size (impeccable `adapt.md`). Narrow is a different reading posture, a different input method and often a different reason for being on the page. Ask what won't *fit*, what won't *work* (hover states on touch, a 24px target under a thumb), and what is *inappropriate* — a desktop pattern on a phone, a phone pattern on a desk.
- **Never hide core functionality at narrow widths.** If it matters, make it work; `display: none` also still downloads.

## Breakpoints

Three or four, content-driven. As a default:

```css
@media (min-width: 40rem) { /* ~640px — tablet, small laptop */ }
@media (min-width: 60rem) { /* ~960px — desktop baseline */ }
@media (min-width: 90rem) { /* ~1440px — wide */ }
```

Use `rem` so the breakpoints respect the user's font size.

**Name breakpoints by behaviour, not by device.** The name is what a future reader reasons with; `--bp-tablet` tells them nothing about what changes there.

```css
--bp-stack:   0;
--bp-sidebar: 640px;
--bp-columns: 900px;
--bp-wide:    1200px;
```

Find them the way designpowers' `responsive-patterns` does: start at 320px, widen slowly, and where the layout looks wrong, that is the breakpoint.

**Page layout is `@media`; component adaptation is `@container`.**

| Use case | Query |
| --- | --- |
| Page-level layout | `@media` |
| Component adapting to the space it sits in | `@container` |

A component that decides from the viewport is wrong in every column except the one it was written in. The mechanics are in [`layout-and-space.md`](layout-and-space.md) § Grids.

**Content priority at narrow widths** is a decision with four outcomes, and it gets written down: **kept** (essential to the task) · **collapsed** (behind a toggle) · **deferred** (further down the scroll order) · **hidden** (removed — last resort). An undocumented collapse is how a section silently stops existing on mobile.

## The test matrix

Not "check it on a phone". Six points, every time (designpowers `responsive-patterns` § Testing, plus the zoom protocol from `inclusive/responsive-accessibility`):

1. **320px.**
2. **One pixel below each breakpoint** — the widest state of each layout, which is where it is most likely to overflow.
3. **200 % zoom at a 1280px viewport** — the WCAG 1.4.10 reflow condition.
4. **150 % zoom** as the intermediate step. Layouts that survive 100 % and 200 % still break in between, because a two-column grid that has not yet collapsed is at its most cramped there.
5. **Landscape phone.**
6. **A real device** — see § Real devices below.

At every point verify the same four things: no horizontal scroll, no clipped text, no overlapping elements, every interaction still functional.

**Text-spacing survival (WCAG 1.4.12).** The user can override line-height to 1.5×, paragraph spacing to 2×, letter-spacing to 0.12em and word-spacing to 0.16em, and the layout must not lose content or function. What fails it is fixed heights on text containers — use `min-height` — and any container sized to the text it happens to hold today.

## Fluid scaling

Prefer `clamp()` for sizes that change continuously; use media queries for layouts that change discretely.

```css
h1 { font-size: clamp(2.5rem, 4vw + 1rem, 6rem); }
.container { padding-inline: clamp(1rem, 4vw, 4rem); }
```

## Pointer and hover queries

```css
@media (hover: hover) and (pointer: fine) {
  .card:hover { transform: translateY(-2px); }
}
@media (pointer: coarse) {
  .btn { min-height: 48px; }
}
```

Never build a mouse-hover interaction that has no touch equivalent.

**Screen size does not tell you the input method** (impeccable `adapt.md` § Detect input method): a laptop can have a touchscreen and a tablet can have a keyboard. `pointer: coarse` earns a larger target and more spacing between targets; `hover: none` means the hover branch never runs and `:active` has to carry the feedback. Combine them — `@media (hover: hover) and (pointer: fine)` — when the effect only makes sense for a real cursor.

**Thumb zone.** On a phone the bottom half of the screen is reachable and the top corners are not. Primary actions belong in the reachable half; a primary action parked in the top-right of a tall page is a two-handed action.

## Clickable text — never wraps

Buttons, primary nav links, footer links, tab labels, breadcrumbs, and CTAs must read as **single-line affordances at every viewport between 320 px and 1920 px**. A button or nav link wrapping to two lines looks broken — visitors read it as a styling error, not as intentional. The shortest fix is almost always to shorten the label.

```css
/* Affordances are single-line — let the parent reflow, not the label. */
.btn,
.nav__link,
.foot__link,
.cta {
  white-space: nowrap;
}
```

```css
/* When the row can't fit, collapse the row, not the labels. */
@media (max-width: 40rem) {
  .nav__rail { display: none; }      /* desktop nav hides */
  .nav__sheet-toggle { display: grid; } /* mobile menu shows */
}
```

**Order of fixes**, when something does wrap:

1. **Shorten the label.** *"Get started free"* → *"Start free"*. *"Read the documentation"* → *"Read docs"*. *"Schedule a demo"* → *"Book demo"*. Most CTA labels are 30–40 % longer than they need to be.
2. **`white-space: nowrap`** on the affordance, let the parent flex/grid reflow.
3. **`hidden=until-found`** the lowest-priority nav item at narrow widths (it remains in DOM for find-in-page and SEO).
4. **Collapse the nav** into a sheet / off-canvas / disclosure menu below a content-driven breakpoint.

**Never:** let a primary CTA or top-level nav link wrap. Long footer-link labels can wrap *only* in a footer column where wrapping is part of the column's rhythm — not in the inline footer link strip (Ft2).

This is gate **49** in [`slop-test.md`](slop-test.md). Audit any output that ships interactive affordances and confirm none wrap at the breakpoints listed above.

## Viewport units

- Use `dvh` / `svh` / `lvh` instead of `vh` for heights that interact with mobile chrome.
- **`min-height: 100dvh`, never `height: 100vh`,** on a full-height hero. `100vh` is measured against the viewport *without* iOS Safari's address bar, so the section jumps as the bar collapses and expands; `min-height` also lets the section grow when the content inside it does (stitch § viewport stability: *"NEVER use `h-screen` for full-height Hero sections"*). This overrides the `min-height: 100vh` shorthand that shows up in generated markup — and note that the *pattern* stays banned in [`layout-and-space.md`](layout-and-space.md) § Bans regardless of unit: a full-height hero holding one centred sentence is the template, and the correct unit does not redeem it.
- Never `width: 100vw`. Use `width: 100%` with padding; `100vw` includes the scrollbar on desktop and causes overflow.

## Safe areas

For iOS notch / Android navigation bars:

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```

```css
body {
  padding-inline: max(1rem, env(safe-area-inset-left));
  padding-bottom: max(1rem, env(safe-area-inset-bottom));
}
```

## Tables on small screens

Tables of data that won't fit: collapse to cards. Use `display: block` on `<tr>` and `data-label` attributes keyed from `<th>`, rendered via `::before`. Or, the better option: redesign the data for small screens — tables are rarely the right mobile representation.

## Images

- `srcset` with width descriptors for responsive sizing.
- `<picture>` for art direction (different crop at different widths).
- `loading="lazy"` on anything below the fold.
- `width` and `height` attributes on every image, always, to avoid CLS.

## Internationalisation

- Reserve 30–40% extra horizontal space for German, Russian, and Finnish translations.
- Use logical properties: `margin-inline-start`, `padding-block`, `border-inline-end`. Not `margin-left` etc. RTL comes for free.
- Don't hard-code language-specific punctuation or date formats.

## Real devices

DevTools emulation is good for layout and blind to almost everything else: real touch behaviour, actual CPU and memory limits, network latency patterns, font rendering, and the browser chrome and keyboard appearing over the layout. Test on at least one real iPhone and one real Android — and **a cheap Android reveals performance problems no simulator ever will** (impeccable `adapt.md` § Testing).

## Bans

- Desktop-first media queries (`max-width: 768px` as the primary direction).
- `vh` on full-height layouts (use `dvh`).
- `100vw` widths.
- Device-sniffing UA strings instead of feature queries.
- Hover-only interactions.
- Ignoring `prefers-color-scheme` when the app claims to support dark mode.
- Fixed pixel breakpoints that don't respect `rem`.
- Tables of 10+ columns on mobile without a redesign.
- **Sticky or fixed chrome that eats the viewport at zoom.** A header taking 30 % of the viewport at 200 % zoom is a barrier, not a header (`inclusive/responsive-accessibility` § Zoom-safe patterns). Every fixed-position layer is tested at 200 %: the header, the scroll progress bar, the cookie strip, and **the fixed layers of a pinned scroll act** — a pinned act is exactly this pattern, held for the length of a section. Give sticky chrome a zoom-aware height (`clamp()` or a `max-height` in `vh`) or let it un-stick above a zoom threshold. Tooltips and popovers must still be reachable at 200 %, and a modal whose content exceeds the zoomed viewport must scroll.
- Fixed `height` on anything containing text (breaks WCAG 1.4.12) — `min-height` instead.
