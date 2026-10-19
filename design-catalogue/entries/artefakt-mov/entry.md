---
title: "Artefakt"
url: https://artefakt.mov/
source_url: https://artefakt.mov/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: pixel-dissolve-production-reel
dna: "Hybrid production studio x pixel-dissolve between films"
register: cinematic dark
grammar: rhythmic cutlist
lane: "A Frankfurt production studio whose reel cuts between full-bleed commercials by dissolving each film into ragged pixel blocks that reveal the next one, with a small project title in the lower left."
mode: experience
traits: ["full-bleed commercial films", "pixel-block dissolve between films", "small caps titles lower left", "mono metadata in corners", "Taxi transitions"]
palette: ["#0B0B0B", "#4A5772", "#202D3F", "#4D3648", "#7E9376", "#351C23"]
type: ["DrukWide", "TronicaMono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The transition is the identity: every cut is a pixel dissolve, ragged blocks of the next film eating through the current one. It fits a 'hybrid' (AI + film) studio and makes a plain reel distinctive.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Use a pixel-block dissolve as the only cut in a reel
- Keep titles tiny so the transition is the visible design

## What to leave

- Black frames during load
- Dissolve frames obscure faces

## Signature move

Films that dissolve into ragged pixel blocks to reveal the next one.

## Motion

Intro: black for ~2.5 s. Scroll (Lenis, ~150 px glide, Taxi, three.js): first film full bleed (football 'Future Stars'); each scroll step dissolves it in ragged pixel blocks into the next (Nightography, a finance ad, McDonald's 'Käsy', music video); titles swap lower left.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; Taxi page transitions; WebGL canvas x1 (three.js); 6 video; split text; smoothed scroll (median 159 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the rhythmic cutlist grammar: a Frankfurt production studio whose reel cuts between full-bleed commercials by dissolving each film into ragged pixel blocks that reveal the next one, with a small project title in the lower left. Type: DrukWide, TronicaMono.
Ground and ink from the measured palette (#0B0B0B, #4A5772, #202D3F). Motion carries the page through
films that dissolve into ragged pixel blocks to reveal the next one. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — commercial film frames, saturated grading

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: commercial film frames, saturated grading

## Reference lock

Primary reference/direction: Artefakt — A Frankfurt production studio whose reel cuts between full-bleed commercials by dissolving each film into ragged pixel blocks that reveal the next one, with a small project title in the lower left.
Preserve (3-5 traits): full-bleed commercial films; pixel-block dissolve between films; small caps titles lower left; mono metadata in corners; Taxi transitions.
Borrow only (1-2): Use a pixel-block dissolve as the only cut in a reel; Keep titles tiny so the transition is the visible design
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: commercial film frames, saturated grading
Reject: Black frames during load; Dissolve frames obscure faces
Token commitments: palette #0B0B0B, #4A5772, #202D3F, #4D3648, #7E9376, #351C23; type DrukWide, TronicaMono; engine GSAP + Lenis linked (never vendored).
