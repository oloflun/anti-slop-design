---
title: "Smooothy - slider library"
url: https://smooothy.federic.ooo/
source_url: https://smooothy.federic.ooo/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: "playful"
family: bubble-type-library-site
dna: "Open-source slider library x giant bubble letters and food illustrations"
register: illustrated dark
grammar: chaptered editorial
lane: "A library site on black: a food-illustration slider demo, then chapters each named by a giant puffy white bubble word ('SET', 'GET', 'MESLI', 'WEBGL', 'READY', 'USE', 'OPEN SOURCE') that tumbles in, with thin-line icons explaining features (infinite, snapping, lerp, callbacks) and a WebGL ramen bowl for the WebGL section, ending on 'SMOOOTHY'."
mode: persuade
traits: ["giant puffy bubble words", "thin-line feature icons", "black ground", "food illustration demos", "WebGL ramen bowl", "chapter words tumbling in"]
palette: ["#000000", "#FFFFFF", "#606061", "#424242", "#171717", "#A1A1A1"]
type: ["Geist Mono", "Geist"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Giant bubble words as chapter titles give a developer library a playful, memorable voice, and each chapter demonstrates the slider itself.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Federico Valla).

## What to borrow (principle)

- Name each chapter with one giant playful word

## What to leave

- Very small feature text

## Signature move

Giant puffy white words like 'SET' and 'GET' tumbling across black.

## Motion

Intro: black with a dot loader (~2 s), the food slider. Wheel (Lenis, 242 split): each bubble word tumbles in and bounces; line icons draw; the ramen bowl rotates in 3D; words wobble as they exit.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x1 (three.js); split text; smoothed scroll (median 129 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the chaptered editorial grammar: a library site on black: a food-illustration slider demo, then chapters each named by a giant puffy white bubble word ('SET', 'GET', 'MESLI', 'WEBGL', 'READY', 'USE', 'OPEN SOURCE') that tumbles in, with thin-line icons explaining features (infinite, snapping, lerp, callbacks) and a WebGL ramen bowl for the WebGL section, ending on 'SMOOOTHY'. Type: Geist Mono, Geist.
Ground and ink from the measured palette (#000000, #FFFFFF, #606061). Motion carries the page through
giant puffy white words like 'SET' and 'GET' tumbling across black. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — food illustration, 3D ramen

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: food illustration, 3D ramen

## Reference lock

Primary reference/direction: Smooothy - slider library — A library site on black: a food-illustration slider demo, then chapters each named by a giant puffy white bubble word ('SET', 'GET', 'MESLI', 'WEBGL', 'READY', 'USE', 'OPEN SOURCE') that tumbles in, with thin-line icons explaining features (infinite, snapping, lerp, callbacks) and a WebGL ramen bowl for the WebGL section, ending on 'SMOOOTHY'.
Preserve (3-5 traits): giant puffy bubble words; thin-line feature icons; black ground; food illustration demos; WebGL ramen bowl.
Borrow only (1-2): Name each chapter with one giant playful word
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: food illustration, 3D ramen
Reject: Very small feature text
Token commitments: palette #000000, #FFFFFF, #606061, #424242, #171717, #A1A1A1; type Geist Mono, Geist; engine GSAP + Lenis linked (never vendored).
