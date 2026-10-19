---
title: "EASYSELLER"
url: https://easyseller.it/
source_url: https://easyseller.it/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: ""
family: glitch-flower-sales-agency
dna: "Italian e-commerce agency x glitching flower bud"
register: modern clean
grammar: chaptered editorial
lane: "A sales agency page where a dark teal flower bud behind 'Elevate Your Sales' slices into vertical glitch strips as you scroll until it collapses into a single stem line, then numbers and values follow in blue serif and caps."
mode: persuade
traits: ["dark flower bud photo as hero object", "vertical slit-scan glitch that collapses the image", "condensed serif statement", "blue numeric counters", "inline glitch-chip images inside caps lines", "16 pinned sections"]
palette: ["#FEFEFE", "#02040E", "#285153", "#10262B", "#559291", "#DAE0E1"]
type: ["icomoon", "Font1", "Font2"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

One photograph does the hero's work: the flower is sliced into vertical strips that stretch and narrow with scroll until only the stem remains, a striking way to 'scroll through' an image. The rest is plain, with small glitch chips inside the caps statements tying back to it.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: EGO55 Studio).

## What to borrow (principle)

- Slit-scan an image into vertical strips that collapse with scroll
- Reuse tiny strips of the hero image as inline chips inside later text

## What to leave

- Generic stock lifestyle photos lower down
- Many pins for a short page

## Signature move

A flower bud sliced into vertical strips that collapse to a single stem as you scroll.

## Motion

Intro: blue panel splits, white page with the flower and 'Elevate Your Sales' (~1 s). Scroll (Barba, 65 ScrollTriggers, 16 pins, WebGL): the flower is cut into vertical strips that stretch, darken and narrow until only the stem line remains under the fixed headline; intro paragraph; 20+ / 13+ / 1M+ counters in blue; caps values with inline glitch chips; photo cards appear one by one.

Measured (`motion/probe.json`): GSAP 3.11.5; 65 ScrollTriggers; 16 pinned sections; Barba page transitions; WebGL canvas x2 (three.js); 4 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a sales agency page where a dark teal flower bud behind 'Elevate Your Sales' slices into vertical glitch strips as you scroll until it collapses into a single stem line, then numbers and values follow in blue serif and caps. Type: icomoon, Font1, Font2.
Ground and ink from the measured palette (#FEFEFE, #02040E, #285153). Motion carries the page through
a flower bud sliced into vertical strips that collapse to a single stem as you scroll. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — one dramatic botanical photo on white; lifestyle product shots

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: one dramatic botanical photo on white; lifestyle product shots

## Reference lock

Primary reference/direction: EASYSELLER — A sales agency page where a dark teal flower bud behind 'Elevate Your Sales' slices into vertical glitch strips as you scroll until it collapses into a single stem line, then numbers and values follow in blue serif and caps.
Preserve (3-5 traits): dark flower bud photo as hero object; vertical slit-scan glitch that collapses the image; condensed serif statement; blue numeric counters; inline glitch-chip images inside caps lines.
Borrow only (1-2): Slit-scan an image into vertical strips that collapse with scroll; Reuse tiny strips of the hero image as inline chips inside later text
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: one dramatic botanical photo on white; lifestyle product shots
Reject: Generic stock lifestyle photos lower down; Many pins for a short page
Token commitments: palette #FEFEFE, #02040E, #285153, #10262B, #559291, #DAE0E1; type icomoon, Font1, Font2; engine GSAP + Lenis linked (never vendored).
