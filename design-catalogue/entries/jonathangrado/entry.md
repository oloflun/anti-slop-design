---
title: "Jonathan Grado - Conceptual Photographer"
url: https://www.jonathangrado.com/
source_url: https://www.jonathangrado.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: photographer-centred-frame-scroll
dna: "Conceptual photographer x one centred image frame that resizes per series"
register: warm photographic
grammar: gallery/catalog
lane: "A photographer's folio: a figure with a disco ball head in a field, then a centred frame where each series appears and the frame changes size and the ground changes colour (a balloon in black and white, a figure with flowers for a head, a red barn, colourful balls in a car, a neon sign on pink, a portrait on red curtains), with tiny captions."
mode: read
traits: ["single centred frame", "frame resizes per image", "ground colour follows the image", "tiny captions", "surreal conceptual photos", "italic bio at the end"]
palette: ["#FFFFFF", "#EBE7E4", "#422D21", "#060606", "#B9B9B8", "#67675E"]
type: ["items", "sctoGrotesk"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Letting the frame and ground adapt to each photograph gives every series its own room without a grid.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Resize the frame and recolour the ground for each image

## What to leave

- Captions too small

## Signature move

A centred photo frame resizing as the ground changes colour.

## Motion

Intro: dark (~1 s), the disco-ball photo. Wheel: each image slides up into the centred frame; the frame width eases to the image's proportion; the page background crossfades to match; the bio fades in at the end.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; 1 video; smoothed scroll (median 144 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the gallery/catalog grammar: a photographer's folio: a figure with a disco ball head in a field, then a centred frame where each series appears and the frame changes size and the ground changes colour (a balloon in black and white, a figure with flowers for a head, a red barn, colourful balls in a car, a neon sign on pink, a portrait on red curtains), with tiny captions. Type: items, sctoGrotesk.
Ground and ink from the measured palette (#FFFFFF, #EBE7E4, #422D21). Motion carries the page through
a centred photo frame resizing as the ground changes colour. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — conceptual photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: conceptual photography

## Reference lock

Primary reference/direction: Jonathan Grado - Conceptual Photographer — A photographer's folio: a figure with a disco ball head in a field, then a centred frame where each series appears and the frame changes size and the ground changes colour (a balloon in black and white, a figure with flowers for a head, a red barn, colourful balls in a car, a neon sign on pink, a portrait on red curtains), with tiny captions.
Preserve (3-5 traits): single centred frame; frame resizes per image; ground colour follows the image; tiny captions; surreal conceptual photos.
Borrow only (1-2): Resize the frame and recolour the ground for each image
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: conceptual photography
Reject: Captions too small
Token commitments: palette #FFFFFF, #EBE7E4, #422D21, #060606, #B9B9B8, #67675E; type items, sctoGrotesk; engine GSAP + Lenis linked (never vendored).
