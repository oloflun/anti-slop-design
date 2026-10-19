---
title: "Corentin Bernadou"
url: https://corentinbernadou.com/
source_url: https://corentinbernadou.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: photo-cube-orange-initials
dna: "Freelance developer folio x photo-tiled Rubik's cube"
register: cinematic dark
grammar: live surface
lane: "A black folio with giant orange initials 'FW' at the bottom left, a long column of project names down the right edge, and a Rubik's-cube made of project photos that tumbles and twists in the middle as you wheel."
mode: experience
traits: ["photo-tiled 3D Rubik's cube", "giant orange initials", "dense name list down the right edge", "black ground", "cube rotates and twists on wheel"]
palette: ["#080305", "#231D1D", "#B03E16", "#A6978B", "#9E5234"]
type: ["H"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

All the work is tiled onto one object you can play with, a Rubik's cube whose faces are project photos, twisting layer by layer. Next to a dense typographic index and one orange, the cube is the only image and the toy-like interaction is the signature.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Corentin Bernadou).

## What to borrow (principle)

- Tile project images onto one manipulable 3D object (a cube that twists by layers)
- Pair the object with a plain dense text index

## What to leave

- Photos are too small on the cube faces
- The index text is tiny

## Signature move

A Rubik's cube of project photos that twists layer by layer.

## Motion

Intro: black with a small percentage, then 'FW' rises with the name list and the cube drops in (~2.5 s). Wheel (Lenis, WebGL): the cube rotates and individual layers twist, revealing other photos; the index highlights the active project.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; WebGL canvas x1 (three.js); smoothed scroll (median 118 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the live surface grammar: a black folio with giant orange initials 'FW' at the bottom left, a long column of project names down the right edge, and a Rubik's-cube made of project photos that tumbles and twists in the middle as you wheel. Type: H.
Ground and ink from the measured palette (#080305, #231D1D, #B03E16). Motion carries the page through
a Rubik's cube of project photos that twists layer by layer. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — fashion and editorial photos as small square tiles

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: fashion and editorial photos as small square tiles

## Reference lock

Primary reference/direction: Corentin Bernadou — A black folio with giant orange initials 'FW' at the bottom left, a long column of project names down the right edge, and a Rubik's-cube made of project photos that tumbles and twists in the middle as you wheel.
Preserve (3-5 traits): photo-tiled 3D Rubik's cube; giant orange initials; dense name list down the right edge; black ground; cube rotates and twists on wheel.
Borrow only (1-2): Tile project images onto one manipulable 3D object (a cube that twists by layers); Pair the object with a plain dense text index
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: fashion and editorial photos as small square tiles
Reject: Photos are too small on the cube faces; The index text is tiny
Token commitments: palette #080305, #231D1D, #B03E16, #A6978B, #9E5234; type H; engine GSAP + Lenis linked (never vendored).
