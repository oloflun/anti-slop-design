---
title: "Siempreric"
url: https://siemprericc.com/
source_url: https://siemprericc.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: horizontal-photo-strip-photographer
dna: "Photographer and director x horizontal portrait strip"
register: modern clean
grammar: gallery/catalog
lane: "A photographer's site with a brush-script signature logo on white, then a horizontal strip of portraits where the current one sits centred and large while neighbours peek in at the edges, with a live clock and caption."
mode: read
traits: ["brush signature logo", "horizontal photo strip", "centred active image with neighbours peeking", "white ground", "live clock and caption"]
palette: ["#F5F5F5", "#000000", "#272423", "#8A725D", "#BDA783", "#DFE0DA"]
type: ["SF Pro Display", "Neue Haas Grotesk Display Pro"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

One photograph at a time, centred, with just enough of the neighbours visible to invite the next. The white ground and tiny chrome make each portrait read like a print on a wall.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Centre one photo at a time with neighbours peeking at the edges

## What to leave

- Captions very small
- No overview of the series

## Signature move

A centred portrait with its neighbours peeking in from the edges.

## Motion

Intro: black, then the signature logo on white (~1.5 s). Wheel (Lenis): the strip slides horizontally one portrait at a time; the centred image scales up slightly; caption updates.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the gallery/catalog grammar: a photographer's site with a brush-script signature logo on white, then a horizontal strip of portraits where the current one sits centred and large while neighbours peek in at the edges, with a live clock and caption. Type: SF Pro Display, Neue Haas Grotesk Display Pro.
Ground and ink from the measured palette (#F5F5F5, #000000, #272423). Motion carries the page through
a centred portrait with its neighbours peeking in from the edges. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — music and celebrity portraiture, strong colour

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: music and celebrity portraiture, strong colour

## Reference lock

Primary reference/direction: Siempreric — A photographer's site with a brush-script signature logo on white, then a horizontal strip of portraits where the current one sits centred and large while neighbours peek in at the edges, with a live clock and caption.
Preserve (3-5 traits): brush signature logo; horizontal photo strip; centred active image with neighbours peeking; white ground; live clock and caption.
Borrow only (1-2): Centre one photo at a time with neighbours peeking at the edges
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: music and celebrity portraiture, strong colour
Reject: Captions very small; No overview of the series
Token commitments: palette #F5F5F5, #000000, #272423, #8A725D, #BDA783, #DFE0DA; type SF Pro Display, Neue Haas Grotesk Display Pro; engine GSAP + Lenis linked (never vendored).
