---
title: "Lumosine - Living systems, soft tech"
url: http://lumosine.webflow.io/
source_url: http://lumosine.webflow.io/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: "editorial"
family: algae-biotech-soft-green
dna: "Algae biomaterials x a molecule diagram that opens into an underwater film"
register: modern clean
grammar: chaptered editorial
lane: "A biomaterials concept on pale mint: a molecule-like diagram with a circular photo of algae at its core, which grows into a large lens of the sea; stacked product cards (Tactile, Edible, Remedy, Living) slide over each other; a dark green diagram section; a full-bleed underwater seagrass film with glass captions; a lime curved band; FAQ and a contact."
mode: persuade
traits: ["molecule diagram as the brand mark", "circular photo that grows", "stacked product cards", "underwater seagrass film", "glass captions over video", "lime curved band"]
palette: ["#F2FFF2", "#102610", "#34856D", "#BEC5C1", "#264E2D", "#9CA09B"]
type: ["Dmmono", "Delight", "Instrumentserif"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The molecule diagram is both logo and diagram, and its centre photo grows into the sea, so the brand's source material literally opens the page.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Let the logo's centre become a window that grows
- Stack product cards so each slides over the last

## What to leave

- Very thin type
- Pale text on mint

## Signature move

A molecule diagram whose centre opens into a lens of algae and sea.

## Motion

Intro: dark green with a spark and the name (~1.5 s), then the diagram on mint. EXPLORE SYSTEMS gate (unlocked). Wheel (Lenis ~110 px glide, 57 triggers): the centre circle grows into a large lens; product cards slide up and stack; the diagram returns on dark green and rotates; the seagrass film fills the screen while glass captions rise; a lime band curves up; the contact settles.

Measured (`motion/probe.json`): GSAP 3.15.0; 57 ScrollTriggers; Lenis; 2 video; smoothed scroll (median 151 px still travelling after input stops); entry gate: EXPLORE SYSTEMS. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a biomaterials concept on pale mint: a molecule-like diagram with a circular photo of algae at its core, which grows into a large lens of the sea; stacked product cards (Tactile, Edible, Remedy, Living) slide over each other; a dark green diagram section; a full-bleed underwater seagrass film with glass captions; a lime curved band; FAQ and a contact. Type: Dmmono, Delight, Instrumentserif.
Ground and ink from the measured palette (#F2FFF2, #102610, #34856D). Motion carries the page through
a molecule diagram whose centre opens into a lens of algae and sea. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — seaweed and underwater film, interiors, lab photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: seaweed and underwater film, interiors, lab photography

## Reference lock

Primary reference/direction: Lumosine - Living systems, soft tech — A biomaterials concept on pale mint: a molecule-like diagram with a circular photo of algae at its core, which grows into a large lens of the sea; stacked product cards (Tactile, Edible, Remedy, Living) slide over each other; a dark green diagram section; a full-bleed underwater seagrass film with glass captions; a lime curved band; FAQ and a contact.
Preserve (3-5 traits): molecule diagram as the brand mark; circular photo that grows; stacked product cards; underwater seagrass film; glass captions over video.
Borrow only (1-2): Let the logo's centre become a window that grows; Stack product cards so each slides over the last
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: seaweed and underwater film, interiors, lab photography
Reject: Very thin type; Pale text on mint
Token commitments: palette #F2FFF2, #102610, #34856D, #BEC5C1, #264E2D, #9CA09B; type Dmmono, Delight, Instrumentserif; engine GSAP + Lenis linked (never vendored).
