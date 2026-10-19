---
title: "Adam Vromman"
url: https://adamvromman.net/en/
source_url: https://adamvromman.net/en/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: tumbling-3d-letters-grid-folio
dna: "Designer-developer x chunky 3D letters tumbling over a blueprint grid"
register: illustrated dark
grammar: live surface
lane: "A folio on a grid: a blueprint grid draws itself, then the name in blue, chunky 3D letters in red, green and blue tumbling across a project list on a coral grid, with a project preview (Kickstarter video illustration) and 'KICKSTARTER VIDEO' large at the bottom."
mode: experience
traits: ["blueprint grid drawing", "tumbling 3D letters", "coral and blue grid", "project list with highlight", "big project name bottom", "illustrated preview"]
palette: ["#EFEFEF", "#BEADB6", "#8C4B4E"]
type: ["Geist"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The tumbling letters bring physical play to a grid layout; hovering projects swaps the preview.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Tumble chunky 3D letters across a grid as a playful layer

## What to leave

- Letters cover the text

## Signature move

Chunky 3D letters tumbling across a coral blueprint grid.

## Motion

Intro: a grid draws in blue lines (~2 s), the name appears. Scroll (virtual): 3D letters keep tumbling and bouncing across the grid; the project preview changes per item.

Measured (`motion/probe.json`): GSAP 3.12.7; WebGL canvas x1 (three.js); 7 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the live surface grammar: a folio on a grid: a blueprint grid draws itself, then the name in blue, chunky 3D letters in red, green and blue tumbling across a project list on a coral grid, with a project preview (Kickstarter video illustration) and 'KICKSTARTER VIDEO' large at the bottom. Type: Geist.
Ground and ink from the measured palette (#EFEFEF, #BEADB6, #8C4B4E). Motion carries the page through
chunky 3D letters tumbling across a coral blueprint grid. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D letters, illustration

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D letters, illustration

## Reference lock

Primary reference/direction: Adam Vromman — A folio on a grid: a blueprint grid draws itself, then the name in blue, chunky 3D letters in red, green and blue tumbling across a project list on a coral grid, with a project preview (Kickstarter video illustration) and 'KICKSTARTER VIDEO' large at the bottom.
Preserve (3-5 traits): blueprint grid drawing; tumbling 3D letters; coral and blue grid; project list with highlight; big project name bottom.
Borrow only (1-2): Tumble chunky 3D letters across a grid as a playful layer
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D letters, illustration
Reject: Letters cover the text
Token commitments: palette #EFEFEF, #BEADB6, #8C4B4E; type Geist; engine GSAP + Lenis linked (never vendored).
