---
title: "OLIPOP"
url: https://drinkolipop.com
source_url: https://drinkolipop.com
captured: 2026-09-04
origin: refero
extract: ok
category: playful
category2: "consumer-brand"
family: apothecary-soda-fountain
dna: "Vintage apothecary display serif x flavor-locked pastel product cards"
register: illustrated dark
grammar: gallery/catalog
lane: "A warm cream canvas bracketed top and bottom by forest-teal bands carries a poster-scale retro-serif hero panel and a horizontal carousel of pastel flavor cards, each card colour reserved exclusively for its own product"
mode: persuade
traits: ["weight 800-900 retro display serif, 1.0 leading", "cream canvas, forest-teal dark bookends", "15-colour palette, flavor-locked to product cards", "pill radius on every interactive element", "circle motif for every product image", "one soft glow shadow, on the primary CTA only"]
palette: ["#14433d", "#fdf7e7", "#d3e8e3", "#3a3a3a", "#7e0022", "#2ad2c9"]
type: ["WindsorEF", "Ano"]
kind: reference-style
source: anton
status: ready
refero: processed/OLIPOP.md
---

## Why it works

Palette and type are read from Refero's extracted tokens. Forest-teal `#14433d`
is the system's one authoritative dark, appearing only as the announcement bar,
footer, and primary CTA fill — bracketing the cream page top and bottom like the
covers of a book. Product-card colour is treated as strictly separate namespace:
a 15-hue pastel palette is "flavor-locked," meaning each colour belongs to
exactly one product and must never be reused for UI chrome, buttons, or section
backgrounds. That separation is what lets the product carousel feel vivid and
candy-shop bright without any of that vibrancy leaking into — or competing with
— navigation and buttons.

WindsorEF, a high-contrast retro display serif, is reserved for headlines 32px
and above at weight 800-900 with an extremely tight 1.0 line-height; Ano, a clean
modern sans, does every other job with generous 1.5-1.82 line-heights that keep
body copy breathable. The pairing recreates a specific historical reference —
apothecary and soda-fountain packaging — without needing any literal illustration
to say so.

Elevation is almost entirely absent except for one exception stated explicitly:
a soft ambient glow shadow lives only on the primary CTA button, nowhere else.
Combined with a strict two-radius system (16px for cards, 50px/pill for every
interactive element) and a recurring circle motif for every product photo, the
page reads as a vintage general-store menu translated into modern e-commerce
rather than a typical DTC storefront.

## What to borrow (principle)

- **Flavor-lock a palette to specific products, not to UI.** Assigning each
  named colour to exactly one item (never reused for chrome) makes a large
  palette feel curated rather than arbitrary.
- **Bracket the page with one dark colour, top and bottom only.** A single
  forest-teal announcement bar and footer, with nothing dark between them, frames
  a light page without needing alternating section bands.
- **Reserve elevation for exactly one component.** A single soft glow shadow,
  applied only to the primary CTA, makes that one button read as "the" action
  without requiring shadows anywhere else.
- **Recreate a specific historical reference through pairing, not literal
  props.** A high-contrast display serif against a friendly workhorse sans can
  evoke "vintage apothecary" without a single period illustration.
- **Repeat one shape as a structural motif.** Circular crops on every product
  image (and nowhere else) create a recognizable, medallion-like rhythm across
  an otherwise rectangular grid.

## What to leave

- A 15-colour flavor-locked palette requires real production discipline — every
  new SKU needs a genuinely new hue, and a large enough product line will
  eventually run out of distinguishable pastels.
- WindsorEF's extremely tight 1.0 line-height at display sizes depends on a
  typeface with generous internal leading in its metrics; a substitute serif
  without that headroom will clip ascenders/descenders.
- Reserving shadow for exactly one component is easy to erode as a product page
  grows — a second "important" CTA will tempt a team to add the glow elsewhere,
  diluting the signal.

## Signature move

