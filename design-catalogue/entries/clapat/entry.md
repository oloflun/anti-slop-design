---
title: "Moz Agency - Clapat portfolio template"
url: https://www.clapat.com/templates/moz/
source_url: https://www.clapat.com/templates/moz/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: stacking-card-template-agency
dna: "Portfolio template x stacking project cards with a centred label and a counter loader"
register: modern clean
grammar: chaptered editorial
lane: "A theme demo: a black counter loader, then project cards (an orange portrait, a dark embossed book, a blue figure with spikes) stacked full width, each sliding up over the last with the title split around a small circular 'drag' cursor, a mission statement, 'Latest projects P.04' with a grid, and a capabilities list where the active item darkens."
mode: persuade
traits: ["counter loader", "full-width cards stacking", "title split around a cursor badge", "P.04 / S.08 numbering", "capabilities list highlight", "white ground"]
palette: ["#000000", "#F5F5F5", "#404E55", "#BD6217", "#20201F", "#593017"]
type: ["Inter", "Roboto Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

A well-made template: card stacking and the split title are executed cleanly but are the stock moves of the genre.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Clapat Studio).

## What to borrow (principle)

- Number sections like P.04 / S.08 for an editorial feel

## What to leave

- Generic template structure

## Signature move

Project cards stacking with the title split around a small circular cursor.

## Motion

Intro: black with a rolling counter (~2 s). Wheel (Lenis ~145 px glide, 4 pins, 82 triggers): cards rise and stack over each other; the title letters spread around the cursor; the statement fills; the grid slides; the capabilities list darkens the line at the centre.

Measured (`motion/probe.json`): GSAP 3.13.0; 82 ScrollTriggers; 4 pinned sections; Lenis; 2 video; smoothed scroll (median 146 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a theme demo: a black counter loader, then project cards (an orange portrait, a dark embossed book, a blue figure with spikes) stacked full width, each sliding up over the last with the title split around a small circular 'drag' cursor, a mission statement, 'Latest projects P.04' with a grid, and a capabilities list where the active item darkens. Type: Inter, Roboto Mono.
Ground and ink from the measured palette (#000000, #F5F5F5, #404E55). Motion carries the page through
project cards stacking with the title split around a small circular cursor. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — art-directed photography and renders

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: art-directed photography and renders

## Reference lock

Primary reference/direction: Moz Agency - Clapat portfolio template — A theme demo: a black counter loader, then project cards (an orange portrait, a dark embossed book, a blue figure with spikes) stacked full width, each sliding up over the last with the title split around a small circular 'drag' cursor, a mission statement, 'Latest projects P.04' with a grid, and a capabilities list where the active item darkens.
Preserve (3-5 traits): counter loader; full-width cards stacking; title split around a cursor badge; P.04 / S.08 numbering; capabilities list highlight.
Borrow only (1-2): Number sections like P.04 / S.08 for an editorial feel
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: art-directed photography and renders
Reject: Generic template structure
Token commitments: palette #000000, #F5F5F5, #404E55, #BD6217, #20201F, #593017; type Inter, Roboto Mono; engine GSAP + Lenis linked (never vendored).
