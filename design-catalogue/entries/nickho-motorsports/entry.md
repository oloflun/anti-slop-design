---
title: "Nick Ho Motorsports"
url: https://nickho-motorsports.nl/
source_url: https://nickho-motorsports.nl/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: race-number-driver-poster
dna: "Racing driver profile x race-number poster type"
register: cinematic dark
grammar: chaptered editorial
lane: "A racing driver's page that counts in on a giant race number 98, cuts to black-and-white helmet photography with lap timers, then runs sponsor walls, a career timeline and a race calendar in condensed caps with one signal yellow."
mode: persuade
traits: ["giant race number as the loader and hero", "condensed caps (Anton) with yellow highlighted phrases", "black-and-white motorsport photography", "live-looking lap timer", "helmet as a centred object among sponsor logos", "career steps 1/5 to 5/5"]
palette: ["#FFFFFF", "#0E0E0E", "#D0C99F", "#55595B", "#98968F", "#2C2C2D"]
type: ["Anton", "Helvetica"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The page borrows the visual grammar of a race weekend: the car number is the hero, a timer ticks in the corner, sponsor marks sit around the helmet like on a livery board. Photography is black-and-white so the one yellow (the team colour) marks only what matters: key phrases and controls.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: BORING).

## What to borrow (principle)

- Use the subject's own number or code as the loader and the hero type
- Highlight the important clause of a manifesto in the accent colour instead of bolding it
- Set an object (helmet) at centre and let sponsors orbit it as a logo wall

## What to leave

- 97 ScrollTriggers for a page of this length
- Some sections are very empty black with a single small photo

## Signature move

A race number '98' that counts in and becomes the hero over the driver's helmet.

## Motion

Intro: dotted loader, then '98' snaps in at centre on white and the black-and-white driver photo fills behind it (~2.5 s). Scroll (Lenis, 97 ScrollTriggers, SplitText): the hero compresses upward; manifesto lines reveal with yellow phrases; logos scatter in around a rotating helmet; career chapters 1/5–5/5 pin with photos crossfading; 'MEDIA & ARTICLES' huge outline type behind a horizontal card row; race calendar with the car rising between the list columns.

Measured (`motion/probe.json`): GSAP 3.15.0; 97 ScrollTriggers; Lenis; WebGL canvas x1 (three.js); 1 video; split text; smoothed scroll (median 81 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a racing driver's page that counts in on a giant race number 98, cuts to black-and-white helmet photography with lap timers, then runs sponsor walls, a career timeline and a race calendar in condensed caps with one signal yellow. Type: Anton, Helvetica.
Ground and ink from the measured palette (#FFFFFF, #0E0E0E, #D0C99F). Motion carries the page through
a race number '98' that counts in and becomes the hero over the driver's helmet. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — high-contrast black-and-white motorsport photography, helmets, pit lane, one team colour

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: high-contrast black-and-white motorsport photography, helmets, pit lane, one team colour

## Reference lock

Primary reference/direction: Nick Ho Motorsports — A racing driver's page that counts in on a giant race number 98, cuts to black-and-white helmet photography with lap timers, then runs sponsor walls, a career timeline and a race calendar in condensed caps with one signal yellow.
Preserve (3-5 traits): giant race number as the loader and hero; condensed caps (Anton) with yellow highlighted phrases; black-and-white motorsport photography; live-looking lap timer; helmet as a centred object among sponsor logos.
Borrow only (1-2): Use the subject's own number or code as the loader and the hero type; Highlight the important clause of a manifesto in the accent colour instead of bolding it
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: high-contrast black-and-white motorsport photography, helmets, pit lane, one team colour
Reject: 97 ScrollTriggers for a page of this length; Some sections are very empty black with a single small photo
Token commitments: palette #FFFFFF, #0E0E0E, #D0C99F, #55595B, #98968F, #2C2C2D; type Anton, Helvetica; engine GSAP + Lenis linked (never vendored).