The circle-cropped product photo: every can, illustration, or feature image is
masked to a perfect circle — referencing vintage bottle caps and medallions — a
device repeated consistently enough (flavor cards, rewards section, logo
treatment) that it becomes the brand's structural signature independent of any
single instance.

## Motion

No motion or interaction tokens are captured in the Refero export. Note: the
live site did not finish loading within this session's capture window (a
networkidle timeout, likely from third-party trackers/pixels common on DTC
storefronts), so this entry's images are drawn from the Refero export rather
than a fresh capture. Inferred from the image and the "flavor carousel"
component description: the product-card row most plausibly scrolls
horizontally on drag or arrow-click, consistent with the "Pure Nostalgia-ahh"
carousel label, though no easing or duration is documented. (inferred)

## Brief

Build a nostalgic prebiotic-soda DTC landing page. Bracket the page with forest-
teal `#14433d` bands at the very top (announcement bar) and very bottom
(footer); everything between sits on cream `#fdf7e7` canvas. Set headlines 32px
and above in a high-contrast retro display serif at weight 800-900, 1.0 line-
height; use a friendly modern sans for everything else at 1.5+ line-height. The
hero is a two-tone composition: a mint-sage `#d3e8e3` inset panel (24px radius)
holding the display headline and a forest-teal pill CTA with a soft ambient
glow shadow — the system's one elevated element. Below, run a horizontal
carousel of flavor cards, each a full-bleed pastel colour (16px radius) unique
to its product, with a circular photo crop and the flavor name in the display
serif. Repeat the circle-crop motif for any illustration or feature image. Use
50px pill radius for every button and input; reserve a wine-red accent for rare
"specialness" labels and a bright teal for one secondary CTA only. No shadows
anywhere except the primary button's glow.

## Image recipe

Studio product photograph of [SUBJECT] — a beverage can shot on a clean,
single-colour pastel backdrop matching its flavor identity, straight-on or
slight three-quarter angle, sharp focus, no lifestyle context, no hands, no
environment — cropped or composed to sit within a circular mask, high-key
lighting with minimal shadow beneath the can.

## Photo search

Unsplash first, Pexels second.
- "soda can product shot pastel background"
- "beverage can flat colour backdrop studio"
- "fruit flat lay pastel colour palette"
- "vintage soda fountain illustration retro"

## Reference lock

Primary reference/direction: OLIPOP — retro apothecary soda-fountain page,
flavor-locked pastel product cards bracketed by forest-teal bands.
Preserve (3-5 traits): cream `#fdf7e7` canvas bracketed top and bottom by
forest-teal `#14433d` bands only; 15-colour pastel palette strictly flavor-
locked to individual product cards, never reused for UI chrome; WindsorEF
weight 800-900 at 1.0 leading for all headlines 32px+, Ano for everything else;
50px pill radius on every interactive element, 16px on cards; a single soft
glow shadow reserved for the primary CTA only.
Borrow only (1-2): the circular product-photo crop as a recurring structural
motif; the mint-sage inset hero panel ("card on a card") device.
Role rules: flavor-card pastels never appear on buttons, nav, or borders; wine-
red and bright-teal accents never combine in the same component; WindsorEF
never sets text below 20px.
Media strategy: photo:unsplash — clean, single-colour-backdrop product
photography and retro folk-art illustration only; no lifestyle staging, no
people.
Reject: shadows on anything but the primary CTA; sharp corners (0-8px) on any
button or input; a second dark UI colour beyond forest-teal; reusing a flavor
colour as UI chrome; body text below 1.4 line-height.
Token commitments: bg `#fdf7e7`, panel `#d3e8e3`, dark `#14433d`, ink `#3a3a3a`,
accent-wine `#7e0022`, accent-teal `#2ad2c9`; display WindsorEF 800-900 at
20-80px/leading 1.0; body Ano 400-700 at 12-24px/leading 1.2-2.33; radius 16px
cards, 50px pills, 24px hero panel; page max-width 1200px, section gap 40-64px.
