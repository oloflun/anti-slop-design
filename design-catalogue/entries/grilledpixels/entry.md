---
title: "Adam Roberts - Senior Designer and Developer"
url: https://www.grilledpixels.com/
source_url: https://www.grilledpixels.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: pixel-marquee-case-folio
dna: "Designer-developer x pixel-font marquees naming each case"
register: cinematic dark
grammar: rhythmic cutlist
lane: "A designer-developer folio on black: hourglass loader, a red smeared name, then each case enters as a giant pixel-font marquee (FINKEE, OTHERSIDE, EIGER, SUPERVOICE, RETREATER, PHOTOSCOPE, LIQUID CRYSTAL) running across its own project image with a short write-up, followed by a dense catalog grid of every screen and a pixelated portrait behind a red 'Let's work together' marquee."
mode: read
traits: ["giant pixel-font case marquees", "each case gets its own colour world", "hourglass loader", "dense catalog grid of screens", "pixelated portrait", "red marquee CTA"]
palette: ["#010101", "#36292B"]
type: ["untitledSans", "tronicaMono", "atHaussMono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The pixel marquee is the recurring device: each case is the same moving band in a new colour world, so a long list of projects reads as a sequence of title cards with one voice.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One marquee treatment as the title card for every case
- A catalog grid after the hero cases as the archive

## What to leave

- Write-ups too small over images
- Catalog grid is very dense

## Signature move

Giant pixel-font marquees running across each case image.

## Motion

Intro: black hourglass loader with percent, then a red smear reveals the name (~2 s). Wheel (Lenis ~80 px glide): each case marquee scrolls sideways while its image cross-fades from the previous case; the catalog grid rises in rows; the portrait pixelates in as the red marquee runs.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; WebGL canvas x1 (three.js); smoothed scroll (median 101 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the rhythmic cutlist grammar: a designer-developer folio on black: hourglass loader, a red smeared name, then each case enters as a giant pixel-font marquee (FINKEE, OTHERSIDE, EIGER, SUPERVOICE, RETREATER, PHOTOSCOPE, LIQUID CRYSTAL) running across its own project image with a short write-up, followed by a dense catalog grid of every screen and a pixelated portrait behind a red 'Let's work together' marquee. Type: untitledSans, tronicaMono, atHaussMono.
Ground and ink from the measured palette (#010101, #36292B). Motion carries the page through
giant pixel-font marquees running across each case image. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project screenshots and renders, portrait

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project screenshots and renders, portrait

## Reference lock

Primary reference/direction: Adam Roberts - Senior Designer and Developer — A designer-developer folio on black: hourglass loader, a red smeared name, then each case enters as a giant pixel-font marquee (FINKEE, OTHERSIDE, EIGER, SUPERVOICE, RETREATER, PHOTOSCOPE, LIQUID CRYSTAL) running across its own project image with a short write-up, followed by a dense catalog grid of every screen and a pixelated portrait behind a red 'Let's work together' marquee.
Preserve (3-5 traits): giant pixel-font case marquees; each case gets its own colour world; hourglass loader; dense catalog grid of screens; pixelated portrait.
Borrow only (1-2): One marquee treatment as the title card for every case; A catalog grid after the hero cases as the archive
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project screenshots and renders, portrait
Reject: Write-ups too small over images; Catalog grid is very dense
Token commitments: palette #010101, #36292B; type untitledSans, tronicaMono, atHaussMono; engine GSAP + Lenis linked (never vendored).
