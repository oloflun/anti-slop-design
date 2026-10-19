---
title: "Gabriel Veres"
url: https://www.gabrielveres.com/
source_url: https://www.gabrielveres.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: 3d-card-corridor-folio
dna: "Web designer x a corridor of project screens receding in 3D"
register: cinematic dark
grammar: live surface
lane: "A designer folio on black: dozens of website screenshots arranged as a receding diagonal corridor of cards in 3D, the camera moving along them as you scroll so each project slides past (concept design, a restaurant, a Brooklyn property site, an elite talent agency)."
mode: experience
traits: ["3D corridor of screenshot cards", "diagonal recession", "camera moving through", "black ground", "small labels", "overview/index toggle"]
palette: ["#000000", "#1B201B", "#3F342C", "#686A5B", "#D4D5D2"]
type: ["__mabry_c4a60f", "__fkDisplay_9aebc6"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Turning the whole portfolio into one receding corridor makes browsing a camera move.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Arrange the work as a 3D corridor the camera travels along

## What to leave

- Hard to read any single project

## Signature move

A diagonal corridor of website screenshots receding into black.

## Motion

Intro: black, cards fly in and stack into the corridor (~2 s). Wheel (Lenis): the camera moves down the corridor; cards slide past and light up as they near; labels update.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the live surface grammar: a designer folio on black: dozens of website screenshots arranged as a receding diagonal corridor of cards in 3D, the camera moving along them as you scroll so each project slides past (concept design, a restaurant, a Brooklyn property site, an elite talent agency). Type: __mabry_c4a60f, __fkDisplay_9aebc6.
Ground and ink from the measured palette (#000000, #1B201B, #3F342C). Motion carries the page through
a diagonal corridor of website screenshots receding into black. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — website screenshots

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: website screenshots

## Reference lock

Primary reference/direction: Gabriel Veres — A designer folio on black: dozens of website screenshots arranged as a receding diagonal corridor of cards in 3D, the camera moving along them as you scroll so each project slides past (concept design, a restaurant, a Brooklyn property site, an elite talent agency).
Preserve (3-5 traits): 3D corridor of screenshot cards; diagonal recession; camera moving through; black ground; small labels.
Borrow only (1-2): Arrange the work as a 3D corridor the camera travels along
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: website screenshots
Reject: Hard to read any single project
Token commitments: palette #000000, #1B201B, #3F342C, #686A5B, #D4D5D2; type __mabry_c4a60f, __fkDisplay_9aebc6; engine GSAP + Lenis linked (never vendored).
