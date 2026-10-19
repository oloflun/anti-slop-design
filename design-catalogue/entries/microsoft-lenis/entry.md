---
title: "Microsoft Design"
url: https://microsoft.design/
source_url: https://microsoft.design/
captured: 2026-10-03
origin: raw-url
extract: none
category: editorial
category2: "institutional"
family: serif-ux-journal-cards
dna: "Design journal x white page, a light serif headline with collectible sticker objects around it, then an article card grid"
register: editorial print
grammar: gallery/catalog
lane: "A design team's journal: 'A global UX community bringing you behind the design & research.' in a light serif, small objects (a clock, an ampersand tile, a doodle, a box) popping in around it one by one, a filter row, a grid of article cards with bold editorial images, a full-bleed soft-shadow video ('Our design brief was simple'), feature series and more cards."
mode: read
traits: ["light serif headline", "objects popping around the headline", "editorial card grid", "soft-shadow video interlude"]
palette: ["#FAFAFA", "#745458", "#BEC0BF"]
type: ["Segoe Sans", "Segoe Serif"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Small objects appearing around a calm serif headline set a curious, human tone for a big company's design blog.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Microsoft).

## What to borrow (principle)

- Let a few small objects appear around a calm headline

## What to leave

- Long uniform card grid

## Signature move

An orange ampersand tile and a clock popping in around a light serif headline.

## Motion

Intro: logo on black (~1 s). Wheel (Lenis): objects pop in with spring; cards rise in rows; the video section pins briefly.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; 10 video; smoothed scroll (median 126 px still travelling after input stops); entry gate: Reject. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the gallery/catalog grammar: a design team's journal: 'A global UX community bringing you behind the design & research.' in a light serif, small objects (a clock, an ampersand tile, a doodle, a box) popping in around it one by one, a filter row, a grid of article cards with bold editorial images, a full-bleed soft-shadow video ('Our design brief was simple'), feature series and more cards. Type: Segoe Sans, Segoe Serif.
Ground and ink from the measured palette (#FAFAFA, #745458, #BEC0BF). Motion carries the page through
an orange ampersand tile and a clock popping in around a light serif headline. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — editorial illustration and photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: editorial illustration and photography

## Reference lock

Primary reference/direction: Microsoft Design — A design team's journal: 'A global UX community bringing you behind the design & research.' in a light serif, small objects (a clock, an ampersand tile, a doodle, a box) popping in around it one by one, a filter row, a grid of article cards with bold editorial images, a full-bleed soft-shadow video ('Our design brief was simple'), feature series and more cards.
Preserve (3-5 traits): light serif headline; objects popping around the headline; editorial card grid; soft-shadow video interlude.
Borrow only (1-2): Let a few small objects appear around a calm headline
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: editorial illustration and photography
Reject: Long uniform card grid
Token commitments: palette #FAFAFA, #745458, #BEC0BF; type Segoe Sans, Segoe Serif; engine GSAP + Lenis linked (never vendored).
