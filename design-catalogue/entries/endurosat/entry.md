---
title: "EnduroSat - space missions made simple"
url: https://www.endurosat.com/space-service
source_url: https://www.endurosat.com/space-service
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "institutional"
family: night-earth-satellite-console
dna: "Satellite operator x a night Earth limb, wireframe satellites and a mission console on deep navy"
register: cinematic dark
grammar: continuous world
lane: "A satellite service as one orbit: 'Space missions made simple' beside a satellite drifting over the Earth's limb, a zoom down to a satellite image of a coastline ('Define'), chapters 'Receive', 'Command your fleet', 'Access your data' as dashboards projected on the globe, 'Software flexible' with satellites crossing, a blue wireframe bus opened into modules, 'Fixed cost' with a slider from 50 satellites to 30 M, a counter of cost per gigabyte rolling down to 1, and 'Get to orbit today' over the limb, then client logos and a large footer."
mode: persuade
traits: ["night Earth limb", "wireframe satellite exploded", "dashboards projected on the globe", "segmented progress bar of chapters", "rolling cost counter", "blue accent on navy"]
palette: ["#000000", "#141A24", "#243654", "#58789A"]
type: ["Magnetik"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Keeping the Earth in every frame makes a B2B service feel like one mission, and the counter rolling a price down to 1 turns the pricing argument into the climax.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: 60fps, Kreativa Studio).

## What to borrow (principle)

- Let the pricing argument be the scrubbed climax, not a table

## What to leave

- Long footer

## Signature move

A cost counter rolling down to 1 USD/GB over the dark globe.

## Motion

Intro: cookie gate, satellite drifts in (~2 s). Wheel (Lenis, swup, 8 triggers): camera dives to the coastline and pulls back; dashboards fade onto the globe; the wireframe bus explodes; slider and counter are scrubbed; a segmented bar tracks the chapter.

Measured (`motion/probe.json`): GSAP 3.15.0/3.13.0; 8 ScrollTriggers; Lenis; Swup page transitions; WebGL canvas x1 (three.js); split text; smoothed scroll (median 117 px still travelling after input stops); entry gate: Reject All, LAUNCH LAUNCH LAUNCH. Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the continuous world grammar: a satellite service as one orbit: 'Space missions made simple' beside a satellite drifting over the Earth's limb, a zoom down to a satellite image of a coastline ('Define'), chapters 'Receive', 'Command your fleet', 'Access your data' as dashboards projected on the globe, 'Software flexible' with satellites crossing, a blue wireframe bus opened into modules, 'Fixed cost' with a slider from 50 satellites to 30 M, a counter of cost per gigabyte rolling down to 1, and 'Get to orbit today' over the limb, then client logos and a large footer. Type: Magnetik.
Ground and ink from the measured palette (#000000, #141A24, #243654). Motion carries the page through
a cost counter rolling down to 1 USD/GB over the dark globe. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL globe, satellite renders, UI

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL globe, satellite renders, UI

## Reference lock

Primary reference/direction: EnduroSat - space missions made simple — A satellite service as one orbit: 'Space missions made simple' beside a satellite drifting over the Earth's limb, a zoom down to a satellite image of a coastline ('Define'), chapters 'Receive', 'Command your fleet', 'Access your data' as dashboards projected on the globe, 'Software flexible' with satellites crossing, a blue wireframe bus opened into modules, 'Fixed cost' with a slider from 50 satellites to 30 M, a counter of cost per gigabyte rolling down to 1, and 'Get to orbit today' over the limb, then client logos and a large footer.
Preserve (3-5 traits): night Earth limb; wireframe satellite exploded; dashboards projected on the globe; segmented progress bar of chapters; rolling cost counter.
Borrow only (1-2): Let the pricing argument be the scrubbed climax, not a table
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL globe, satellite renders, UI
Reject: Long footer
Token commitments: palette #000000, #141A24, #243654, #58789A; type Magnetik; engine GSAP + Lenis linked (never vendored).
