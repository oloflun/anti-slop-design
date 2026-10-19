---
title: "Helmut - Luxury creative agency"
url: https://helmutagency.com/
source_url: https://helmutagency.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "luxury-craft"
family: luxury-agency-white-grid
dna: "Luxury beauty agency x a white case grid and a full-bleed perfume set"
register: modern clean
grammar: gallery/catalog
lane: "A luxury agency: a one-line tagline loader on black, a white page with a giant 'HELMUT', a beauty portrait, a short manifesto, a filterable grid of luxury campaigns (Prada, Armani, Louis Vuitton, YSL, Lancôme), a full-bleed Jean Paul Gaultier perfume set on orange, more cases and a dark sculpture."
mode: read
traits: ["white grid of campaigns", "filter tabs", "full-bleed hero case", "luxury beauty imagery", "giant wordmark", "dark closing image"]
palette: ["#FFFFFF", "#240707", "#AFA39A", "#977260", "#C6D1D3", "#535159"]
type: ["Helvetica Now Display Bold", "Helvetica Now Display Regular"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The work speaks for itself; one full-bleed case breaks the grid's rhythm.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Break a clean grid with one full-bleed case

## What to leave

- Very small labels

## Signature move

A full-bleed Jean Paul Gaultier perfume set breaking a white case grid.

## Motion

Intro: black with the tagline (~2 s). Wheel: the wordmark lifts; the portrait scales; the manifesto fades; grid images rise; the full-bleed case scales up; the dark image ends.

Measured (`motion/probe.json`): GSAP 3.12.5; 1 pinned sections; Lenis; 12 video; split text; smoothed scroll (median 41 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the gallery/catalog grammar: a luxury agency: a one-line tagline loader on black, a white page with a giant 'HELMUT', a beauty portrait, a short manifesto, a filterable grid of luxury campaigns (Prada, Armani, Louis Vuitton, YSL, Lancôme), a full-bleed Jean Paul Gaultier perfume set on orange, more cases and a dark sculpture. Type: Helvetica Now Display Bold, Helvetica Now Display Regular.
Ground and ink from the measured palette (#FFFFFF, #240707, #AFA39A). Motion carries the page through
a full-bleed Jean Paul Gaultier perfume set breaking a white case grid. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — luxury campaign photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: luxury campaign photography

## Reference lock

Primary reference/direction: Helmut - Luxury creative agency — A luxury agency: a one-line tagline loader on black, a white page with a giant 'HELMUT', a beauty portrait, a short manifesto, a filterable grid of luxury campaigns (Prada, Armani, Louis Vuitton, YSL, Lancôme), a full-bleed Jean Paul Gaultier perfume set on orange, more cases and a dark sculpture.
Preserve (3-5 traits): white grid of campaigns; filter tabs; full-bleed hero case; luxury beauty imagery; giant wordmark.
Borrow only (1-2): Break a clean grid with one full-bleed case
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: luxury campaign photography
Reject: Very small labels
Token commitments: palette #FFFFFF, #240707, #AFA39A, #977260, #C6D1D3, #535159; type Helvetica Now Display Bold, Helvetica Now Display Regular; engine GSAP + Lenis linked (never vendored).
