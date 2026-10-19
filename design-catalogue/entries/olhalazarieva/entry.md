---
title: "Olha Lazarieva - Creative Designer"
url: https://olhalazarieva.com/
source_url: https://olhalazarieva.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: ring-text-gallery-room
dna: "Creative designer x a rotating text ring and a 3D gallery room for cases"
register: cinematic dark
grammar: continuous world
lane: "A designer folio: a 3D ring of text ('Design that changes the world') spinning on white with a percent, 'About me' rising, a black statement whose letters scatter and settle, a portrait with a mono bio, then 'Recent work' where the camera walks down a white-lit 3D gallery corridor to a framed screen with a rock image, and services and awards on white."
mode: read
traits: ["3D rotating text ring", "letters scattering and resettling", "mono body text", "3D gallery corridor for cases", "framed screen at the end of the room", "condensed headline face"]
palette: ["#F7F7F7", "#525152", "#ABABAB", "#838383", "#DBDBDB", "#3D3D3D"]
type: ["Sofia Sans Condensed", "Spline Sans Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Walking down a gallery corridor to the work is a strong spatial metaphor, and the text ring gives the loader a memorable form.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Present a case inside a 3D gallery room you walk into

## What to leave

- Scattered letters hard to read
- Small mono text

## Signature move

The camera walking down a lit gallery corridor towards a framed case.

## Motion

Intro: white, a ring of text spins and tilts while a percent counts (~3 s). Wheel (Lenis, WebGL): 'About me' rises on grey; the black statement's letters fly apart and back; the portrait slides in; the camera moves through the corridor to the framed screen; the room fades to the white services panel.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x2 (three.js); smoothed scroll (median 145 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the continuous world grammar: a designer folio: a 3D ring of text ('Design that changes the world') spinning on white with a percent, 'About me' rising, a black statement whose letters scatter and settle, a portrait with a mono bio, then 'Recent work' where the camera walks down a white-lit 3D gallery corridor to a framed screen with a rock image, and services and awards on white. Type: Sofia Sans Condensed, Spline Sans Mono.
Ground and ink from the measured palette (#F7F7F7, #525152, #ABABAB). Motion carries the page through
the camera walking down a lit gallery corridor towards a framed case. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D text and gallery room, portrait

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D text and gallery room, portrait

## Reference lock

Primary reference/direction: Olha Lazarieva - Creative Designer — A designer folio: a 3D ring of text ('Design that changes the world') spinning on white with a percent, 'About me' rising, a black statement whose letters scatter and settle, a portrait with a mono bio, then 'Recent work' where the camera walks down a white-lit 3D gallery corridor to a framed screen with a rock image, and services and awards on white.
Preserve (3-5 traits): 3D rotating text ring; letters scattering and resettling; mono body text; 3D gallery corridor for cases; framed screen at the end of the room.
Borrow only (1-2): Present a case inside a 3D gallery room you walk into
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D text and gallery room, portrait
Reject: Scattered letters hard to read; Small mono text
Token commitments: palette #F7F7F7, #525152, #ABABAB, #838383, #DBDBDB, #3D3D3D; type Sofia Sans Condensed, Spline Sans Mono; engine GSAP + Lenis linked (never vendored).
