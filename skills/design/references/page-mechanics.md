# Page mechanics — the settings a page needs before it has any components

Ported from Refero's `craft-details.md` §§ 1, 4, 5, 6
(`upstream/refero/skills/refero-design/references/craft-details.md`), whose own framing
is the reason it exists: *"Implementation details that separate polished products from
rough ones. Most AI models miss these."*

None of this is visible in a screenshot. All of it is visible the moment someone uses
a keyboard, a thumb, or an anchor link. A page can clear every numbered gate and still
feel like a prototype because one of these ten lines is missing.

Scope: **page-level mechanics**. Per-component state design lives in
[`interaction-and-states.md`](interaction-and-states.md); the budget and the loading
order live in [`performance.md`](performance.md); the audit lives in `a11y-audit`.

## 1 · Focus

**`:focus-visible`, not `:focus`.** `:focus` triggers on any focus including a mouse
click, so a plain `:focus` ring means every click leaves a ring behind.
`:focus-visible` fires only for keyboard navigation.

```css
.button:focus-visible { outline: 2px solid var(--color-accent); outline-offset: 2px; }
```

**Never remove focus without replacing it.** `outline: none` on its own breaks keyboard
navigation. If the default ring is wrong for the surface, draw a better one — the
two-ring `box-shadow` form survives a dark ground and a busy background alike:

```css
.button:focus-visible {
  outline: none;
  box-shadow: 0 0 0 2px var(--color-bg), 0 0 0 4px var(--color-accent);
}
```

**`:focus-within` for compound controls.** When a group behaves as one control — an
input with an icon, a search field with a button — focus on any child highlights the
parent, not just the child.

```css
.search-wrapper:focus-within { border-color: var(--color-accent); }
```

The ring's own contrast and offset floor is in
[`interaction-and-states.md`](interaction-and-states.md); this section is about which
selector carries it.

## 2 · Touch and mobile

```css
/* Removes the 300 ms tap delay. */
* { touch-action: manipulation; }

/* Set it intentionally. Do not just disable it. */
button, a { -webkit-tap-highlight-color: rgba(0, 0, 0, 0.1); }

/* No scroll chaining out of a sheet into the page behind it. */
.modal, .drawer, .sheet { overscroll-behavior: contain; }
```

**Autofocus is desktop-only.** On mobile it opens the keyboard unexpectedly and eats
the fold. One primary input per page at most, and it has to be justified — "the page is
a search page" is a reason, "there is an input" is not.

## 3 · Anchors and long pages

**Every `[id]` gets a `scroll-margin-top`** whenever the page has fixed or sticky
chrome, or the anchor target lands underneath it:

```css
[id] { scroll-margin-top: 80px; } /* fixed header height + buffer */
```

**`content-visibility: auto` is the CSS-only virtualisation.** Upstream reaches for it
for lists of 50+ items; on a long scroll page it is the cheapest single win there is
(see [`performance.md`](performance.md) § 2). It needs an intrinsic size or it will
shift:

```css
.long-list, .below-fold-act {
  content-visibility: auto;
  contain-intrinsic-size: 0 50px;   /* estimated item / section height */
}
```

**No layout reads during render.** Reading `offsetHeight` (or any geometry) while
producing markup forces a synchronous layout recalculation. Let CSS do it, or observe
it with a `ResizeObserver` and write the result once. The scroll-handler form of the
same mistake — and why the engine's passive-listener + one-rAF shape is the model — is
in [`performance.md`](performance.md) § 3.

## 4 · What the head needs

```html
<link rel="preconnect" href="https://cdn.example.com">
<link rel="preload" href="/fonts/display.woff2" as="font" type="font/woff2" crossorigin>
```

`preconnect` to any origin the fold actually needs; `preload` the critical woff2 —
`as`, `type` and `crossorigin` are all required or the file is fetched twice.
**Which** file and **how many** is a budget question, and
[`performance.md`](performance.md) § 2 is the authority: the display weight that
appears in the fold, and only that one.

## 5 · Elements that behave like what they are

- **A div with a click handler is not a button.** `<button>` for actions, `<a href>`
  for navigation. Everything the browser gives free — focus, Enter, Space, middle-click,
  open-in-new-tab, the screen-reader role — is what you are re-implementing badly.
- **A custom interactive element needs its keyboard half.** `role`, `tabindex="0"`, and
  a `keydown` handler that treats **Enter and Space** as the click, with
  `preventDefault()` so Space does not scroll the page.
- **Heading levels do not skip.** `h1 → h2 → h3`, never `h1 → h4`. One `<h1>` per page.
  Mechanically covered by `detect.mjs`'s `skipped-heading` and `heading-rhythm`.
- **Async updates get announced.** A toast, a validation message, or anything that
  appears without a navigation goes in a live region:

```html
<div role="status" aria-live="polite">…</div>
```

## What does not port

Refero's `craft-details.md` is written for React, and four of its passages are
framework mechanics rather than page mechanics. They are deliberately not restated
here: list virtualisation via `virtua`/`react-window` (the CSS form above is what a
single-file HTML page uses), uncontrolled inputs to avoid per-keystroke re-renders, the
`ResizeObserver` hook shape, and the `beforeunload` unsaved-changes warning. Read them
in the upstream file when the target is a React codebase. § 2 (Forms) and § 3 (Images)
are not here either — forms belong to
[`interaction-and-states.md`](interaction-and-states.md), images to
[`performance.md`](performance.md) § 2, which already carries the
`width`/`height`/`decoding`/`fetchpriority` set with the chain's own budget attached.

## Related

[`interaction-and-states.md`](interaction-and-states.md) ·
[`performance.md`](performance.md) · [`responsive.md`](responsive.md) ·
[`numbers.md`](numbers.md) · `a11y-audit` ·
`upstream/refero/skills/refero-design/references/craft-details.md` §§ 1, 4, 5, 6.
