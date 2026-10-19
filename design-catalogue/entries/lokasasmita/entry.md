---
title: "Alexander Lokasasmita"
url: http://lokasasmita.com/
source_url: http://lokasasmita.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: wordmark-black-panel-folio
dna: "Web dev and animation folio x giant name over a black panel"
register: modern clean
grammar: typographic poster
lane: "A minimal folio: a tiny counter on white, a black bar that grows into a rectangle and expands to fill the lower half, then the giant 'lokasasmita' name sits on the line between white and black with a small intro and nav above."
mode: read
traits: ["counter loader", "bar that grows into the layout", "giant lowercase name", "white over black split", "small flower mark", "minimal nav"]
palette: ["#FFFFFF", "#1A1A1A", "#2F2F2F", "#CACACA", "#878787", "#E8E8E8"]
type: ["Satoshi-Bold", "Satoshi-Variable"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The loader becomes the layout: the bar grows into the black half the name stands on, so the intro and the hero are one shot.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Let the loader shape grow into the hero layout

## What to leave

- Capture never got past the hero
- Small intro copy

## Signature move

A loading bar that grows into the black half under a giant name.

## Motion

Intro: white, a tiny counter to 100, a thin black bar grows, thickens into a rectangle and expands to the full lower half as the name slides up onto the edge (~3 s). Wheel: no movement captured past the hero.

Measured (`motion/probe.json`): GSAP 3.13.0; WebGL canvas x2 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the typographic poster grammar: a minimal folio: a tiny counter on white, a black bar that grows into a rectangle and expands to fill the lower half, then the giant 'lokasasmita' name sits on the line between white and black with a small intro and nav above. Type: Satoshi-Bold, Satoshi-Variable.
Ground and ink from the measured palette (#FFFFFF, #1A1A1A, #2F2F2F). Motion carries the page through
a loading bar that grows into the black half under a giant name. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — none in the hero

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: none in the hero

## Reference lock

Primary reference/direction: Alexander Lokasasmita — A minimal folio: a tiny counter on white, a black bar that grows into a rectangle and expands to fill the lower half, then the giant 'lokasasmita' name sits on the line between white and black with a small intro and nav above.
Preserve (3-5 traits): counter loader; bar that grows into the layout; giant lowercase name; white over black split; small flower mark.
Borrow only (1-2): Let the loader shape grow into the hero layout
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: none in the hero
Reject: Capture never got past the hero; Small intro copy
Token commitments: palette #FFFFFF, #1A1A1A, #2F2F2F, #CACACA, #878787, #E8E8E8; type Satoshi-Bold, Satoshi-Variable; engine GSAP + Lenis linked (never vendored).
