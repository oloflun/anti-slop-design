---
title: "Horizonte Village"
url: https://horizonte-village.com/
source_url: https://horizonte-village.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: hospitality
category2: "luxury-craft"
family: split-choice-villa-estate
dna: "Luxury villa estate x paper ground and torn-shape photo reveal"
register: warm photographic
grammar: split stage
lane: "A villa development that opens on a stone-paper ground with a monogram and 0% loader, then offers two words, VILLAS and RESIDENCES; hovering one reveals its photograph through a torn, painterly mask."
mode: persuade
traits: ["paper/stone texture ground", "thin serif (Canela) + mono", "two-path choice landing", "torn painterly image mask", "monogram loader"]
palette: ["#DFD8CC", "#5E4F45"]
type: ["ApercuMono", "Canela"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The landing is a choice between two products, and each reveals itself through a ragged brush-shaped window into its photograph, so the image feels like it is being uncovered from the paper rather than placed on it.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: The First The Last Agency).

## What to borrow (principle)

- Reveal photography through an organic, torn mask on a textured ground
- Offer two product paths as the landing when the offer is genuinely two

## What to leave

- Nothing scrolls before a choice
- Thin light serif at small size

## Signature move

A photograph uncovered through a torn, painterly mask on stone-paper.

## Motion

Intro: monogram on paper, 'loading 0%', then VILLAS and RESIDENCES fade in either side (~1.5 s). Hover/scroll (Lenis, SplitText): the RESIDENCES photo appears through a torn brush mask behind the word; the page holds on the choice.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; split text; smoothed scroll (median 100 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the split stage grammar: a villa development that opens on a stone-paper ground with a monogram and 0% loader, then offers two words, VILLAS and RESIDENCES; hovering one reveals its photograph through a torn, painterly mask. Type: ApercuMono, Canela.
Ground and ink from the measured palette (#DFD8CC, #5E4F45). Motion carries the page through
a photograph uncovered through a torn, painterly mask on stone-paper. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — architecture with planting in warm evening light

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: architecture with planting in warm evening light

## Reference lock

Primary reference/direction: Horizonte Village — A villa development that opens on a stone-paper ground with a monogram and 0% loader, then offers two words, VILLAS and RESIDENCES; hovering one reveals its photograph through a torn, painterly mask.
Preserve (3-5 traits): paper/stone texture ground; thin serif (Canela) + mono; two-path choice landing; torn painterly image mask; monogram loader.
Borrow only (1-2): Reveal photography through an organic, torn mask on a textured ground; Offer two product paths as the landing when the offer is genuinely two
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: architecture with planting in warm evening light
Reject: Nothing scrolls before a choice; Thin light serif at small size
Token commitments: palette #DFD8CC, #5E4F45; type ApercuMono, Canela; engine GSAP + Lenis linked (never vendored).
