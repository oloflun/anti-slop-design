---
title: "Assistantly - staffing for founders"
url: https://www.assistantly.com/
source_url: https://www.assistantly.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: ""
family: unicorn-mascot-staffing-saas
dna: "Staffing service x pale grey page, a plush unicorn tucked in the headline, portrait tiles and a thick blue ribbon"
register: modern clean
grammar: chaptered editorial
lane: "An offshore staffing service: 'Scale faster with [unicorn] talent' with a plush unicorn sitting in the gap of the headline, portrait cards fanning out and gathering into a grid beside 'More than staffing, your unicorn team', process cards, a thick blue ribbon drawing through value cards ('Scale faster', 'Save smarter', 'Gain an edge'), role cards per department and 'What makes Assistantly different'."
mode: persuade
traits: ["mascot set inside the headline", "portrait cards fanning into a grid", "thick blue drawn ribbon", "value cards on the ribbon"]
palette: ["#F9F9F9", "#C6C2C5", "#6B6682"]
type: ["Geist Mono", "Manrope"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Placing the mascot in the gap of the headline gives a generic B2B claim one memorable image.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Face 44).

## What to borrow (principle)

- Put the single image inside the headline's gap

## What to leave

- Generic card grids

## Signature move

A plush unicorn sitting between 'with' and 'Talent'.

## Motion

Wheel (Lenis, 14 triggers): the unicorn scales into the headline gap; portraits fan and gather; the blue ribbon draws along scroll; cards rise.

Measured (`motion/probe.json`): GSAP 3.15.0; 14 ScrollTriggers; Lenis; 3 video; split text; smoothed scroll (median 73 px still travelling after input stops); entry gate: Start Hiring. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: an offshore staffing service: 'Scale faster with [unicorn] talent' with a plush unicorn sitting in the gap of the headline, portrait cards fanning out and gathering into a grid beside 'More than staffing, your unicorn team', process cards, a thick blue ribbon drawing through value cards ('Scale faster', 'Save smarter', 'Gain an edge'), role cards per department and 'What makes Assistantly different'. Type: Geist Mono, Manrope.
Ground and ink from the measured palette (#F9F9F9, #C6C2C5, #6B6682). Motion carries the page through
a plush unicorn sitting between 'with' and 'Talent'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — portrait photography, 3D mascot

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: portrait photography, 3D mascot

## Reference lock

Primary reference/direction: Assistantly - staffing for founders — An offshore staffing service: 'Scale faster with [unicorn] talent' with a plush unicorn sitting in the gap of the headline, portrait cards fanning out and gathering into a grid beside 'More than staffing, your unicorn team', process cards, a thick blue ribbon drawing through value cards ('Scale faster', 'Save smarter', 'Gain an edge'), role cards per department and 'What makes Assistantly different'.
Preserve (3-5 traits): mascot set inside the headline; portrait cards fanning into a grid; thick blue drawn ribbon; value cards on the ribbon.
Borrow only (1-2): Put the single image inside the headline's gap
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: portrait photography, 3D mascot
Reject: Generic card grids
Token commitments: palette #F9F9F9, #C6C2C5, #6B6682; type Geist Mono, Manrope; engine GSAP + Lenis linked (never vendored).
