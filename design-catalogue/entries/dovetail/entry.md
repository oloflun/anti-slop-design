---
title: "Dovetail"
url: https://dovetail.no/
source_url: https://dovetail.no/
captured: 2026-09-04
origin: refero
extract: ok
category: institutional
category2: editorial
family: butter-cream-pill-stack
dna: "Printed-magazine investment memo x stacked pill capability tags"
register: editorial print
grammar: split stage
lane: "A butter-cream canvas holds an oversized left-aligned headline against a monochrome editorial illustration, then the page alternates two-column splits and centred statements, each closed off by a hairline rule instead of a shadow"
mode: persuade
traits: ["72px display, single typeface at three weights", "91px pill radius reserved for capability tags only", "9999px pill for buttons/nav, 16px for cards", "flat, hairline dividers, zero shadow", "monochrome illustration vs colour photography, never mixed", "butter cream + ink black + two neutrals, no accent colour"]
palette: ["#f9e5b1", "#1d1e21", "#fef9f3", "#e5e7eb", "#000000"]
type: ["Lausanne"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
refero: processed/Dovetail.md
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the live
capture. The system has no accent colour at all — butter cream `#f9e5b1`, ink
black `#1d1e21`, warm bone and ash gray carry the entire page. That absence is
itself the brand signal: a venture firm's site with no "brand blue" reads as more
considered, not less finished, because every visual decision is forced onto type,
scale and whitespace instead of a swatch.

A single typeface, Lausanne, runs the whole system at exactly three weights —
400 for body and nav, 600 for subheadings and button labels, 700 reserved
strictly for headlines 28px and above, capped at a 72px ceiling. Letter-spacing
follows classical convention rather than a flat value: it tightens at display
size and opens slightly at small body sizes, which is what keeps a single-family
system from feeling monotonous across six size steps.

Radius is split with unusual discipline into three distinct, non-overlapping
uses: 9999px for buttons and nav items, 16px for photo cards, and a striking 91px
reserved exclusively for the capability pill tags stacked in the right rail —
never applied to a button or a card. Combined with a strict two-mode imagery rule
(monochrome editorial illustration in the hero, full-colour photography in
portfolio/about sections, never overlapping), the page reads as a printed
editorial spread rather than a fundraising deck.

## What to borrow (principle)

- **Ship a system with zero accent colour on purpose.** Two neutrals plus one
  warm canvas and one ink can carry an entire institutional brand without ever
  reaching for a "brand colour."
- **Give one radius value a single, exclusive job.** Reserving the largest pill
  radius (91px) for exactly one component type (capability tags) makes that
  device recognisable on sight, everywhere it appears.
- **Alternate two imagery modes, never mix them in one view.** Monochrome
  illustration for mood, full-colour photography for proof — kept strictly
  separate so each mode stays legible as intentional.
- **Cap display type at a stated maximum.** Declaring "72px is the ceiling —
  nothing goes larger" prevents the usual creep toward ever-bigger hero text.
- **Use letter-spacing that opens at small sizes, tightens at large.** Classical
  tracking (not a flat value) is what keeps both extremes of the type scale
  comfortable to read.

## What to leave

- Zero accent colour is a genuinely hard constraint for a product or marketing
  team that later needs a state colour (success, warning, notification) — the
  system offers no built-in answer for that.
- The 91px-radius pill tags depend on short, punchy labels ("+ Design", "+ Tech");
  longer category names would break the lozenge reading the source describes.
- A single typeface at three weights only works if that face has a genuinely
  distinctive 700 cut — a generic substitute risks the display headlines losing
  the "literary weight" the source attributes to Lausanne specifically.

## Signature move

The stacked capability pill cluster: four or five 91px-radius pill tags
("Capital", "+ Design", "+ Tech", "+ Strategy", "+ Finance") right-aligned in a
tight vertical column with 8-12px gaps, reading as a word-cloud list of
disciplines rather than a conventional tag row.

## Motion

(from designlang extract) Feel reads as mixed, and the page is scroll-linked —
correcting the earlier "no motion tokens" read. Transitions run fast and quiet:
150ms and 200ms, mostly on a standard `cubic-bezier(0.4, 0, 0.2, 1)` curve (10
uses) with a single plain `ease` use elsewhere. No keyframe animations are
confirmed firing, which fits the source's explicit "no z-axis layering" rule —
motion here lives entirely in short property transitions (colour, border,
opacity on hover/focus), not choreographed reveals. (observed in capture) the
live capture confirms a static hero on load with no animated reveal; any
scroll-triggered motion is most plausibly a simple opacity fade given the
"strictly horizontal and two-dimensional" constraint.

| Token | Value | Easing |
|---|---|---|
| xs | 150ms | `cubic-bezier(0.4, 0, 0.2, 1)` |
| sm | 200ms | `cubic-bezier(0.4, 0, 0.2, 1)` / `ease` |

## Brief

Build an institutional investment-firm homepage. Canvas is butter cream `#f9e5b1`
for hero and feature sections; ink black `#1d1e21` carries all text and filled
buttons; warm bone `#fef9f3` lifts card surfaces; ash gray `#e5e7eb` is the only
border colour — no accent hue anywhere. Set the wordmark in Lausanne 700 at
32-48px top-left, nav links at 16px weight 400 top-right, a small geometric brand
glyph far right. Open with a two-column hero: an oversized 72px weight-700
headline with negative tracking on the left, a monochrome line-and-fill editorial
illustration on the right, one dark filled pill button ("Get in touch") below the
headline. Alternate subsequent sections between two-column splits (text-left,
photo-right in a 16px-radius hairline-bordered card) and centred statement
headlines, separated only by 1px ash-gray hairlines — never a shadow, never a
background change. Stack capability tags (91px radius, warm-bone fill, ash-gray
border) in a tight right-aligned column wherever disciplines need listing. Keep
64-96px section gaps.

## Image recipe

Two distinct treatments, never combined in one section: (1) a detailed monochrome
line-and-fill illustration of [SUBJECT] — fine linework, organic shapes, solid
black fills, no colour, no gradient, functioning as a literary counterweight to
type; (2) full-colour documentary photography of [SUBJECT] — natural light team
or workspace shots, unstaged, presented in a 16px-radius card with a 1px hairline
border, no filter or duotone treatment.

## Photo search

Unsplash first, Pexels second.
- "team workspace overhead natural light documentary"
- "office collaboration candid photography"
- "hand-drawn line illustration people editorial"
- "startup team portrait natural light"

## Reference lock

Primary reference/direction: Dovetail — butter-cream editorial investment-firm
page, zero accent colour, stacked 91px pill capability tags.
Preserve (3-5 traits): butter cream `#f9e5b1` canvas with ink black `#1d1e21`
text, no accent colour anywhere; single typeface (Lausanne) at exactly three
weights, 700 capped to headlines 28px and above with a 72px ceiling; three
distinct radius values each reserved for one component (9999px buttons/nav, 16px
cards, 91px capability tags only); 1px ash-gray hairlines as the only section
divider, zero shadows; monochrome illustration and colour photography kept in
strictly separate sections.
Borrow only (1-2): the stacked, right-aligned capability pill cluster; the
custom geometric brand-glyph logomark.
Role rules: 91px radius never applies outside capability tags; illustration and
photography never share a section; body text stays left-aligned below 32px;
weight 700 never sets body copy.
Media strategy: photo:unsplash for documentary team/workspace photography;
supplement with commissioned monochrome line illustration for hero moments — no
stock illustration, no 3D, no icon badges or avatars.
Reject: a second accent colour; a shadow or gradient anywhere; pill radius on
cards or images; center-aligned long-form body text; overlapping/z-axis layered
decoration.
Token commitments: bg `#f9e5b1`, card `#fef9f3`, border `#e5e7eb`, ink `#1d1e21`,
ink-hard `#000000`; display Lausanne 700 at 48-72px/leading 1.0/-0.005 to -0.01em
tracking; body 400 at 20-22px/leading 1.36-1.4; radius 16px cards, 9999px
buttons/nav, 91px capability tags; page max-width 1200px, section gap 64-96px.
