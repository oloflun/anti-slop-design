---
title: "Don Molinico - stuffed piquillo peppers"
url: https://www.donmolinico.es/
source_url: https://www.donmolinico.es/
captured: 2026-10-03
origin: raw-url
extract: none
category: consumer-brand
category2: "hospitality"
family: red-cream-food-poster
dna: "Spanish food brand x tomato red and cream, condensed poster type and tabletop photos dealt like cards"
register: warm photographic
grammar: typographic poster
lane: "A food brand like a festival poster: a cream loader, a red panel with the wordmark that splits open onto a tabletop photo, 'Desde Navarra a toda España' in huge condensed caps, a centred story paragraph in red caps, tabletop photos dealt like cards with a 'discover' badge, 'Prueba el sabor de la nueva tradición', jars in a photo with 'Nueva tradición, para picar', a yellow product section with 'Pimientos del piquillo' and a jar sitting in the type, awards and a footer."
mode: persuade
traits: ["tomato red on cream", "condensed poster caps", "tabletop photos dealt as cards", "jar sitting inside the headline", "yellow product band", "crown glyph"]
palette: ["#FCF5E8", "#582B13", "#AF734E", "#BE2525", "#B59875", "#E3B198"]
type: ["super-med"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Poster type and photos of a shared table make a jarred product feel like a fiesta rather than a supermarket shelf.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Auge Experience, ET Studio).

## What to borrow (principle)

- Set the product inside the headline instead of beside it

## What to leave

- Long paragraphs in red caps

## Signature move

A jar sitting inside 'Pimientos del piquillo' on yellow.

## Motion

Intro: cream to red panel, wordmark, the panel splits to the photo (~3 s). Wheel (Lenis): headlines rise line by line; photo cards fan and rotate; the jar scales into the type; sections wipe.

Measured (`motion/probe.json`): GSAP 3.11.3; Lenis; split text; smoothed scroll (median 136 px still travelling after input stops); entry gate: Rechazar. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the typographic poster grammar: a food brand like a festival poster: a cream loader, a red panel with the wordmark that splits open onto a tabletop photo, 'Desde Navarra a toda España' in huge condensed caps, a centred story paragraph in red caps, tabletop photos dealt like cards with a 'discover' badge, 'Prueba el sabor de la nueva tradición', jars in a photo with 'Nueva tradición, para picar', a yellow product section with 'Pimientos del piquillo' and a jar sitting in the type, awards and a footer. Type: super-med.
Ground and ink from the measured palette (#FCF5E8, #582B13, #AF734E). Motion carries the page through
a jar sitting inside 'Pimientos del piquillo' on yellow. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — food and tabletop photography, product shots

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: food and tabletop photography, product shots

## Reference lock

Primary reference/direction: Don Molinico - stuffed piquillo peppers — A food brand like a festival poster: a cream loader, a red panel with the wordmark that splits open onto a tabletop photo, 'Desde Navarra a toda España' in huge condensed caps, a centred story paragraph in red caps, tabletop photos dealt like cards with a 'discover' badge, 'Prueba el sabor de la nueva tradición', jars in a photo with 'Nueva tradición, para picar', a yellow product section with 'Pimientos del piquillo' and a jar sitting in the type, awards and a footer.
Preserve (3-5 traits): tomato red on cream; condensed poster caps; tabletop photos dealt as cards; jar sitting inside the headline; yellow product band.
Borrow only (1-2): Set the product inside the headline instead of beside it
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: food and tabletop photography, product shots
Reject: Long paragraphs in red caps
Token commitments: palette #FCF5E8, #582B13, #AF734E, #BE2525, #B59875, #E3B198; type super-med; engine GSAP + Lenis linked (never vendored).
