---
title: "Oto Nove Fest by Studio Khi"
url: https://otonove.studiokhi.com/
source_url: https://otonove.studiokhi.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "playful"
family: festival-gradient-bars
dna: "Music festival x coral gradient bars like an equaliser"
register: other
grammar: live surface
lane: "A festival landing: white, then coral gradient vertical bars rise like an equaliser and settle into a striped field, with 'OTO NOVE FEST' in condensed white type at the bottom and vertical day labels."
mode: experience
traits: ["coral gradient vertical bars", "bars rising like an equaliser", "condensed white title", "vertical day labels", "single screen", "stacked logo icon"]
palette: ["#E16353", "#EF806C", "#FDFCFC", "#F3C1B6"]
type: ["Inter", "Galgo"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The equaliser bars make the music festival's subject the visual in one move.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Turn the subject's own visual (an equaliser) into the hero field

## What to leave

- Nothing beyond the hero captured

## Signature move

Coral gradient bars rising like an equaliser behind 'OTO NOVE FEST'.

## Motion

Intro: white, bars rise from the bottom at different heights and fill the screen (~2 s), the title slides up. Scroll: no change captured.

Measured (`motion/probe.json`): GSAP 3.12.7; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: PLAY SOUND. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the live surface grammar: a festival landing: white, then coral gradient vertical bars rise like an equaliser and settle into a striped field, with 'OTO NOVE FEST' in condensed white type at the bottom and vertical day labels. Type: Inter, Galgo.
Ground and ink from the measured palette (#E16353, #EF806C, #FDFCFC). Motion carries the page through
coral gradient bars rising like an equaliser behind 'OTO NOVE FEST'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — gradient graphics

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: gradient graphics

## Reference lock

Primary reference/direction: Oto Nove Fest by Studio Khi — A festival landing: white, then coral gradient vertical bars rise like an equaliser and settle into a striped field, with 'OTO NOVE FEST' in condensed white type at the bottom and vertical day labels.
Preserve (3-5 traits): coral gradient vertical bars; bars rising like an equaliser; condensed white title; vertical day labels; single screen.
Borrow only (1-2): Turn the subject's own visual (an equaliser) into the hero field
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: gradient graphics
Reject: Nothing beyond the hero captured
Token commitments: palette #E16353, #EF806C, #FDFCFC, #F3C1B6; type Inter, Galgo; engine GSAP + Lenis linked (never vendored).
