---
title: "Artisans de Geneve - Bespoke Watch Personalization"
url: http://artisansdegeneve.com/en
source_url: http://artisansdegeneve.com/en
captured: 2026-10-02
origin: raw-url
extract: none
category: luxury-craft
category2: "consumer-brand"
family: watch-atelier-macro-editorial
dna: "Geneva watch customisation atelier x macro dial photography and thin serif"
register: warm photographic
grammar: chaptered editorial
lane: "A bespoke watch atelier: a legal-notice gate, a macro shot of a dial through a loupe 'New Personalization: Val Viola', then full-bleed atelier photos (bench, sketches, hands) that shrink into framed images on white with thin serif titles, bespoke project movements, warranty band, black-and-white client portraits and an exploded movement for 'Begin your personalization'."
mode: read
traits: ["macro dial photography", "full-bleed photos shrinking into frames", "thin serif titles", "bench and sketch imagery", "black and white client portraits", "floating watch movement"]
palette: ["#FFFDFC", "#504845", "#050608", "#281914", "#483021", "#7A8189"]
type: ["Futura", "Victor"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The full-bleed-to-framed shrink repeats the act of looking through a loupe and stepping back, which suits a craft measured in fractions of a millimetre.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Digidop).

## What to borrow (principle)

- Shrink full-bleed photos into framed images as the section change
- Macro detail as the hero

## What to leave

- Legal gate on arrival
- Very thin pale serif

## Signature move

A dial seen through a loupe, then atelier photos shrinking from full bleed into frames.

## Motion

Intro: legal notice gate (I understand clicked), cookie declined, then the macro dial video. Wheel (native): each full-bleed photo scales down into a framed image as the white section rises; titles fade in; the project grid shifts; portraits slide in; the movement floats and turns at the end.

Measured (`motion/probe.json`): GSAP 3.15.0; 20 ScrollTriggers; Lenis; 2 video; split text; entry gate: Decline Decline, close, I understand. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a bespoke watch atelier: a legal-notice gate, a macro shot of a dial through a loupe 'New Personalization: Val Viola', then full-bleed atelier photos (bench, sketches, hands) that shrink into framed images on white with thin serif titles, bespoke project movements, warranty band, black-and-white client portraits and an exploded movement for 'Begin your personalization'. Type: Futura, Victor.
Ground and ink from the measured palette (#FFFDFC, #504845, #050608). Motion carries the page through
a dial seen through a loupe, then atelier photos shrinking from full bleed into frames. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — macro watch photography, atelier photography, portraits

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: macro watch photography, atelier photography, portraits

## Reference lock

Primary reference/direction: Artisans de Geneve - Bespoke Watch Personalization — A bespoke watch atelier: a legal-notice gate, a macro shot of a dial through a loupe 'New Personalization: Val Viola', then full-bleed atelier photos (bench, sketches, hands) that shrink into framed images on white with thin serif titles, bespoke project movements, warranty band, black-and-white client portraits and an exploded movement for 'Begin your personalization'.
Preserve (3-5 traits): macro dial photography; full-bleed photos shrinking into frames; thin serif titles; bench and sketch imagery; black and white client portraits.
Borrow only (1-2): Shrink full-bleed photos into framed images as the section change; Macro detail as the hero
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: macro watch photography, atelier photography, portraits
Reject: Legal gate on arrival; Very thin pale serif
Token commitments: palette #FFFDFC, #504845, #050608, #281914, #483021, #7A8189; type Futura, Victor; engine GSAP + Lenis linked (never vendored).
