---
title: "Weisdevice - Xianyao Wei"
url: https://www.weisdevice.xyz/
source_url: https://www.weisdevice.xyz/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: retro-installer-floating-island
dna: "Creative technologist x a retro OS installer loader and a floating desk island"
register: illustrated dark
grammar: live surface
lane: "A folio as a toy: a retro Windows-style installer dialog loading files on sage green with a 'click and drag to explore' tip, a sketch frame, then a low-poly floating island with a cactus, a robot at a computer desk, power lines and signposts, which you can drag to rotate; scrolling pulls the camera back."
mode: experience
traits: ["retro installer dialog loader", "floating low-poly island", "robot at a computer as the self-portrait", "signposts as navigation", "sage green ground", "drag to rotate"]
palette: ["#C5DAA8", "#90804F"]
type: ["Pixellari", "VT323"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The installer gag sets a nostalgic tone and the island is the whole site as one explorable object.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A retro OS dialog as the loader
- One floating diorama as the whole navigation

## What to leave

- Scroll only zooms out
- Signposts too small to read

## Signature move

A robot at a desk on a floating cactus island after a retro installer loads.

## Motion

Intro: sage, a retro installer dialog fills its bar file by file (~4 s), a sketch frame draws, the island drops in. Wheel (virtual): the camera pulls back so the island shrinks to the centre; drag rotates it.

Measured (`motion/probe.json`): GSAP 3.13.0; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: ENTER (NO MUSIC). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the live surface grammar: a folio as a toy: a retro Windows-style installer dialog loading files on sage green with a 'click and drag to explore' tip, a sketch frame, then a low-poly floating island with a cactus, a robot at a computer desk, power lines and signposts, which you can drag to rotate; scrolling pulls the camera back. Type: Pixellari, VT323.
Ground and ink from the measured palette (#C5DAA8, #90804F). Motion carries the page through
a robot at a desk on a floating cactus island after a retro installer loads. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — low-poly 3D diorama

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: low-poly 3D diorama

## Reference lock

Primary reference/direction: Weisdevice - Xianyao Wei — A folio as a toy: a retro Windows-style installer dialog loading files on sage green with a 'click and drag to explore' tip, a sketch frame, then a low-poly floating island with a cactus, a robot at a computer desk, power lines and signposts, which you can drag to rotate; scrolling pulls the camera back.
Preserve (3-5 traits): retro installer dialog loader; floating low-poly island; robot at a computer as the self-portrait; signposts as navigation; sage green ground.
Borrow only (1-2): A retro OS dialog as the loader; One floating diorama as the whole navigation
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: low-poly 3D diorama
Reject: Scroll only zooms out; Signposts too small to read
Token commitments: palette #C5DAA8, #90804F; type Pixellari, VT323; engine GSAP + Lenis linked (never vendored).
