---
title: "NOVA - Exploring Mars"
url: http://nova-mars-exploration.webflow.io/
source_url: http://nova-mars-exploration.webflow.io/
captured: 2026-10-02
origin: raw-url
extract: none
category: editorial
category2: "playful"
family: mars-scrollytelling-webflow
dna: "Webflow GSAP challenge x a Mars journey with a glowing robot companion"
register: cinematic dark
grammar: continuous world
lane: "A Mars storytelling piece: a small robot with two glowing eyes as the loader, 'MARS' over a red planet, then a journey: asteroids, orbit diagram from Earth to Mars, an astronaut on grey regolith, temperature extremes, Olympus Mons, dust storms, a rover, the suit, the lander, facts and sunset, with a blurred orange glow (the robot's light) following the scroll the whole way."
mode: experience
traits: ["robot guide with glowing eyes", "orange glow that follows the scroll", "wide extended display type", "orbit diagram", "AI-generated Mars imagery", "mono captions"]
palette: ["#704F3D", "#060606", "#1B1B1B", "#8C8073"]
type: ["Thegoodmonolith", "Panchang"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The glowing companion is the signature object that stays in frame through every chapter, so a long set of facts reads as one guided walk.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A small guide object whose glow stays in frame through every section

## What to leave

- The glow covers content
- Imagery quality uneven

## Signature move

A glowing orange robot light following you across Mars.

## Motion

Intro: black 'loading Mars', two robot eyes blink on (~2 s), START (unlocked). Wheel (native, 52 triggers): the planet rises behind 'MARS'; asteroids fly past; orbit lines draw from Earth to Mars; the astronaut walks; sections fade between grey and orange; the dust storm sweeps; the lander scales up behind the giant word; facts count up; the glow stays centred throughout.

Measured (`motion/probe.json`): GSAP 3.15.0; 52 ScrollTriggers; split text; entry gate: START EXPLORING. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the continuous world grammar: a Mars storytelling piece: a small robot with two glowing eyes as the loader, 'MARS' over a red planet, then a journey: asteroids, orbit diagram from Earth to Mars, an astronaut on grey regolith, temperature extremes, Olympus Mons, dust storms, a rover, the suit, the lander, facts and sunset, with a blurred orange glow (the robot's light) following the scroll the whole way. Type: Thegoodmonolith, Panchang.
Ground and ink from the measured palette (#704F3D, #060606, #1B1B1B). Motion carries the page through
a glowing orange robot light following you across Mars. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — Mars renders and AI imagery

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: Mars renders and AI imagery

## Reference lock

Primary reference/direction: NOVA - Exploring Mars — A Mars storytelling piece: a small robot with two glowing eyes as the loader, 'MARS' over a red planet, then a journey: asteroids, orbit diagram from Earth to Mars, an astronaut on grey regolith, temperature extremes, Olympus Mons, dust storms, a rover, the suit, the lander, facts and sunset, with a blurred orange glow (the robot's light) following the scroll the whole way.
Preserve (3-5 traits): robot guide with glowing eyes; orange glow that follows the scroll; wide extended display type; orbit diagram; AI-generated Mars imagery.
Borrow only (1-2): A small guide object whose glow stays in frame through every section
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: Mars renders and AI imagery
Reject: The glow covers content; Imagery quality uneven
Token commitments: palette #704F3D, #060606, #1B1B1B, #8C8073; type Thegoodmonolith, Panchang; engine GSAP + Lenis linked (never vendored).
