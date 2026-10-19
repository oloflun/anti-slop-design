---
title: "Thomas Monavon - Interactive Designer"
url: https://www.thomasmonavon.com/
source_url: https://www.thomasmonavon.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: split-checkerboard-folio
dna: "Interactive designer x a split checkerboard of project photos that swap halves"
register: modern clean
grammar: rhythmic cutlist
lane: "A designer folio: a white page split into a 2x2 checkerboard of project images and white cells (a Marlboro F1 helmet, a white flower, a skier, a green-lit object 'Rafting Pills', a red-lit helmet) with a small black thumbnail card and the client name and number (Gregory Lallé 01, Thibaud Fellay 02, Angus Emmerson 03, Makepill 04), where quadrants swap as you scroll and black panels cut in."
mode: read
traits: ["2x2 checkerboard of images and white", "quadrants swapping on scroll", "small black thumbnail card", "name and number labels", "black cut-in panels", "no colour except photos"]
palette: ["#FFFFFF", "#7695B9", "#291D1B", "#9DB3C9", "#08090B", "#C6BFB9"]
type: ["Lay Grotesk"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The checkerboard rhythm shows two images per project and keeps the grid alive through constant swaps.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Swap image quadrants in a checkerboard as the project changes

## What to leave

- Long black frames

## Signature move

A checkerboard of a Marlboro helmet, a white flower and a skier swapping halves.

## Motion

Intro: white (~1 s), the first images slide in. Wheel: quadrants slide out and in on each step; the small card swaps; names flip; black panels sweep across between projects.

Measured (`motion/probe.json`): GSAP 3.12.7; WebGL canvas x1; 50 video; split text; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the rhythmic cutlist grammar: a designer folio: a white page split into a 2x2 checkerboard of project images and white cells (a Marlboro F1 helmet, a white flower, a skier, a green-lit object 'Rafting Pills', a red-lit helmet) with a small black thumbnail card and the client name and number (Gregory Lallé 01, Thibaud Fellay 02, Angus Emmerson 03, Makepill 04), where quadrants swap as you scroll and black panels cut in. Type: Lay Grotesk.
Ground and ink from the measured palette (#FFFFFF, #7695B9, #291D1B). Motion carries the page through
a checkerboard of a Marlboro helmet, a white flower and a skier swapping halves. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project photography

## Reference lock

Primary reference/direction: Thomas Monavon - Interactive Designer — A designer folio: a white page split into a 2x2 checkerboard of project images and white cells (a Marlboro F1 helmet, a white flower, a skier, a green-lit object 'Rafting Pills', a red-lit helmet) with a small black thumbnail card and the client name and number (Gregory Lallé 01, Thibaud Fellay 02, Angus Emmerson 03, Makepill 04), where quadrants swap as you scroll and black panels cut in.
Preserve (3-5 traits): 2x2 checkerboard of images and white; quadrants swapping on scroll; small black thumbnail card; name and number labels; black cut-in panels.
Borrow only (1-2): Swap image quadrants in a checkerboard as the project changes
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project photography
Reject: Long black frames
Token commitments: palette #FFFFFF, #7695B9, #291D1B, #9DB3C9, #08090B, #C6BFB9; type Lay Grotesk; engine GSAP + Lenis linked (never vendored).
