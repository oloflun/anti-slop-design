---
title: "SurImpression - Labo School of Design exhibition"
url: https://surimpression.studiokhi.com/
source_url: https://surimpression.studiokhi.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "editorial"
family: exhibition-grid-blue-pixels
dna: "Design school exhibition x blue pixel wipe and a table grid of exhibitors"
register: modern clean
grammar: gallery/catalog
lane: "An exhibition site: a blue screen that breaks into pixel blocks to reveal white, 'SurImpression+ Labo School of Design 23.03.24 > 12.05.24' in large grotesk, an intro, then a table grid of exhibitors where each cell turns blue with a preview image on hover, and a vertical menu tab."
mode: read
traits: ["blue pixel block wipe", "large grotesk title and dates", "table grid of exhibitors", "cells turning blue with preview", "vertical side tab", "blue and white only"]
palette: ["#FFFFFF", "#E0E0E1", "#A8A9B2", "#181860", "#4F4F7E", "#C7C7CD"]
type: ["Helvetica Neue"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

A strict grid and one accent colour make an exhibition listing feel like a printed catalogue.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A pixel-block wipe in the accent colour as the intro

## What to leave

- Grid repeats

## Signature move

A blue pixel-block wipe revealing a white exhibition grid.

## Motion

Intro: blue fills, then breaks into stepped blocks that pull away (~2 s). Wheel: the intro fades; grid cells reveal; hovered cells fill blue with a preview.

Measured (`motion/probe.json`): GSAP 3.12.5; 1 pinned sections; ScrollSmoother. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the gallery/catalog grammar: an exhibition site: a blue screen that breaks into pixel blocks to reveal white, 'SurImpression+ Labo School of Design 23.03.24 > 12.05.24' in large grotesk, an intro, then a table grid of exhibitors where each cell turns blue with a preview image on hover, and a vertical menu tab. Type: Helvetica Neue.
Ground and ink from the measured palette (#FFFFFF, #E0E0E1, #A8A9B2). Motion carries the page through
a blue pixel-block wipe revealing a white exhibition grid. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — exhibition previews

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: exhibition previews

## Reference lock

Primary reference/direction: SurImpression - Labo School of Design exhibition — An exhibition site: a blue screen that breaks into pixel blocks to reveal white, 'SurImpression+ Labo School of Design 23.03.24 > 12.05.24' in large grotesk, an intro, then a table grid of exhibitors where each cell turns blue with a preview image on hover, and a vertical menu tab.
Preserve (3-5 traits): blue pixel block wipe; large grotesk title and dates; table grid of exhibitors; cells turning blue with preview; vertical side tab.
Borrow only (1-2): A pixel-block wipe in the accent colour as the intro
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: exhibition previews
Reject: Grid repeats
Token commitments: palette #FFFFFF, #E0E0E1, #A8A9B2, #181860, #4F4F7E, #C7C7CD; type Helvetica Neue; engine GSAP + Lenis linked (never vendored).
