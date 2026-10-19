---
title: "New Studio Partners - Brand Transformation Studio"
url: https://www.new.studio/
source_url: https://www.new.studio/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: silk-hero-serif-agency
dna: "Brand transformation studio x electric blue silk and italic serif"
register: editorial print
grammar: chaptered editorial
lane: "A brand studio: an electric blue 3D silk field behind an italic serif 'Transforming Brands, Building Futures', which dissolves away in an ink-splash wipe to a light page of serif statements, two-up case images, a full-bleed library case, an insights row and a blue footer with a giant wordmark."
mode: persuade
traits: ["electric blue 3D silk hero", "italic serif accents inside roman headlines", "ink-splash dissolve from hero to page", "floating pill nav", "two-up case images with tags", "giant wordmark in blue footer"]
palette: ["#354DCE", "#D5D5D5", "#F7F7F7", "#0A118E", "#768FD3", "#2528A9"]
type: ["FoundersGrotesk", "MartinaPlantijn"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The silk field and italic accents set a premium editorial tone, and the ink dissolve is the one memorable transition; the blue comes back in the footer so the page is bracketed by the same colour.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Dissolve a full colour hero into the page with a liquid wipe
- Bracket the page with the hero colour in the footer

## What to leave

- Generic case grid between the bookends
- Small tags under cases

## Signature move

Electric blue silk dissolving in an ink splash into a light serif page.

## Motion

Intro: white, then the silk field fades in and the serif headline resolves letter by letter (~2 s). Wheel (Lenis, ~120 px glide): the blue field dissolves away from the bottom in an ink-splash mask; statements reveal by line; case images slide up in pairs; a full-bleed case scales up; the footer arrives as a blue panel with the wordmark rising.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; WebGL canvas x1 (three.js); split text; smoothed scroll (median 126 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a brand studio: an electric blue 3D silk field behind an italic serif 'Transforming Brands, Building Futures', which dissolves away in an ink-splash wipe to a light page of serif statements, two-up case images, a full-bleed library case, an insights row and a blue footer with a giant wordmark. Type: FoundersGrotesk, MartinaPlantijn.
Ground and ink from the measured palette (#354DCE, #D5D5D5, #F7F7F7). Motion carries the page through
electric blue silk dissolving in an ink splash into a light serif page. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D silk, case photography and screen mockups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D silk, case photography and screen mockups

## Reference lock

Primary reference/direction: New Studio Partners - Brand Transformation Studio — A brand studio: an electric blue 3D silk field behind an italic serif 'Transforming Brands, Building Futures', which dissolves away in an ink-splash wipe to a light page of serif statements, two-up case images, a full-bleed library case, an insights row and a blue footer with a giant wordmark.
Preserve (3-5 traits): electric blue 3D silk hero; italic serif accents inside roman headlines; ink-splash dissolve from hero to page; floating pill nav; two-up case images with tags.
Borrow only (1-2): Dissolve a full colour hero into the page with a liquid wipe; Bracket the page with the hero colour in the footer
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D silk, case photography and screen mockups
Reject: Generic case grid between the bookends; Small tags under cases
Token commitments: palette #354DCE, #D5D5D5, #F7F7F7, #0A118E, #768FD3, #2528A9; type FoundersGrotesk, MartinaPlantijn; engine GSAP + Lenis linked (never vendored).
