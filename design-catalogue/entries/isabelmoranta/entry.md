---
title: "Isabel Moranta - Design and Art Director"
url: https://www.isabelmoranta.com/
source_url: https://www.isabelmoranta.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: serif-quote-dark-folio
dna: "Art director x a giant serif quote over a black page with a small project card"
register: cinematic dark
grammar: chaptered editorial
lane: "An art director's folio on black: a tiny loader and a small square that opens, 'ALL EXTREMES OF FEELING ARE ALLIED WITH MADNESS' in a huge high-contrast serif that scrolls up line by line with project thumbnails passing between the lines, then a small central video card of a project (grey, cinematic) with mono labels and corner nav."
mode: read
traits: ["huge high-contrast serif quote", "thumbnails passing between lines", "black ground", "small central video card", "mono labels", "page transitions"]
palette: ["#080808", "#5D5E5D"]
type: ["Ogg", "CentSchbook Mono BT"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

A single quote at enormous scale sets the tone; the small project card afterwards feels precious by contrast.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Set one quote at huge scale and pass thumbnails between its lines

## What to leave

- Long black empty frames at start

## Signature move

'ALL EXTREMES OF FEELING ARE ALLIED WITH MADNESS' in huge serif on black.

## Motion

Intro: black with a tiny square opening (~3 s). Wheel (Lenis, Flip, Barba): the quote scrolls line by line; thumbnails slide between lines; the page settles on a small video card that cycles.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; Barba page transitions; WebGL canvas x1; 11 video; smoothed scroll (median 135 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: an art director's folio on black: a tiny loader and a small square that opens, 'ALL EXTREMES OF FEELING ARE ALLIED WITH MADNESS' in a huge high-contrast serif that scrolls up line by line with project thumbnails passing between the lines, then a small central video card of a project (grey, cinematic) with mono labels and corner nav. Type: Ogg, CentSchbook Mono BT.
Ground and ink from the measured palette (#080808, #5D5E5D). Motion carries the page through
'ALL EXTREMES OF FEELING ARE ALLIED WITH MADNESS' in huge serif on black. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project video

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project video

## Reference lock

Primary reference/direction: Isabel Moranta - Design and Art Director — An art director's folio on black: a tiny loader and a small square that opens, 'ALL EXTREMES OF FEELING ARE ALLIED WITH MADNESS' in a huge high-contrast serif that scrolls up line by line with project thumbnails passing between the lines, then a small central video card of a project (grey, cinematic) with mono labels and corner nav.
Preserve (3-5 traits): huge high-contrast serif quote; thumbnails passing between lines; black ground; small central video card; mono labels.
Borrow only (1-2): Set one quote at huge scale and pass thumbnails between its lines
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project video
Reject: Long black empty frames at start
Token commitments: palette #080808, #5D5E5D; type Ogg, CentSchbook Mono BT; engine GSAP + Lenis linked (never vendored).
