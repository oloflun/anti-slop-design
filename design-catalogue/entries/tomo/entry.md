---
title: "TOMO"
url: https://tomoseattle.com/
source_url: https://tomoseattle.com/
captured: 2026-09-04
origin: refero
extract: ok
category: hospitality
category2: playful
family: zine-fridge-collage
dna: "Torn-paper sticker navigation x rubber-stamp tomato-red marquee"
register: illustrated dark
grammar: gallery/catalog
lane: "A warm linen page opens on a red marquee ribbon and a viewport-wide serif wordmark, then unfolds as an art-directed collage of overlapping food and street photography with torn-paper sticker labels — no card grid, no menu accordion, no reservation widget"
mode: experience
traits: ["120px wordmark, single line, no padding", "torn-paper sticker nav, not a bar", "one red, marquees and stamps only, never a button", "0px radius, 1px black hairline everywhere", "full-bleed collage, overlapping and rotated", "no max-width container on the homepage"]
palette: ["#eee2d4", "#000000", "#ffffff", "#ff6347", "#efefef"]
type: ["Recife", "Times"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
refero: processed/TOMO.md
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the
live capture. Warm linen `#eee2d4` is the sole canvas — the source states
white is a surface only, never the page background — and tomato red
`#ff6347` is fenced entirely to marquee ribbons and rubber-stamp text, with
an explicit ban on ever using it as a button fill. That restriction is what
keeps the one loud colour reading as printed ink (a stamp, a strip of taped
paper) rather than as UI chrome asking to be clicked.

Recife carries the entire display voice at a single light weight (300),
scaled from the 96px section titles up to a ~120px wordmark that spans the
viewport with no padding — "the heaviest typographic moment on any page."
Times, kept deliberately small at 13px, exists only for functional fine
print, so the system never confuses "large and serif" with "small and
serif" — the two sit at opposite, non-overlapping ends of the scale with
nothing in between.

The layout refuses every restaurant-website convention by name: no
accordion menus, no floating reservation widget, no colour-coded CTAs. Every
photograph sits at 0px radius with only a 1px black hairline (or nothing),
overlapping and bleeding off the frame like a collage taped to cream paper
rather than a card grid — and navigation itself becomes physical objects
(torn-paper stickers with borders) instead of a conventional nav bar.

## What to borrow (principle)

- **Fence the one accent colour to non-interactive surfaces only.** Banning
  red from ever being a button fill — reserving it for marquees and stamps —
  keeps a bold colour readable as ink, not as a call to action.
- **Turn navigation into physical objects, not a bar.** Rendering nav items
  as individual bordered "stickers" with gaps between them, rather than a
  unified nav container, reinforces the collage/zine metaphor structurally.
- **Refuse category-specific web conventions by name.** Explicitly ruling out
  accordion menus and floating reservation widgets forces genuinely different
  solutions instead of defaulting to industry templates.
- **Let photography overlap and bleed instead of gridding it.** Images placed
  at irregular scale and position, allowed to overlap type and each other,
  read as a collage rather than a card layout.
- **Keep a whisper-weight display serif at genuinely extreme scale.** Weight
  300 at 80-120px only works because the size itself carries the authority —
  adding weight would collapse the "elegant, not heavy" effect the source
  names directly.

## What to leave

- Zero max-width container on the homepage is a deliberate full-bleed choice
  that depends on carefully art-directed positioning at every breakpoint; a
  responsive rebuild without that same care will collapse into visual noise.
- Banning shadows, radius, and any elevation language entirely removes a
  common toolkit for signalling "this is clickable" — every interactive
  element instead needs a border or fill-change to read as actionable.
- A single-accent, no-CTA-button system genuinely limits conversion-focused
  design; a reservation flow or checkout would need to invent its own
  affordance language within these constraints.

## Signature move

The rubber-stamp section title: large display text (80-120px) rendered with
a distressed, slightly rotated offset-print texture, floating art-directed
(never centred) over a photography collage — treating a section header as a
printed stamp mark rather than a typeset heading.

## Motion

(from designlang extract) Feel reads as smooth, and the page is scroll-linked.
The system is genuinely minimal: one duration (200ms) on a plain `ease` curve.
Two keyframes are confirmed firing — `fade-pulse-in` (an opacity fade) and
`spin-loading` (a rotate transform) — the latter almost certainly a loading
spinner rather than brand choreography, consistent with the "surfaces never
lift... this is a printed page, not a glass UI" elevation philosophy holding
for everything except a functional loading state. (observed in capture) the
live capture confirms a static, collage-composed layout matching the
structure (marquee, wordmark, sticker nav, photo collage) with no visible
animated reveal beyond that; any interaction state most plausibly relies on a
border or fill swap on the sticker nav, on the same 200ms `ease`.

| Token | Value | Easing |
|---|---|---|
| sm | 200ms | `ease` |
| fade-pulse-in | opacity fade | 1 use |
| spin-loading | rotate transform | loading spinner |

## Brief

Build a full-bleed, collage-style restaurant homepage with no max-width
container. Canvas is warm linen `#eee2d4` everywhere; white is a surface
colour only (sticker fills, reverse-type panels), never the background. Open
with a full-bleed tomato-red `#ff6347` marquee ribbon of uppercase Recife
text, then a single-line wordmark at up to 120px, weight 300, spanning the
viewport with no padding. Render navigation as individual white, 1px-
bordered "sticker" labels with small gaps between them, not a bar. Lay
photography as an art-directed collage — 0px radius, 1px black hairline
borders or none, images overlapping and bleeding off the frame at varying
scale, never in an equal-gutter grid. Float rubber-stamp section titles
(80-120px, rotated 2-4°, distressed texture) over the photo collage,
positioned asymmetrically. Reserve tomato red strictly for marquees and
stamp ink — never a button fill, never a CTA. Keep body/caption text small
(13-26px) and functional. Space sections with 65-115px padding; no shadows,
no gradients, no rounded corners anywhere.

## Image recipe

Tightly cropped documentary photograph of [SUBJECT] — food close-ups or
neighbourhood street scenes shot in natural light with saturated, unfiltered
colour, no soft-focus or styled food-photography lighting, cropped tight and
placed to overlap or bleed off the frame edge as a collage element rather
than a standalone hero image.

## Photo search

Unsplash first, Pexels second.
- "food close up natural light saturated"
- "neighborhood street photography documentary"
- "restaurant interior candid natural light"
- "vintage sign storefront street photography"

## Reference lock

Primary reference/direction: TOMO — zine-collage restaurant homepage, torn-
paper sticker nav, tomato-red marquees and stamps only.
Preserve (3-5 traits): warm linen `#eee2d4` as the sole background, white as
a surface colour only; tomato red `#ff6347` confined to marquee ribbons and
stamp text, never a button or CTA fill; Recife weight 300 for every display
moment (80-120px), Times reserved for 13px fine print only, nothing between;
0px radius and 1px black hairline as the only border language; full-bleed,
overlapping, asymmetric photo collage with no max-width container.
Borrow only (1-2): the rotated rubber-stamp section-title texture; the
torn-paper sticker nav-item treatment.
Role rules: red never fills a button or clickable chip; Times never sets
display text; the layout is never centred by default — composition is
always art-directed and asymmetric.
Media strategy: photo:unsplash — tightly cropped, saturated documentary food
and street photography; no soft-focus styling, no lifestyle staging.
Reject: any filled red CTA button; box-shadow or gradient anywhere; rounded
corners on any element; a centred/gridded card layout; a max-width container
on the homepage.
Token commitments: bg `#eee2d4`, ink `#000000`, surface `#ffffff`, accent
`#ff6347`, neutral `#efefef`; display Recife 300 at 80-120px/leading 1.0;
body 13-26px; radius 0px universal; base spacing unit 6px, section gap
65-115px.
