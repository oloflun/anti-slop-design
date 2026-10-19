---
title: "YanXin Zhang - designer portfolio"
url: https://yanxinzhang.com/
source_url: https://yanxinzhang.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: emoji-glyph-headline-portfolio
dna: "Designer portfolio x a headline whose letters start as objects and stickers and settle into type, then orange and black chapters"
register: other
grammar: chaptered editorial
lane: "A designer's site: 'the chaos of making sh*t real' assembling from stray objects (a toy, a vinyl, a chip, a cassette) that turn into its letters, a bio with tiny inline images between words, project cards fanned in a stack, a lime marquee 'It's a success!' with check stamps, 'featured work*' scrolling sideways, project rows, an orange 'what i do*' with a 3D tomato, a black 'clients*' where project photos float in depth, and 'YanXin /2026'."
mode: persuade
traits: ["objects that become letters", "inline images inside the bio", "fanned project stack", "lime success marquee", "orange services chapter", "photos floating in 3D on black"]
palette: ["#FFFFFF", "#EAEAEA", "#4A1136", "#836469", "#CCF662", "#C4D4A9"]
type: ["EB Garamond", "Outfit", "EB Garamond Placeholder", "Outfit Placeholder"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Letters that start as objects make the headline's claim (chaos into something real) happen in front of you.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: YanXin Zhang).

## What to borrow (principle)

- Let the headline's letters begin as objects and settle into type

## What to leave

- Asterisks on every heading

## Signature move

'the chaos of making sh*t real' assembling from stray objects.

## Motion

Intro: objects fall into letter positions and swap for glyphs (~2 s). Wheel (Lenis): cards fan; the marquee runs; the featured title scrolls sideways; photos drift in depth on black.

Measured (`motion/probe.json`): Lenis; 7 video; smoothed scroll (median 119 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a designer's site: 'the chaos of making sh*t real' assembling from stray objects (a toy, a vinyl, a chip, a cassette) that turn into its letters, a bio with tiny inline images between words, project cards fanned in a stack, a lime marquee 'It's a success!' with check stamps, 'featured work*' scrolling sideways, project rows, an orange 'what i do*' with a 3D tomato, a black 'clients*' where project photos float in depth, and 'YanXin /2026'. Type: EB Garamond, Outfit, EB Garamond Placeholder, Outfit Placeholder.
Ground and ink from the measured palette (#FFFFFF, #EAEAEA, #4A1136). Motion carries the page through
'the chaos of making sh*t real' assembling from stray objects. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product objects, project imagery

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product objects, project imagery

## Reference lock

Primary reference/direction: YanXin Zhang - designer portfolio — A designer's site: 'the chaos of making sh*t real' assembling from stray objects (a toy, a vinyl, a chip, a cassette) that turn into its letters, a bio with tiny inline images between words, project cards fanned in a stack, a lime marquee 'It's a success!' with check stamps, 'featured work*' scrolling sideways, project rows, an orange 'what i do*' with a 3D tomato, a black 'clients*' where project photos float in depth, and 'YanXin /2026'.
Preserve (3-5 traits): objects that become letters; inline images inside the bio; fanned project stack; lime success marquee; orange services chapter.
Borrow only (1-2): Let the headline's letters begin as objects and settle into type
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product objects, project imagery
Reject: Asterisks on every heading
Token commitments: palette #FFFFFF, #EAEAEA, #4A1136, #836469, #CCF662, #C4D4A9; type EB Garamond, Outfit, EB Garamond Placeholder, Outfit Placeholder; engine GSAP + Lenis linked (never vendored).
