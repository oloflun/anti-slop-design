---
title: "National Geographic - Into the Amazon"
url: https://www.nationalgeographic.com/into-the-amazon/
source_url: https://www.nationalgeographic.com/into-the-amazon/
captured: 2026-10-03
origin: raw-url
extract: none
category: editorial
category2: "institutional"
family: scrollytelling-expedition
dna: "Long-form story x a camera flight from a glacier through clouds and painted 3D hills into the rainforest, with text cards and illustrated species"
register: warm photographic
grammar: continuous world
lane: "An expedition story: a dark intro with the partner statement, a flight through night clouds, the source of the Amazon on a glacier with a weather station and a giant year, clouds, painted 3D hills with photo inserts of bears and people, 'The price of gold' in serif caps over a dark jungle, an illustrated toucan on a branch, the forest at night with fireflies, a pointillist flooded forest and 'Where the river parts the sea'."
mode: read
traits: ["continuous camera flight", "painted 3D terrain", "photo inserts on the terrain", "illustrated species", "serif chapter titles"]
palette: ["#27303F", "#DDE0E2", "#F4F5F5", "#99A0A6", "#C7C9CB", "#646B6E"]
type: ["AberMono", "Geograph Edit", "Grosvenor Book"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

One continuous flight from glacier to sea makes a long scientific story feel like a single journey down the river.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Gladeye).

## What to borrow (principle)

- Follow the subject's own path (the river) as the camera path

## What to leave

- Long dark intro

## Signature move

A camera flight from a glacier's weather station down through clouds into painted hills.

## Motion

Wheel (Lenis): a scrubbed WebGL/video camera flight; text cards fade over; photos pop onto the terrain; chapter titles rise.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; WebGL canvas x1 (three.js); smoothed scroll (median 132 px still travelling after input stops); entry gate: Continue without Accepting. Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the continuous world grammar: an expedition story: a dark intro with the partner statement, a flight through night clouds, the source of the Amazon on a glacier with a weather station and a giant year, clouds, painted 3D hills with photo inserts of bears and people, 'The price of gold' in serif caps over a dark jungle, an illustrated toucan on a branch, the forest at night with fireflies, a pointillist flooded forest and 'Where the river parts the sea'. Type: AberMono, Geograph Edit, Grosvenor Book.
Ground and ink from the measured palette (#27303F, #DDE0E2, #F4F5F5). Motion carries the page through
a camera flight from a glacier's weather station down through clouds into painted hills. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL terrain, documentary photography, illustration

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL terrain, documentary photography, illustration

## Reference lock

Primary reference/direction: National Geographic - Into the Amazon — An expedition story: a dark intro with the partner statement, a flight through night clouds, the source of the Amazon on a glacier with a weather station and a giant year, clouds, painted 3D hills with photo inserts of bears and people, 'The price of gold' in serif caps over a dark jungle, an illustrated toucan on a branch, the forest at night with fireflies, a pointillist flooded forest and 'Where the river parts the sea'.
Preserve (3-5 traits): continuous camera flight; painted 3D terrain; photo inserts on the terrain; illustrated species; serif chapter titles.
Borrow only (1-2): Follow the subject's own path (the river) as the camera path
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL terrain, documentary photography, illustration
Reject: Long dark intro
Token commitments: palette #27303F, #DDE0E2, #F4F5F5, #99A0A6, #C7C9CB, #646B6E; type AberMono, Geograph Edit, Grosvenor Book; engine GSAP + Lenis linked (never vendored).
