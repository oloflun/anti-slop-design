---
title: "Gaurav Verma"
url: https://www.briskgaurav.in/
source_url: https://www.briskgaurav.in/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: pixel-skull-hud-folio
dna: "Developer folio x pixel skull and HUD grid"
register: cinematic dark
grammar: live surface
lane: "A black HUD folio that counts 04 → 99, blurs into an about panel, then sits on a grid where a pixel skull, a box, glowing eyes and the name 'GAURAV' cycle in the centre square with glitch transitions."
mode: experience
traits: ["number loader", "HUD grid with corner labels", "pixel skull and eyes icons", "glitch transitions between icons", "monospace UI"]
palette: ["#070707", "#1F1F1F"]
type: ["PPSupplyMono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

A single central square cycles through pixel characters with glitches between them, like a game's idle screen. It is an identity loop rather than a page.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A central square that cycles through a few pixel characters as the idle hero

## What to leave

- Nothing scrolls; the page is an idle loop
- Blurred about panel

## Signature move

A pixel skull that glitches into glowing eyes and the name inside a central square.

## Motion

Intro: '04' → '98' → '99' on black, then blur into an about panel (~3 s). Then: HUD grid; the centre square cycles skull → box → eyes → GAURAV → dots with glitch streaks; wheel does not scroll.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; 4 video; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: ENTER TO CONTINUE, SKIP TUTORIAL. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the live surface grammar: a black HUD folio that counts 04 → 99, blurs into an about panel, then sits on a grid where a pixel skull, a box, glowing eyes and the name 'GAURAV' cycle in the centre square with glitch transitions. Type: PPSupplyMono.
Ground and ink from the measured palette (#070707, #1F1F1F). Motion carries the page through
a pixel skull that glitches into glowing eyes and the name inside a central square. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — pixel icons in white on black, HUD lines

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: pixel icons in white on black, HUD lines

## Reference lock

Primary reference/direction: Gaurav Verma — A black HUD folio that counts 04 → 99, blurs into an about panel, then sits on a grid where a pixel skull, a box, glowing eyes and the name 'GAURAV' cycle in the centre square with glitch transitions.
Preserve (3-5 traits): number loader; HUD grid with corner labels; pixel skull and eyes icons; glitch transitions between icons; monospace UI.
Borrow only (1-2): A central square that cycles through a few pixel characters as the idle hero
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: pixel icons in white on black, HUD lines
Reject: Nothing scrolls; the page is an idle loop; Blurred about panel
Token commitments: palette #070707, #1F1F1F; type PPSupplyMono; engine GSAP + Lenis linked (never vendored).
