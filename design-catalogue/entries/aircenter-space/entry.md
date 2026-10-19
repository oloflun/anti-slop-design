---
title: "AIR business center"
url: https://aircenter.space/
source_url: https://aircenter.space/
captured: 2026-10-03
origin: raw-url
extract: none
category: luxury-craft
category2: "institutional"
family: tower-office-white-split
dna: "Office towers x 'A I R' split wide and white spiral ribbons over glass architecture"
register: modern clean
grammar: chaptered editorial
lane: "A business centre: 'A I R' spread across white with a white spiral ribbon forming, full-bleed glass towers against the sky, caps paragraphs, 'A NEW PREMIUM FORMAT' split across the width, the spiral ribbon returning as a sculpture, 'AT THE CENTER OF LIFE' with a black location section (Mall, Metro station, Downtown, Highway tabs and minute counts) and a dark map, a plaza render, lobby renders with a wavy ceiling numbered 1, 2, and 'CHOOSE AN OFFICE' with 'A I R' split again on black."
mode: persuade
traits: ["letters split across the width", "white spiral ribbon sculpture", "glass tower renders", "caps paragraphs", "dark map with pins", "numbered lobby renders"]
palette: ["#FFFFFF", "#A4A29D", "#DDDEDE", "#B1BDCF", "#4C4C4C"]
type: ["Onest"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Splitting each heading across the full width echoes the airy, wide-open spaces being sold.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Vide Infra).

## What to borrow (principle)

- Split short headings across the full width

## What to leave

- Cookie bar in every frame

## Signature move

'A I R' spread across white with a spiral ribbon forming between the letters.

## Motion

Intro: white with 'A I R' and a spiral drawing (~2 s). Wheel: the tower image scales; paragraphs reveal; the heading splits apart; the ribbon spins; the black section rises with counters; the map draws; renders slide; the closing word splits.

Measured (`motion/probe.json`): Locomotive; Barba page transitions; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a business centre: 'A I R' spread across white with a white spiral ribbon forming, full-bleed glass towers against the sky, caps paragraphs, 'A NEW PREMIUM FORMAT' split across the width, the spiral ribbon returning as a sculpture, 'AT THE CENTER OF LIFE' with a black location section (Mall, Metro station, Downtown, Highway tabs and minute counts) and a dark map, a plaza render, lobby renders with a wavy ceiling numbered 1, 2, and 'CHOOSE AN OFFICE' with 'A I R' split again on black. Type: Onest.
Ground and ink from the measured palette (#FFFFFF, #A4A29D, #DDDEDE). Motion carries the page through
'A I R' spread across white with a spiral ribbon forming between the letters. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — architecture renders

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: architecture renders

## Reference lock

Primary reference/direction: AIR business center — A business centre: 'A I R' spread across white with a white spiral ribbon forming, full-bleed glass towers against the sky, caps paragraphs, 'A NEW PREMIUM FORMAT' split across the width, the spiral ribbon returning as a sculpture, 'AT THE CENTER OF LIFE' with a black location section (Mall, Metro station, Downtown, Highway tabs and minute counts) and a dark map, a plaza render, lobby renders with a wavy ceiling numbered 1, 2, and 'CHOOSE AN OFFICE' with 'A I R' split again on black.
Preserve (3-5 traits): letters split across the width; white spiral ribbon sculpture; glass tower renders; caps paragraphs; dark map with pins.
Borrow only (1-2): Split short headings across the full width
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: architecture renders
Reject: Cookie bar in every frame
Token commitments: palette #FFFFFF, #A4A29D, #DDDEDE, #B1BDCF, #4C4C4C; type Onest; engine GSAP + Lenis linked (never vendored).
