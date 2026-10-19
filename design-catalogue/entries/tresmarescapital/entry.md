---
title: "Tresmares Capital - private credit for SMEs"
url: https://www.tresmarescapital.com/
source_url: https://www.tresmarescapital.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: institutional
category2: "editorial"
family: white-fund-red-paper-cutouts
dna: "Pan-European fund x white page, grey snowy peak, red paper rectangles and a dried plant cut through each strategy name"
register: modern clean
grammar: chaptered editorial
lane: "A private-credit fund in Spanish: 'Impulso para crecer' in grey grotesk with a misty mountain fading up behind, a centred mission line, founding facts as red serif numerals in a ruled grid (2014, +3.500, +100, +2.000, +60), then the four strategies as one pinned grey stage where a dried flower stem and red paper blocks rearrange around each giant ghost name (Private Equity, Direct Lending, Fund of Funds, Fund Financing), a partnership line with city photos fanned in an arc, a map with red dots for the offices, the team in black and white, and offices as a row of interiors."
mode: persuade
traits: ["serif red numerals in a ruled grid", "dried plant and red paper collage per strategy", "ghost strategy names", "photos fanned in an arc", "map with red office dots", "black and white team row"]
palette: ["#FFFFFF", "#D5D5D5", "#682725", "#B0A7A7"]
type: ["PP Fragment Serif", "PP Neue Montreal"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

A still life rebuilt for each strategy gives four abstract financial products four distinct images without any stock photography of handshakes.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Dgrees).

## What to borrow (principle)

- Recompose one still life per product instead of using a stock photo per product

## What to leave

- Cookie bar across every frame
- Tiny body copy

## Signature move

A dried flower stem threaded through red paper rectangles over the words Direct Lending.

## Motion

Intro: mountain fades in (~1 s). Wheel (Lenis, taxi transitions): numerals count in a grid; the strategy stage holds while red blocks and the stem swap with clip and rotation per name; city photos fan out on an arc; map dots pulse; team portraits slide.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; Taxi page transitions; WebGL canvas x1 (three.js); split text; smoothed scroll (median 104 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a private-credit fund in Spanish: 'Impulso para crecer' in grey grotesk with a misty mountain fading up behind, a centred mission line, founding facts as red serif numerals in a ruled grid (2014, +3.500, +100, +2.000, +60), then the four strategies as one pinned grey stage where a dried flower stem and red paper blocks rearrange around each giant ghost name (Private Equity, Direct Lending, Fund of Funds, Fund Financing), a partnership line with city photos fanned in an arc, a map with red dots for the offices, the team in black and white, and offices as a row of interiors. Type: PP Fragment Serif, PP Neue Montreal.
Ground and ink from the measured palette (#FFFFFF, #D5D5D5, #682725). Motion carries the page through
a dried flower stem threaded through red paper rectangles over the words Direct Lending. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — still-life collage, black and white portraits, city photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: still-life collage, black and white portraits, city photography

## Reference lock

Primary reference/direction: Tresmares Capital - private credit for SMEs — A private-credit fund in Spanish: 'Impulso para crecer' in grey grotesk with a misty mountain fading up behind, a centred mission line, founding facts as red serif numerals in a ruled grid (2014, +3.500, +100, +2.000, +60), then the four strategies as one pinned grey stage where a dried flower stem and red paper blocks rearrange around each giant ghost name (Private Equity, Direct Lending, Fund of Funds, Fund Financing), a partnership line with city photos fanned in an arc, a map with red dots for the offices, the team in black and white, and offices as a row of interiors.
Preserve (3-5 traits): serif red numerals in a ruled grid; dried plant and red paper collage per strategy; ghost strategy names; photos fanned in an arc; map with red office dots.
Borrow only (1-2): Recompose one still life per product instead of using a stock photo per product
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: still-life collage, black and white portraits, city photography
Reject: Cookie bar across every frame; Tiny body copy
Token commitments: palette #FFFFFF, #D5D5D5, #682725, #B0A7A7; type PP Fragment Serif, PP Neue Montreal; engine GSAP + Lenis linked (never vendored).
