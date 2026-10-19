---
title: "QuietCubes"
url: https://quietcubes.com/
source_url: https://quietcubes.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "product-focused"
family: pod-selector-office-booths
dna: "Office pods maker x pill-shaped product selector"
register: cinematic dark
grammar: split stage
lane: "A dark landing that asks you to 'Select Your Pod' from four pill-shaped buttons, each tinted in the pod's colour (orange, blue, green, sand) with a tiny product image."
mode: persuade
traits: ["four pill selector buttons", "colour per product", "tiny product thumbnails inside pills", "dark gradient ground", "choice landing"]
palette: ["#0A0A0A", "#363331"]
type: ["Inter Tight Variable"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The landing is the product chooser: four pills, each in its product's colour, so the decision is the first and only thing on the page.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: ADELT).

## What to borrow (principle)

- A coloured pill per product line as the landing choice

## What to leave

- Nothing beyond the selector was captured
- Very small type

## Signature move

Four colour-coded pills to 'Select Your Pod'.

## Motion

Intro: pills slide in with 'please wait…' then 'Select Your Pod' (~2 s). Holds on the selector; wheel does not move the page.

Measured (`motion/probe.json`): GSAP 3.15.0; 21 ScrollTriggers; Lenis; 3 video; split text; smoothed scroll (median 102 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the split stage grammar: a dark landing that asks you to 'Select Your Pod' from four pill-shaped buttons, each tinted in the pod's colour (orange, blue, green, sand) with a tiny product image. Type: Inter Tight Variable.
Ground and ink from the measured palette (#0A0A0A, #363331). Motion carries the page through
four colour-coded pills to 'Select Your Pod'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product pods photographed small inside pills

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product pods photographed small inside pills

## Reference lock

Primary reference/direction: QuietCubes — A dark landing that asks you to 'Select Your Pod' from four pill-shaped buttons, each tinted in the pod's colour (orange, blue, green, sand) with a tiny product image.
Preserve (3-5 traits): four pill selector buttons; colour per product; tiny product thumbnails inside pills; dark gradient ground; choice landing.
Borrow only (1-2): A coloured pill per product line as the landing choice
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product pods photographed small inside pills
Reject: Nothing beyond the selector was captured; Very small type
Token commitments: palette #0A0A0A, #363331; type Inter Tight Variable; engine GSAP + Lenis linked (never vendored).
