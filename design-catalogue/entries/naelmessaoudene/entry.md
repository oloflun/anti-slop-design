---
title: "Nael Messaoudene - Freelance Creative Developer"
url: https://www.naelmessaoudene.com/
source_url: https://www.naelmessaoudene.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: ""
family: webgl-wave-project-slider
dna: "Creative developer x a big percent loader and a project image that ripples in"
register: cinematic dark
grammar: live surface
lane: "A developer folio: a black screen with a big '0%' to '100%' counter bottom right, then a large project image (a private jet over clouds) that arrives through a dark pixel wave, a pink card for Dassault below, and small corner labels."
mode: read
traits: ["big percent counter", "pixel wave reveal on image", "large project image", "pink project card", "small corner labels"]
palette: ["#1D1818", "#2F3033", "#E6BCBA", "#4B626C", "#949E9D"]
type: ["champ", "hkgros", "roboto"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The wave reveal on the first project is a nice entrance; the rest is a single slide.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Reveal the first project through a dark wave

## What to leave

- No scroll progress captured

## Signature move

A jet over clouds rippling in through a dark pixel wave.

## Motion

Intro: black with the counter 0 to 100 (~2 s). Then: the image arrives through a wave of dark pixels; the pink card slides up; the slider waits for drag.

Measured (`motion/probe.json`): GSAP 3.12.2; Lenis; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the live surface grammar: a developer folio: a black screen with a big '0%' to '100%' counter bottom right, then a large project image (a private jet over clouds) that arrives through a dark pixel wave, a pink card for Dassault below, and small corner labels. Type: champ, hkgros, roboto.
Ground and ink from the measured palette (#1D1818, #2F3033, #E6BCBA). Motion carries the page through
a jet over clouds rippling in through a dark pixel wave. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project imagery

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project imagery

## Reference lock

Primary reference/direction: Nael Messaoudene - Freelance Creative Developer — A developer folio: a black screen with a big '0%' to '100%' counter bottom right, then a large project image (a private jet over clouds) that arrives through a dark pixel wave, a pink card for Dassault below, and small corner labels.
Preserve (3-5 traits): big percent counter; pixel wave reveal on image; large project image; pink project card; small corner labels.
Borrow only (1-2): Reveal the first project through a dark wave
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project imagery
Reject: No scroll progress captured
Token commitments: palette #1D1818, #2F3033, #E6BCBA, #4B626C, #949E9D; type champ, hkgros, roboto; engine GSAP + Lenis linked (never vendored).
