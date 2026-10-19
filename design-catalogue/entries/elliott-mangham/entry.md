---
title: "Elliott Mangham - Creative Web Developer"
url: https://elliott.mangham.dev/
source_url: https://elliott.mangham.dev/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: dense-spec-header-dev-folio
dna: "WordPress developer x dense mono spec header and a project thumbnail rail"
register: cinematic dark
grammar: split stage
lane: "A developer folio on black: a percent loader across five columns, a dense mono header of facts (position, recognition, brands, connect), a short bio that rewrites itself line by line as you scroll, and a monochrome project thumbnail rail running along the bottom."
mode: read
traits: ["dense mono spec header", "bio that rewrites on scroll", "monochrome thumbnail rail", "five-column loader", "small type everywhere", "single screen layout"]
palette: ["#111111", "#323132", "#4C4C4C", "#626262", "#DEDEDE", "#919191"]
type: ["Neue Montreal", "Roobert Mono", "Antartica", "NeueMontreal"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Everything stays on one screen: the header, the changing bio and the rail; scroll changes the sentence rather than the page.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Scroll rewrites the bio in place instead of moving the page

## What to leave

- Tiny unreadable text
- Thumbnails too small to judge

## Signature move

A bio that rewrites itself line by line above a monochrome project rail.

## Motion

Intro: black, five column percentages count up (~1.5 s), the header types in. Wheel (Lenis, 1 pin): the bio lines split and reassemble into new sentences; the thumbnail rail slides sideways.

Measured (`motion/probe.json`): GSAP 3.13.0; 1 pinned sections; Lenis; split text; smoothed scroll (median 129 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the split stage grammar: a developer folio on black: a percent loader across five columns, a dense mono header of facts (position, recognition, brands, connect), a short bio that rewrites itself line by line as you scroll, and a monochrome project thumbnail rail running along the bottom. Type: Neue Montreal, Roobert Mono, Antartica, NeueMontreal.
Ground and ink from the measured palette (#111111, #323132, #4C4C4C). Motion carries the page through
a bio that rewrites itself line by line above a monochrome project rail. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — monochrome project thumbnails

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: monochrome project thumbnails

## Reference lock

Primary reference/direction: Elliott Mangham - Creative Web Developer — A developer folio on black: a percent loader across five columns, a dense mono header of facts (position, recognition, brands, connect), a short bio that rewrites itself line by line as you scroll, and a monochrome project thumbnail rail running along the bottom.
Preserve (3-5 traits): dense mono spec header; bio that rewrites on scroll; monochrome thumbnail rail; five-column loader; small type everywhere.
Borrow only (1-2): Scroll rewrites the bio in place instead of moving the page
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: monochrome project thumbnails
Reject: Tiny unreadable text; Thumbnails too small to judge
Token commitments: palette #111111, #323132, #4C4C4C, #626262, #DEDEDE, #919191; type Neue Montreal, Roobert Mono, Antartica, NeueMontreal; engine GSAP + Lenis linked (never vendored).
