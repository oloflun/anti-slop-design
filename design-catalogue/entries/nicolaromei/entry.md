---
title: "Nicola Romei - Digital Experience Designer"
url: https://www.nicolaromei.com/
source_url: https://www.nicolaromei.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: monochrome-artboard-wall
dna: "Digital experience designer x a scrolling monochrome artboard wall"
register: cinematic dark
grammar: gallery/catalog
lane: "A designer's folio as one endless monochrome wall: a tiny image loader on white, then 'THE ARTBOARD' fills the screen with columns of black-and-white portraits, product shots, posters and type pieces moving at different speeds and wrapping around forever."
mode: experience
traits: ["monochrome image wall", "columns at different speeds", "infinite wrap", "poster type tiles mixed with photos", "tiny metadata header", "virtual scroll"]
palette: ["#1C1C1C", "#474747", "#9E9F9F", "#888888", "#656565", "#C2C2C2"]
type: ["Easegeometricb", "Host Grotesk", "john-doe", "prestige-elite-std"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Desaturating everything turns very different projects into one artwork, and the columns moving at different speeds give a flat grid depth.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Desaturate a mixed portfolio into one wall
- Run columns at different speeds for depth

## What to leave

- No way to tell projects apart while scrolling
- Text tiles hard to read in motion

## Signature move

An endless black-and-white artboard wall with columns sliding at different speeds.

## Motion

Intro: white with a tiny thumbnail loader cycling images (~2 s), then the wall cuts in. Wheel (virtual, no native scroll): columns move vertically at different speeds and wrap; tiles flicker into place; the 'THE ARTBOARD' label stays fixed bottom left. Barba page transitions.

Measured (`motion/probe.json`): GSAP 3.15.0; 1 ScrollTriggers; Barba page transitions; WebGL canvas x1 (three.js); 1 video; split text; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: CLOSE. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the gallery/catalog grammar: a designer's folio as one endless monochrome wall: a tiny image loader on white, then 'THE ARTBOARD' fills the screen with columns of black-and-white portraits, product shots, posters and type pieces moving at different speeds and wrapping around forever. Type: Easegeometricb, Host Grotesk, john-doe, prestige-elite-std.
Ground and ink from the measured palette (#1C1C1C, #474747, #9E9F9F). Motion carries the page through
an endless black-and-white artboard wall with columns sliding at different speeds. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — monochrome photography, posters, device mockups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: monochrome photography, posters, device mockups

## Reference lock

Primary reference/direction: Nicola Romei - Digital Experience Designer — A designer's folio as one endless monochrome wall: a tiny image loader on white, then 'THE ARTBOARD' fills the screen with columns of black-and-white portraits, product shots, posters and type pieces moving at different speeds and wrapping around forever.
Preserve (3-5 traits): monochrome image wall; columns at different speeds; infinite wrap; poster type tiles mixed with photos; tiny metadata header.
Borrow only (1-2): Desaturate a mixed portfolio into one wall; Run columns at different speeds for depth
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: monochrome photography, posters, device mockups
Reject: No way to tell projects apart while scrolling; Text tiles hard to read in motion
Token commitments: palette #1C1C1C, #474747, #9E9F9F, #888888, #656565, #C2C2C2; type Easegeometricb, Host Grotesk, john-doe, prestige-elite-std; engine GSAP + Lenis linked (never vendored).
