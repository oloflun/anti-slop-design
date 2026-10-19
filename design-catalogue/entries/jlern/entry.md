---
title: "Justin Lerner"
url: https://jlern.com/
source_url: https://jlern.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: letter-grid-icon-folio
dna: "Creative technologist folio x grid of letters and project icons"
register: modern clean
grammar: gallery/catalog
lane: "A white folio laid out as a grid of cells where the letters J-L-E-R-N sit among small project icons (an umbrella, a funnel, a body scan, a logo), the cells shifting and blurring as the grid scrolls."
mode: experience
traits: ["grid of cells mixing letters and icons", "white ground", "serif letter glyphs", "project icons as tiles", "blur on cells in motion"]
palette: ["#FFFFFF", "#C1BFBC"]
type: ["museo-slab"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The name is spelled across a grid in which the other cells are the projects, so identity and work are one tile system. Moving cells blur while scrolling and settle sharp.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Spell the name across a tile grid shared with project icons

## What to leave

- Hard to tell which tiles are clickable
- Most frames blurred in motion

## Signature move

The name's letters set as tiles among project icons in one grid.

## Motion

Intro: white for ~1 s, then the grid fades in tile by tile. Scroll (Lenis, WebGL x5, SplitText): the grid shifts up, tiles blur in motion and sharpen; project captions appear under hovered tiles.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; WebGL canvas x5; split text. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the gallery/catalog grammar: a white folio laid out as a grid of cells where the letters J-L-E-R-N sit among small project icons (an umbrella, a funnel, a body scan, a logo), the cells shifting and blurring as the grid scrolls. Type: museo-slab.
Ground and ink from the measured palette (#FFFFFF, #C1BFBC). Motion carries the page through
the name's letters set as tiles among project icons in one grid. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — small flat icons and illustrations on white

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: small flat icons and illustrations on white

## Reference lock

Primary reference/direction: Justin Lerner — A white folio laid out as a grid of cells where the letters J-L-E-R-N sit among small project icons (an umbrella, a funnel, a body scan, a logo), the cells shifting and blurring as the grid scrolls.
Preserve (3-5 traits): grid of cells mixing letters and icons; white ground; serif letter glyphs; project icons as tiles; blur on cells in motion.
Borrow only (1-2): Spell the name across a tile grid shared with project icons
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: small flat icons and illustrations on white
Reject: Hard to tell which tiles are clickable; Most frames blurred in motion
Token commitments: palette #FFFFFF, #C1BFBC; type museo-slab; engine GSAP + Lenis linked (never vendored).
