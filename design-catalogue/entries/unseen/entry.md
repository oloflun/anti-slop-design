---
title: "Unseen Studio - brand, digital, motion"
url: https://unseen.co/
source_url: https://unseen.co/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: ""
family: pastel-arch-water-hero
dna: "Studio x a pastel 3D room of arches, stairs and a water floor, 'Creating the unexpected' in a light serif"
register: cinematic dark
grammar: live surface
lane: "A studio landing: a loader where 'Unseen' becomes a pair of googly eyes, an Enter button, then a still WebGL room in pink plaster with arched openings, a stair, a stone and a reflective water floor, 'Creating the unexpected' set in a light italic serif over it with a small 'View our work' button. The page does not scroll; the scene breathes with the pointer."
mode: experience
traits: ["pastel 3D architecture", "water reflection floor", "googly-eye loader", "light serif over WebGL", "single-screen hero"]
palette: ["#A58C93", "#EBCCC9", "#89767F", "#BFA7AB", "#F5E9EF"]
type: ["Neue Montreal", "Saol Display"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

One calm, surreal room is enough to say 'unexpected' without a list of projects on the first screen.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase.

## What to borrow (principle)

- One still, surreal room as the whole first impression

## What to leave

- Enter gate
- No scroll path

## Signature move

A pink plaster room with arches over a reflective water floor.

## Motion

Intro: letters to googly eyes (~2 s), Enter. Pointer-driven camera drift; no scroll.

Measured (`motion/probe.json`): GSAP 3.6.0; WebGL canvas x1 (three.js); split text; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: ENTER WITHOUT AUDIO. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the live surface grammar: a studio landing: a loader where 'Unseen' becomes a pair of googly eyes, an Enter button, then a still WebGL room in pink plaster with arched openings, a stair, a stone and a reflective water floor, 'Creating the unexpected' set in a light italic serif over it with a small 'View our work' button. The page does not scroll; the scene breathes with the pointer. Type: Neue Montreal, Saol Display.
Ground and ink from the measured palette (#A58C93, #EBCCC9, #89767F). Motion carries the page through
a pink plaster room with arches over a reflective water floor. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL 3D scene

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL 3D scene

## Reference lock

Primary reference/direction: Unseen Studio - brand, digital, motion — A studio landing: a loader where 'Unseen' becomes a pair of googly eyes, an Enter button, then a still WebGL room in pink plaster with arched openings, a stair, a stone and a reflective water floor, 'Creating the unexpected' set in a light italic serif over it with a small 'View our work' button. The page does not scroll; the scene breathes with the pointer.
Preserve (3-5 traits): pastel 3D architecture; water reflection floor; googly-eye loader; light serif over WebGL; single-screen hero.
Borrow only (1-2): One still, surreal room as the whole first impression
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL 3D scene
Reject: Enter gate; No scroll path
Token commitments: palette #A58C93, #EBCCC9, #89767F, #BFA7AB, #F5E9EF; type Neue Montreal, Saol Display; engine GSAP + Lenis linked (never vendored).
