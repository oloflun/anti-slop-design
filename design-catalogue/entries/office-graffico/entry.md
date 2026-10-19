---
title: "Graffico Office"
url: https://office.graffico.it/
source_url: https://office.graffico.it/
captured: 2026-10-02
origin: raw-url
extract: none
category: playful
category2: "portfolio"
family: walkthrough-3d-office
dna: "Design studio x walkable 3D office"
register: warm photographic
grammar: continuous world
lane: "A studio site that is a 3D model of the studio's own office: a loader bar, an 'ENTER THE OFFICE' gate, then a sunlit room with desks and shelves to walk through."
mode: experience
traits: ["full 3D interior as the site", "loader with progress bar and retro script logo", "enter gate", "warm low-sun lighting", "no scroll; navigation by movement"]
palette: ["#63472B", "#392816", "#9E8768", "#8A7053", "#BDB2A1"]
type: ["Shrikhand", "Work Sans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Instead of describing the studio it puts you in the room. The lighting does the brand work: late sun through blinds, warm floor, plain furniture. The site is an experiment more than a page, which is why it sits in the showcase as a GSAP-core piece.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Graffico Studio).

## What to borrow (principle)

- When the place is the brand, render the place and let the visitor stand in it
- Warm directional light sells a 3D scene more than detail does

## What to leave

- Nothing reachable by scroll; the wheel does nothing
- Heavy load for a studio introduction

## Signature move

The office itself, rendered in 3D, as the homepage.

## Motion

Intro: dark loader with 'Graffico Office' in a retro script and a filling bar, then 'ENTER THE OFFICE' (~3 s). After entering: camera fades up into the sunlit room; movement is by keys/drag, not scroll (the wheel leaves the view still).

Measured (`motion/probe.json`): WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: ENTER THE OFFICE. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the continuous world grammar: a studio site that is a 3D model of the studio's own office: a loader bar, an 'ENTER THE OFFICE' gate, then a sunlit room with desks and shelves to walk through. Type: Shrikhand, Work Sans.
Ground and ink from the measured palette (#63472B, #392816, #9E8768). Motion carries the page through
the office itself, rendered in 3D, as the homepage. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D interior render, low warm sun, simple furniture

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D interior render, low warm sun, simple furniture

## Reference lock

Primary reference/direction: Graffico Office — A studio site that is a 3D model of the studio's own office: a loader bar, an 'ENTER THE OFFICE' gate, then a sunlit room with desks and shelves to walk through.
Preserve (3-5 traits): full 3D interior as the site; loader with progress bar and retro script logo; enter gate; warm low-sun lighting; no scroll; navigation by movement.
Borrow only (1-2): When the place is the brand, render the place and let the visitor stand in it; Warm directional light sells a 3D scene more than detail does
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D interior render, low warm sun, simple furniture
Reject: Nothing reachable by scroll; the wheel does nothing; Heavy load for a studio introduction
Token commitments: palette #63472B, #392816, #9E8768, #8A7053, #BDB2A1; type Shrikhand, Work Sans; engine GSAP + Lenis linked (never vendored).
