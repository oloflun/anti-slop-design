---
title: "Monologue"
url: https://www.monologue.to/
source_url: https://www.monologue.to/
captured: 2026-09-04
origin: refero
extract: ok
category: product-focused
category2: editorial
family: velvet-library-cyan-spark
dna: "400px italic-serif ghost wordmark x embossed physical product device"
register: cinematic dark
grammar: split stage
lane: "A near-black canvas carries an italic serif headline over generous whitespace while a 400px ghosted wordmark bleeds across the full viewport behind it, and a single physical-feeling white product device — complete with an embossed stamp badge — anchors the centre with the page's only saturated colour"
mode: persuade
traits: ["400px ghost wordmark as background layer", "italic Instrument Serif at every display size", "DM Mono for all UI chrome, never prose", "one electric cyan spark, 2-3 uses per screen", "physical multi-layer shadow on the product device only", "fully rounded pills, generous card radii"]
palette: ["#000000", "#191919", "#282828", "#19d0e8", "#ffffff", "#7f7f7f"]
type: ["Instrument Serif", "Geist Mono", "Geist"]
measured: designlang
kind: reference-style
source: anton
status: ready
refero: processed/Monologue.md
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the live
capture. The canvas is void black with a five-step gray scale for card surfaces
(midnight → graphite → charcoal → slate), and exactly one chromatic accent,
electric cyan, is capped at "2-3 times per screen" — the source's own language
for it is "a spark, not a wash." Everything else in the system, including the
primary CTA button, stays in white or near-black; cyan is reserved for punctuation
only, never for a large surface.

Three typefaces carry three strictly separate jobs. Instrument Serif, always set
in italic, is the only display face — it runs from a 400px ghosted background
wordmark down to 28px pull-quotes, with negative tracking that intensifies at
scale. Geist Mono owns every piece of UI chrome (labels, tags, button text,
metadata) with a slight positive tracking that gives small system text a
deliberate, spaced-out quality — the designlang extract shows this face
self-hosted as `geistMono` and used across 1,372 elements, correcting the
original "DM Mono" read to the actual Vercel Geist Mono cut. Geist, at a
slightly-larger-than-default 17px, is reserved purely for prose. The rule the
source states outright — "never mix these roles" — is what keeps a three-font
system from reading as inconsistent.

Elevation is rationed as tightly as colour: the void canvas and flat cards carry
no shadow at all, but the one physical hero object — the white product device —
gets a genuinely complex multi-layer inset-and-outset shadow stack that makes it
read as a real object resting on a dark surface. Confining that shadow complexity
to a single element is what makes the device feel tangible against an otherwise
paper-flat interface.

## What to borrow (principle)

- **Cap a chromatic accent to a stated frequency, not just "sparingly."** "2-3
  times per screen" is a rule a design review can actually check.
- **Assign each typeface exactly one job and never let them overlap.** Serif for
  voice, mono for system chrome, sans for prose — mixing any two roles breaks the
  reading a viewer has learned.
- **Reserve complex shadow layering for one hero object only.** A flat system
  with a single, genuinely dimensional "real thing" makes that object read as
  physically present rather than merely decorated.
- **Let the wordmark become atmosphere, not chrome.** A giant, ghosted brand name
  behind the content (rather than in a header) can carry identity continuously
  without taking up functional space.
- **Tighten serif tracking at scale, open mono tracking at small sizes.** Two
  opposite tracking rules, each serving its own face's job, is more legible than
  one flat tracking value applied everywhere.

## What to leave

- A 400px background wordmark demands a short brand name and a very tall hero
  section to avoid overwhelming the content sitting on top of it.
- Complex multi-layer inset/outset shadows on a single "hero object" require a
  genuinely well-modeled asset (the source lists four distinct shadow layers for
  the product device) — a flatter illustration would not survive the same
  treatment.
- Locking Instrument Serif to italic-only at every size is a strong brand
  commitment; any content team that needs an upright serif for a different
  register will need to introduce a second face, which the system's "never mix
  roles" rule doesn't accommodate.

## Signature move

The embossed "Made by [Parent]" stamp badge: a small scalloped, postage-stamp-
shaped badge with a heavy inset shadow, overlapping the top edge of the product
device — a single physical-feeling attribution mark that reads as pressed into
the object rather than a flat logo lockup.

## Motion

