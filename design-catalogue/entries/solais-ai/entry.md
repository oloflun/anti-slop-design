---
title: "Solais - AI visibility platform"
url: https://solais.ai/
source_url: https://solais.ai/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: ""
family: burgundy-white-3d-blocks-ai
dna: "AI visibility tool x burgundy and white with 3D blocks floating and a white maze"
register: cinematic dark
grammar: chaptered editorial
lane: "A product page: a typed loader on burgundy, 'What is Solais?' with red 3D tiles over a wire grid, a white world where 'Discovering your voice' fades through steps (set your prompts, track responses, act with confidence) with small cubes drifting, 'Why brands choose Solais' over a white stepped maze with red icons, a giant 'SOLAIS' marquee, a dashboard on a monitor, 'Find your industry' cards and 'Take control of the conversation' with a live-users counter."
mode: persuade
traits: ["burgundy and white", "3D tiles and cubes", "white stepped maze", "mono caps", "giant marquee", "live counter"]
palette: ["#3C091F", "#F0F0F0", "#762D31", "#CFA49E"]
type: ["ki", "teknolog"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The white maze and the floating cubes give an abstract data product a physical stage; the colour split is clean.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: The Start).

## What to borrow (principle)

- Use a 3D maze as the ground for a 'why us' chapter

## What to leave

- Long typed loader

## Signature move

Red icon tiles floating over a white stepped maze.

## Motion

Intro: typed lines on burgundy (~4 s). Wheel (Lenis): tiles rotate over the grid; the world turns white; steps fade through; cubes drift; the maze rises and the camera moves over it; the marquee runs; the monitor tilts in.

Measured (`motion/probe.json`): GSAP 3.12.5; 1 pinned sections; Lenis; ScrollSmoother; WebGL canvas x1 (three.js); split text; smoothed scroll (median 132 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a product page: a typed loader on burgundy, 'What is Solais?' with red 3D tiles over a wire grid, a white world where 'Discovering your voice' fades through steps (set your prompts, track responses, act with confidence) with small cubes drifting, 'Why brands choose Solais' over a white stepped maze with red icons, a giant 'SOLAIS' marquee, a dashboard on a monitor, 'Find your industry' cards and 'Take control of the conversation' with a live-users counter. Type: ki, teknolog.
Ground and ink from the measured palette (#3C091F, #F0F0F0, #762D31). Motion carries the page through
red icon tiles floating over a white stepped maze. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D blocks, UI

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D blocks, UI

## Reference lock

Primary reference/direction: Solais - AI visibility platform — A product page: a typed loader on burgundy, 'What is Solais?' with red 3D tiles over a wire grid, a white world where 'Discovering your voice' fades through steps (set your prompts, track responses, act with confidence) with small cubes drifting, 'Why brands choose Solais' over a white stepped maze with red icons, a giant 'SOLAIS' marquee, a dashboard on a monitor, 'Find your industry' cards and 'Take control of the conversation' with a live-users counter.
Preserve (3-5 traits): burgundy and white; 3D tiles and cubes; white stepped maze; mono caps; giant marquee.
Borrow only (1-2): Use a 3D maze as the ground for a 'why us' chapter
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D blocks, UI
Reject: Long typed loader
Token commitments: palette #3C091F, #F0F0F0, #762D31, #CFA49E; type ki, teknolog; engine GSAP + Lenis linked (never vendored).
