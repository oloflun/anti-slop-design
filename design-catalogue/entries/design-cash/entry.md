---
title: "Cash App Brand Guidelines"
url: https://design.cash.app/
source_url: https://design.cash.app/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: ""
family: brand-guidelines-asset-wall
dna: "Cash App guidelines x a black wall of brand assets drifting"
register: cinematic dark
grammar: gallery/catalog
lane: "A brand guidelines home: the dollar logo morphing through styles on black, then a black wall of brand assets (cards, 3D icons, illustrations, UI, photos) in rows drifting sideways at different speeds."
mode: read
traits: ["logo morphing loader", "wall of brand assets", "rows drifting sideways", "black ground", "green accent", "dense small footer text"]
palette: ["#000000", "#F3F3F2", "#468F5C", "#121E1B", "#A9A49B", "#282D35"]
type: ["CashSans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The asset wall shows the breadth of the brand system at a glance.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Drift rows of brand assets as a guideline homepage

## What to leave

- No guidance on the home itself

## Signature move

A black wall of Cash App assets drifting sideways.

## Motion

Intro: black, the logo morphs through styles to the green $ (~2 s). Wheel: rows drift sideways at different speeds.

Measured (`motion/probe.json`): GSAP 3.15.0; 31 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the gallery/catalog grammar: a brand guidelines home: the dollar logo morphing through styles on black, then a black wall of brand assets (cards, 3D icons, illustrations, UI, photos) in rows drifting sideways at different speeds. Type: CashSans.
Ground and ink from the measured palette (#000000, #F3F3F2, #468F5C). Motion carries the page through
a black wall of Cash App assets drifting sideways. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — brand assets, 3D icons

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: brand assets, 3D icons

## Reference lock

Primary reference/direction: Cash App Brand Guidelines — A brand guidelines home: the dollar logo morphing through styles on black, then a black wall of brand assets (cards, 3D icons, illustrations, UI, photos) in rows drifting sideways at different speeds.
Preserve (3-5 traits): logo morphing loader; wall of brand assets; rows drifting sideways; black ground; green accent.
Borrow only (1-2): Drift rows of brand assets as a guideline homepage
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: brand assets, 3D icons
Reject: No guidance on the home itself
Token commitments: palette #000000, #F3F3F2, #468F5C, #121E1B, #A9A49B, #282D35; type CashSans; engine GSAP + Lenis linked (never vendored).
