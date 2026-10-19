---
title: "TILToooTILT (TOTE)"
url: https://tiltoootilt.tote.co.jp/
source_url: https://tiltoootilt.tote.co.jp/
captured: 2026-10-02
origin: raw-url
extract: none
category: playful
category2: ""
family: tilting-dark-physics-toy
dna: "Japanese studio experiment x physics toy on a striped dark stage"
register: illustrated dark
grammar: live surface
lane: "An experiment page: a dark striped stage with graffiti-like lettering and a small coloured object at centre that changes and tilts as you drag, with weight and inertia."
mode: experience
traits: ["dark red striped stage", "graffiti/brush lettering backdrop", "small object that swaps colour and tilts", "drag + inertia", "no scroll"]
palette: ["#340F0D", "#644A43", "#4C2521"]
type: []
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

'Everything has weight' is shown as a toy: an object you push, which tilts and settles with inertia on a moody striped stage. It is a pure Draggable/Inertia demonstration.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Tote Inc.).

## What to borrow (principle)

- Demonstrate weight with drag and inertia on a single object

## What to leave

- No content beyond the toy
- Dark low-contrast stage

## Signature move

A small object that tilts and settles with weight when you drag it.

## Motion

Intro: a dark shape glows at centre, the striped stage fades up (~2 s). Interaction (Draggable, Inertia, WebGL): the central object swaps colour on each push and tilts back to rest with inertia. Wheel does nothing.

Measured (`motion/probe.json`): GSAP 3.15.0; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the live surface grammar: an experiment page: a dark striped stage with graffiti-like lettering and a small coloured object at centre that changes and tilts as you drag, with weight and inertia. Type: read from the captures.
Ground and ink from the measured palette (#340F0D, #644A43, #4C2521). Motion carries the page through
a small object that tilts and settles with weight when you drag it. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — dark graphic stage with brush lettering

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: dark graphic stage with brush lettering

## Reference lock

Primary reference/direction: TILToooTILT (TOTE) — An experiment page: a dark striped stage with graffiti-like lettering and a small coloured object at centre that changes and tilts as you drag, with weight and inertia.
Preserve (3-5 traits): dark red striped stage; graffiti/brush lettering backdrop; small object that swaps colour and tilts; drag + inertia; no scroll.
Borrow only (1-2): Demonstrate weight with drag and inertia on a single object
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: dark graphic stage with brush lettering
Reject: No content beyond the toy; Dark low-contrast stage
Token commitments: palette #340F0D, #644A43, #4C2521; type -; engine GSAP + Lenis linked (never vendored).
