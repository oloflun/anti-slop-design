---
title: "eloyb.design"
url: https://eloyb.design/
source_url: https://eloyb.design/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: glitch-lime-designer-folio
dna: "UI designer and glitch artist x lime ground and doubled glitch type"
register: other
grammar: chaptered editorial
lane: "A designer folio: 'User interface designer, Webflow developer & glitch artist' in doubled glitch type over a lime ground with a halftone flower, 'SELECTED WORK' repeated in a stretching stack, then a dark mosaic of projects drifting at different speeds and a pixel-dot field with 'click to connect'."
mode: persuade
traits: ["lime ground", "doubled glitch headline", "stretching repeated title", "halftone graphics", "drifting project mosaic", "pixel-dot field"]
palette: ["#2B2C27", "#D8FC82", "#869959", "#657247", "#444B34", "#ACC46F"]
type: ["Px 437 Phoenixvga 8 X 16", "Px 437 Phoenixega 8 X 8 2 Y"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The glitch typography is the personal signature and it stretches into the section change.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Stretch a repeated title vertically as the transition into work

## What to leave

- Mosaic is crowded

## Signature move

Doubled glitch type on lime stretching into 'SELECTED WORK'.

## Motion

Intro: lime with the doubled headline flickering. Wheel (Lenis ~125 px glide, 20 triggers, 1309 split): the headline lifts; 'SELECTED WORK' repeats and stretches into the dark; project tiles drift in columns; pixel dots blink.

Measured (`motion/probe.json`): GSAP 3.15.0; 20 ScrollTriggers; Lenis; split text; smoothed scroll (median 109 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a designer folio: 'User interface designer, Webflow developer & glitch artist' in doubled glitch type over a lime ground with a halftone flower, 'SELECTED WORK' repeated in a stretching stack, then a dark mosaic of projects drifting at different speeds and a pixel-dot field with 'click to connect'. Type: Px 437 Phoenixvga 8 X 16, Px 437 Phoenixega 8 X 8 2 Y.
Ground and ink from the measured palette (#2B2C27, #D8FC82, #869959). Motion carries the page through
doubled glitch type on lime stretching into 'SELECTED WORK'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project screenshots, halftone art

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project screenshots, halftone art

## Reference lock

Primary reference/direction: eloyb.design — A designer folio: 'User interface designer, Webflow developer & glitch artist' in doubled glitch type over a lime ground with a halftone flower, 'SELECTED WORK' repeated in a stretching stack, then a dark mosaic of projects drifting at different speeds and a pixel-dot field with 'click to connect'.
Preserve (3-5 traits): lime ground; doubled glitch headline; stretching repeated title; halftone graphics; drifting project mosaic.
Borrow only (1-2): Stretch a repeated title vertically as the transition into work
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project screenshots, halftone art
Reject: Mosaic is crowded
Token commitments: palette #2B2C27, #D8FC82, #869959, #657247, #444B34, #ACC46F; type Px 437 Phoenixvga 8 X 16, Px 437 Phoenixega 8 X 8 2 Y; engine GSAP + Lenis linked (never vendored).
