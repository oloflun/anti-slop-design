---
title: "MERSI Architecture"
url: https://www.mersi-architecture.com/
source_url: https://www.mersi-architecture.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: luxury-craft
category2: ""
family: wood-mask-logo-interiors
dna: "Paris interior architects x wood-textured monogram and project collages"
register: warm photographic
grammar: gallery/catalog
lane: "An interior architecture studio whose loader is the MS monogram cut out of warm materials (wood, plaster) that change texture, then each project appears as a collage of interior photographs with the project name on a coloured label holding the same monogram."
mode: persuade
traits: ["monogram filled with changing material textures", "interior photo collages", "coloured project labels with the monogram", "warm beige ground", "Taxi transitions"]
palette: ["#EEE6DE", "#8A786D", "#5E4A3B", "#A09FA1", "#C5C1BE"]
type: ["Doner", "Switzer Variable"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The monogram is a material sample: its letters are windows onto wood and plaster that swap like a swatch book, which tells you the studio is about materials before any photo appears.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Fill a monogram with changing material textures as the loader
- Label each project with a small coloured tag carrying the monogram

## What to leave

- Captured mostly the first collages; deeper sections not reached
- Small labels

## Signature move

An 'MS' monogram whose letters swap between wood and plaster textures.

## Motion

Intro: beige ground, 'MS' letters filled with wood, then plaster, then darker wood (~2.5 s). Scroll (Lenis, Taxi, SplitText): project collages (Hamelin, Paix, Atokym) with labels slide in; capture ended after the first projects.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; Taxi page transitions; split text; smoothed scroll (median 212 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the gallery/catalog grammar: an interior architecture studio whose loader is the MS monogram cut out of warm materials (wood, plaster) that change texture, then each project appears as a collage of interior photographs with the project name on a coloured label holding the same monogram. Type: Doner, Switzer Variable.
Ground and ink from the measured palette (#EEE6DE, #8A786D, #5E4A3B). Motion carries the page through
an 'MS' monogram whose letters swap between wood and plaster textures. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — warm interior photography: wood, plaster, curved furniture

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: warm interior photography: wood, plaster, curved furniture

## Reference lock

Primary reference/direction: MERSI Architecture — An interior architecture studio whose loader is the MS monogram cut out of warm materials (wood, plaster) that change texture, then each project appears as a collage of interior photographs with the project name on a coloured label holding the same monogram.
Preserve (3-5 traits): monogram filled with changing material textures; interior photo collages; coloured project labels with the monogram; warm beige ground; Taxi transitions.
Borrow only (1-2): Fill a monogram with changing material textures as the loader; Label each project with a small coloured tag carrying the monogram
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: warm interior photography: wood, plaster, curved furniture
Reject: Captured mostly the first collages; deeper sections not reached; Small labels
Token commitments: palette #EEE6DE, #8A786D, #5E4A3B, #A09FA1, #C5C1BE; type Doner, Switzer Variable; engine GSAP + Lenis linked (never vendored).
