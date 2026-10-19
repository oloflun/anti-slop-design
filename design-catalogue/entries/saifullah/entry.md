---
title: "Saifullah Butt"
url: https://www.saifullah.dev/
source_url: https://www.saifullah.dev/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: particle-face-dev-folio
dna: "Creative frontend developer x particle-scan portrait"
register: cinematic dark
grammar: live surface
lane: "A dark folio that loads 0% → 100% while a face forms out of particles, then holds a white particle-scan portrait at centre with 'CREATIVE DEVELOPER' glitching in and out at left and a HUD of skills at right."
mode: experience
traits: ["percentage loader", "particle/point-cloud portrait", "glitching condensed headline", "HUD stat panel", "marquee nav row", "ScrambleText"]
palette: ["#111111", "#494949"]
type: ["denominary", "csGenio"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The portrait is the content: a point-cloud face that assembles during the load and keeps breathing. The headline flickers between faint and bright as if scanned, and a small HUD at the side makes the page read as a readout of the person.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Form the hero object out of particles during the percentage load
- A headline that flickers in brightness like a scan instead of a static title

## What to leave

- Nothing changes under the wheel; the page is one screen
- Headline is mostly faint

## Signature move

A point-cloud portrait that assembles during the loader and keeps breathing.

## Motion

Intro: 0% → 17% → 85% → 100% in the corner while the face resolves from a blur into points (~2.5 s); 'Enter portfolio'. Then: the particle face rotates subtly; 'CREATIVE DEVELOPER' flickers line by line; nav marquee runs; the HUD values scramble. Wheel does not move the page (ScrollSmoother present, single screen).

Measured (`motion/probe.json`): GSAP 3.15.0; WebGL canvas x2 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Enter portfolio. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the live surface grammar: a dark folio that loads 0% → 100% while a face forms out of particles, then holds a white particle-scan portrait at centre with 'CREATIVE DEVELOPER' glitching in and out at left and a HUD of skills at right. Type: denominary, csGenio.
Ground and ink from the measured palette (#111111, #494949). Motion carries the page through
a point-cloud portrait that assembles during the loader and keeps breathing. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D scanned face as a point cloud, white on black

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D scanned face as a point cloud, white on black

## Reference lock

Primary reference/direction: Saifullah Butt — A dark folio that loads 0% → 100% while a face forms out of particles, then holds a white particle-scan portrait at centre with 'CREATIVE DEVELOPER' glitching in and out at left and a HUD of skills at right.
Preserve (3-5 traits): percentage loader; particle/point-cloud portrait; glitching condensed headline; HUD stat panel; marquee nav row.
Borrow only (1-2): Form the hero object out of particles during the percentage load; A headline that flickers in brightness like a scan instead of a static title
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D scanned face as a point cloud, white on black
Reject: Nothing changes under the wheel; the page is one screen; Headline is mostly faint
Token commitments: palette #111111, #494949; type denominary, csGenio; engine GSAP + Lenis linked (never vendored).
