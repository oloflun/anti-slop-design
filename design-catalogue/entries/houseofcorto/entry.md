---
title: "House of Corto - Furniture by Jessica Mille"
url: https://www.houseofcorto.com/
source_url: https://www.houseofcorto.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "luxury-craft"
family: green-frame-furniture-wall
dna: "Furniture designer x olive green frames that scatter into a product wall"
register: warm photographic
grammar: gallery/catalog
lane: "A furniture house: an olive green framed card with 'CORTO', which shrinks to a small frame on cream, then many green frames tumble down and settle into a grid, filling with interiors and then with a wall of chairs, tables and stools shot in warm rooms."
mode: read
traits: ["olive green frame motif", "frames tumbling into a grid", "cream ground", "warm interior photography", "sculptural chairs", "virtual scroll grid"]
palette: ["#F2EFE7", "#3E2915", "#CFCAC0", "#BAAB99", "#715B45", "#9C714F"]
type: ["canada-type-gibson", "canora-frente"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The green frame is the brand's unit: it is the loader, then the shape every product sits in, so the catalogue grid is literally built from the logo.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Flot Noir, Thomas Carré).

## What to borrow (principle)

- Let the loader frame multiply into the grid cells

## What to leave

- Grid repeats without hierarchy
- Tiny captions

## Signature move

Olive green frames tumbling down and settling into a grid of chairs.

## Motion

Intro: a large green frame with 'CORTO' (~2 s) shrinks to a small frame on cream. Wheel (virtual, Barba): frames drop in a scattered pile, straighten into a grid and fill with interiors, then crossfade to a product wall that drifts as you scroll.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; Barba page transitions; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the gallery/catalog grammar: a furniture house: an olive green framed card with 'CORTO', which shrinks to a small frame on cream, then many green frames tumble down and settle into a grid, filling with interiors and then with a wall of chairs, tables and stools shot in warm rooms. Type: canada-type-gibson, canora-frente.
Ground and ink from the measured palette (#F2EFE7, #3E2915, #CFCAC0). Motion carries the page through
olive green frames tumbling down and settling into a grid of chairs. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — furniture and interior photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: furniture and interior photography

## Reference lock

Primary reference/direction: House of Corto - Furniture by Jessica Mille — A furniture house: an olive green framed card with 'CORTO', which shrinks to a small frame on cream, then many green frames tumble down and settle into a grid, filling with interiors and then with a wall of chairs, tables and stools shot in warm rooms.
Preserve (3-5 traits): olive green frame motif; frames tumbling into a grid; cream ground; warm interior photography; sculptural chairs.
Borrow only (1-2): Let the loader frame multiply into the grid cells
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: furniture and interior photography
Reject: Grid repeats without hierarchy; Tiny captions
Token commitments: palette #F2EFE7, #3E2915, #CFCAC0, #BAAB99, #715B45, #9C714F; type canada-type-gibson, canora-frente; engine GSAP + Lenis linked (never vendored).
