---
title: "VITURE Luma - XR glasses"
url: http://luma.viture.com/
source_url: http://luma.viture.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "consumer-brand"
family: black-glow-xr-glasses
dna: "XR glasses x black ground, red-pink-violet light ribbons and gradients, glasses floating with a diagonal panel cut"
register: cinematic dark
grammar: chaptered editorial
lane: "Glasses product page: 'Illuminate your victory' with the letters lighting in a gradient over glasses wrapped in a pink light ribbon, a diagonal black panel cutting across into '1200p 4K-like display', spec cards, 'The best just got better' with a transparent render, a model wearing the glasses, 'For everyone' with interpupillary ranges counting on a violet horizon, a red planet arc with '52°' field of view, and feature tiles."
mode: persuade
traits: ["light ribbons around the product", "diagonal panel cuts", "gradient-lit headline letters", "violet horizon glow", "rolling spec numbers"]
palette: ["#000000", "#10112C", "#49284E", "#39030E", "#8D6284"]
type: ["seasonSans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The diagonal cuts between chapters and the glowing horizon keep a spec-heavy page feeling like a product film.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase.

## What to borrow (principle)

- Cut chapters with one consistent diagonal

## What to leave

- Thin grey spec text on black

## Signature move

Glasses wrapped in a pink light ribbon under 'Illuminate your victory'.

## Motion

Wheel: diagonal panels slide over; letters fill with gradient; numbers count; the horizon glow rises.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x3; 17 video; split text; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Discover. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: glasses product page: 'Illuminate your victory' with the letters lighting in a gradient over glasses wrapped in a pink light ribbon, a diagonal black panel cutting across into '1200p 4K-like display', spec cards, 'The best just got better' with a transparent render, a model wearing the glasses, 'For everyone' with interpupillary ranges counting on a violet horizon, a red planet arc with '52°' field of view, and feature tiles. Type: seasonSans.
Ground and ink from the measured palette (#000000, #10112C, #49284E). Motion carries the page through
glasses wrapped in a pink light ribbon under 'Illuminate your victory'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D product renders, portraits

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D product renders, portraits

## Reference lock

Primary reference/direction: VITURE Luma - XR glasses — Glasses product page: 'Illuminate your victory' with the letters lighting in a gradient over glasses wrapped in a pink light ribbon, a diagonal black panel cutting across into '1200p 4K-like display', spec cards, 'The best just got better' with a transparent render, a model wearing the glasses, 'For everyone' with interpupillary ranges counting on a violet horizon, a red planet arc with '52°' field of view, and feature tiles.
Preserve (3-5 traits): light ribbons around the product; diagonal panel cuts; gradient-lit headline letters; violet horizon glow; rolling spec numbers.
Borrow only (1-2): Cut chapters with one consistent diagonal
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D product renders, portraits
Reject: Thin grey spec text on black
Token commitments: palette #000000, #10112C, #49284E, #39030E, #8D6284; type seasonSans; engine GSAP + Lenis linked (never vendored).
