---
title: "BOTTEGA53"
url: https://www.bottega53.com/
source_url: https://www.bottega53.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: blur-scroll-wedding-photo
dna: "Wedding photographer x white column and motion blur"
register: modern clean
grammar: gallery/catalog
lane: "A white wedding-photography site where the name counts in 0% → 100%, then a single centred column of photographs scrolls through, each image blurred while moving and sharp at rest, with vertical MENU/CONTACT at the edges."
mode: read
traits: ["bold grotesque wordmark loader", "single centred photo column", "motion blur on images while scrolling", "vertical nav words on the edges", "white ground", "192 WebGL image planes"]
palette: ["#FFFFFF", "#010000", "#B5896B", "#807B67", "#6A5143", "#382827"]
type: ["FormaDJRVariable", "FreightBigPro"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Photographs are rendered as WebGL planes that blur with scroll velocity and come sharp when you stop, so the page behaves like a camera panning: moving = soft, stopped = in focus. A single narrow column keeps one image at a time.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: The First The Last agency).

## What to borrow (principle)

- Velocity blur on image planes so stopping brings the photo into focus
- One centred image column for a photographer, one photo at a time

## What to leave

- Captures mostly show the blurred state
- Cookie card covers the bottom of the column

## Signature move

Wedding photographs that blur while you scroll and sharpen when you stop.

## Motion

Intro: 'BOTTEGA53 STUDIO' rises with 0% → 100% (~2 s). Scroll (Lenis, ~150–190 px glide, WebGL ×192): the centred column of photos passes; each image blurs and stretches with speed and resolves at rest; captions under each; side words fixed.

Measured (`motion/probe.json`): GSAP 3.12.2; Lenis; WebGL canvas x192; 3 video; smoothed scroll (median 161 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the gallery/catalog grammar: a white wedding-photography site where the name counts in 0% → 100%, then a single centred column of photographs scrolls through, each image blurred while moving and sharp at rest, with vertical MENU/CONTACT at the edges. Type: FormaDJRVariable, FreightBigPro.
Ground and ink from the measured palette (#FFFFFF, #010000, #B5896B). Motion carries the page through
wedding photographs that blur while you scroll and sharpen when you stop. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — documentary wedding photography, film tones

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: documentary wedding photography, film tones

## Reference lock

Primary reference/direction: BOTTEGA53 — A white wedding-photography site where the name counts in 0% → 100%, then a single centred column of photographs scrolls through, each image blurred while moving and sharp at rest, with vertical MENU/CONTACT at the edges.
Preserve (3-5 traits): bold grotesque wordmark loader; single centred photo column; motion blur on images while scrolling; vertical nav words on the edges; white ground.
Borrow only (1-2): Velocity blur on image planes so stopping brings the photo into focus; One centred image column for a photographer, one photo at a time
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: documentary wedding photography, film tones
Reject: Captures mostly show the blurred state; Cookie card covers the bottom of the column
Token commitments: palette #FFFFFF, #010000, #B5896B, #807B67, #6A5143, #382827; type FormaDJRVariable, FreightBigPro; engine GSAP + Lenis linked (never vendored).
