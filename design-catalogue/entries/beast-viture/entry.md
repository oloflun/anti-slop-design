---
title: "VITURE The Beast"
url: https://beast.viture.com/
source_url: https://beast.viture.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: ""
family: blue-macro-lens-product
dna: "XR glasses x an extreme blue macro of the lens filling the screen, the title fading through"
register: cinematic dark
grammar: filmic one-shot
lane: "A product teaser: 'The Beast' in blue on black, a blue glass lens rushing toward the camera and filling the screen, 'Unleash' fading in and out through the glass, award badges; the capture stayed on the lens macro for the rest of the scroll."
mode: experience
traits: ["extreme macro of the product", "blue on black", "title fading through glass"]
palette: ["#000000", "#142A87", "#4070BE", "#060930", "#0E185F"]
type: ["seasonSans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Filling the screen with one material close-up makes the product feel huge before any spec.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase.

## What to borrow (principle)

- Open on an extreme macro of the product's material

## What to leave

- Capture shows no progress past the macro

## Signature move

A blue glass lens rushing toward the camera.

## Motion

Intro: title fades in blue (~1 s). Wheel: the lens video scrubs toward the camera; words fade through.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; 22 video; split text; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Discover. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the filmic one-shot grammar: a product teaser: 'The Beast' in blue on black, a blue glass lens rushing toward the camera and filling the screen, 'Unleash' fading in and out through the glass, award badges; the capture stayed on the lens macro for the rest of the scroll. Type: seasonSans.
Ground and ink from the measured palette (#000000, #142A87, #4070BE). Motion carries the page through
a blue glass lens rushing toward the camera. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product macro video

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product macro video

## Reference lock

Primary reference/direction: VITURE The Beast — A product teaser: 'The Beast' in blue on black, a blue glass lens rushing toward the camera and filling the screen, 'Unleash' fading in and out through the glass, award badges; the capture stayed on the lens macro for the rest of the scroll.
Preserve (3-5 traits): extreme macro of the product; blue on black; title fading through glass.
Borrow only (1-2): Open on an extreme macro of the product's material
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product macro video
Reject: Capture shows no progress past the macro
Token commitments: palette #000000, #142A87, #4070BE, #060930, #0E185F; type seasonSans; engine GSAP + Lenis linked (never vendored).
