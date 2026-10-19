---
title: "Gianluca Gradogna - Multidisciplinary Designer"
url: https://gianlucagradogna.com/
source_url: https://gianlucagradogna.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: photo-essay-horizontal-lofoten
dna: "Designer and photographer x a horizontal photo essay with serif titles"
register: editorial print
grammar: chaptered editorial
lane: "A photo-essay folio: a counter on black, a card 'Crafting narrative through design', 'Through this lens' with a portrait set between the words, then a sideways-moving essay through Lofoten (a tall photo of red cabins, serif statements in caps, a wide mountain panorama, a small aurora inset, a yellow house) where photos and text alternate as you scroll."
mode: read
traits: ["portrait between title words", "horizontal photo essay", "thin serif caps statements", "tall and wide photos alternating", "small inset photos", "counter loader"]
palette: ["#FFFFFF", "#95BCE5", "#228ADF", "#211C31", "#04070F", "#434A68"]
type: ["LZ", "Neue-Montreal", "PPNeue-Montreal"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Moving sideways through a sequence of photos and short statements reads like a printed photo book.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Run a photo essay sideways, alternating tall and wide frames with text

## What to leave

- Thin serif small text

## Signature move

A sideways photo essay through Lofoten in serif caps.

## Motion

Intro: black counter 0 to 96 (~2 s), the title card. Wheel: the portrait sits between words; the page moves sideways; photos slide in and scale; text blocks fade between them.

Measured (`motion/probe.json`): GSAP 3.12.5; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Explore. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a photo-essay folio: a counter on black, a card 'Crafting narrative through design', 'Through this lens' with a portrait set between the words, then a sideways-moving essay through Lofoten (a tall photo of red cabins, serif statements in caps, a wide mountain panorama, a small aurora inset, a yellow house) where photos and text alternate as you scroll. Type: LZ, Neue-Montreal, PPNeue-Montreal.
Ground and ink from the measured palette (#FFFFFF, #95BCE5, #228ADF). Motion carries the page through
a sideways photo essay through Lofoten in serif caps. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — landscape and travel photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: landscape and travel photography

## Reference lock

Primary reference/direction: Gianluca Gradogna - Multidisciplinary Designer — A photo-essay folio: a counter on black, a card 'Crafting narrative through design', 'Through this lens' with a portrait set between the words, then a sideways-moving essay through Lofoten (a tall photo of red cabins, serif statements in caps, a wide mountain panorama, a small aurora inset, a yellow house) where photos and text alternate as you scroll.
Preserve (3-5 traits): portrait between title words; horizontal photo essay; thin serif caps statements; tall and wide photos alternating; small inset photos.
Borrow only (1-2): Run a photo essay sideways, alternating tall and wide frames with text
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: landscape and travel photography
Reject: Thin serif small text
Token commitments: palette #FFFFFF, #95BCE5, #228ADF, #211C31, #04070F, #434A68; type LZ, Neue-Montreal, PPNeue-Montreal; engine GSAP + Lenis linked (never vendored).
