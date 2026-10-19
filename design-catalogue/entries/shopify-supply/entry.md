---
title: "Shopify Supply - Performance Pack"
url: https://shopify.supply/collections/performance-pack
source_url: https://shopify.supply/collections/performance-pack
captured: 2026-10-03
origin: raw-url
extract: none
category: consumer-brand
category2: "product-focused"
family: dark-merch-drop-scroller
dna: "Merch drop x graphite diagonal stripes, a polaroid scatter and a horizontal run of garments beside lifestyle photos"
register: warm photographic
grammar: gallery/catalog
lane: "A merch collection page: graphite ground with wide diagonal stripes, a stack of polaroid photos dealt onto the centre, 'Performance Pack' in heavy slanted caps over them, the polaroids scattering outward, then one long sideways run where a 3D garment turns beside each lifestyle photo with name, price and 'Quick view', a ticker of materials (cotton, 3D embroidery, rubber patch) running along the top."
mode: persuade
traits: ["diagonal stripe ground", "polaroid deal and scatter", "heavy italic display caps", "garment render beside lifestyle photo", "horizontal product run", "materials ticker"]
palette: ["#0F0F0F", "#B7B9B5", "#47463D"]
type: ["Inter-Variable", "Fraktion", "Condor"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Pairing each turning garment with a photo of someone wearing it answers how it looks on and what it is in one frame.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Shopify).

## What to borrow (principle)

- Pair each product render with an in-use photograph in a horizontal run

## What to leave

- Cookie dialog over the title

## Signature move

Polaroids dealt onto graphite and scattered under 'Performance Pack'.

## Motion

Intro: polaroids dealt one by one (~2 s). Wheel converted to horizontal travel: renders rotate; photos slide in; the materials ticker loops; quick-view buttons fade.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; WebGL canvas x1 (three.js); entry gate: Decline, Skip to content. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the gallery/catalog grammar: a merch collection page: graphite ground with wide diagonal stripes, a stack of polaroid photos dealt onto the centre, 'Performance Pack' in heavy slanted caps over them, the polaroids scattering outward, then one long sideways run where a 3D garment turns beside each lifestyle photo with name, price and 'Quick view', a ticker of materials (cotton, 3D embroidery, rubber patch) running along the top. Type: Inter-Variable, Fraktion, Condor.
Ground and ink from the measured palette (#0F0F0F, #B7B9B5, #47463D). Motion carries the page through
polaroids dealt onto graphite and scattered under 'Performance Pack'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — lifestyle photography, 3D garment renders

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: lifestyle photography, 3D garment renders

## Reference lock

Primary reference/direction: Shopify Supply - Performance Pack — A merch collection page: graphite ground with wide diagonal stripes, a stack of polaroid photos dealt onto the centre, 'Performance Pack' in heavy slanted caps over them, the polaroids scattering outward, then one long sideways run where a 3D garment turns beside each lifestyle photo with name, price and 'Quick view', a ticker of materials (cotton, 3D embroidery, rubber patch) running along the top.
Preserve (3-5 traits): diagonal stripe ground; polaroid deal and scatter; heavy italic display caps; garment render beside lifestyle photo; horizontal product run.
Borrow only (1-2): Pair each product render with an in-use photograph in a horizontal run
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: lifestyle photography, 3D garment renders
Reject: Cookie dialog over the title
Token commitments: palette #0F0F0F, #B7B9B5, #47463D; type Inter-Variable, Fraktion, Condor; engine GSAP + Lenis linked (never vendored).
