---
title: "Moto - premium membership card"
url: https://www.moto-card.com/
source_url: https://www.moto-card.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: luxury-craft
category2: "product-focused"
family: card-on-plinth-luxury-fintech
dna: "Premium card x a metal card on a lit plinth and a globe"
register: cinematic dark
grammar: filmic one-shot
lane: "A membership card on black: a light from above onto a plinth where a metal card lies, 'BUILT FOR MODERN WEALTH', the camera moving down past the plinth to 'INFRASTRUCTURE FOR HOW YOU MOVE' with a night globe, a thin line dropping, a dark gallery of floating photos with the white card turning in the middle 'THE CARD IS ONLY THE BEGINNING', a white section where currency amounts scroll past 'SPEND GLOBALLY. 0 FX FEES', interiors ('24/7 concierge'), a stone surface with lights, an access list, FAQ and 'A QUIETER WAY TO MOVE THROUGH THE WORLD'."
mode: persuade
traits: ["card on a lit plinth", "night globe", "floating photo gallery around the card", "currency amounts scrolling", "stone and lamp photography", "small caps headings"]
palette: ["#080808", "#E8EBEC", "#1D1F21", "#ABAFB1"]
type: ["Neuemontreal"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Treating the card like a museum object (plinth, spotlight, gallery) sells exclusivity without saying it.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Properly Studio).

## What to borrow (principle)

- Present the product on a lit plinth like a museum object

## What to leave

- Small text on dark

## Signature move

A metal card on a plinth under a single overhead light.

## Motion

Intro: black, a light comes on over the plinth (~2 s). Wheel (Lenis, 1 pin): the camera descends past the plinth; the globe rises; a line drops; photos float in depth around the turning card; the ground flips white as amounts scroll; interiors crossfade; the list rows reveal.

Measured (`motion/probe.json`): GSAP 3.15.0; 32 ScrollTriggers; 1 pinned sections; Lenis; WebGL canvas x3 (three.js); 1 video; smoothed scroll (median 95 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the filmic one-shot grammar: a membership card on black: a light from above onto a plinth where a metal card lies, 'BUILT FOR MODERN WEALTH', the camera moving down past the plinth to 'INFRASTRUCTURE FOR HOW YOU MOVE' with a night globe, a thin line dropping, a dark gallery of floating photos with the white card turning in the middle 'THE CARD IS ONLY THE BEGINNING', a white section where currency amounts scroll past 'SPEND GLOBALLY. 0 FX FEES', interiors ('24/7 concierge'), a stone surface with lights, an access list, FAQ and 'A QUIETER WAY TO MOVE THROUGH THE WORLD'. Type: Neuemontreal.
Ground and ink from the measured palette (#080808, #E8EBEC, #1D1F21). Motion carries the page through
a metal card on a plinth under a single overhead light. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D product, interior photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D product, interior photography

## Reference lock

Primary reference/direction: Moto - premium membership card — A membership card on black: a light from above onto a plinth where a metal card lies, 'BUILT FOR MODERN WEALTH', the camera moving down past the plinth to 'INFRASTRUCTURE FOR HOW YOU MOVE' with a night globe, a thin line dropping, a dark gallery of floating photos with the white card turning in the middle 'THE CARD IS ONLY THE BEGINNING', a white section where currency amounts scroll past 'SPEND GLOBALLY. 0 FX FEES', interiors ('24/7 concierge'), a stone surface with lights, an access list, FAQ and 'A QUIETER WAY TO MOVE THROUGH THE WORLD'.
Preserve (3-5 traits): card on a lit plinth; night globe; floating photo gallery around the card; currency amounts scrolling; stone and lamp photography.
Borrow only (1-2): Present the product on a lit plinth like a museum object
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D product, interior photography
Reject: Small text on dark
Token commitments: palette #080808, #E8EBEC, #1D1F21, #ABAFB1; type Neuemontreal; engine GSAP + Lenis linked (never vendored).
