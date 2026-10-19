---
title: "ITom"
url: https://itomdev.com/
source_url: https://itomdev.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: pencil-sketch-house-folio
dna: "3D developer folio x pencil-sketch house facade"
register: illustrated dark
grammar: live surface
lane: "A developer folio that loads on crumpled paper with a line tearing down it, then shows a pencil-sketched brick house with a 'PORTFOLIO' sign, a cat and a tree, the tech logos as stickers on the door."
mode: experience
traits: ["crumpled paper ground", "line that tears down the page (loader)", "pencil-sketch 3D scene", "tech logo stickers on the door", "explore prompt"]
palette: ["#D9D9D9", "#B7B7B7"]
type: ["Inter", "Cabin Sketch", "Rubik Scribble"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The folio is an illustrated place: a sketched house you can explore, with the skills stuck on the door like stickers. The paper texture and torn line loader keep it in one hand-drawn world.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Use a tearing line as the loader on a paper ground
- Put skills as stickers on an object in the scene

## What to leave

- Nothing scrolls; exploration is click-based
- Grey sketch at low contrast

## Signature move

A pencil-sketched house whose door is covered in tech-logo stickers.

## Motion

Intro: crumpled paper with a dashed circle and percentage 21 → 90 as a line draws/tears down the page (~2.5 s). Then: the sketched house scene; 'explore' prompt; idle animation (cat, tree). Wheel does not move the scene.

Measured (`motion/probe.json`): GSAP 3.14.2; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the live surface grammar: a developer folio that loads on crumpled paper with a line tearing down it, then shows a pencil-sketched brick house with a 'PORTFOLIO' sign, a cat and a tree, the tech logos as stickers on the door. Type: Inter, Cabin Sketch, Rubik Scribble.
Ground and ink from the measured palette (#D9D9D9, #B7B7B7). Motion carries the page through
a pencil-sketched house whose door is covered in tech-logo stickers. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — pencil-sketch 3D illustration on paper texture

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: pencil-sketch 3D illustration on paper texture

## Reference lock

Primary reference/direction: ITom — A developer folio that loads on crumpled paper with a line tearing down it, then shows a pencil-sketched brick house with a 'PORTFOLIO' sign, a cat and a tree, the tech logos as stickers on the door.
Preserve (3-5 traits): crumpled paper ground; line that tears down the page (loader); pencil-sketch 3D scene; tech logo stickers on the door; explore prompt.
Borrow only (1-2): Use a tearing line as the loader on a paper ground; Put skills as stickers on an object in the scene
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: pencil-sketch 3D illustration on paper texture
Reject: Nothing scrolls; exploration is click-based; Grey sketch at low contrast
Token commitments: palette #D9D9D9, #B7B7B7; type Inter, Cabin Sketch, Rubik Scribble; engine GSAP + Lenis linked (never vendored).
