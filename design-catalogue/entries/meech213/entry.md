---
title: "Meech213"
url: https://www.meech213.com/
source_url: https://www.meech213.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: floating-tilted-photo-wall
dna: "Fashion photographer x tilted prints drifting on cream"
register: editorial print
grammar: gallery/catalog
lane: "A photographer's site where a small arc of thumbnails opens into an endless drift of tilted prints and magazine covers floating across a cream ground, with a faint category wheel (Artist, Brands, Magazine, Beauty, Fashion) at the bottom."
mode: experience
traits: ["tilted prints drifting across cream", "magazine covers among the photos", "category word wheel at the bottom", "tiny handwriting logo", "no grid"]
palette: ["#F6F4F0", "#9C8A7F", "#403835", "#C6BBB3"]
type: ["Ceraph Roman", "articulat-cf"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The archive behaves like prints spilled on a table that slowly slide past; tilt and overlap make it feel physical. Magazine covers mixed in act as proof without a separate press section.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: The Blackpepper Studio).

## What to borrow (principle)

- Drift tilted prints across a plain ground instead of a grid
- Mix press covers into the work stream as proof

## What to leave

- No way to stop on one image in captures
- Category wheel is very faint

## Signature move

Tilted fashion prints and magazine covers drifting across a cream ground.

## Motion

Intro: cream with a faint category wheel, a single print appears, then an arc of thumbnails (~2 s). Wheel (virtual, Lenis, WebGL): prints slide across at varying tilt and speed; the category wheel rotates to the active category.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; 20 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the gallery/catalog grammar: a photographer's site where a small arc of thumbnails opens into an endless drift of tilted prints and magazine covers floating across a cream ground, with a faint category wheel (Artist, Brands, Magazine, Beauty, Fashion) at the bottom. Type: Ceraph Roman, articulat-cf.
Ground and ink from the measured palette (#F6F4F0, #9C8A7F, #403835). Motion carries the page through
tilted fashion prints and magazine covers drifting across a cream ground. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — editorial fashion and portrait photography, magazine covers

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: editorial fashion and portrait photography, magazine covers

## Reference lock

Primary reference/direction: Meech213 — A photographer's site where a small arc of thumbnails opens into an endless drift of tilted prints and magazine covers floating across a cream ground, with a faint category wheel (Artist, Brands, Magazine, Beauty, Fashion) at the bottom.
Preserve (3-5 traits): tilted prints drifting across cream; magazine covers among the photos; category word wheel at the bottom; tiny handwriting logo; no grid.
Borrow only (1-2): Drift tilted prints across a plain ground instead of a grid; Mix press covers into the work stream as proof
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: editorial fashion and portrait photography, magazine covers
Reject: No way to stop on one image in captures; Category wheel is very faint
Token commitments: palette #F6F4F0, #9C8A7F, #403835, #C6BBB3; type Ceraph Roman, articulat-cf; engine GSAP + Lenis linked (never vendored).
