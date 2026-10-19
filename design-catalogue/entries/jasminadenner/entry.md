---
title: "Jasmina Denner - longevity intelligence"
url: https://jasminadenner.com/
source_url: https://jasminadenner.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: institutional
category2: "editorial"
family: bust-thread-longevity
dna: "Longevity thinker x a glowing marble bust and a thread that carries cards"
register: cinematic dark
grammar: continuous world
lane: "A personal brand on deep violet: a marble bust with light flowing over it between 'JASMINA' and 'DENNER' in serif caps, an italic line 'Where health, technology, and human capability converge', a spotlight on 'EXPLORE JASMINA'S WORK', then a thin glowing thread that runs across the screen carrying floating cards one at a time (a gold brain tree for Longevity Intelligence, a book, a Lab card, a bust in a ring for J. Ventures), each with a serif title and a button."
mode: read
traits: ["glowing marble bust", "serif caps split around the bust", "thin glowing thread line", "cards carried along the thread", "deep violet ground", "spotlight cone"]
palette: ["#0A0622", "#201940", "#675D79"]
type: ["Work Sans", "Taviraj"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The thread literally connects her ventures, so the scroll reads as one line of thought from idea to book to lab to fund.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Carry each offer along one glowing thread across the screen

## What to leave

- Small body text

## Signature move

A thin glowing thread carrying a gold brain-tree card across violet.

## Motion

Intro: violet (~1 s), the bust fades in with light flowing over it and the name splits. Wheel (Lenis): the bust sinks; the italic line fades; a spotlight opens on the title; the thread draws; each card slides in along the thread, tilts flat, and leaves to the top right as the next arrives.

Measured (`motion/probe.json`): GSAP 3.12.2; WebGL canvas x1; split text; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Explore. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the continuous world grammar: a personal brand on deep violet: a marble bust with light flowing over it between 'JASMINA' and 'DENNER' in serif caps, an italic line 'Where health, technology, and human capability converge', a spotlight on 'EXPLORE JASMINA'S WORK', then a thin glowing thread that runs across the screen carrying floating cards one at a time (a gold brain tree for Longevity Intelligence, a book, a Lab card, a bust in a ring for J. Ventures), each with a serif title and a button. Type: Work Sans, Taviraj.
Ground and ink from the measured palette (#0A0622, #201940, #675D79). Motion carries the page through
a thin glowing thread carrying a gold brain-tree card across violet. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D bust and objects

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D bust and objects

## Reference lock

Primary reference/direction: Jasmina Denner - longevity intelligence — A personal brand on deep violet: a marble bust with light flowing over it between 'JASMINA' and 'DENNER' in serif caps, an italic line 'Where health, technology, and human capability converge', a spotlight on 'EXPLORE JASMINA'S WORK', then a thin glowing thread that runs across the screen carrying floating cards one at a time (a gold brain tree for Longevity Intelligence, a book, a Lab card, a bust in a ring for J. Ventures), each with a serif title and a button.
Preserve (3-5 traits): glowing marble bust; serif caps split around the bust; thin glowing thread line; cards carried along the thread; deep violet ground.
Borrow only (1-2): Carry each offer along one glowing thread across the screen
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D bust and objects
Reject: Small body text
Token commitments: palette #0A0622, #201940, #675D79; type Work Sans, Taviraj; engine GSAP + Lenis linked (never vendored).
