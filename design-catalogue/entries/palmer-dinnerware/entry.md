---
title: "Palmer Dinnerware - Miami collection"
url: https://www.palmer-dinnerware.com/
source_url: https://www.palmer-dinnerware.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "luxury-craft"
family: tableware-horizontal-collection
dna: "Tableware maker x plates floating and a horizontal collection story"
register: warm photographic
grammar: chaptered editorial
lane: "A tableware collection page: plates scattered and floating on cream, then 'Miami' on pale blue with a stacked set, the page sliding sideways through a flat-lay of blue plates with vegetables, a plate with pasta beside a sea photo, and a grid of the collection's products, before plates scatter again."
mode: read
traits: ["plates scattered as the loader", "horizontal scroll through the story", "pale blue palette", "flat-lay food photography", "product grid", "scatter returns at the end"]
palette: ["#B4C3C7", "#477791", "#153542", "#4D5358", "#908479", "#A2AEAE"]
type: ["TWK Lausanne"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The sideways movement suits a collection lookbook, and the floating plates bracket the page.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Scatter products as the loader and the outro

## What to leave

- Cookie panel at start
- Small specs

## Signature move

Blue plates floating and scattering on cream.

## Motion

Intro: plates drift and scatter (~2 s), cookie declined. Wheel (Lenis, 76 triggers): the page moves sideways through panels; photos slide in from the right; the grid scrolls; plates scatter again at the end.

Measured (`motion/probe.json`): GSAP 3.15.0; 76 ScrollTriggers; Lenis; split text; smoothed scroll (median 89 px still travelling after input stops); entry gate: Avvisa alla, x, explore collection explore collection. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a tableware collection page: plates scattered and floating on cream, then 'Miami' on pale blue with a stacked set, the page sliding sideways through a flat-lay of blue plates with vegetables, a plate with pasta beside a sea photo, and a grid of the collection's products, before plates scatter again. Type: TWK Lausanne.
Ground and ink from the measured palette (#B4C3C7, #477791, #153542). Motion carries the page through
blue plates floating and scattering on cream. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — tableware and food photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: tableware and food photography

## Reference lock

Primary reference/direction: Palmer Dinnerware - Miami collection — A tableware collection page: plates scattered and floating on cream, then 'Miami' on pale blue with a stacked set, the page sliding sideways through a flat-lay of blue plates with vegetables, a plate with pasta beside a sea photo, and a grid of the collection's products, before plates scatter again.
Preserve (3-5 traits): plates scattered as the loader; horizontal scroll through the story; pale blue palette; flat-lay food photography; product grid.
Borrow only (1-2): Scatter products as the loader and the outro
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: tableware and food photography
Reject: Cookie panel at start; Small specs
Token commitments: palette #B4C3C7, #477791, #153542, #4D5358, #908479, #A2AEAE; type TWK Lausanne; engine GSAP + Lenis linked (never vendored).
