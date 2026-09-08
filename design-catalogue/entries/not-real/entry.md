---
title: "Not Real"
url: https://notreal.tv/
source_url: https://notreal.tv/
captured: 2026-09-04
origin: refero
extract: ok
category: portfolio
category2: editorial
family: vellum-gallery-zpattern
dna: "Didone gallery-label serif x chromatic CGI on a three-colour vellum canvas"
register: editorial print
grammar: gallery/catalog
lane: "A warm off-white vellum canvas holds a staggered, asymmetric grid of full-bleed CGI renders at native resolution, each captioned below by an em-dash-split serif title and a slash-delimited sans metadata line, with a rotated running-text strip pinned to the right margin"
mode: persuade
traits: ["three colours total, chromatic content only in artwork", "0px radius everywhere, zero elevation", "em-dash title / italic subtitle pairing", "staggered vertical offset grid, no rigid rows", "vertical rotated metadata strip", "single weight (400) on both typefaces"]
palette: ["#292a2c", "#f2f2f2", "#000000"]
type: ["ogg", "telegraf"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
refero: processed/Not Real.md
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the live
capture. The system runs on exactly three colours — ink charcoal, vellum canvas,
full black — and states its rule in the plainest possible terms: "the more vivid
the artwork, the more monochrome and silent the surrounding UI must be." Because
the studio's own CGI renders already carry violets, pinks, greens and golds at
full saturation, a chromatic UI would compete with the work it exists to show;
three neutrals let every render register at full intensity.

Both typefaces run at a single weight (400) with no bold anywhere, so hierarchy
is built entirely from size, letterform contrast, and tracking direction. ogg, a
high-contrast didone-flavoured serif, announces each project at up to 55px with
aggressive negative tracking; telegraf, a geometric sans, documents it below with
tracking that runs the opposite direction — widening as size decreases, which is
what keeps 15px metadata tags legible as deliberate small caps rather than merely
cramped. The two faces meet at 55px exactly once, a rare moment the source calls
out specifically, where the serif announces the project name and the sans
describes it at identical scale.

Zero elevation and zero radius across the entire system push all of the page's
perceived depth into a single mechanism: the intentional vertical offset of
images within the asymmetric grid. A left-column tile starting 200px from the
top against a right-column neighbour starting at 80px creates the z-pattern
staggering that would otherwise need a shadow to achieve — flatness is a
deliberate "anti-SaaS" signal, the source states, meant to read as a printed
gallery catalog rather than a software interface.

## What to borrow (principle)

- **State the colour rule as an inverse relationship.** "The more vivid the
  artwork, the more silent the UI" is a portable principle for any portfolio
  built around saturated work.
- **Run both typefaces at one weight only.** Removing bold as an option forces
  every hierarchy decision onto size and letterform, which reads as more
  editorial than weight-driven emphasis.
- **Track two typefaces in opposite directions.** A serif that tightens at scale
  paired with a sans that widens at small sizes gives each face a distinct,
  legible signature.
- **Use vertical offset instead of shadow to create depth in a grid.** Staggering
  tile positions achieves a layered, z-pattern read without any elevation
  effects.
- **Give metadata a place to live that isn't a caption.** A rotated running-text
  strip pinned to the viewport edge (project ID, timestamp) behaves like a
  printed magazine running header rather than UI chrome.

## What to leave

- Zero border-radius and zero shadow across an entire portfolio is a genuinely
  narrow constraint — any borrowed component with a rounded corner or a card
  shadow will immediately look foreign against this system.
- The em-dash title/italic-subtitle pairing depends on every project having a
  two-part name; a single-word project title loses the device's rhythm entirely.
- A three-colour, artwork-only-colour rule assumes a deep, consistently
  high-quality CGI/photography library; a thin portfolio would leave long
  stretches of the page with nothing but grey type.

## Signature move

The vertical rotated running-text strip: project reference codes and timestamps
(e.g. "BA 08:00AM — MAD 01:00PM") set in telegraf, rotated 90° and pinned
absolutely along the right viewport edge — a printed-magazine running header
that persists independent of scroll content.

## Motion

(from designlang extract) Feel reads as mechanical — a fitting label for a
system this flat — and the page is scroll-linked. Interactions are dominated by
plain `linear` easing (12 uses) at 200-300ms, with a small custom
`cubic-bezier(0.4, 0, 0.22, 1)` set and a couple of `ease` uses; there is no
spring or overshoot anywhere, matching the "anti-elevation" register. One
keyframe is confirmed firing: `moveSlideshow`, a slide-x transform driving a
horizontal slideshow/carousel — the one place the page does move content across
the screen rather than staggering it in a static grid. A generic `spin`
keyframe exists in the stylesheet but is not confirmed in use. (observed in
capture) given the explicit anti-elevation, anti-shadow stance, hover states on
inline links most plausibly thicken the existing 1px underline border rather
than introducing colour or movement, consistent with the "border is the visual
weight" component note.

| Token | Value | Easing |
|---|---|---|
| sm | 200ms | `linear` |
| md | 300ms | `linear` / `cubic-bezier(0.4, 0, 0.22, 1)` |
| moveSlideshow | slide-x transform | 1 use |

## Brief

Build a CGI/design-studio portfolio homepage. Canvas is vellum `#f2f2f2`
throughout, text is ink charcoal `#292a2c`, with full black `#000000` reserved
for underline borders and rare dark inversions — no fourth colour, and no
chromatic UI colour at all. Set the wordmark and every project title in ogg at a
single weight (400): 55px with -0.036em tracking for the largest headlines, 26px
with -0.02em for pull-quotes, always split as "Title — Subtitle" with the
subtitle in italic. Use telegraf for everything else — nav, body, metadata tags —
with tracking that widens as size decreases (0.002em at 55px up to 0.04em at
15px). Lay out a two-column asymmetric grid with no max-width constraint: large
project tiles and compact secondary tiles at native aspect ratio, zero
border-radius, no shadow, positioned with deliberate vertical offset between
neighbouring columns to create a staggered z-pattern. Below each image, a caption
block: em-dash title/subtitle in ogg, then category tags in telegraf separated by
" / ". Pin a rotated (90°) metadata strip along the right viewport edge. Keep
120px section gaps and let the page flow to the viewport edges with no card
containers anywhere.

## Image recipe

High-production CGI render of [SUBJECT] — glossy or metallic abstract or product-
adjacent form (crystal, liquid simulation, branded object), studio-lit with soft
gradient or bokeh backdrop in saturated, unexpected colour (violet, pink, gold,
green), photorealistic rendering quality, sharp focus on the subject with the
background allowed to blur, presented uncropped at native resolution with no
overlay or duotone treatment.

## Photo search

Unsplash first, Pexels second.
- "abstract 3D render glossy metallic gradient background"
- "crystal formation studio lighting colourful"
- "liquid simulation render vivid colour"
- "product CGI render pastel gradient background"

## Reference lock

Primary reference/direction: Not Real — three-colour vellum gallery grid,
chromatic content confined entirely to CGI artwork.
Preserve (3-5 traits): exactly three colours (`#292a2c` ink, `#f2f2f2` vellum,
`#000000` black), no chromatic UI colour under any circumstance; both typefaces
locked to weight 400, no bold anywhere; 0px radius and zero elevation on every
element, depth achieved only through staggered image offset; em-dash title /
italic-subtitle pairing on every project heading; telegraf tracking widening as
size decreases, ogg tracking tightening as size increases.
Borrow only (1-2): the rotated 90° running-text metadata strip on the right
margin; the " / "-delimited category tag format.
Role rules: no fourth colour is ever introduced; ogg never sets body copy or
metadata; a filled CTA button is never created — links stay text with a 1px
border only.
Media strategy: CGI/3D render or high-production photography, always saturated,
always the page's sole source of colour; no illustration, no icon system beyond
simple glyphs.
Reject: any chromatic UI element (button fill, coloured link, badge); border-
radius on any element including images; box-shadow of any kind; a centred or
max-width-constrained layout; bold or semibold type.
Token commitments: bg `#f2f2f2`, ink `#292a2c`, hard `#000000`; display ogg 400
at 24-55px/leading 1.06-1.5/-0.036 to -0.02em tracking; body telegraf 400 at
15-25px/leading 0.75-2.0/0.002-0.04em tracking; radius 0px universal; page
max-width 1440px, section gap 120px, base spacing unit 6px.
