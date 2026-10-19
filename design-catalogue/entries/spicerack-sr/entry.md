---
title: "SHISAKU - Spicerack experiments"
url: https://www.spicerack-sr.com/shisaku/
source_url: https://www.spicerack-sr.com/shisaku/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: motion-experiments-dark
dna: "Japanese studio's motion lab x dark demos of scroll techniques"
register: cinematic dark
grammar: chaptered editorial
lane: "A motion experiments page on black: concentric rings and a red dot around 'SHISAKU / 試作', then each experiment as a chapter with a serif title ('Visual layering with fixed card offsets', 'Motion text', 'Card snap and scroll-linked loop animation') demonstrated live: product renders stacking, kinetic text rows, cards snapping and looping around a centre."
mode: read
traits: ["experiment chapters", "serif titles with Japanese captions", "live demos", "concentric ring intro", "product render cards", "kinetic text rows"]
palette: ["#000000", "#34312F", "#1A1817", "#84786F"]
type: ["Noto Sans JP", "Roboto", "Libre Baskerville", "Noto Serif"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

A catalogue of scroll techniques shown on themselves; useful as a reference of named patterns.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Name and demonstrate each motion pattern as a chapter

## What to leave

- Demos without a story

## Signature move

Product renders stacking under 'Visual layering with fixed card offsets'.

## Motion

Intro: black with a thin loader, rings and the red dot (~2 s). Wheel (14 triggers): each chapter title types in; cards stack with offsets; text rows slide in alternating directions; cards snap and loop around the centre.

Measured (`motion/probe.json`): GSAP 3.12.7; 14 ScrollTriggers; 8 video. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a motion experiments page on black: concentric rings and a red dot around 'SHISAKU / 試作', then each experiment as a chapter with a serif title ('Visual layering with fixed card offsets', 'Motion text', 'Card snap and scroll-linked loop animation') demonstrated live: product renders stacking, kinetic text rows, cards snapping and looping around a centre. Type: Noto Sans JP, Roboto, Libre Baskerville, Noto Serif.
Ground and ink from the measured palette (#000000, #34312F, #1A1817). Motion carries the page through
product renders stacking under 'Visual layering with fixed card offsets'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D product renders

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D product renders

## Reference lock

Primary reference/direction: SHISAKU - Spicerack experiments — A motion experiments page on black: concentric rings and a red dot around 'SHISAKU / 試作', then each experiment as a chapter with a serif title ('Visual layering with fixed card offsets', 'Motion text', 'Card snap and scroll-linked loop animation') demonstrated live: product renders stacking, kinetic text rows, cards snapping and looping around a centre.
Preserve (3-5 traits): experiment chapters; serif titles with Japanese captions; live demos; concentric ring intro; product render cards.
Borrow only (1-2): Name and demonstrate each motion pattern as a chapter
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D product renders
Reject: Demos without a story
Token commitments: palette #000000, #34312F, #1A1817, #84786F; type Noto Sans JP, Roboto, Libre Baskerville, Noto Serif; engine GSAP + Lenis linked (never vendored).
