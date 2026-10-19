---
title: "PP Frama - Pangram Pangram typeface"
url: https://pp-frama.com/
source_url: https://pp-frama.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: editorial
category2: "product-focused"
family: industrial-type-specimen
dna: "Type specimen x chrome ducts and pipes, technical-sheet layouts and colour posters"
register: editorial print
grammar: typographic poster
lane: "A typeface launch: black loader, a lawn photo with 'Simplicity, versatility & clarity', a chrome Y-pipe, '2in1' in chrome letters, weight specimens in two columns, a spiral duct crossing the screen with letters, a 'Technical sheet' in pale blue, 'Engineered for efficiency' with a giant 'a', '100 % geometric', a 'shapes display' poster with a stacked toy, an orange 'try Frama' band, an engineering-manual page, accent sets, a 'Nails' poster, 'bring precision into your life' on a ramp, 'Baseform' on an orange case and closing colour posters."
mode: persuade
traits: ["chrome industrial objects", "technical-sheet layouts", "colour posters per chapter", "giant single glyph", "weight specimen columns"]
palette: ["#000000", "#C3C6C5", "#876430", "#588071", "#9B9B7E", "#AAB098"]
type: ["PP Frama Text Variable Light", "PP Frama Variable Thin", "PP Frama Black", "PP Frama Text Medium"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Industrial parts and engineering-sheet layouts make a geometric face feel machined, which is the claim of the font.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Pangram Pangram).

## What to borrow (principle)

- Stage the typeface on objects that share its geometry

## What to leave

- Some unreadable specimen blocks

## Signature move

A chrome Y-pipe on black introducing a geometric sans.

## Motion

Intro: black (~1 s). Wheel (Lenis, no GSAP): chrome renders rotate; poster sections slide; the ramp text slants in; colour bands wipe.

Measured (`motion/probe.json`): Lenis; 1 video; smoothed scroll (median 125 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the typographic poster grammar: a typeface launch: black loader, a lawn photo with 'Simplicity, versatility & clarity', a chrome Y-pipe, '2in1' in chrome letters, weight specimens in two columns, a spiral duct crossing the screen with letters, a 'Technical sheet' in pale blue, 'Engineered for efficiency' with a giant 'a', '100 % geometric', a 'shapes display' poster with a stacked toy, an orange 'try Frama' band, an engineering-manual page, accent sets, a 'Nails' poster, 'bring precision into your life' on a ramp, 'Baseform' on an orange case and closing colour posters. Type: PP Frama Text Variable Light, PP Frama Variable Thin, PP Frama Black, PP Frama Text Medium.
Ground and ink from the measured palette (#000000, #C3C6C5, #876430). Motion carries the page through
a chrome Y-pipe on black introducing a geometric sans. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D chrome renders, poster layouts

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D chrome renders, poster layouts

## Reference lock

Primary reference/direction: PP Frama - Pangram Pangram typeface — A typeface launch: black loader, a lawn photo with 'Simplicity, versatility & clarity', a chrome Y-pipe, '2in1' in chrome letters, weight specimens in two columns, a spiral duct crossing the screen with letters, a 'Technical sheet' in pale blue, 'Engineered for efficiency' with a giant 'a', '100 % geometric', a 'shapes display' poster with a stacked toy, an orange 'try Frama' band, an engineering-manual page, accent sets, a 'Nails' poster, 'bring precision into your life' on a ramp, 'Baseform' on an orange case and closing colour posters.
Preserve (3-5 traits): chrome industrial objects; technical-sheet layouts; colour posters per chapter; giant single glyph; weight specimen columns.
Borrow only (1-2): Stage the typeface on objects that share its geometry
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D chrome renders, poster layouts
Reject: Some unreadable specimen blocks
Token commitments: palette #000000, #C3C6C5, #876430, #588071, #9B9B7E, #AAB098; type PP Frama Text Variable Light, PP Frama Variable Thin, PP Frama Black, PP Frama Text Medium; engine GSAP + Lenis linked (never vendored).
