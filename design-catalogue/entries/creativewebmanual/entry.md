---
title: "The Creative Website Manual"
url: https://www.creativewebmanual.com/
source_url: https://www.creativewebmanual.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: editorial
category2: "portfolio"
family: black-manual-chapters
dna: "Web design manual x black pages, a percentage loader, chapter cards and giant typographic interludes"
register: cinematic dark
grammar: chaptered editorial
lane: "A manual on making creative websites: a percentage loader with mono metadata, a white card 'Creativity' and '</Technicality>' merging, statements centred on black, chapters (design and development, grids and layouts, typography, colours, animations) each opened by a white or yellow shape breaking the grid, worked examples from real sites with notes, hover demos, a giant 'Practice' set in stretched line type, and a closing index of resources under a huge R."
mode: read
traits: ["percentage loader", "chapter cards breaking the grid", "worked examples with notes", "stretched line-type interlude", "giant initial index"]
palette: ["#070707", "#797979", "#1D1D1D", "#B2B2B2", "#464646"]
type: ["Ppneuemontreal", "Ppneuemontreal Variable", "Rand Mono", "Ppmondwest"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Each principle is followed immediately by a live example, so the manual demonstrates instead of asserting.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Ivor Jian).

## What to borrow (principle)

- Follow each principle with a live example on the page itself

## What to leave

- Very small mono notes

## Signature move

A white card where 'Creativity' and '</Technicality>' collide.

## Motion

Intro: counter 0-100 (~3 s). Wheel (Lenis, barba, 36 triggers): cards scale in; text splits by line; shapes cut across the grid; the 'Practice' lines stretch on scroll.

Measured (`motion/probe.json`): GSAP 3.15.0; 36 ScrollTriggers; 4 pinned sections; Lenis; Barba page transitions; 6 video; split text; smoothed scroll (median 88 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a manual on making creative websites: a percentage loader with mono metadata, a white card 'Creativity' and '</Technicality>' merging, statements centred on black, chapters (design and development, grids and layouts, typography, colours, animations) each opened by a white or yellow shape breaking the grid, worked examples from real sites with notes, hover demos, a giant 'Practice' set in stretched line type, and a closing index of resources under a huge R. Type: Ppneuemontreal, Ppneuemontreal Variable, Rand Mono, Ppmondwest.
Ground and ink from the measured palette (#070707, #797979, #1D1D1D). Motion carries the page through
a white card where 'Creativity' and '</Technicality>' collide. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — site screenshots, shapes

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: site screenshots, shapes

## Reference lock

Primary reference/direction: The Creative Website Manual — A manual on making creative websites: a percentage loader with mono metadata, a white card 'Creativity' and '</Technicality>' merging, statements centred on black, chapters (design and development, grids and layouts, typography, colours, animations) each opened by a white or yellow shape breaking the grid, worked examples from real sites with notes, hover demos, a giant 'Practice' set in stretched line type, and a closing index of resources under a huge R.
Preserve (3-5 traits): percentage loader; chapter cards breaking the grid; worked examples with notes; stretched line-type interlude; giant initial index.
Borrow only (1-2): Follow each principle with a live example on the page itself
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: site screenshots, shapes
Reject: Very small mono notes
Token commitments: palette #070707, #797979, #1D1D1D, #B2B2B2, #464646; type Ppneuemontreal, Ppneuemontreal Variable, Rand Mono, Ppmondwest; engine GSAP + Lenis linked (never vendored).
