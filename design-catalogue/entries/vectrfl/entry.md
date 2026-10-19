---
title: "Vectr - industrial staffing platform"
url: https://www.vectrfl.com/
source_url: https://www.vectrfl.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "institutional"
family: isometric-plant-staffing
dna: "Industrial staffing x an isometric white plant with light flowing through its steps"
register: modern clean
grammar: chaptered editorial
lane: "A staffing platform on pale blue: a spinning loader, 'The new standard in staffing' over white isometric industrial buildings, four steps (activation, cleared to count, proven field match, seamless arrival) as the camera moves over the plant with a blue light beam flowing through cooling towers, a grid of tiles, a dotted arrow, 'Designed for today's operations' with icons appearing, a nuclear-site photo, FAQ and a dark CTA."
mode: persuade
traits: ["isometric white plant", "blue light beam flowing", "steps as camera moves", "pale blue ground", "icon grid appearing in order", "site photography"]
palette: ["#D2E0ED", "#92A4B6"]
type: ["Roboto"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

A light beam travelling through the plant makes the four steps one continuous process.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Utsubo).

## What to borrow (principle)

- Let a light beam travel through a model as the steps advance

## What to leave

- Generic lower half

## Signature move

A blue light beam flowing through white cooling towers.

## Motion

Intro: a ring loader (~1 s). Wheel: the camera glides over the plant; the beam flows step to step; tiles rise; the arrow forms from dots; icons pop in order; the photo slides; the CTA darkens.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; Taxi page transitions; smoothed scroll (median 118 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a staffing platform on pale blue: a spinning loader, 'The new standard in staffing' over white isometric industrial buildings, four steps (activation, cleared to count, proven field match, seamless arrival) as the camera moves over the plant with a blue light beam flowing through cooling towers, a grid of tiles, a dotted arrow, 'Designed for today's operations' with icons appearing, a nuclear-site photo, FAQ and a dark CTA. Type: Roboto.
Ground and ink from the measured palette (#D2E0ED, #92A4B6). Motion carries the page through
a blue light beam flowing through white cooling towers. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D isometric scene

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D isometric scene

## Reference lock

Primary reference/direction: Vectr - industrial staffing platform — A staffing platform on pale blue: a spinning loader, 'The new standard in staffing' over white isometric industrial buildings, four steps (activation, cleared to count, proven field match, seamless arrival) as the camera moves over the plant with a blue light beam flowing through cooling towers, a grid of tiles, a dotted arrow, 'Designed for today's operations' with icons appearing, a nuclear-site photo, FAQ and a dark CTA.
Preserve (3-5 traits): isometric white plant; blue light beam flowing; steps as camera moves; pale blue ground; icon grid appearing in order.
Borrow only (1-2): Let a light beam travel through a model as the steps advance
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D isometric scene
Reject: Generic lower half
Token commitments: palette #D2E0ED, #92A4B6; type Roboto; engine GSAP + Lenis linked (never vendored).
