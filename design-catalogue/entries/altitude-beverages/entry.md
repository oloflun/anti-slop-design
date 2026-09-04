---
title: "Altitude Beverages"
url: https://altitudebev.com
source_url: https://altitudebev.com
captured: 2026-09-04
origin: refero
extract: ok
category: consumer-brand
category2: editorial
family: mono-gallery-catalog
dna: "Fashion-magazine monochrome x saturated can photography"
register: editorial print
grammar: chaptered editorial
lane: "A near-white gallery page that opens on one massive compressed headline, then alternates single-statement chapters of full-bleed gradient-lit can photography against an all-black watermark section, never mixing colour into the UI itself"
mode: persuade
traits: ["160px compressed display", "serif/sans/mono three-way voice split", "monochrome UI, chromatic photography only", "100px pill nav + 44px card radius", "no shadows, tone-step depth", "dark gradient watermark interlude"]
palette: ["#fafafa", "#d9d9d9", "#cdcdce", "#07060b", "#000000", "#ddfcff"]
type: ["HelveticaNowDisplay", "EditorialNew", "DepartureMono"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
refero: processed/Altitude Beverages.md
---

## Why it works

Palette and type are read from Refero's extracted tokens. The system deliberately
empties itself of colour — canvas, cards and text stay inside four near-neutral
values — so that the only saturated thing on the page is the product itself: cans
photographed on gradient backdrops (orange, amber, teal) that read as almost lurid
against the gallery-white UI. That contrast is the whole strategy: colour is a
property of the product, not of the interface.

Type carries the identity work colour would normally do. Three faces are kept in
strict, non-overlapping roles — HelveticaNowDisplay at weight 800 owns the single
160px hero line, EditorialNew at weight 200 owns mid-scale pull-quote subheads, and
DepartureMono owns every functional label (nav, buttons, ingredient lists). Because
the ultra-bold display and the whisper-thin serif never appear at the same size,
the 800-vs-200 weight jump reads as tension rather than inconsistency, and the
monospace signals "this is UI, not editorial" wherever it shows up.

Depth is entirely tonal: canvas white steps to warm-ash grey for the pill nav and
cards, with no shadow anywhere. That flatness is what lets the one dark, full-bleed
gradient section — a near-black band with a faint watermark wordmark and nothing
else — land as a genuine tonal event rather than just another card.

## What to borrow (principle)

- **Let the product own the only saturated colour on the page.** Keeping UI chrome
  monochrome makes the photography, not the brand palette, feel chromatic.
- **Split type roles by function, not by size alone.** One face for the singular
  hero statement, one for editorial mid-copy, one monospace for everything
  functional — never let two of them share a size class.
- **Use radius as a register signal.** A 100px pill on nav/buttons and 44px on
  cards, with nothing in between, keeps the geometry legible as one family of
  shapes rather than an arbitrary scale.
- **Spend a full-bleed dark section as punctuation.** One tonal reset with almost
  no content reads as a pause in a page that is otherwise dense with photography.

## What to leave

- A single 160px headline with -0.05em tracking depends entirely on having one
  short, strong line of copy; it fails immediately with anything but a tight
  sentence.
- The near-invisible watermark wordmark on the dark section only works once — used
  twice on a page it reads as a template, not a device.
- Zero brand-colour UI chrome is a hard constraint: any hover or active state that
  needs to signal "brand" rather than "neutral" has nowhere to live in this system.

## Signature move

The dark full-bleed gradient interlude: a section with no headline, no button, no
card — just a top-to-bottom black-to-light gradient and a faintly legible watermark
wordmark centred in it. It functions purely as a tonal breath between two
photographic, high-energy product chapters.

## Motion

(from designlang extract) Feel reads as mixed rather than a single house style, and
the page is scroll-linked — sections and cards animate in relative to scroll
position rather than firing purely on load. Interaction transitions are fast and
utilitarian: hover/focus states on links, buttons and form fields resolve in 150ms,
while larger content changes (image or opacity swaps) take 500ms. Both run on a
single standard easing curve, no springs or overshoot are used anywhere in the
system. No custom keyframe animations are defined beyond Tailwind's stock
pulse/bounce/spin/ping utilities, which are reserved, not visibly driving the page.
The flat, shadow-free system reads as considered rather than kinetic — motion
supports state changes, it doesn't perform. (observed in capture) the alternating
light/dark full-bleed sections and overlapping product-card compositions suggest
simple crossfades between chapters and a light, parallax-free reveal on scroll.

| Token | Value | Easing |
|---|---|---|
| xs (state changes) | 150ms | `cubic-bezier(0.4, 0, 0.2, 1)` |
| lg (content swaps) | 500ms | `cubic-bezier(0.4, 0, 0.2, 1)` |

## Brief

Build a monochrome product-gallery landing page for a canned beverage brand. Canvas
is near-white `#fafafa`, elevated surfaces step to warm ash `#d9d9d9`, text is
near-black `#07060b`; the only chromatic colour anywhere is in product photography.
Open on a single HelveticaNowDisplay weight-800 headline at up to 160px with tight
-0.05em tracking, paired with an EditorialNew weight-200 subhead and a DepartureMono
uppercase pill button. Float a pill navigation (100px radius, warm-ash fill) over
the hero. Below, alternate full-bleed product feature cards — 44px radius, gradient-
lit can photography, a smaller overlapping card in the corner — with a single dark,
near-black full-bleed section carrying only a faint watermark wordmark. No shadows
anywhere; depth is tone-stepping only. Keep section gaps generous (36-80px) and let
each chapter read as one uninterrupted statement.

## Image recipe

Studio product shot of [SUBJECT] — a beverage can lit against a saturated gradient
backdrop (orange-to-amber or teal-to-green), condensation beading on the metal,
one sprig of fresh garnish (rosemary, citrus, flower) resting against the can,
dramatic raking light creating a dark-to-light gradient wrap on the can surface
itself, tight crop with the object bleeding past the frame edge, no studio props
beyond the single garnish, no visible background horizon.

## Photo search

Unsplash first, Pexels second.
- "beverage can product shot gradient background studio"
- "condensation can drink close up"
- "rosemary garnish drink flat lay"
- "citrus fruit product photography saturated colour"

## Reference lock

Primary reference/direction: Altitude Beverages — monochrome editorial-gallery UI
around saturated gradient-lit can photography, three-way type role split.
Preserve (3-5 traits): near-white canvas `#fafafa` stepping to warm-ash `#d9d9d9`
for surfaces, near-black `#07060b` ink, zero brand colour in UI chrome; strict type
role split (HelveticaNowDisplay hero only, EditorialNew mid-copy only, DepartureMono
functional labels only); 100px pill radius on nav/buttons, 44px on cards, nothing
between; no shadows, tone-step depth only; alternating light photographic chapters
with one dark full-bleed watermark interlude.
Borrow only (1-2): the 160px single-line display headline; the overlapping
feature-card + floating-card product composition.
Role rules: EditorialNew never appears below 14px or above 60px; HelveticaNowDisplay
never carries body text; DepartureMono is the only face permitted in buttons, nav
and metadata; product photography is the sole source of saturated colour.
Media strategy: photo:unsplash — tightly cropped, gradient-lit product stills with
one garnish accent; no illustration, no icon-heavy decoration.
Reject: any UI chrome in brand colour; card radius outside 44px/100px; drop shadows;
line-height above 1.06 on headlines; icons or illustration in the interface.
Token commitments: bg `#fafafa`, surface `#d9d9d9`, border `#cdcdce`, ink `#07060b`,
ink-hard `#000000`, micro-accent `#ddfcff`; display weight 800 at 160px/-0.05em,
editorial weight 200 at 40-60px, mono uppercase at 11-12px/-0.071em; radius 44px
cards, 100px pills; page max-width 1440px, section gap 36-80px.
