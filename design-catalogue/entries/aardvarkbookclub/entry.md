---
title: "Aardvark Book Club"
url: https://www.aardvarkbookclub.com/
source_url: https://www.aardvarkbookclub.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: consumer-brand
category2: "playful"
family: book-box-pop-colour
dna: "Book subscription x a patterned box that opens and bold genre lists"
register: other
grammar: chaptered editorial
lane: "A subscription brand: a purple screen with the aardvark logo, 'Unbox stories worth talking about' on yellow waves with books falling, 'Our Oct books' as a row of covers, 'How it works' as tilted step cards with doodles, a patterned box on cyan that opens ('Think inside the box'), a magenta list of genres with book covers appearing over it, stickers 'Why Aardvark?', FAQ, 'outside of the box' and a members' choice section."
mode: persuade
traits: ["patterned box opening", "genre word list with covers", "tilted step cards", "stickers on a circle", "yellow, magenta and cyan", "rounded panels"]
palette: ["#A5F7F9", "#FEC846", "#FFFFFF", "#4C2B57", "#FCED92", "#81787A"]
type: ["Hello Organichand Webfont", "Degular", "Champ"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The box opening is the product moment; the genre list with covers popping over it is a lively catalogue.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Dylan Brouwer, Eduard Bodak, FUTURE THREE®).

## What to borrow (principle)

- Open the product box on scroll
- Pop covers over a big genre list

## What to leave

- Crowded stickers

## Signature move

A patterned box opening on cyan under 'Think inside the box'.

## Motion

Intro: purple with the logo (~1 s). Wheel: books fall; covers slide in a row; step cards fan; the box rotates and its lid opens; the genre list scrolls with covers popping; stickers spin around a circle.

Measured (`motion/probe.json`): GSAP 3.15.0; 18 ScrollTriggers; Lenis; Barba page transitions; split text; smoothed scroll (median 75 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a subscription brand: a purple screen with the aardvark logo, 'Unbox stories worth talking about' on yellow waves with books falling, 'Our Oct books' as a row of covers, 'How it works' as tilted step cards with doodles, a patterned box on cyan that opens ('Think inside the box'), a magenta list of genres with book covers appearing over it, stickers 'Why Aardvark?', FAQ, 'outside of the box' and a members' choice section. Type: Hello Organichand Webfont, Degular, Champ.
Ground and ink from the measured palette (#A5F7F9, #FEC846, #FFFFFF). Motion carries the page through
a patterned box opening on cyan under 'Think inside the box'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D box, book covers, illustration

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D box, book covers, illustration

## Reference lock

Primary reference/direction: Aardvark Book Club — A subscription brand: a purple screen with the aardvark logo, 'Unbox stories worth talking about' on yellow waves with books falling, 'Our Oct books' as a row of covers, 'How it works' as tilted step cards with doodles, a patterned box on cyan that opens ('Think inside the box'), a magenta list of genres with book covers appearing over it, stickers 'Why Aardvark?', FAQ, 'outside of the box' and a members' choice section.
Preserve (3-5 traits): patterned box opening; genre word list with covers; tilted step cards; stickers on a circle; yellow, magenta and cyan.
Borrow only (1-2): Open the product box on scroll; Pop covers over a big genre list
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D box, book covers, illustration
Reject: Crowded stickers
Token commitments: palette #A5F7F9, #FEC846, #FFFFFF, #4C2B57, #FCED92, #81787A; type Hello Organichand Webfont, Degular, Champ; engine GSAP + Lenis linked (never vendored).
