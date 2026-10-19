---
title: "History of Graphic Design - timeline"
url: https://historyofgraphicdesign.com/
source_url: https://historyofgraphicdesign.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: editorial
category2: ""
family: horizontal-poster-timeline
dna: "Design history x a horizontal timeline of movements with a poster per era"
register: cinematic dark
grammar: chaptered editorial
lane: "A history site on black: a percent loader, posters fanning into 'GRAPHIC DESIGN HISTORY', a statement with bold words, then a horizontal timeline where each movement (Victorian 1837–1901, Art & Crafts, Art Nouveau, Art Deco, Constructivist, Heroic Realism) passes with its condensed title, dates and a tilted poster."
mode: read
traits: ["horizontal timeline", "condensed white titles", "one poster per era", "dates in serif", "black ground", "progress rule"]
palette: ["#0C0C0C", "#9A8777", "#313130", "#F2EFEB", "#C0BCAE", "#6D4844"]
type: ["Chapman Test Extended", "Bebas Neue", "Author"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

One poster per era on a horizontal rail is the simplest honest way to show a history, and the pace lets each poster be seen.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Florence Jeev, Moussa Mamadou).

## What to borrow (principle)

- One artefact per chapter on a horizontal rail with dates

## What to leave

- No vertical content after the rail

## Signature move

'ART NOUVEAU 1880–1910' with a tilted poster on a horizontal rail.

## Motion

Intro: counter 0 to 100 (~2 s), posters fan into the title. Wheel (Lenis): the statement highlights words; the page turns sideways; eras slide past with posters tilting in; the rule advances.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; WebGL canvas x1 (three.js); split text; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a history site on black: a percent loader, posters fanning into 'GRAPHIC DESIGN HISTORY', a statement with bold words, then a horizontal timeline where each movement (Victorian 1837–1901, Art & Crafts, Art Nouveau, Art Deco, Constructivist, Heroic Realism) passes with its condensed title, dates and a tilted poster. Type: Chapman Test Extended, Bebas Neue, Author.
Ground and ink from the measured palette (#0C0C0C, #9A8777, #313130). Motion carries the page through
'ART NOUVEAU 1880–1910' with a tilted poster on a horizontal rail. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — historical posters

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: historical posters

## Reference lock

Primary reference/direction: History of Graphic Design - timeline — A history site on black: a percent loader, posters fanning into 'GRAPHIC DESIGN HISTORY', a statement with bold words, then a horizontal timeline where each movement (Victorian 1837–1901, Art & Crafts, Art Nouveau, Art Deco, Constructivist, Heroic Realism) passes with its condensed title, dates and a tilted poster.
Preserve (3-5 traits): horizontal timeline; condensed white titles; one poster per era; dates in serif; black ground.
Borrow only (1-2): One artefact per chapter on a horizontal rail with dates
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: historical posters
Reject: No vertical content after the rail
Token commitments: palette #0C0C0C, #9A8777, #313130, #F2EFEB, #C0BCAE, #6D4844; type Chapman Test Extended, Bebas Neue, Author; engine GSAP + Lenis linked (never vendored).
