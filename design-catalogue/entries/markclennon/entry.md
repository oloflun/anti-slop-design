---
title: "Mark Clennon - photographer"
url: https://www.markclennon.com/
source_url: https://www.markclennon.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: photographer-column-wall
dna: "Photographer x four columns of portraits scrolling at different speeds"
register: warm photographic
grammar: gallery/catalog
lane: "A photographer's home: four columns of portraits and campaign images (Time 100 cover, Nike 'Just Do It', athletes, musicians) scrolling at different speeds in a loop, with a small serif name and nav."
mode: read
traits: ["four columns at different speeds", "infinite loop", "rich colour photography", "small serif name", "no other content"]
palette: ["#2D2723", "#A2A196", "#4A514E", "#0A0909", "#BEBDB0", "#937669"]
type: ["Boogy Brut Poster Web White"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The columns at different speeds show a lot of work with depth; the photos carry it.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Columns of work at different speeds as the home

## What to leave

- No hierarchy

## Signature move

Four columns of portraits drifting at different speeds.

## Motion

Intro: black (~1 s), columns fill. Wheel (Lenis): columns move at different speeds and wrap.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; Barba page transitions; WebGL canvas x1 (three.js); 12 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the gallery/catalog grammar: a photographer's home: four columns of portraits and campaign images (Time 100 cover, Nike 'Just Do It', athletes, musicians) scrolling at different speeds in a loop, with a small serif name and nav. Type: Boogy Brut Poster Web White.
Ground and ink from the measured palette (#2D2723, #A2A196, #4A514E). Motion carries the page through
four columns of portraits drifting at different speeds. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — portrait and campaign photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: portrait and campaign photography

## Reference lock

Primary reference/direction: Mark Clennon - photographer — A photographer's home: four columns of portraits and campaign images (Time 100 cover, Nike 'Just Do It', athletes, musicians) scrolling at different speeds in a loop, with a small serif name and nav.
Preserve (3-5 traits): four columns at different speeds; infinite loop; rich colour photography; small serif name; no other content.
Borrow only (1-2): Columns of work at different speeds as the home
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: portrait and campaign photography
Reject: No hierarchy
Token commitments: palette #2D2723, #A2A196, #4A514E, #0A0909, #BEBDB0, #937669; type Boogy Brut Poster Web White; engine GSAP + Lenis linked (never vendored).
