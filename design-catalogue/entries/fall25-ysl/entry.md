---
title: "Saint Laurent - Fall 25"
url: https://fall25.ysl.com/women
source_url: https://fall25.ysl.com/women
captured: 2026-10-03
origin: raw-url
extract: none
category: luxury-craft
category2: "editorial"
family: monochrome-campaign-scroll
dna: "Fashion campaign x black-and-white photography on white, photos stepping in at different sizes and offsets, tiny product credits"
register: editorial print
grammar: gallery/catalog
lane: "A fashion campaign: the logo on white, two portraits appearing, then a long column of black-and-white campaign photos at varying sizes and positions that slide and crop as you scroll, product shots (sunglasses, jacket) in a small carousel beside the look, tiny numbered credits, close crops of leather and hair, and an 'Explore men' link at the end."
mode: persuade
traits: ["black-and-white photography only", "varying frame sizes and offsets", "tiny numbered credits", "product carousel beside the look"]
palette: ["#FFFFFF", "#BDBDBD", "#272727", "#060606", "#494949", "#838383"]
type: ["Helvetica Neue"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Varying the size and offset of every photo makes a simple scroll of images feel edited like a printed lookbook.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase.

## What to borrow (principle)

- Vary frame size and offset like a lookbook spread

## What to leave

- Microscopic credits

## Signature move

Black-and-white campaign photos stepping in at different sizes on white.

## Motion

Wheel: photos translate at different speeds and crop with masks; the carousel slides.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; 3 video; smoothed scroll (median 198 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the gallery/catalog grammar: a fashion campaign: the logo on white, two portraits appearing, then a long column of black-and-white campaign photos at varying sizes and positions that slide and crop as you scroll, product shots (sunglasses, jacket) in a small carousel beside the look, tiny numbered credits, close crops of leather and hair, and an 'Explore men' link at the end. Type: Helvetica Neue.
Ground and ink from the measured palette (#FFFFFF, #BDBDBD, #272727). Motion carries the page through
black-and-white campaign photos stepping in at different sizes on white. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — black-and-white fashion photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: black-and-white fashion photography

## Reference lock

Primary reference/direction: Saint Laurent - Fall 25 — A fashion campaign: the logo on white, two portraits appearing, then a long column of black-and-white campaign photos at varying sizes and positions that slide and crop as you scroll, product shots (sunglasses, jacket) in a small carousel beside the look, tiny numbered credits, close crops of leather and hair, and an 'Explore men' link at the end.
Preserve (3-5 traits): black-and-white photography only; varying frame sizes and offsets; tiny numbered credits; product carousel beside the look.
Borrow only (1-2): Vary frame size and offset like a lookbook spread
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: black-and-white fashion photography
Reject: Microscopic credits
Token commitments: palette #FFFFFF, #BDBDBD, #272727, #060606, #494949, #838383; type Helvetica Neue; engine GSAP + Lenis linked (never vendored).
