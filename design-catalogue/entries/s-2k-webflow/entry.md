---
title: "S-2K - Honda S2000 tribute"
url: https://s-2k.webflow.io/
source_url: https://s-2k.webflow.io/
captured: 2026-10-02
origin: raw-url
extract: none
category: editorial
category2: "consumer-brand"
family: car-tribute-tachometer
dna: "Honda S2000 tribute x a tachometer that tracks the scroll"
register: cinematic dark
grammar: chaptered editorial
lane: "A car tribute: a tachometer loader revving to redline, 'Honda S2000 (99-09)' on a road photo, the intro filling in, then a long story (Engineering meets artistry, Milestones in motion with AP1/AP2 spec cards, Pure analog with a gear-shift pattern, Under the surface with a chassis drawing) while a small tachometer in the corner climbs from 0 to redline as you read."
mode: read
traits: ["tachometer as the progress indicator", "condensed italic headings", "spec cards per generation", "gear-shift H pattern section", "chassis line drawing", "orange accent on dark"]
palette: ["#EEEEEE", "#1C1F24", "#06080A", "#666868", "#C3C5C1"]
type: ["Digital 7", "Ppneuemontreal", "Ppneuemontreal Book", "Ppformula"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The tachometer is the signature object: it is the loader and then the scroll progress, so reading the page is revving the engine.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Ivor Jian).

## What to borrow (principle)

- Turn the product's own gauge into the scroll progress indicator

## What to leave

- Small spec text
- Long page

## Signature move

A tachometer in the corner revving towards redline as you scroll.

## Motion

Intro: black, the tachometer needle sweeps to redline and back (~2 s). Wheel (Lenis ~105 px glide, 780 triggers): the road photo lifts; text fills grey to black; the corner gauge rises with progress; car photos slide and scale; spec cards stack; the gear pattern highlights gears 1-3-5; the chassis drawing draws itself.

Measured (`motion/probe.json`): GSAP 3.15.0; 780 ScrollTriggers; 1 pinned sections; Lenis; 3 video; split text; smoothed scroll (median 104 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a car tribute: a tachometer loader revving to redline, 'Honda S2000 (99-09)' on a road photo, the intro filling in, then a long story (Engineering meets artistry, Milestones in motion with AP1/AP2 spec cards, Pure analog with a gear-shift pattern, Under the surface with a chassis drawing) while a small tachometer in the corner climbs from 0 to redline as you read. Type: Digital 7, Ppneuemontreal, Ppneuemontreal Book, Ppformula.
Ground and ink from the measured palette (#EEEEEE, #1C1F24, #06080A). Motion carries the page through
a tachometer in the corner revving towards redline as you scroll. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — car photography, line drawings

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: car photography, line drawings

## Reference lock

Primary reference/direction: S-2K - Honda S2000 tribute — A car tribute: a tachometer loader revving to redline, 'Honda S2000 (99-09)' on a road photo, the intro filling in, then a long story (Engineering meets artistry, Milestones in motion with AP1/AP2 spec cards, Pure analog with a gear-shift pattern, Under the surface with a chassis drawing) while a small tachometer in the corner climbs from 0 to redline as you read.
Preserve (3-5 traits): tachometer as the progress indicator; condensed italic headings; spec cards per generation; gear-shift H pattern section; chassis line drawing.
Borrow only (1-2): Turn the product's own gauge into the scroll progress indicator
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: car photography, line drawings
Reject: Small spec text; Long page
Token commitments: palette #EEEEEE, #1C1F24, #06080A, #666868, #C3C5C1; type Digital 7, Ppneuemontreal, Ppneuemontreal Book, Ppformula; engine GSAP + Lenis linked (never vendored).
