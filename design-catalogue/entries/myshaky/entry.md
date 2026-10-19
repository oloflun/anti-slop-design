---
title: "Shaky Gotcha"
url: https://myshaky.com/gotcha
source_url: https://myshaky.com/gotcha
captured: 2026-10-02
origin: raw-url
extract: none
category: playful
category2: ""
family: neon-space-gacha-game
dna: "Gacha mini-game x neon space arcade"
register: illustrated dark
grammar: live surface
lane: "A browser game page: a starfield with neon UFO beams and a START button, then a 3D rotating tower of collectible cards, behind a daily-rewards modal."
mode: experience
traits: ["3D starfield with neon light beams", "START button gate", "rotating 3D card tower", "neon arcade UI panels", "game modal on entry"]
palette: ["#011C2D", "#0D0A0B", "#6E7464", "#6F9F77", "#4C453E"]
type: []
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

It is an arcade cabinet rather than a page: the intro is an attract screen, START opens a spinning 3D tower of collectibles. It sits in the showcase for its Observer-driven interaction, not for scroll.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- An attract-screen intro (moving scene + START) for a page that is a game

## What to leave

- A rewards modal blocks the first view
- No scroll path; the wheel is unused

## Signature move

A rotating 3D tower of collectible cards launched from a neon space attract screen.

## Motion

Intro: black with a small loader, a starfield with UFOs sweeping neon beams, 'START' (~2.5 s). After START: camera swings to a rotating cylinder of cards with portal effects; a daily-rewards modal opens on top (captured frames stay on it). Observer handles drag/wheel input.

Measured (`motion/probe.json`): WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: ×, START. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the live surface grammar: a browser game page: a starfield with neon UFO beams and a START button, then a 3D rotating tower of collectible cards, behind a daily-rewards modal. Type: read from the captures.
Ground and ink from the measured palette (#011C2D, #0D0A0B, #6E7464). Motion carries the page through
a rotating 3D tower of collectible cards launched from a neon space attract screen. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D toy characters and neon arcade graphics

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D toy characters and neon arcade graphics

## Reference lock

Primary reference/direction: Shaky Gotcha — A browser game page: a starfield with neon UFO beams and a START button, then a 3D rotating tower of collectible cards, behind a daily-rewards modal.
Preserve (3-5 traits): 3D starfield with neon light beams; START button gate; rotating 3D card tower; neon arcade UI panels; game modal on entry.
Borrow only (1-2): An attract-screen intro (moving scene + START) for a page that is a game
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D toy characters and neon arcade graphics
Reject: A rewards modal blocks the first view; No scroll path; the wheel is unused
Token commitments: palette #011C2D, #0D0A0B, #6E7464, #6F9F77, #4C453E; type -; engine GSAP + Lenis linked (never vendored).
