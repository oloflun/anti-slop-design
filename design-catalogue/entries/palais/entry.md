---
title: "Pa'lais"
url: https://www.palais.bio/
source_url: https://www.palais.bio/
captured: 2026-09-04
origin: refero
extract: ok
category: playful
category2: "consumer-brand"
family: honeyed-sketchbook-cookbook
dna: "Hand-bound botanical sketchbook x condensed-serif editorial food-magazine confidence"
register: illustrated dark
grammar: chaptered editorial
lane: "A cream paper canvas carries condensed all-caps indigo headlines and a handwritten script tagline, divided from full-bleed lifestyle photography by an organic honey-and-sage blob rather than a straight line, with toile-style botanical line-art bleeding off every section edge"
mode: persuade
traits: ["single cool indigo, all warmth in organic blobs", "condensed all-caps display + handwritten script duet", "0.13-0.27em tracking on every label", "wavy SVG blobs replace straight dividers", "botanical line-art bleeding off page edges", "pill buttons, soft-corner cards, hairline borders"]
palette: ["#234386", "#fbf9f6", "#ffc400", "#ed7328", "#a2d3a6", "#000000"]
type: ["hwt-artz", "Delivery Note DEMO", "Axiforma", "Sonder Sans Black Rough"]
measured: designlang
kind: reference-style
source: anton
status: ready
refero: processed/Palais.md
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the live
capture. The system draws a hard "colour lane" boundary the source states as an
explicit rule: deep indigo `#234386` is the only cool saturated hue and it alone
owns type, links and filled buttons; every warm colour (honey gold, burnt
orange, mint sage) is confined to organic blob shapes and outlined secondary
actions, never body text or buttons. Cream paper `#fbf9f6` underneath both is
what makes the rule legible — warm enough that indigo reads as a deliberate cool
counterpoint, saturated enough that white cards lift without needing gray
separators.

