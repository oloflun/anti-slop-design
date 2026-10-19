---
title: "THE1 - office building, Amsterdam"
url: https://the1.amsterdam/
source_url: https://the1.amsterdam/
captured: 2026-10-03
origin: raw-url
extract: none
category: hospitality
category2: "institutional"
family: colour-entrance-office-building
dna: "Office building x pale grey, colour blocks for its coloured entrances, a giant numeral per fact and photos of the wharf"
register: modern clean
grammar: chaptered editorial
lane: "An office building: 'For the one who is creative / social' with the last word cycling, four colour blocks (green, pink, yellow, red) with the building in each, 'Why are we the one?', facts as giant numerals filling coloured panels (2 colourful entrances, 4 floors of space), a strip of neighbourhood photos, a ferry, 'we cultivate creativity, collaboration' with photos scaled into a circle, interiors with an amenity list, a map on yellow and 'THE1' in huge letters with colour blocks."
mode: persuade
traits: ["cycling last word", "colour blocks per entrance", "giant numerals on coloured panels", "circle photo mask", "amenity list beside interiors"]
palette: ["#D9D9D9", "#F09EC8", "#1C2123", "#9B8B8E", "#4B7767", "#C2C2BE"]
type: ["KH Teka Regular", "KH Teka Medium", "KH Teka Regular Placeholder", "KH Teka Medium Placeholder"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The building's coloured entrances become the page's palette and wayfinding, so the brand comes from the architecture itself.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Analogue Agency).

## What to borrow (principle)

- Take the palette from a physical feature of the place

## What to leave

- Small amenity text

## Signature move

Giant numerals '2' and '4' filling yellow and pink panels.

## Motion

Wheel (Lenis): the last word cycles; colour panels slide over each other; photos scale into a circle; numerals rise.

Measured (`motion/probe.json`): Lenis; 2 video; split text; smoothed scroll (median 77 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: an office building: 'For the one who is creative / social' with the last word cycling, four colour blocks (green, pink, yellow, red) with the building in each, 'Why are we the one?', facts as giant numerals filling coloured panels (2 colourful entrances, 4 floors of space), a strip of neighbourhood photos, a ferry, 'we cultivate creativity, collaboration' with photos scaled into a circle, interiors with an amenity list, a map on yellow and 'THE1' in huge letters with colour blocks. Type: KH Teka Regular, KH Teka Medium, KH Teka Regular Placeholder, KH Teka Medium Placeholder.
Ground and ink from the measured palette (#D9D9D9, #F09EC8, #1C2123). Motion carries the page through
giant numerals '2' and '4' filling yellow and pink panels. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — architectural and neighbourhood photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: architectural and neighbourhood photography

## Reference lock

Primary reference/direction: THE1 - office building, Amsterdam — An office building: 'For the one who is creative / social' with the last word cycling, four colour blocks (green, pink, yellow, red) with the building in each, 'Why are we the one?', facts as giant numerals filling coloured panels (2 colourful entrances, 4 floors of space), a strip of neighbourhood photos, a ferry, 'we cultivate creativity, collaboration' with photos scaled into a circle, interiors with an amenity list, a map on yellow and 'THE1' in huge letters with colour blocks.
Preserve (3-5 traits): cycling last word; colour blocks per entrance; giant numerals on coloured panels; circle photo mask; amenity list beside interiors.
Borrow only (1-2): Take the palette from a physical feature of the place
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: architectural and neighbourhood photography
Reject: Small amenity text
Token commitments: palette #D9D9D9, #F09EC8, #1C2123, #9B8B8E, #4B7767, #C2C2BE; type KH Teka Regular, KH Teka Medium, KH Teka Regular Placeholder, KH Teka Medium Placeholder; engine GSAP + Lenis linked (never vendored).
