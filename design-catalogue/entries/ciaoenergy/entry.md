---
title: "Ciao Energy - energy drink"
url: https://www.ciaoenergy.com/
source_url: https://www.ciaoenergy.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: consumer-brand
category2: "product-focused"
family: can-carousel-dark-stage
dna: "Energy drink x a 3D can on a dark stage with a flavour carousel"
register: cinematic dark
grammar: chaptered editorial
lane: "A drink site: the 'CIAO ENERGY' logo on black with a percent, a 3D can under a spotlight with a flavour name ('Double litchi') and a progress bar, a carousel of cans fanning around it, the can tilting close with claims (moins de sucre, caféine issue de grains de café, arômes naturels) on violet smoke, a 'ZERO BULLS' violet panel, a long row of flavour cans curving away, FAQ and 'Rejoignez-nous'."
mode: persuade
traits: ["3D can under a spotlight", "flavour carousel fanning", "claims beside the tilted can", "violet smoke", "curved row of cans", "condensed italic caps"]
palette: ["#000000", "#201B2F", "#4A455A", "#79767F"]
type: ["Geistmono", "Franklin Gothic Atf", "Geist"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The can never leaves the stage; flavours, claims and the lineup all happen around it.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Skaald).

## What to borrow (principle)

- One product under a spotlight; everything else moves around it

## What to leave

- Repeats the carousel twice

## Signature move

A violet can under a spotlight with a fan of other flavours behind it.

## Motion

Intro: logo with a percent (~2 s). Wheel (Lenis): the can rotates and tilts; the carousel fans out and back; claims slide in as the can turns; violet smoke rises; the row of cans curves past; FAQ rows open.

Measured (`motion/probe.json`): GSAP 3.15.0; 14 ScrollTriggers; Lenis; WebGL canvas x1 (three.js); 7 video; split text; smoothed scroll (median 42 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a drink site: the 'CIAO ENERGY' logo on black with a percent, a 3D can under a spotlight with a flavour name ('Double litchi') and a progress bar, a carousel of cans fanning around it, the can tilting close with claims (moins de sucre, caféine issue de grains de café, arômes naturels) on violet smoke, a 'ZERO BULLS' violet panel, a long row of flavour cans curving away, FAQ and 'Rejoignez-nous'. Type: Geistmono, Franklin Gothic Atf, Geist.
Ground and ink from the measured palette (#000000, #201B2F, #4A455A). Motion carries the page through
a violet can under a spotlight with a fan of other flavours behind it. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D product

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D product

## Reference lock

Primary reference/direction: Ciao Energy - energy drink — A drink site: the 'CIAO ENERGY' logo on black with a percent, a 3D can under a spotlight with a flavour name ('Double litchi') and a progress bar, a carousel of cans fanning around it, the can tilting close with claims (moins de sucre, caféine issue de grains de café, arômes naturels) on violet smoke, a 'ZERO BULLS' violet panel, a long row of flavour cans curving away, FAQ and 'Rejoignez-nous'.
Preserve (3-5 traits): 3D can under a spotlight; flavour carousel fanning; claims beside the tilted can; violet smoke; curved row of cans.
Borrow only (1-2): One product under a spotlight; everything else moves around it
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D product
Reject: Repeats the carousel twice
Token commitments: palette #000000, #201B2F, #4A455A, #79767F; type Geistmono, Franklin Gothic Atf, Geist; engine GSAP + Lenis linked (never vendored).