(from designlang extract) Feel reads as responsive, and the page is scroll-linked
— this corrects the earlier "no explicit tokens" read substantially: the site
runs a genuinely rich choreography system. Five duration steps run from an
instant 40ms up to 460ms, mostly on ease-out curves (69 uses across three related
beziers, e.g. `cubic-bezier(0.22, 1, 0.36, 1)`), with a slower custom
`cubic-bezier(0.77, 0, 0.175, 1)` for a handful of larger moves. Ten distinct
keyframes are confirmed firing: `feature-app-float` (a slide-transform loop, 12
uses) most likely gives the feature app icons a gentle floating bob;
`feature-app-orbit-clockwise` (rotate) suggests at least one icon orbits the hero
product device, extending the "physical object" metaphor into motion, not just
shadow; `dictation-caret-blink`/`feature-caret-blink` (opacity fade) simulate a
live text cursor; `testimonial-enter`/`testimonial-progress` (slide-y + scale)
drive an auto-advancing testimonial carousel; `product-story-progress` (scale)
and `product-story-copy-in` (slide-y) stage a scrollytelling reveal; and
`trusted-logo-scroll` (slide) drives a logo marquee. (observed in capture) given
the "physical device" metaphor and multi-layer shadow treatment, the static hero
frame the live capture caught is consistent with a page that is normally far more
animated than a single screenshot suggests.

| Token | Value | Easing |
|---|---|---|
| instant | 40ms | ease-out family |
| xs | 90ms | ease-out family |
| sm | 160ms | ease-out family |
| md | 260ms | ease-out family |
| lg | 460ms | `cubic-bezier(0.77, 0, 0.175, 1)` (larger moves) |
| feature-app-float | slide, loop | 12 uses |
| feature-app-orbit-clockwise | rotate | 1 use |
| testimonial-enter / -progress | slide-y + scale | carousel |

## Brief

Build a dark-mode productivity-app landing page. Canvas is void black `#000000`;
cards step through midnight `#191919`, graphite `#282828` and charcoal `#363636`
with no shadow at any of those levels. Electric cyan `#19d0e8` is the only
chromatic accent, appearing at most 2-3 times per screen — an inline text
emphasis, a thin border, or a product-screen gradient, never a button fill. Open
the hero with an italic Instrument Serif headline at 64-96px, negative tracking
intensifying with size, over a 400px ghosted wordmark bleeding behind the content
as a background layer. Use DM Mono, slightly positively tracked, for every label,
tag, and button — including a white, fully-rounded pill download button, the
system's one light-on-dark surface. Render a single hero product device with a
genuinely complex multi-layer shadow (inset and outset combined) so it reads as a
physical object, complete with a small embossed attribution stamp overlapping its
top edge. Keep body copy in Geist at 17px, left-aligned, never centred except for
testimonials and the wordmark itself. Section gaps run 80px.

## Image recipe

Not primarily photographic — the hero visual is a rendered physical product
device (a rounded white hardware object with a gradient teal screen) rather than
a photograph. Where supplementary imagery is needed: a dark, textured [SUBJECT]
close-up (fabric ripple, water undulation) at very low contrast, used purely as
atmospheric background texture behind type — never a literal photographic
subject, never lit brightly enough to compete with the headline.

## Photo search

Unsplash first, Pexels second.
- "dark texture ripple abstract background"
- "black fabric wave texture close up"
- "dark water surface ripple minimal"
- "abstract dark gradient texture"

## Reference lock

Primary reference/direction: Monologue — void-black productivity app with a
400px ghost-wordmark hero and a single physical product device.
Preserve (3-5 traits): void-black `#000000` canvas stepping through a five-tier
gray card scale, no shadow at any card level; italic Instrument Serif as the only
display face at every size, DM Mono for all UI chrome, Geist for prose only —
never mixed; electric cyan `#19d0e8` capped at 2-3 appearances per screen, never
a button fill; complex multi-layer shadow reserved for exactly one hero product
object; fully-rounded pill radius for buttons and tags, 12-40px for cards and the
device body.
Borrow only (1-2): the ghosted 400px background wordmark; the embossed
scalloped attribution stamp badge.
Role rules: cyan never becomes a large surface fill; Instrument Serif never sets
body prose or drops below 28px; DM Mono never carries paragraph copy.
Media strategy: 3D/product render for the hero device; supplementary photography
stays dark, textural, and low-contrast — no lifestyle or people photography.
Reject: a bright or warm second accent colour; heavy shadow on flat text cards;
a proportional (non-mono) font for system labels; centred body paragraphs
outside testimonials.
Token commitments: bg `#000000`, card `#191919`, interactive `#282828`, accent
`#19d0e8`, ink `#ffffff`, muted `#7f7f7f`; display Instrument Serif italic 400 at
28-96px/leading 0.9-1.3/-0.03 to -0.04em tracking; mono UI 10-20px/positive
tracking; body Geist 17px/leading 1.4; radius 4-8px small, 18-40px cards/device,
100000px pills; page max-width 1200px, section gap 80px.
