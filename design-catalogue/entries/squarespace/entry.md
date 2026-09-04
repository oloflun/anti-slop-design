---
title: "Squarespace"
url: https://www.squarespace.com
source_url: https://www.squarespace.com
captured: 2026-09-04
origin: refero
extract: ok
category: product-focused
category2: editorial
family: cinematic-monochrome-gallery
dna: "0% colourfulness black/white contrast x whisper-weight 72px cinematic headlines"
register: modern clean
grammar: chaptered editorial
lane: "The page alternates pure black and pure white bands, each announcing itself through scale rather than colour, opening on full-bleed documentary video with a weight-300 headline floating over it and no accent colour anywhere on the marketing surface"
mode: persuade
traits: ["0% colourfulness, pure black/white bands only", "weight 300 at 64-96px, -0.06em tracking", "0px radius on buttons, 100px on pills only", "sharp/soft radius contrast by component type", "full-bleed documentary photo/video hero", "user content is the only source of colour"]
palette: ["#000000", "#ffffff", "#2f2f2f", "#898989", "#dddddd", "#999999"]
type: ["Clarkson", "Clarkson Serif"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
refero: processed/Squarespace.md
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the
live capture. The system declares itself "0% colourfulness by design" — six
tokens total, all black, white, or gray, with the explicit rule that
chromatic colour is never introduced anywhere on the marketing surface. That
absolute constraint is strategic, not merely minimal: because Squarespace
sells websites, reserving all colour for the user-built sites shown in
screenshots and video makes the product itself the only vivid thing on the
page.

Clarkson runs the whole system at three weights with a precise inverse
relationship between size and tracking: whisper-light 300 at 64-96px display
(-0.06em, tight enough to feel "serif-like" in density despite being a
geometric sans), regular 400 for body, and 500 reserved for active nav and
tab labels only. That weight-300-at-display choice, paired with real
documentary photography (a barber cutting hair, "no studio lighting, no
staged perfection") rather than stock imagery, is what keeps a purely
achromatic system from reading as cold.

Radius is split by component type with clear intent: 0px on buttons (a
deliberate sharp contrast to the pill shapes used elsewhere), 8px on cards,
100px reserved exclusively for pill-shaped filter tabs. The source calls this
"sharp-to-soft radius contrast... intentional" — mixing a hard-edged CTA
against soft pill tabs on the same page reads as a considered choice rather
than an inconsistency, because each shape is confined to exactly one role.

## What to borrow (principle)

- **Declare an exact colourfulness percentage and hold to it.** "0%
  colourfulness by design" is a stricter, more auditable commitment than "use
  colour sparingly" — it forces every chromatic need onto user content instead.
- **Reserve all saturated colour for the product being sold.** When the
  product itself is visually rich (websites, in this case), an achromatic
  marketing shell makes that richness the only thing worth looking at.
- **Split radius by component role, not by a single scale.** Sharp buttons
  next to fully-rounded pill tabs reads as intentional when each shape has
  exactly one job, never overlapping.
- **Use real, unstaged documentary footage for the hero.** A candid, non-
  studio moment (rather than posed stock photography) keeps a black-and-white
  page from feeling sterile.
- **Reserve the higher font weight for active states only.** Weight 500
  appearing only on active nav/tab labels, never elsewhere, makes that single
  weight jump meaningful as a state signal.

## What to leave

- Zero chromatic colour anywhere is a genuinely hard constraint for anything
  beyond a confident, established brand — a newer brand may need at least a
  functional colour for error/success states that this system doesn't
  provide a pattern for.
- Weight-300 Clarkson at 64-96px depends on a typeface with a true light cut
  that survives at that scale without becoming illegible; a generic sans
  substitute risks looking merely thin rather than "editorial."
- The sharp-button/soft-pill radius split requires strict component
  discipline — a single rounded button introduced elsewhere would blur the
  otherwise clear role distinction between the two shapes.

## Signature move

The stat display block: a massive number (80-100px, weight 300) on a pure
black band, with the decimal or comma point rendered as a small superscript
element beside the digits — treating a statistic as a typographic sculpture
rather than a data callout.

## Motion

(from designlang extract) Feel reads as mixed, and the page is scroll-linked —
this is a substantially richer system than "no tokens documented" suggested.
Five easing families cover 345+ combined uses across five durations
(100-750ms): two custom curves dominate (216 uses,
`cubic-bezier(0.455, 0.03, 0.515, 0.955)` and `cubic-bezier(0.645, 0.045,
0.355, 1)`), a fast ease-out family follows (67 uses), and — distinctively for
this catalogue — a `steps()` timing function appears 49 times
(`steps(1, start)` / `steps(1)`), the discrete, non-interpolated stepping
usually reserved for frame-by-frame or "ticking" reveals. That's a strong fit
for the stat-display block's massive counted numbers, which would plausibly
tick digit-by-digit rather than tween smoothly. No named keyframes are
confirmed firing, so this choreography lives in property transitions and the
step function, not custom `@keyframes`. (observed in capture) the live
capture confirms the hero displays autoplaying documentary video (a barber
cutting hair, with visible pause/play control) rather than a static
photograph, and shows a distinct second hero variant on reload (two people in
conversation) — the hero video/photo rotates or is served dynamically, and the
documented nav behaviour (transparent over hero, transitions to `#000000` on
scroll) plausibly rides the same fast ease-out family.

| Token | Value | Easing |
|---|---|---|
| xs | 100ms | custom family |
| sm | 200ms | custom family |
| md | 300ms | ease-out family |
| lg | 450ms | ease-out family |
| xl | 750ms | `steps(1, start)` (stat ticking) |

## Brief

Build a website-builder marketing homepage with zero chromatic colour on the
marketing surface. Alternate pure black `#000000` and pure white `#ffffff`
full-bleed section bands — no gray-blend transition, no colour anywhere else
in the system beyond charcoal `#2f2f2f` (filled buttons) and three gray text
tones (`#898989`, `#dddddd`, `#999999`). Open full-bleed on real, unstaged
documentary video or photography with a centred weight-300 headline at
64-96px, tracking -0.06em, and a sharp-cornered (0px radius) ghost button
below it. Follow with a black stat band: three columns of massive weight-300
numbers (80-100px) with small uppercase labels beneath. Drop to white for a
centred section headline, a row of 100px-radius pill filter tabs (inactive
transparent, active `#dddddd` fill), and a 3-4-column card grid of dark,
full-bleed feature cards at 8px radius with white headline/body text and a
bottom-right arrow icon. Cap buttons at 0px radius always; reserve 100px
exclusively for pill tabs; use 8px for cards. No drop shadows, no gradients
beyond one permitted decorative atmospheric wash — never a UI fill.

## Image recipe

Real, unstaged documentary photograph or video of [SUBJECT] — a genuine
moment captured with available or practical light, no studio setup, no posed
perfection, full-bleed with no crop constraint, presented in natural colour
(the imagery itself is the system's only source of chromatic richness against
an otherwise black-and-white UI).

## Photo search

Unsplash first, Pexels second.
- "candid documentary portrait natural light"
- "small business owner at work authentic"
- "creative studio candid moment"
- "artisan craftsperson working documentary"

## Reference lock

Primary reference/direction: Squarespace — cinematic monochrome gallery,
weight-300 display type, zero chromatic colour on the marketing surface.
Preserve (3-5 traits): strictly achromatic palette (black, white, three
grays), 0% colourfulness with all saturated colour confined to user/product
content; Clarkson at weight 300 for display (64-96px, -0.06em tracking),
weight 500 reserved for active states only; radius split by role — 0px
buttons, 8px cards, 100px pill tabs exclusively; full-bleed documentary
(unstaged) photography or video for the hero, never stock.
Borrow only (1-2): the superscript decimal/comma treatment on stat numbers;
the single decorative (non-UI) gradient wash reserved for one atmospheric
moment only.
Role rules: no chromatic colour enters any UI component under any
circumstance; weight 700+ is never used on Clarkson; pill radius (100px)
never applies to a rectangular button or card.
Media strategy: photo:unsplash/video — real, unstaged documentary photography
and video only; no stock-posed imagery, no illustration.
Reject: any chromatic accent colour on a button, badge, or link; box-shadow on
any card; pill radius on rectangular elements; body copy below 14px or
looser than the documented gray hierarchy.
Token commitments: bg `#ffffff`/`#000000`, filled-button `#2f2f2f`, muted
`#898989`, border `#dddddd`, tertiary `#999999`; display Clarkson 300 at
40-72px/leading 0.93-1.0/-0.05 to -0.06em tracking; body 400 at 14-15px;
radius 0px buttons, 8px cards, 100px pills; page max-width 1200px, section
gap 80-120px.
