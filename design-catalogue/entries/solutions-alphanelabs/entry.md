---
title: "Alphane Labs - Materials characterisation"
url: https://solutions.alphanelabs.com/
source_url: https://solutions.alphanelabs.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: "institutional"
family: line-drawing-instrument-explainer
dna: "Lab instrument maker x a blue line-drawn instrument that rotates and annotates itself"
register: modern clean
grammar: split stage
lane: "A lab-instrument page on pale blue: logo loader, bubble shapes behind a statement, then the MGA-1 analyzer as a blue technical line drawing that rotates, separates into modules, gains dimension lines and callout boxes, shows measurement charts, and finally appears as a photo-real render with blue spheres for contract testing, closing on a giant lowercase wordmark."
mode: persuade
traits: ["technical line drawing of the product", "rotating isometric views", "callout boxes and dimension lines", "measurement charts", "line drawing to render switch", "giant lowercase wordmark"]
palette: ["#F2F8FD", "#9AC7D1"]
type: ["Aeonik", "Aeonik Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The instrument as a blueprint that rotates and annotates itself explains a complex product without photos, and the final switch to a render rewards the scroll.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Explain a technical product as an animated line drawing with callouts
- Switch from drawing to render at the end

## What to leave

- Very small callout text

## Signature move

A blue line-drawn lab instrument rotating and annotating itself.

## Motion

Intro: pale blue with the logo and a loading line (~3 s). Wheel (Lenis ~140-195 px glide, 5 pins): bubbles drift; the drawing pins and rotates through isometric angles; modules separate and slide; dimension lines draw; callout boxes pop; charts plot; the render rises; the wordmark slides up.

Measured (`motion/probe.json`): GSAP 3.13.0; 5 pinned sections; Lenis; WebGL canvas x1; smoothed scroll (median 200 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the split stage grammar: a lab-instrument page on pale blue: logo loader, bubble shapes behind a statement, then the MGA-1 analyzer as a blue technical line drawing that rotates, separates into modules, gains dimension lines and callout boxes, shows measurement charts, and finally appears as a photo-real render with blue spheres for contract testing, closing on a giant lowercase wordmark. Type: Aeonik, Aeonik Mono.
Ground and ink from the measured palette (#F2F8FD, #9AC7D1). Motion carries the page through
a blue line-drawn lab instrument rotating and annotating itself. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — technical line drawings, product render

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: technical line drawings, product render

## Reference lock

Primary reference/direction: Alphane Labs - Materials characterisation — A lab-instrument page on pale blue: logo loader, bubble shapes behind a statement, then the MGA-1 analyzer as a blue technical line drawing that rotates, separates into modules, gains dimension lines and callout boxes, shows measurement charts, and finally appears as a photo-real render with blue spheres for contract testing, closing on a giant lowercase wordmark.
Preserve (3-5 traits): technical line drawing of the product; rotating isometric views; callout boxes and dimension lines; measurement charts; line drawing to render switch.
Borrow only (1-2): Explain a technical product as an animated line drawing with callouts; Switch from drawing to render at the end
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: technical line drawings, product render
Reject: Very small callout text
Token commitments: palette #F2F8FD, #9AC7D1; type Aeonik, Aeonik Mono; engine GSAP + Lenis linked (never vendored).
