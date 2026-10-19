---
title: "Jesper Landberg"
url: https://jesperlandberg.com/
source_url: https://jesperlandberg.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: curved-panel-gallery-wall
dna: "Creative developer folio x curved WebGL gallery wall"
register: cinematic dark
grammar: gallery/catalog
lane: "A black space where every project is a large card bent onto a curved wall, the wall turning past the viewer as you wheel, with a floor grid giving depth."
mode: experience
traits: ["project cards bent on a curved WebGL wall", "floor grid perspective", "wheel turns the wall (virtual)", "small mono chrome", "text panels in the same wall"]
palette: ["#000000", "#857470", "#352624", "#61524B", "#AFACA5"]
type: ["sans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The developer's craft is the presentation itself: cards are mapped onto a curved surface so they bend as they pass the centre, and a faint floor grid makes the black a room. Text cards sit in the same wall as the images, so the story and the work share one surface.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Jesper Landberg).

## What to borrow (principle)

- Bend cards onto a curved surface so passing motion reads as depth
- A faint floor grid turns a black background into a space
- Put text panels in the same carousel as the work

## What to leave

- Wheel-only; no overview
- Cards cropped at both edges at all times

## Signature move

Project cards bent onto a curved wall that turns past the viewer.

## Motion

Intro: black, a small dashed loader, then the curved wall fades in mid-turn (~2.5 s). Wheel (virtual, WebGL, GSAP core): the wall rotates continuously with inertia; cards bend more at the edges; a pink blank card marks a section break; the about card with large type passes in the same row.

Measured (`motion/probe.json`): GSAP 3.15.0; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the gallery/catalog grammar: a black space where every project is a large card bent onto a curved wall, the wall turning past the viewer as you wheel, with a floor grid giving depth. Type: sans.
Ground and ink from the measured palette (#000000, #857470, #352624). Motion carries the page through
project cards bent onto a curved wall that turns past the viewer. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project key visuals as large cards on black

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project key visuals as large cards on black

## Reference lock

Primary reference/direction: Jesper Landberg — A black space where every project is a large card bent onto a curved wall, the wall turning past the viewer as you wheel, with a floor grid giving depth.
Preserve (3-5 traits): project cards bent on a curved WebGL wall; floor grid perspective; wheel turns the wall (virtual); small mono chrome; text panels in the same wall.
Borrow only (1-2): Bend cards onto a curved surface so passing motion reads as depth; A faint floor grid turns a black background into a space
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project key visuals as large cards on black
Reject: Wheel-only; no overview; Cards cropped at both edges at all times
Token commitments: palette #000000, #857470, #352624, #61524B, #AFACA5; type sans; engine GSAP + Lenis linked (never vendored).
