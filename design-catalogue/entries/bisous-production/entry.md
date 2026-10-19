---
title: "Bisous"
url: https://bisous-production.com/
source_url: https://bisous-production.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "luxury-craft"
family: cgi-luxury-product-reel
dna: "CGI production studio x luxury beauty product films"
register: cinematic dark
grammar: rhythmic cutlist
lane: "A CGI studio whose index is a thin vertical strip of thumbnails on white; scrolling expands each into full-bleed CGI product films (a cream swirl, a petal splash, a compact case, gold liquid) that slide over each other with the client name in a corner."
mode: experience
traits: ["vertical thumbnail strip on white", "full-bleed CGI product films", "films sliding over each other", "tiny corner captions", "Taxi transitions"]
palette: ["#FFFFFF", "#000000", "#91753D", "#C2B17F", "#634C28", "#AA935D"]
type: ["Antarctica", "Basier Square Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The work (photoreal CGI for cosmetics) is so rich that the page only provides a strip to enter and then gets out of the way: each film takes the full frame and the next one slides over it.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Beaucoup Studio).

## What to borrow (principle)

- Start from a thin strip of thumbnails that expands into full-bleed films
- Stack films so each slides over the last

## What to leave

- White blank frames before the strip appears
- Cookie notice on every frame

## Signature move

A thin strip of thumbnails that opens into full-bleed CGI product films.

## Motion

Intro: white for ~2.5 s, then a narrow vertical strip of thumbnails with '100 • 100'. Wheel (virtual, Lenis, Taxi): the strip slides and the active thumbnail grows to full bleed; films (cream swirl, Dolce bottle, Estée Lauder compact, gold liquid, flower) slide over each other with client captions.

Measured (`motion/probe.json`): GSAP 3.12.2; Lenis; Taxi page transitions; WebGL canvas x1 (three.js); 14 video; split text; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the rhythmic cutlist grammar: a CGI studio whose index is a thin vertical strip of thumbnails on white; scrolling expands each into full-bleed CGI product films (a cream swirl, a petal splash, a compact case, gold liquid) that slide over each other with the client name in a corner. Type: Antarctica, Basier Square Mono.
Ground and ink from the measured palette (#FFFFFF, #000000, #91753D). Motion carries the page through
a thin strip of thumbnails that opens into full-bleed CGI product films. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — photoreal CGI of cosmetics, liquids and flowers

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: photoreal CGI of cosmetics, liquids and flowers

## Reference lock

Primary reference/direction: Bisous — A CGI studio whose index is a thin vertical strip of thumbnails on white; scrolling expands each into full-bleed CGI product films (a cream swirl, a petal splash, a compact case, gold liquid) that slide over each other with the client name in a corner.
Preserve (3-5 traits): vertical thumbnail strip on white; full-bleed CGI product films; films sliding over each other; tiny corner captions; Taxi transitions.
Borrow only (1-2): Start from a thin strip of thumbnails that expands into full-bleed films; Stack films so each slides over the last
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: photoreal CGI of cosmetics, liquids and flowers
Reject: White blank frames before the strip appears; Cookie notice on every frame
Token commitments: palette #FFFFFF, #000000, #91753D, #C2B17F, #634C28, #AA935D; type Antarctica, Basier Square Mono; engine GSAP + Lenis linked (never vendored).
