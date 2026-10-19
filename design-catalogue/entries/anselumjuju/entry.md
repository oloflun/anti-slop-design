---
title: "Juju Anselum - Software Developer and Designer"
url: https://www.anselumjuju.com/
source_url: https://www.anselumjuju.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: scattered-mockups-dev-folio
dna: "Software developer x scattered laptop mockups and a split 'About myself' portrait"
register: modern clean
grammar: chaptered editorial
lane: "A developer folio: 'Crafting journeys through vision' on black, a mosaic of device mockups, a 'Work' section where laptop mockups are scattered at different sizes and drift past, a portrait that shrinks into a frame while 'About' and 'Myself' split either side, a black about section, a 'Since 2020 / Based in India' marquee and a contact block."
mode: persuade
traits: ["scattered laptop mockups", "portrait shrinking into a frame", "words split either side of the portrait", "double marquee", "black and white alternation", "enter gate"]
palette: ["#FFFFFF", "#C3B8A8", "#81785C", "#22201E", "#A28C72", "#6A4F2E"]
type: ["Outfit"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The portrait shrinking between split words is the page's best moment; the scattered mockups give work a casual, physical feel.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Shrink a full-bleed portrait into a frame while its label splits around it

## What to leave

- Generic marquee
- Small project captions

## Signature move

A portrait shrinking into a frame as 'About' and 'Myself' split around it.

## Motion

Intro: black, the tagline fades in (~2 s); Enter gate clicked; the mockup mosaic. Wheel (Lenis ~165 px glide, 1 pin): mockups drift up at different speeds; the portrait fills the screen then scales down into a framed card while the two words slide apart; the black panel rises; marquees run both directions; the contact block slides up.

Measured (`motion/probe.json`): GSAP 3.15.0; 1 pinned sections; Lenis; WebGL canvas x2; 1 video; split text; smoothed scroll (median 181 px still travelling after input stops); entry gate: Explore my work. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a developer folio: 'Crafting journeys through vision' on black, a mosaic of device mockups, a 'Work' section where laptop mockups are scattered at different sizes and drift past, a portrait that shrinks into a frame while 'About' and 'Myself' split either side, a black about section, a 'Since 2020 / Based in India' marquee and a contact block. Type: Outfit.
Ground and ink from the measured palette (#FFFFFF, #C3B8A8, #81785C). Motion carries the page through
a portrait shrinking into a frame as 'About' and 'Myself' split around it. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — device mockups, portrait

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: device mockups, portrait

## Reference lock

Primary reference/direction: Juju Anselum - Software Developer and Designer — A developer folio: 'Crafting journeys through vision' on black, a mosaic of device mockups, a 'Work' section where laptop mockups are scattered at different sizes and drift past, a portrait that shrinks into a frame while 'About' and 'Myself' split either side, a black about section, a 'Since 2020 / Based in India' marquee and a contact block.
Preserve (3-5 traits): scattered laptop mockups; portrait shrinking into a frame; words split either side of the portrait; double marquee; black and white alternation.
Borrow only (1-2): Shrink a full-bleed portrait into a frame while its label splits around it
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: device mockups, portrait
Reject: Generic marquee; Small project captions
Token commitments: palette #FFFFFF, #C3B8A8, #81785C, #22201E, #A28C72, #6A4F2E; type Outfit; engine GSAP + Lenis linked (never vendored).
