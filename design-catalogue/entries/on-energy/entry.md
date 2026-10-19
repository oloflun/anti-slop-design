---
title: "ON.energy - grid-safe AI power"
url: https://www.on.energy/
source_url: https://www.on.energy/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "institutional"
family: black-yellow-industrial-hardware
dna: "Energy hardware x black studio, a grey UPS cabinet that multiplies into a field, and yellow blocks"
register: cinematic dark
grammar: chaptered editorial
lane: "An energy hardware company: 'Grid-safe power for AI factories' over a lit grey UPS cabinet, a yellow panel with the company statement that slides up over the hero, the cabinet seen from the side ('ERCOT-grade voltage ride-through'), then duplicated into a row and a whole field of units under a spotlight, feature cards, testimonial, yellow light streaks behind 'Performance proven at scale', stat cards (3 GW, 99.9 %), news and a yellow footer."
mode: persuade
traits: ["single product multiplied into a field", "yellow statement panel over the hero", "spotlit cabinets", "yellow light streaks", "stat cards"]
palette: ["#606369", "#090B0A", "#313334", "#9B9C93", "#484B4E", "#1D1F1F"]
type: ["Univers Next Pro", "ABC Monument Grotesk Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Showing one cabinet and then a field of them makes scale visible without a chart.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Studio 28K).

## What to borrow (principle)

- Multiply the one product into a field to show scale

## What to leave

- Generic news grid at the end

## Signature move

One grey cabinet duplicating into a spotlit field of units.

## Motion

Intro: the cabinet lights up (~1 s). Wheel (Lenis, smoothed): the yellow panel wipes over; the camera turns to the side; units duplicate and recede; streaks sweep; stats count.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x1 (three.js); 2 video; smoothed scroll (median 155 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: an energy hardware company: 'Grid-safe power for AI factories' over a lit grey UPS cabinet, a yellow panel with the company statement that slides up over the hero, the cabinet seen from the side ('ERCOT-grade voltage ride-through'), then duplicated into a row and a whole field of units under a spotlight, feature cards, testimonial, yellow light streaks behind 'Performance proven at scale', stat cards (3 GW, 99.9 %), news and a yellow footer. Type: Univers Next Pro, ABC Monument Grotesk Mono.
Ground and ink from the measured palette (#606369, #090B0A, #313334). Motion carries the page through
one grey cabinet duplicating into a spotlit field of units. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D product renders

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D product renders

## Reference lock

Primary reference/direction: ON.energy - grid-safe AI power — An energy hardware company: 'Grid-safe power for AI factories' over a lit grey UPS cabinet, a yellow panel with the company statement that slides up over the hero, the cabinet seen from the side ('ERCOT-grade voltage ride-through'), then duplicated into a row and a whole field of units under a spotlight, feature cards, testimonial, yellow light streaks behind 'Performance proven at scale', stat cards (3 GW, 99.9 %), news and a yellow footer.
Preserve (3-5 traits): single product multiplied into a field; yellow statement panel over the hero; spotlit cabinets; yellow light streaks; stat cards.
Borrow only (1-2): Multiply the one product into a field to show scale
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D product renders
Reject: Generic news grid at the end
Token commitments: palette #606369, #090B0A, #313334, #9B9C93, #484B4E, #1D1F1F; type Univers Next Pro, ABC Monument Grotesk Mono; engine GSAP + Lenis linked (never vendored).
