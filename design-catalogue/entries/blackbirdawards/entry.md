---
title: "Blackbird Awards"
url: https://blackbirdawards.com/
source_url: https://blackbirdawards.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: playful
category2: "institutional"
family: fire-bird-awards-countdown
dna: "Website awards x polygon blackbird in molten fire"
register: cinematic dark
grammar: live surface
lane: "An awards launch page: a pixel 'BLACKBIRD' logo, then a low-poly black bird statue standing in swirling molten orange fire with 'JOIN THE CREATIVE REVOLUTION' and a live countdown at the top."
mode: persuade
traits: ["low-poly black bird statue", "molten fire WebGL", "condensed caps headline with orange", "countdown timer", "pixel logo"]
palette: ["#000000", "#231510", "#974826", "#DAA861"]
type: ["Schabo", "Funnel Display"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

A single hero object (the award trophy as a polygon bird) in a living fire is the entire page, with a countdown that turns it into an event. It is a launch teaser built on one strong image.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One trophy object in a living WebGL element as a launch teaser
- A countdown as the only call to action

## What to leave

- Nothing scrolls
- Small subtext

## Signature move

A low-poly black bird standing in swirling molten fire.

## Motion

Intro: pixel logo letters reshuffle on black (~2.5 s). Then: the bird and fire fade in; headline wipes in with an orange bar; countdown ticks; fire swirls continuously (WebGL). Wheel does not move the page.

Measured (`motion/probe.json`): GSAP 3.13.0; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the live surface grammar: an awards launch page: a pixel 'BLACKBIRD' logo, then a low-poly black bird statue standing in swirling molten orange fire with 'JOIN THE CREATIVE REVOLUTION' and a live countdown at the top. Type: Schabo, Funnel Display.
Ground and ink from the measured palette (#000000, #231510, #974826). Motion carries the page through
a low-poly black bird standing in swirling molten fire. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — low-poly 3D statue in fiery fluid simulation

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: low-poly 3D statue in fiery fluid simulation

## Reference lock

Primary reference/direction: Blackbird Awards — An awards launch page: a pixel 'BLACKBIRD' logo, then a low-poly black bird statue standing in swirling molten orange fire with 'JOIN THE CREATIVE REVOLUTION' and a live countdown at the top.
Preserve (3-5 traits): low-poly black bird statue; molten fire WebGL; condensed caps headline with orange; countdown timer; pixel logo.
Borrow only (1-2): One trophy object in a living WebGL element as a launch teaser; A countdown as the only call to action
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: low-poly 3D statue in fiery fluid simulation
Reject: Nothing scrolls; Small subtext
Token commitments: palette #000000, #231510, #974826, #DAA861; type Schabo, Funnel Display; engine GSAP + Lenis linked (never vendored).
