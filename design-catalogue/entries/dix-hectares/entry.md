---
title: "Dix Hectares"
url: https://dixhectares.com/en
source_url: https://dixhectares.com/en
captured: 2026-09-04
origin: raw-url
extract: ok
raw: raw/a516ff3820f2a85f-screenshot.webp
category: luxury-craft
category2: ""
family: terroir-calendar-atelier
dna: "Wine-terroir provenance x seasonal skincare calendar"
register: editorial print
grammar: gallery/catalog
lane: "A sky-and-grasses photograph carries a giant serif wordmark over a literal month-by-month calendar strip, then cream product plates ruled and priced in euros by season"
mode: persuade
traits: ["giant serif wordmark set on photo", "tracked micro-caps provenance copy", "literal J-D month calendar strip as design device", "cream product-plate grid", "colour-coded seasonal product photography", "euro pricing under each tile", "terracotta accent banner", "wine-estate origin story"]
palette: ["#6E93B5", "#F0EAD9", "#C1552B", "#7C8A3E", "#5A6E3A", "#3A2E1F"]
type: ["Francesco", "Sackers Gothic"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
---

## Why it works

The provenance claim is stated three times in three registers before the reader
sees a single product: a tracked micro-caps line ("French skincare, cultivated
on a Grand Cru terroir..."), a giant serif wordmark, and — most distinctively —
a literal month-by-month calendar strip (`J F M A M J J A S O N D`) running the
full width beneath the hero. The calendar is the unusual move: it makes
"seasonal skincare" a structural, almost architectural feature of the page
layout, not just a line of copy.

The brand borrows its authority from wine, not cosmetics — "Grand Cru terroir"
is a wine-classification term, and the estate origin (a Bordeaux wine château
diversifying into skincare) gives the calendar device real logic: the product
literally changes with the growing season, so a calendar isn't decoration, it's
the product's actual organizing principle.

Product photography is colour-coded by season rather than shot on a single
neutral background: a jar on terracotta orange, a tube on olive green, a bottle
in a glass vase on sage — each SKU gets its own seasonal ground colour, so the
shop grid reads as a colour-mapped calendar in miniature, echoing the strip
above it.

## What to borrow (principle)

- **Turn a seasonal or cyclical product logic into a literal calendar-strip
  layout device**, not just copy — make the structure of the page argue the
  claim.
- **Borrow authority language from an adjacent, higher-status category** (wine
  terroir vocabulary for skincare) when the provenance is genuinely shared.
- **Colour-code product photography by category or season** so the shop grid
  itself communicates organization, not just individual product beauty.
- **State the same core claim in three type registers** (tracked micro-caps,
  giant display, structural layout) so it lands whether the reader skims or
  reads closely.

## What to leave

- A full J-through-D calendar strip is a striking one-time device; repeating it
  as a navigational element throughout the site would wear out its novelty fast.
- Colour-coding every product to its season risks a cluttered shop grid once the
  catalogue grows past a handful of SKUs per season — it needs a neutral-ground
  fallback for larger ranges.

## Signature move

The month-by-month calendar strip: twelve ruled cells, one per month letter,
run full-width directly beneath the hero wordmark — turning "seasonal skincare"
from a tagline into an actual piece of interface.

## Motion

(from designlang extract) Feel is "responsive" with scroll-linked motion
confirmed. The dominant easing is a decelerating ease-out family
(`cubic-bezier(0.33,1,0.68,1)`, `cubic-bezier(0.25,1,0.5,1)`,
`cubic-bezier(0.215,0.61,0.355,1)` — 81 uses combined) on a `300–800ms`
duration ladder, giving hover states and section transitions a smooth,
settled arrival rather than anything springy. Most of the actual keyframes
captured, though, are commerce plumbing rather than page choreography:
Shopify's accelerated-checkout skeleton and rotator/dash spinners, plus a
Swiper carousel preloader — none of it is the calendar-strip or product-tile
reveal the layout implies, which the static extract doesn't confirm either
way.

| token | value | role |
|---|---|---|
| `xs`/`md` | 100/300ms | UI state changes |
| `lg`/`xl` | 500/800ms | larger section transitions |
| ease-out | `cubic-bezier(0.33,1,0.68,1)` etc. | dominant (81 uses) |
| custom | `cubic-bezier(0.65,0,0.35,1)` etc. | secondary (43 uses) |

## Brief

Build an editorial-print skincare page rooted in a genuine seasonal or
provenance story. Open on a photograph of the raw material (a plant, a
landscape, a harvest) with tracked micro-caps provenance copy and a giant serif
wordmark overlaid. Directly beneath, run a literal calendar-strip device (twelve
cells, one per month) as a structural page element, not decoration. Below, on
cream, lay out product tiles as a ruled grid, each shot on its own
season-appropriate colour ground with the price set in the local currency
beneath. Keep an orange or terracotta accent for banners and small UI only.

## Image recipe

A hand or figure holding [SUBJECT] — wild grasses, herbs, or harvest material —
against open sky, natural outdoor light, shallow depth of field with the sky
slightly overexposed, muted natural colour, no visible product or packaging in
the hero shot.

## Photo search

Unsplash first, Pexels second.
- "wild grasses harvest hand against sky"
- "herb bundle natural light outdoor"
- "botanical harvest field golden light"

## Reference lock

Primary reference/direction: Dix Hectares — literal month-calendar strip as a structural device under a terroir-provenance hero.
Preserve (3-5 traits): tracked micro-caps provenance copy stated above a giant serif wordmark; a literal twelve-month calendar strip run full-width as a structural (not decorative) layout device; product photography colour-coded by season on distinct grounds; euro/local-currency pricing set directly beneath each product tile.
Borrow only (1-2): the orange "free delivery" announcement banner; the vase-styled product photography for liquid formats.
Role rules: the calendar-strip device appears once per page, directly under the hero, never repeated as navigation; each product's ground colour must correspond to its season, not be arbitrary; provenance copy stays in tracked micro-caps, never full-size body text.
Media strategy: photo:unsplash — natural outdoor light, raw/harvest material only for hero imagery; product photography is studio-lit on seasonal colour grounds.
Reject: a neutral white-background product grid that discards the seasonal colour-coding; decorative (non-functional) calendar graphics; provenance claims without a genuine sourcing story behind them.
Token commitments: sky `#6E93B5`, cream `#F0EAD9`, terracotta `#C1552B`, olive `#7C8A3E`, sage-product-bg `#5A6E3A`, ink-brown `#3A2E1F`; serif display for the wordmark, tracked small-caps for all provenance/label copy.
