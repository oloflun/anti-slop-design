---
title: "Arijaya Putra"
url: https://arijayaputra.xyz/
source_url: https://arijayaputra.xyz/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: paper-sketchbook-dev-folio
dna: "Frontend engineer folio x handwritten paper sketchbook"
register: editorial print
grammar: live surface
lane: "A cream paper folio written in a handwritten brush/marker face with a red underline, a short manifesto in pencil script, and a paper index card asking for your name before the experience continues."
mode: operate
traits: ["cream paper texture", "handwritten brush title with red underline", "pencil-script manifesto", "paper index card with an input", "small circular icon buttons"]
palette: ["#D4CDBB", "#F1EBDB", "#C0B8A7"]
type: ["Caveat", "Kalam", "Permanent Marker"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The page is a sketchbook: everything is handwritten on paper, and the first interaction is filling in a card like a guestbook. It gives a developer site a personal, analogue voice.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Arijaya Putra).

## What to borrow (principle)

- A guestbook-style card as the first interaction
- Handwritten typography on paper texture for a personal tone

## What to leave

- Nothing scrolls until the card is filled
- Handwriting at small size is hard to read

## Signature move

A paper index card asking for your name before the folio opens.

## Motion

Intro: 'preparing…' with a drawn circle loader (~1.5 s). Then the paper page with title and card fade in; the card waits for input. Wheel does nothing (WebGL ground).

Measured (`motion/probe.json`): GSAP 3.15.0; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the live surface grammar: a cream paper folio written in a handwritten brush/marker face with a red underline, a short manifesto in pencil script, and a paper index card asking for your name before the experience continues. Type: Caveat, Kalam, Permanent Marker.
Ground and ink from the measured palette (#D4CDBB, #F1EBDB, #C0B8A7). Motion carries the page through
a paper index card asking for your name before the folio opens. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — paper textures, handwriting

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: paper textures, handwriting

## Reference lock

Primary reference/direction: Arijaya Putra — A cream paper folio written in a handwritten brush/marker face with a red underline, a short manifesto in pencil script, and a paper index card asking for your name before the experience continues.
Preserve (3-5 traits): cream paper texture; handwritten brush title with red underline; pencil-script manifesto; paper index card with an input; small circular icon buttons.
Borrow only (1-2): A guestbook-style card as the first interaction; Handwritten typography on paper texture for a personal tone
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: paper textures, handwriting
Reject: Nothing scrolls until the card is filled; Handwriting at small size is hard to read
Token commitments: palette #D4CDBB, #F1EBDB, #C0B8A7; type Caveat, Kalam, Permanent Marker; engine GSAP + Lenis linked (never vendored).