Two display voices work in tandem rather than opposition: a bold condensed
all-caps face carries structural headlines at tight 0.043em tracking — the
designlang extract identifies this as "Sonder Sans Black Rough," correcting the
original "Caveat" read, which the live font list does not confirm — while a
handwritten script carries emotional taglines beneath them ("The future
of cooking – today") — a label-plus-signature pairing rather than the
heavy-vs-light contrast used elsewhere in this catalogue. Labels and navigation,
meanwhile, run the widest tracking in the system, up to 0.267em, which the
source calls the "aggressive tracking... the system's signature typographic
device."

The organic blob is the structural device that replaces every straight line in
the layout: section dividers, hero splits, and decorative washes are all
free-form SVG paths in a single accent colour, evoking liquid or botanical
forms rather than a hard edge. Paired with hand-drawn botanical line-art that is
explicitly instructed to "bleed off page edges, overlap section boundaries, and
be partially hidden" rather than sit in a contained box, the page reads as a
living illustrated notebook rather than a templated grid.

## What to borrow (principle)

- **Draw a hard colour-lane boundary and never cross it.** One cool hue owns
  structure (type, links, buttons); all warm hues stay confined to decoration —
  stating the rule explicitly keeps a multi-colour palette disciplined.
- **Pair a structural display voice with an emotional script voice.** A bold
  condensed headline plus a handwritten tagline beneath it gives copy two
  distinct registers without needing a third typeface for body text.
- **Replace every straight divider with an organic shape.** A wavy SVG blob
  between two colour fields creates a hand-painted transition a hard line
  cannot.
- **Let illustration bleed off the page.** Explicitly forbidding illustrations
  from sitting in a contained box is what keeps hand-drawn elements feeling
  "living" rather than stock-decorated.
- **Push label tracking to an extreme and hold it there.** 0.267em tracking on
  the widest labels is aggressive enough to become a recognizable signature
  rather than a default choice.

## What to leave

- A strict colour-lane rule (cool = structure, warm = decoration only) is easy
  to violate under marketing pressure — a "limited edition" callout in a warm
  accent as a text colour would immediately break the system's internal logic.
- Free-form organic blob dividers require custom SVG path work for every new
  section transition; a team without illustration resources will default back
  to straight lines and lose the device entirely.
- The handwritten script accent depends on genuine restraint — the source notes
  it is "not a structural font," and any temptation to use it for UI labels or
  buttons would undermine its rarity as an emotional flourish.

## Signature move

The organic wavy section divider: a large flowing SVG path (honey-gold over
mint-sage, or matching the section below) replacing every hard boundary between
colour fields — cream to orange, white to indigo — with a hand-painted,
watercolor-edge curve instead of a straight line.

## Motion

(from designlang extract) Feel reads as mixed, and the page is scroll-linked.
Interactions run across five durations (150ms-1s) on three easing families: a
plain `ease` for simple state changes, a fast-settling ease-out
(`cubic-bezier(0.3, 0.95, 0.33, 0.98)`, the most-used curve at 21 uses) for
reveals, and `linear` for continuous motion. Three related keyframes —
`WaveCards`, `WaveCards2`, `WaveCards3` — each a slide-x transform, confirm the
recipe-card carousel does move on its own: three cards staggered into a
travelling wave rather than a single block sliding uniformly. (observed in
capture) the minimal circular downward-chevron scroll cue is consistent with a
simple, non-parallax scroll experience elsewhere on the page — the wave motion
is confined to the card carousel, not the whole viewport.

| Token | Value | Easing |
|---|---|---|
| xs | 150ms | `ease` |
| sm | 200ms | `ease` |
| md | 300ms | `cubic-bezier(0.3, 0.95, 0.33, 0.98)` |
| lg | 500ms | `cubic-bezier(0.3, 0.95, 0.33, 0.98)` |
| xl | 1s | `linear` |
| WaveCards 1-3 | slide-x transform | staggered card-wave carousel |

## Brief

Build a warm, illustrated plant-based food-brand landing page. Canvas is cream
paper `#fbf9f6` with white `#ffffff` cards layered on top; deep indigo
`#234386` is the only cool saturated colour, owning every headline, link and
filled button. Reserve honey gold `#ffc400`, burnt orange `#ed7328`, sky blue,
warm sand and mint sage `#a2d3a6` exclusively for organic blob shapes and
outlined secondary buttons — never as text or fill on a primary action. Open
with a split hero: a bold condensed all-caps indigo headline plus a handwritten
script tagline on one side, product photography on the other, divided by a
flowing gold-over-sage SVG blob rather than a straight line. Scatter hand-drawn
botanical line illustrations (indigo or sky-blue stroke, no fill) bleeding off
section edges throughout. Use 32px pill radius for buttons, 8px for cards, and
label/nav text at 0.13-0.27em tracking in a geometric sans. Alternate cream,
white, and full-bleed orange section bands, separated by organic wavy dividers,
with a dark indigo footer band closing the page.

## Image recipe

Warm natural-light food photograph of [SUBJECT] — a plant-based spread or dish
styled on wood, linen or ceramic surfaces, garnished with fresh herbs and nuts,
shallow depth of field, close-up or slightly overhead angle, natural warm
lighting with no harsh flash, an artisan/handmade rather than studio-sterile
mood.

## Photo search

Unsplash first, Pexels second.
- "plant-based spread toast natural light"
- "vegan cheese wooden board overhead"
- "cashew cream sauce close up"
- "botanical herbs kitchen natural light"

## Reference lock

Primary reference/direction: Pa'lais — illustrated plant-kitchen recipe-journal
page, one indigo structural colour against warm decorative blobs.
Preserve (3-5 traits): cream paper `#fbf9f6` canvas with white cards; deep
indigo `#234386` as the sole cool hue, owning all type/links/buttons; warm
accents (gold, orange, sage) confined strictly to organic blob shapes and
outlined buttons, never text or primary fills; condensed all-caps display
paired with a handwritten script tagline; hand-drawn botanical line-art
bleeding off section edges, never boxed.
Borrow only (1-2): the organic wavy SVG section divider; the circular
scroll-indicator icon below the hero.
Role rules: warm accent colours never set body text or fill a primary button;
indigo never appears inside a decorative blob; the script font never appears in
UI chrome, labels or buttons.
Media strategy: photo:unsplash — warm, natural-light artisan food and product
photography, paired with hand-drawn botanical line illustration; no studio-
sterile white-cyc shots.
Reject: a second cool saturated colour; warm accents on buttons or body text;
flat gray surfaces for separation; hard straight-line section dividers; bold
inline emphasis within body copy.
Token commitments: bg `#fbf9f6`, card `#ffffff`, ink-structural `#234386`,
ink-body `#000000`, accent-gold `#ffc400`, accent-orange `#ed7328`, accent-sage
`#a2d3a6`; display 32-88px/leading 0.82-1.2/0.031-0.043em tracking; label
tracking 0.133-0.267em; radius 8px cards, 32px buttons, organic blobs for
dividers; page max-width 1200px, section gap 64px.
