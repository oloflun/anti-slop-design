---
title: "Inkwell - the intelligence layer"
url: https://www.inkwell.tech/
source_url: https://www.inkwell.tech/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: "institutional"
family: ai-ring-of-images-gradient
dna: "Design-AI platform x a ring of images that unrolls into a 3D strip and a sky gradient"
register: modern clean
grammar: continuous world
lane: "An AI platform for design industries on white: a ring of small images around 'The future is built on artificial intelligence', the ring unrolling into an arc of cards for pharmaceuticals and architecture, the cards stacking into a long diagonal 3D strip, a single card, a blue 3D logo mark filling the screen, a sky gradient with a thin circle and the mission, floating round portraits for 'bespoke and human ingenuity', and use cases on a dusk gradient."
mode: persuade
traits: ["ring of images", "images unrolling into a 3D strip", "3D logo mark close-up", "sky to dusk gradient", "floating round portraits", "thin circle frame"]
palette: ["#F6F8FA", "#6D625D", "#CBCFCB", "#949D9A", "#E8E3DA"]
type: ["FK Grotesk Mono", "FK Grotesk"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The same set of images changes formation (ring, arc, strip, single card) and the background moves from white to sky to dusk, so the page reads as one continuous camera move.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Re-form one image set into ring, arc and strip
- Shift the background from day to dusk across the page

## What to leave

- Very small body text

## Signature move

A ring of images unrolling into a long diagonal 3D strip.

## Motion

Intro: white, cookie declined, a ring of thumbnails forms around the line (~2 s). Wheel (Lenis): the ring tilts and opens into an arc; cards flow into a diagonal strip in depth; one card isolates; the logo mark zooms through the screen; the sky gradient fades in; portraits float up; the gradient darkens to dusk.

Measured (`motion/probe.json`): GSAP 3.12.7; Lenis; WebGL canvas x1; split text; smoothed scroll (median 148 px still travelling after input stops); entry gate: Decline. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the continuous world grammar: an AI platform for design industries on white: a ring of small images around 'The future is built on artificial intelligence', the ring unrolling into an arc of cards for pharmaceuticals and architecture, the cards stacking into a long diagonal 3D strip, a single card, a blue 3D logo mark filling the screen, a sky gradient with a thin circle and the mission, floating round portraits for 'bespoke and human ingenuity', and use cases on a dusk gradient. Type: FK Grotesk Mono, FK Grotesk.
Ground and ink from the measured palette (#F6F8FA, #6D625D, #CBCFCB). Motion carries the page through
a ring of images unrolling into a long diagonal 3D strip. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — architectural and product imagery, portraits, 3D mark

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: architectural and product imagery, portraits, 3D mark

## Reference lock

Primary reference/direction: Inkwell - the intelligence layer — An AI platform for design industries on white: a ring of small images around 'The future is built on artificial intelligence', the ring unrolling into an arc of cards for pharmaceuticals and architecture, the cards stacking into a long diagonal 3D strip, a single card, a blue 3D logo mark filling the screen, a sky gradient with a thin circle and the mission, floating round portraits for 'bespoke and human ingenuity', and use cases on a dusk gradient.
Preserve (3-5 traits): ring of images; images unrolling into a 3D strip; 3D logo mark close-up; sky to dusk gradient; floating round portraits.
Borrow only (1-2): Re-form one image set into ring, arc and strip; Shift the background from day to dusk across the page
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: architectural and product imagery, portraits, 3D mark
Reject: Very small body text
Token commitments: palette #F6F8FA, #6D625D, #CBCFCB, #949D9A, #E8E3DA; type FK Grotesk Mono, FK Grotesk; engine GSAP + Lenis linked (never vendored).
