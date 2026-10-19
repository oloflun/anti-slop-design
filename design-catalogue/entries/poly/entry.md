---
title: "Poly - the intelligent file browser"
url: https://poly.app/
source_url: https://poly.app/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: ""
family: desk-to-files-spill-saas
dna: "File browser app x a warm studio desk with a laptop; the camera dives into the screen and the files spill out onto a wooden desk"
register: warm photographic
grammar: filmic one-shot
lane: "A file app: 'The Intelligent File Browser' over a 3D studio desk (pegboard, pencils, tape, a laptop) where the laptop screen boots into the app's grid of files, the camera tilts and swoops past a falling pencil cup, the screen tips and files pour out in a motion-blurred rush, landing as a spread of photos, magazines, records and film strips on a wooden desk around 'Find your files naturally', then the spread rearranges as a search bar filters it."
mode: persuade
traits: ["3D studio desk", "laptop screen boots the product", "files pour out of the screen", "physical spread of media as the file system", "search filtering the physical spread"]
palette: ["#36251E", "#CBB8A6", "#594E47", "#926C5A", "#B29887"]
type: ["Bogue", "Haffer", "Haffer Variable"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Turning files into the photos, records and magazines they stand for makes 'browse naturally' literal: the product is shown as a desk you can sort.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Unseen Studio®).

## What to borrow (principle)

- Spill the product's contents out of the screen into a physical scene

## What to leave

- Hero copy low contrast over the desk

## Signature move

Files pouring out of a laptop screen onto a wooden desk as photos, records and magazines.

## Motion

Wheel: a pre-rendered camera move scrubbed across the desk; the screen boots; a motion-blurred pour transition; the spread rearranges per query.

Measured (`motion/probe.json`): GSAP 3.13.0; 13 video; split text; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the filmic one-shot grammar: a file app: 'The Intelligent File Browser' over a 3D studio desk (pegboard, pencils, tape, a laptop) where the laptop screen boots into the app's grid of files, the camera tilts and swoops past a falling pencil cup, the screen tips and files pour out in a motion-blurred rush, landing as a spread of photos, magazines, records and film strips on a wooden desk around 'Find your files naturally', then the spread rearranges as a search bar filters it. Type: Bogue, Haffer, Haffer Variable.
Ground and ink from the measured palette (#36251E, #CBB8A6, #594E47). Motion carries the page through
files pouring out of a laptop screen onto a wooden desk as photos, records and magazines. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D render sequence

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D render sequence

## Reference lock

Primary reference/direction: Poly - the intelligent file browser — A file app: 'The Intelligent File Browser' over a 3D studio desk (pegboard, pencils, tape, a laptop) where the laptop screen boots into the app's grid of files, the camera tilts and swoops past a falling pencil cup, the screen tips and files pour out in a motion-blurred rush, landing as a spread of photos, magazines, records and film strips on a wooden desk around 'Find your files naturally', then the spread rearranges as a search bar filters it.
Preserve (3-5 traits): 3D studio desk; laptop screen boots the product; files pour out of the screen; physical spread of media as the file system; search filtering the physical spread.
Borrow only (1-2): Spill the product's contents out of the screen into a physical scene
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D render sequence
Reject: Hero copy low contrast over the desk
Token commitments: palette #36251E, #CBB8A6, #594E47, #926C5A, #B29887; type Bogue, Haffer, Haffer Variable; engine GSAP + Lenis linked (never vendored).
