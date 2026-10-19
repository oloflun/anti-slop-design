---
title: "Ironhill - A place the maps don't show"
url: https://ironhill.au/
source_url: https://ironhill.au/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "luxury-craft"
family: engraved-folklore-whisky-map
dna: "Australian whisky x engraved Bigfoot, a forest canopy and a wandering map path"
register: historical art
grammar: continuous world
lane: "A whisky brand built on a myth: a cream page with a serif counter and a little engraved Bigfoot walking across the corner, a dark forest canopy that dissolves into cream, then large serif statements ('There's a place not far from here the maps won't show') while a hand-drawn trail line winds down the page past scattered photo slides and engravings, ending at 'Warden of the Wild' with a glass of whisky on a stump."
mode: read
traits: ["walking engraved Bigfoot loader", "forest canopy dissolving to cream", "hand-drawn trail line through the page", "scattered 35 mm slide frames", "engraved illustrations", "thin serif uppercase statements"]
palette: ["#F4EDDD", "#37402B", "#686E5A", "#ADAD9B"]
type: ["GT America Trial", "GT America", "PP Woodland"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The trail line is the thread: it starts under the canopy and wanders past every statement and slide to the bottle, so the page feels like walking to a hidden place rather than reading sections.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Uncommon Studio).

## What to borrow (principle)

- A drawn path line that leads the eye down the whole page
- A tiny walking character as the loader

## What to leave

- Slow loader
- Very pale secondary text

## Signature move

An engraved Bigfoot walking beside a counter, then a drawn trail winding to a whisky glass.

## Motion

Intro: cream, a large serif counter rises from 000 while a small engraved Bigfoot walks along the corner (~4 s); a dark canopy then fills the top and dissolves in ink-like edges. Wheel (virtual, frame diff): statements fill word by word from pale to dark; the trail line draws itself between sections; slide frames and engravings drift in at angles; the bottle scene rises at the end.

Measured (`motion/probe.json`): GSAP 3.13.0; WebGL canvas x1 (three.js); 3 video. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A historical art page in the continuous world grammar: a whisky brand built on a myth: a cream page with a serif counter and a little engraved Bigfoot walking across the corner, a dark forest canopy that dissolves into cream, then large serif statements ('There's a place not far from here the maps won't show') while a hand-drawn trail line winds down the page past scattered photo slides and engravings, ending at 'Warden of the Wild' with a glass of whisky on a stump. Type: GT America Trial, GT America, PP Woodland.
Ground and ink from the measured palette (#F4EDDD, #37402B, #686E5A). Motion carries the page through
an engraved Bigfoot walking beside a counter, then a drawn trail winding to a whisky glass. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — vintage engravings, 35 mm slides, product still life

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: vintage engravings, 35 mm slides, product still life

## Reference lock

Primary reference/direction: Ironhill - A place the maps don't show — A whisky brand built on a myth: a cream page with a serif counter and a little engraved Bigfoot walking across the corner, a dark forest canopy that dissolves into cream, then large serif statements ('There's a place not far from here the maps won't show') while a hand-drawn trail line winds down the page past scattered photo slides and engravings, ending at 'Warden of the Wild' with a glass of whisky on a stump.
Preserve (3-5 traits): walking engraved Bigfoot loader; forest canopy dissolving to cream; hand-drawn trail line through the page; scattered 35 mm slide frames; engraved illustrations.
Borrow only (1-2): A drawn path line that leads the eye down the whole page; A tiny walking character as the loader
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: vintage engravings, 35 mm slides, product still life
Reject: Slow loader; Very pale secondary text
Token commitments: palette #F4EDDD, #37402B, #686E5A, #ADAD9B; type GT America Trial, GT America, PP Woodland; engine GSAP + Lenis linked (never vendored).
