---
title: "Studio K95"
url: https://k95.it/
source_url: https://k95.it/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: ultramarine-ribbon-gallery
dna: "Italian graphic studio x ultramarine field of floating work"
register: other
grammar: continuous world
lane: "An ultramarine field where dozens of poster and object images hang in 3D space around a silver ribbon sculpture that keeps reforming (a profile, a rose, a column), and wheeling flies the camera through the work."
mode: experience
traits: ["saturated ultramarine ground", "floating 3D cards of real work", "silver ribbon sculpture that morphs", "camera fly-through on wheel", "tiny white chrome"]
palette: ["#0A01C2", "#8B7385", "#C5C2BF", "#4C286E"]
type: ["adaptive"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

A studio with a lot of graphic work shows it as a cloud you fly through, with one silver sculpture at the centre that changes shape (a head, a flower, a column) as a signature. The single saturated blue unifies very different posters into one image.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One morphing centrepiece object as the studio's mark inside a gallery field
- A single saturated ground colour to unify varied work

## What to leave

- No scroll document; everything is in the WebGL scene
- Work is too small to read while flying

## Signature move

A silver ribbon sculpture that keeps reforming at the centre of a cloud of floating work.

## Motion

Intro: blue ground with 'scroll' prompt, then cards stream in around the ribbon (~2 s). Wheel (virtual, Lenis on a WebGL scene): the camera moves forward through the cloud; the ribbon morphs between a profile, a rose and a column; cards pass close enough to read occasionally.

Measured (`motion/probe.json`): Lenis; WebGL canvas x2 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the continuous world grammar: an ultramarine field where dozens of poster and object images hang in 3D space around a silver ribbon sculpture that keeps reforming (a profile, a rose, a column), and wheeling flies the camera through the work. Type: adaptive.
Ground and ink from the measured palette (#0A01C2, #8B7385, #C5C2BF). Motion carries the page through
a silver ribbon sculpture that keeps reforming at the centre of a cloud of floating work. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — graphic design work (posters, packaging) as flat cards, plus one chrome sculpture

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: graphic design work (posters, packaging) as flat cards, plus one chrome sculpture

## Reference lock

Primary reference/direction: Studio K95 — An ultramarine field where dozens of poster and object images hang in 3D space around a silver ribbon sculpture that keeps reforming (a profile, a rose, a column), and wheeling flies the camera through the work.
Preserve (3-5 traits): saturated ultramarine ground; floating 3D cards of real work; silver ribbon sculpture that morphs; camera fly-through on wheel; tiny white chrome.
Borrow only (1-2): One morphing centrepiece object as the studio's mark inside a gallery field; A single saturated ground colour to unify varied work
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: graphic design work (posters, packaging) as flat cards, plus one chrome sculpture
Reject: No scroll document; everything is in the WebGL scene; Work is too small to read while flying
Token commitments: palette #0A01C2, #8B7385, #C5C2BF, #4C286E; type adaptive; engine GSAP + Lenis linked (never vendored).
