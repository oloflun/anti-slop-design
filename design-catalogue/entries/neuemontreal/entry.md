---
title: "PP Neue Montreal - typeface site"
url: https://neuemontreal.com/
source_url: https://neuemontreal.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: editorial
category2: "playful"
family: type-specimen-colour-blocks
dna: "Typeface specimen x giant glyphs, colour blocks and Expo 67 photography"
register: editorial print
grammar: typographic poster
lane: "A type specimen: a ring of 'NM' marks, 'Out with the old, in with the Neue' in colour on black, a typeface timeline with posters flying, 'From Vieux-Montreal to Neue-Montreal' over a highway photo, a weights rainbow, giant glyphs (a, 8, h, ss, ae) in bold on cream, 'Already in use, worldwide!' in orange italic on sky blue, language support with Expo 67 flags, accented glyph strips, 'Built for the city' with transit tickets, and 'One font fits all'."
mode: read
traits: ["giant glyphs cropped", "colour blocks per section", "weights rainbow", "Expo 67 photography", "transit ticket props", "italic orange display"]
palette: ["#EF4B45", "#1A1A1A", "#596161", "#737474", "#ABBC98", "#8E3B4A"]
type: ["PP Neue Montreal Text Medium", "PP Neue Montreal Text Regular", "PP Neue Montreal Hairline", "PP Neue Montreal Extralight"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The specimen uses the typeface as the image: glyphs at poster scale and colour blocks do what photos would.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Demande Spéciale, Pangram Pangram).

## What to borrow (principle)

- Let the letterforms be the imagery at poster scale

## What to leave

- Very dense specimen pages

## Signature move

A giant bold '8' cropped on cream beside 'Display / Extrabold'.

## Motion

Intro: black with the ring (~2 s). Wheel (Lenis): posters fly; the photo scales; the rainbow slides; glyphs scroll at different speeds; colour blocks wipe; tickets slide.

Measured (`motion/probe.json`): Lenis; 1 video; split text; smoothed scroll (median 125 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the typographic poster grammar: a type specimen: a ring of 'NM' marks, 'Out with the old, in with the Neue' in colour on black, a typeface timeline with posters flying, 'From Vieux-Montreal to Neue-Montreal' over a highway photo, a weights rainbow, giant glyphs (a, 8, h, ss, ae) in bold on cream, 'Already in use, worldwide!' in orange italic on sky blue, language support with Expo 67 flags, accented glyph strips, 'Built for the city' with transit tickets, and 'One font fits all'. Type: PP Neue Montreal Text Medium, PP Neue Montreal Text Regular, PP Neue Montreal Hairline, PP Neue Montreal Extralight.
Ground and ink from the measured palette (#EF4B45, #1A1A1A, #596161). Motion carries the page through
a giant bold '8' cropped on cream beside 'Display / Extrabold'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — type, archive photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: type, archive photography

## Reference lock

Primary reference/direction: PP Neue Montreal - typeface site — A type specimen: a ring of 'NM' marks, 'Out with the old, in with the Neue' in colour on black, a typeface timeline with posters flying, 'From Vieux-Montreal to Neue-Montreal' over a highway photo, a weights rainbow, giant glyphs (a, 8, h, ss, ae) in bold on cream, 'Already in use, worldwide!' in orange italic on sky blue, language support with Expo 67 flags, accented glyph strips, 'Built for the city' with transit tickets, and 'One font fits all'.
Preserve (3-5 traits): giant glyphs cropped; colour blocks per section; weights rainbow; Expo 67 photography; transit ticket props.
Borrow only (1-2): Let the letterforms be the imagery at poster scale
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: type, archive photography
Reject: Very dense specimen pages
Token commitments: palette #EF4B45, #1A1A1A, #596161, #737474, #ABBC98, #8E3B4A; type PP Neue Montreal Text Medium, PP Neue Montreal Text Regular, PP Neue Montreal Hairline, PP Neue Montreal Extralight; engine GSAP + Lenis linked (never vendored).
