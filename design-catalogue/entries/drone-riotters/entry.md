---
title: "Aevion - LiDAR inspection drone"
url: https://drone.riotters.com/
source_url: https://drone.riotters.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: ""
family: white-drone-spec-scroll
dna: "Inspection drone x one white drone that turns as specs change"
register: modern clean
grammar: chaptered editorial
lane: "A product page on white: a tiny counter, 'Autonomous LiDAR inspection systems', 'Detecting cracks, deformations and structural risks before they become failures' with words darkening, a white drone hovering with spinning props, 'Gear', spec columns (5 returns, ±2 cm, 450 m) lighting in turn as the drone rotates, 'Solutions' with tabs (Energy, Infrastructure, Industry, Geospatial) and a solar field photo, 'Capabilities' with Scan, Connection and Compactness while the drone turns top-down and folds."
mode: persuade
traits: ["white drone on white", "spec columns lighting in turn", "words darkening", "product rotating per feature", "tabs with photo", "thin grotesk"]
palette: ["#FDFDFD", "#D2D5D5", "#939899"]
type: ["switzer", "protoMono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

One product rotating to show the feature being described keeps the spec list concrete.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Riotters).

## What to borrow (principle)

- Rotate the product to face each spec as it lights

## What to leave

- Very light grey text

## Signature move

A white drone hovering above spec columns that light in turn.

## Motion

Intro: white counter (~2 s). Wheel (Lenis): the headline words darken; the drone flies in and hovers; it rotates as spec columns highlight; tabs swap photos; the drone turns top-down and folds for 'Compactness'.

Measured (`motion/probe.json`): Lenis; WebGL canvas x2 (three.js); 3 video; split text; smoothed scroll (median 90 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a product page on white: a tiny counter, 'Autonomous LiDAR inspection systems', 'Detecting cracks, deformations and structural risks before they become failures' with words darkening, a white drone hovering with spinning props, 'Gear', spec columns (5 returns, ±2 cm, 450 m) lighting in turn as the drone rotates, 'Solutions' with tabs (Energy, Infrastructure, Industry, Geospatial) and a solar field photo, 'Capabilities' with Scan, Connection and Compactness while the drone turns top-down and folds. Type: switzer, protoMono.
Ground and ink from the measured palette (#FDFDFD, #D2D5D5, #939899). Motion carries the page through
a white drone hovering above spec columns that light in turn. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D product

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D product

## Reference lock

Primary reference/direction: Aevion - LiDAR inspection drone — A product page on white: a tiny counter, 'Autonomous LiDAR inspection systems', 'Detecting cracks, deformations and structural risks before they become failures' with words darkening, a white drone hovering with spinning props, 'Gear', spec columns (5 returns, ±2 cm, 450 m) lighting in turn as the drone rotates, 'Solutions' with tabs (Energy, Infrastructure, Industry, Geospatial) and a solar field photo, 'Capabilities' with Scan, Connection and Compactness while the drone turns top-down and folds.
Preserve (3-5 traits): white drone on white; spec columns lighting in turn; words darkening; product rotating per feature; tabs with photo.
Borrow only (1-2): Rotate the product to face each spec as it lights
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D product
Reject: Very light grey text
Token commitments: palette #FDFDFD, #D2D5D5, #939899; type switzer, protoMono; engine GSAP + Lenis linked (never vendored).
