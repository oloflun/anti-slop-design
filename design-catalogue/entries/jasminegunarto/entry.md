---
title: "Jasmine Gunarto"
url: http://jasminegunarto.com/
source_url: http://jasminegunarto.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: condensed-name-motion-designer
dna: "Motion designer folio x condensed caps and video window"
register: editorial print
grammar: chaptered editorial
lane: "A motion designer folio that counts 000 → 070, sets her name huge in condensed caps with 'A MOTION / DESIGNER' sliding together underneath, a reel window that widens to full bleed, a brown statement 'CREATING MOTION WITH MEANING', and featured works in tabs."
mode: persuade
traits: ["counter loader", "huge condensed caps name", "words that slide together (A MOTION / DESIGNER)", "reel window that grows to full bleed", "brown chapter", "tabbed featured works"]
palette: ["#ECEAE6", "#0A0A0A", "#698578", "#AFC0B9", "#D6D5D3"]
type: ["mg", "Manrope"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The two words of her role start far apart and slide together as you scroll while the reel window beneath them widens, a simple choreography where type and video move as one.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Slide two words together as a video window widens below them
- A single warm brown chapter for the statement between light sections

## What to leave

- Captured in virtual mode; some sections blurred
- Generic 'see all work' close

## Signature move

'A MOTION' and 'DESIGNER' sliding together as the reel window widens.

## Motion

Intro: black, counter 000 → 070 (~2 s). Scroll (Taxi, 1 pin, SplitText): name huge; 'A MOTION … DESIGNER' slide together; a reel window grows from a strip to full bleed showing 3D motion; brown 'CREATING MOTION WITH MEANING' reveals line by line; 'FEATURED WORKS' with tabs and project cards (Diamondbacks, community poster); 'BREAK' black close.

Measured (`motion/probe.json`): GSAP 3.13.0; 1 pinned sections; Taxi page transitions; 5 video; split text; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a motion designer folio that counts 000 → 070, sets her name huge in condensed caps with 'A MOTION / DESIGNER' sliding together underneath, a reel window that widens to full bleed, a brown statement 'CREATING MOTION WITH MEANING', and featured works in tabs. Type: mg, Manrope.
Ground and ink from the measured palette (#ECEAE6, #0A0A0A, #698578). Motion carries the page through
'A MOTION' and 'DESIGNER' sliding together as the reel window widens. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D motion stills, campaign graphics

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D motion stills, campaign graphics

## Reference lock

Primary reference/direction: Jasmine Gunarto — A motion designer folio that counts 000 → 070, sets her name huge in condensed caps with 'A MOTION / DESIGNER' sliding together underneath, a reel window that widens to full bleed, a brown statement 'CREATING MOTION WITH MEANING', and featured works in tabs.
Preserve (3-5 traits): counter loader; huge condensed caps name; words that slide together (A MOTION / DESIGNER); reel window that grows to full bleed; brown chapter.
Borrow only (1-2): Slide two words together as a video window widens below them; A single warm brown chapter for the statement between light sections
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D motion stills, campaign graphics
Reject: Captured in virtual mode; some sections blurred; Generic 'see all work' close
Token commitments: palette #ECEAE6, #0A0A0A, #698578, #AFC0B9, #D6D5D3; type mg, Manrope; engine GSAP + Lenis linked (never vendored).
