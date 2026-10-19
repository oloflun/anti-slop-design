---
title: "Maritime Fusion"
url: https://www.maritimefusion.com/
source_url: https://www.maritimefusion.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "institutional"
family: fusion-sun-ship-cutaway
dna: "Fusion energy for ships x a glowing plasma sphere that becomes the reactor inside an X-ray container ship, then an eclipse corona"
register: cinematic dark
grammar: filmic one-shot
lane: "A ship-fusion startup: a dot on black that ignites into a turbulent plasma sun, settles to a glowing sphere, then the camera pulls back so the sphere sits inside a translucent blue X-ray container ship, the ship gliding across, a cut into an orange eclipse corona behind 'The most proven approach to fusion', statements stepping over the corona, then markets (commercial ships, defence) with small ship drawings and an origin story card."
mode: persuade
traits: ["plasma sun from a single dot", "X-ray ship cutaway", "sphere becomes the reactor", "eclipse corona ground", "oversized statements cross-fading"]
palette: ["#000000", "#627A9F", "#ADB9CF", "#2D2E37", "#ECEDEF"]
type: ["Inter"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The sun from the intro becomes the reactor inside the ship, so the product's promise (a star in a hull) is shown in one camera move.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Flexy Global).

## What to borrow (principle)

- Let the intro object become the product's core inside a cutaway

## What to leave

- Statements cropped at the edges while transitioning

## Signature move

A glowing plasma sphere revealed inside a translucent X-ray container ship.

## Motion

Intro: a dot ignites into the sun (~4 s). Wheel (Lenis, 10 triggers): the camera dollies back to reveal the ship; the ship translates; a cut to the corona; statements scale and blur between; ship drawings slide in.

Measured (`motion/probe.json`): GSAP 3.15.0; 10 ScrollTriggers; Lenis; 5 video; smoothed scroll (median 132 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the filmic one-shot grammar: a ship-fusion startup: a dot on black that ignites into a turbulent plasma sun, settles to a glowing sphere, then the camera pulls back so the sphere sits inside a translucent blue X-ray container ship, the ship gliding across, a cut into an orange eclipse corona behind 'The most proven approach to fusion', statements stepping over the corona, then markets (commercial ships, defence) with small ship drawings and an origin story card. Type: Inter.
Ground and ink from the measured palette (#000000, #627A9F, #ADB9CF). Motion carries the page through
a glowing plasma sphere revealed inside a translucent X-ray container ship. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D renders, video

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D renders, video

## Reference lock

Primary reference/direction: Maritime Fusion — A ship-fusion startup: a dot on black that ignites into a turbulent plasma sun, settles to a glowing sphere, then the camera pulls back so the sphere sits inside a translucent blue X-ray container ship, the ship gliding across, a cut into an orange eclipse corona behind 'The most proven approach to fusion', statements stepping over the corona, then markets (commercial ships, defence) with small ship drawings and an origin story card.
Preserve (3-5 traits): plasma sun from a single dot; X-ray ship cutaway; sphere becomes the reactor; eclipse corona ground; oversized statements cross-fading.
Borrow only (1-2): Let the intro object become the product's core inside a cutaway
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D renders, video
Reject: Statements cropped at the edges while transitioning
Token commitments: palette #000000, #627A9F, #ADB9CF, #2D2E37, #ECEDEF; type Inter; engine GSAP + Lenis linked (never vendored).
