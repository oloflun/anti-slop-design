---
title: "SAV1N - High-Performance Web Design"
url: http://sav1n.com/
source_url: http://sav1n.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: 3d-head-freelancer-folio
dna: "Web designer x giant 3D heads and a skyscraper canyon behind project screens"
register: cinematic dark
grammar: chaptered editorial
lane: "A web designer folio: outline-numeral loader, a split hero with a dark glass orb, numbered process cards, 'Creating unique experiences that speak for themselves', then project screens floating in front of large 3D backdrops (a skyscraper canyon, a robot head with a purple visor that dissolves, an ocean cliff), a white 'Crafting digital experiences that convert' with flickering letters and an about block."
mode: persuade
traits: ["outline numeral loader", "big 3D backdrops per project", "robot head that dissolves into particles", "project screen floating in front", "letters flickering on", "dark teal and white"]
palette: ["#000000", "#6E777D", "#192228", "#414346", "#C5CBD1"]
type: ["Roboto", "Rubik", "Inter"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Each project gets a cinematic backdrop, so the screenshots read as scenes, and the dissolving robot head is a memorable transition.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Give each project screen its own 3D backdrop
- Dissolve a 3D object into particles between projects

## What to leave

- Many styles on one page
- Small body text

## Signature move

A robot head with a purple visor dissolving behind a floating project screen.

## Motion

Intro: white with an outline percent counter (~2 s). Wheel (Lenis ~110 px glide, 4 pins, DrawSVG): the orb rotates; process cards stack; the statement letters spread; the camera rises between skyscrapers behind a pinned project screen; the robot head turns and breaks into particles; ocean waves under the next screen; a white panel slides up with flickering letters.

Measured (`motion/probe.json`): GSAP 3.13.0; 47 ScrollTriggers; 4 pinned sections; Lenis; WebGL canvas x8 (three.js); 6 video; split text; smoothed scroll (median 121 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a web designer folio: outline-numeral loader, a split hero with a dark glass orb, numbered process cards, 'Creating unique experiences that speak for themselves', then project screens floating in front of large 3D backdrops (a skyscraper canyon, a robot head with a purple visor that dissolves, an ocean cliff), a white 'Crafting digital experiences that convert' with flickering letters and an about block. Type: Roboto, Rubik, Inter.
Ground and ink from the measured palette (#000000, #6E777D, #192228). Motion carries the page through
a robot head with a purple visor dissolving behind a floating project screen. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D renders, project screenshots, portrait

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D renders, project screenshots, portrait

## Reference lock

Primary reference/direction: SAV1N - High-Performance Web Design — A web designer folio: outline-numeral loader, a split hero with a dark glass orb, numbered process cards, 'Creating unique experiences that speak for themselves', then project screens floating in front of large 3D backdrops (a skyscraper canyon, a robot head with a purple visor that dissolves, an ocean cliff), a white 'Crafting digital experiences that convert' with flickering letters and an about block.
Preserve (3-5 traits): outline numeral loader; big 3D backdrops per project; robot head that dissolves into particles; project screen floating in front; letters flickering on.
Borrow only (1-2): Give each project screen its own 3D backdrop; Dissolve a 3D object into particles between projects
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D renders, project screenshots, portrait
Reject: Many styles on one page; Small body text
Token commitments: palette #000000, #6E777D, #192228, #414346, #C5CBD1; type Roboto, Rubik, Inter; engine GSAP + Lenis linked (never vendored).
