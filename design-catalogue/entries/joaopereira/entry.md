---
title: "João Pereira - Creative Developer"
url: https://www.joaopereira.dev/
source_url: https://www.joaopereira.dev/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: ""
family: teal-framed-gallery-dev
dna: "Creative developer x a framed project gallery sliding through a teal space"
register: cinematic dark
grammar: live surface
lane: "A developer folio on teal: 'Loading...' then a split counter 01/12, 'From concept to code. Interactive experiences, driven by passion.' in teal type, a framed dark panel of photos (a couple, a hooded figure) that drifts sideways across the teal with an orange label chip, more framed panels following, and a website mockup (a car accessory site) inside a frame."
mode: read
traits: ["teal ground with glow", "framed dark panels drifting sideways", "orange label chip", "split counter", "teal display type", "project mockup inside a frame"]
palette: ["#1D938B", "#186D67", "#020303", "#0C322F", "#1B1917", "#3FACA3"]
type: ["__clashMedium_c07759", "__clashBold_172e55"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Treating each project as a framed object drifting through one space keeps the folio calm.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Drift framed projects sideways through one coloured space

## What to leave

- Black frames while WebGL loads

## Signature move

A framed dark panel of photos drifting across teal.

## Motion

Intro: 'Loading...' then a rolling counter 01/12 (~2 s). Wheel: the headline lifts; framed panels drift left and grow; the orange chip moves between items; the next frame slides in.

Measured (`motion/probe.json`): GSAP 3.12.5; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Close. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the live surface grammar: a developer folio on teal: 'Loading...' then a split counter 01/12, 'From concept to code. Interactive experiences, driven by passion.' in teal type, a framed dark panel of photos (a couple, a hooded figure) that drifts sideways across the teal with an orange label chip, more framed panels following, and a website mockup (a car accessory site) inside a frame. Type: __clashMedium_c07759, __clashBold_172e55.
Ground and ink from the measured palette (#1D938B, #186D67, #020303). Motion carries the page through
a framed dark panel of photos drifting across teal. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project photography, mockups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project photography, mockups

## Reference lock

Primary reference/direction: João Pereira - Creative Developer — A developer folio on teal: 'Loading...' then a split counter 01/12, 'From concept to code. Interactive experiences, driven by passion.' in teal type, a framed dark panel of photos (a couple, a hooded figure) that drifts sideways across the teal with an orange label chip, more framed panels following, and a website mockup (a car accessory site) inside a frame.
Preserve (3-5 traits): teal ground with glow; framed dark panels drifting sideways; orange label chip; split counter; teal display type.
Borrow only (1-2): Drift framed projects sideways through one coloured space
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project photography, mockups
Reject: Black frames while WebGL loads
Token commitments: palette #1D938B, #186D67, #020303, #0C322F, #1B1917, #3FACA3; type __clashMedium_c07759, __clashBold_172e55; engine GSAP + Lenis linked (never vendored).
