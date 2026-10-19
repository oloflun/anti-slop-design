---
title: "Elegant Seagulls - Digital creative agency"
url: https://www.elegantseagulls.com/
source_url: https://www.elegantseagulls.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: image-filled-letters-agency
dna: "Brand agency x giant words filled with work imagery and a glass lens"
register: modern clean
grammar: chaptered editorial
lane: "An agency on white: 'Creative' huge with its letters filled by a collage of their work, a glass lens playing a reel moving over it, client logos, case studies in pairs, a lime 'View more' where the lens returns, '99%' huge filled with imagery for a client result, a services mosaic and 'Hey' filled with imagery for the contact."
mode: persuade
traits: ["giant words filled with imagery", "glass lens with a reel", "lime accent", "case pairs", "stat number filled with imagery", "services mosaic"]
palette: ["#FFFFFF", "#0F181A", "#594246", "#969991", "#E7D1AF"]
type: ["Haffer"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Filling key words with the work collage (Creative, 99%, Hey) makes the typography carry the portfolio, and the lens is a recurring object.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Fill the giant word with the work collage
- A glass lens that travels and plays the reel

## What to leave

- Generic case grid

## Signature move

'Creative' with its letters filled by a collage of work and a glass lens over it.

## Motion

Intro: white, the word fills with imagery (~1.5 s), the lens floats in playing a reel. Wheel: the lens follows down the page; cases slide; '99%' fills; the mosaic assembles; 'Hey' fills at the end.

Measured (`motion/probe.json`): GSAP 3.12.2; Lenis; WebGL canvas x1 (three.js); smoothed scroll (median 204 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: an agency on white: 'Creative' huge with its letters filled by a collage of their work, a glass lens playing a reel moving over it, client logos, case studies in pairs, a lime 'View more' where the lens returns, '99%' huge filled with imagery for a client result, a services mosaic and 'Hey' filled with imagery for the contact. Type: Haffer.
Ground and ink from the measured palette (#FFFFFF, #0F181A, #594246). Motion carries the page through
'Creative' with its letters filled by a collage of work and a glass lens over it. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — agency case imagery

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: agency case imagery

## Reference lock

Primary reference/direction: Elegant Seagulls - Digital creative agency — An agency on white: 'Creative' huge with its letters filled by a collage of their work, a glass lens playing a reel moving over it, client logos, case studies in pairs, a lime 'View more' where the lens returns, '99%' huge filled with imagery for a client result, a services mosaic and 'Hey' filled with imagery for the contact.
Preserve (3-5 traits): giant words filled with imagery; glass lens with a reel; lime accent; case pairs; stat number filled with imagery.
Borrow only (1-2): Fill the giant word with the work collage; A glass lens that travels and plays the reel
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: agency case imagery
Reject: Generic case grid
Token commitments: palette #FFFFFF, #0F181A, #594246, #969991, #E7D1AF; type Haffer; engine GSAP + Lenis linked (never vendored).
