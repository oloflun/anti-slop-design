---
title: "Berserk - Into the Heart of Darkness"
url: https://berserk-heart-of-darkness.vercel.app/
source_url: https://berserk-heart-of-darkness.vercel.app/
captured: 2026-10-02
origin: raw-url
extract: none
category: editorial
category2: ""
family: manga-tribute-horizontal-chapters
dna: "Berserk fan tribute x engraved manga art and a horizontal chapter book"
register: editorial print
grammar: chaptered editorial
lane: "A tribute to the manga: 'Into the depths...' on black, 'Into the Heart of Darkness' in serif over a dense engraved Guts illustration, a cream preface page that slides in from the right, 'A descent into the abyss' as a horizontal row of chapter cards with colour swatches (Guts curse, Dark fantasies, God Hand, Eclipse, Epilogue), then manga panels and chapter text ('I. The Curse of Guts') laid out like a book spread."
mode: read
traits: ["engraved manga art", "serif display", "cream book pages", "horizontal chapter card row", "colour swatch per chapter", "manga panels as spreads"]
palette: ["#EDE7C9", "#2A2A2A", "#0C0C0C", "#D0CBB1", "#827F72"]
type: ["serif", "sansSerif"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

It treats the story as a book: cream pages slide over the dark art and chapters read like spreads, giving a fan site real editorial structure.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Slide cream book pages over dark art
- Give each chapter a colour swatch card

## What to leave

- Dense small body text

## Signature move

A cream preface page sliding over an engraved dark illustration.

## Motion

Intro: black with 'Into the depths...' (~2 s). Wheel (horizontal): the hero art scales; the cream page slides in from the right; the headline scrolls sideways; chapter cards pass; manga panels slide into a dark spread with the chapter title.

Measured (`motion/probe.json`): GSAP 3.14.1; 5 pinned sections; Lenis; WebGL canvas x1 (three.js); split text; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: BEGIN THE DESCENT→. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a tribute to the manga: 'Into the depths...' on black, 'Into the Heart of Darkness' in serif over a dense engraved Guts illustration, a cream preface page that slides in from the right, 'A descent into the abyss' as a horizontal row of chapter cards with colour swatches (Guts curse, Dark fantasies, God Hand, Eclipse, Epilogue), then manga panels and chapter text ('I. The Curse of Guts') laid out like a book spread. Type: serif, sansSerif.
Ground and ink from the measured palette (#EDE7C9, #2A2A2A, #0C0C0C). Motion carries the page through
a cream preface page sliding over an engraved dark illustration. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — manga illustration

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: manga illustration

## Reference lock

Primary reference/direction: Berserk - Into the Heart of Darkness — A tribute to the manga: 'Into the depths...' on black, 'Into the Heart of Darkness' in serif over a dense engraved Guts illustration, a cream preface page that slides in from the right, 'A descent into the abyss' as a horizontal row of chapter cards with colour swatches (Guts curse, Dark fantasies, God Hand, Eclipse, Epilogue), then manga panels and chapter text ('I. The Curse of Guts') laid out like a book spread.
Preserve (3-5 traits): engraved manga art; serif display; cream book pages; horizontal chapter card row; colour swatch per chapter.
Borrow only (1-2): Slide cream book pages over dark art; Give each chapter a colour swatch card
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: manga illustration
Reject: Dense small body text
Token commitments: palette #EDE7C9, #2A2A2A, #0C0C0C, #D0CBB1, #827F72; type serif, sansSerif; engine GSAP + Lenis linked (never vendored).
