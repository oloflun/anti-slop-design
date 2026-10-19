---
title: "Andres Briganti"
url: https://briganti.works/
source_url: https://briganti.works/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: vertical-name-tile-scatter
dna: "Graphic designer x vertical name and an infinite scatter of work tiles"
register: modern clean
grammar: gallery/catalog
lane: "A designer folio on white: a giant vertical 'BRIGANTI' along the left edge and an infinite loop of scattered work tiles (a red poster, a type specimen, a building cover, 'The tragedy of Macbeth' specimen) scrolling past."
mode: read
traits: ["giant vertical name", "scattered work tiles", "infinite loop", "white ground", "type specimens", "small bio"]
palette: ["#FAFAFA", "#0B0C0C", "#71362D", "#928382", "#CED0D2"]
type: ["Inferi", "Roma Neue"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Simple and confident: the name stays put and the work scrolls forever.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Fix the name vertically and loop the work past it

## What to leave

- Loop repeats quickly

## Signature move

Work tiles scrolling past a giant vertical 'BRIGANTI'.

## Motion

Intro: white, tiles fade in. Wheel: tiles scroll in a loop at different speeds; the vertical name stays fixed.

Measured (`motion/probe.json`): GSAP 3.12.7; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the gallery/catalog grammar: a designer folio on white: a giant vertical 'BRIGANTI' along the left edge and an infinite loop of scattered work tiles (a red poster, a type specimen, a building cover, 'The tragedy of Macbeth' specimen) scrolling past. Type: Inferi, Roma Neue.
Ground and ink from the measured palette (#FAFAFA, #0B0C0C, #71362D). Motion carries the page through
work tiles scrolling past a giant vertical 'BRIGANTI'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — graphic design work

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: graphic design work

## Reference lock

Primary reference/direction: Andres Briganti — A designer folio on white: a giant vertical 'BRIGANTI' along the left edge and an infinite loop of scattered work tiles (a red poster, a type specimen, a building cover, 'The tragedy of Macbeth' specimen) scrolling past.
Preserve (3-5 traits): giant vertical name; scattered work tiles; infinite loop; white ground; type specimens.
Borrow only (1-2): Fix the name vertically and loop the work past it
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: graphic design work
Reject: Loop repeats quickly
Token commitments: palette #FAFAFA, #0B0C0C, #71362D, #928382, #CED0D2; type Inferi, Roma Neue; engine GSAP + Lenis linked (never vendored).
