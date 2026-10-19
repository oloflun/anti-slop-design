---
title: "i-D - Margaret Qualley interview"
url: https://spotlight.i-d.co/margaretqualley
source_url: https://spotlight.i-d.co/margaretqualley
captured: 2026-10-03
origin: raw-url
extract: none
category: editorial
category2: ""
family: magazine-cover-story-colour-shifts
dna: "Magazine cover story x colour grounds that change per chapter and phones playing clips"
register: editorial print
grammar: chaptered editorial
lane: "A magazine feature: 'LIGHTS!!! CAMERA!!! MARGARET!!!' in heavy condensed caps over cover photos, the interview in mono caps body text on grounds that change colour per chapter (black, light blue, yellow, pink), framed photos with coloured borders, tilted phones playing behind-the-scenes clips, pull quotes in serif, and 'REMEMBER, IT'S NOT A MARATHON' to close."
mode: read
traits: ["heavy condensed caps headline", "ground colour per chapter", "mono caps body", "tilted phones with clips", "coloured photo borders", "serif pull quotes"]
palette: ["#000000", "#BCEBFF", "#825E3D", "#A19B81", "#411F10", "#CAD5D6"]
type: ["Telidon Bold", "ABC Gravity Variable", "A-OTF Midashi Min MA31 Pro MA31", "Telidon Italic"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Switching the ground colour per chapter paces a long interview like magazine spreads.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: 27b).

## What to borrow (principle)

- Change the ground colour at each chapter of a long read
- Tilted phones playing behind-the-scenes clips

## What to leave

- All-caps mono body is tiring

## Signature move

Tilted phones playing clips on a yellow ground beside an interview.

## Motion

Intro: the cover headline. Wheel: text scrolls; photos slide in with borders; the ground switches colour at chapters; phones tilt in and play; pull quotes type; the closing headline rises.

Measured (`motion/probe.json`): Lenis; 5 video; smoothed scroll (median 95 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a magazine feature: 'LIGHTS!!! CAMERA!!! MARGARET!!!' in heavy condensed caps over cover photos, the interview in mono caps body text on grounds that change colour per chapter (black, light blue, yellow, pink), framed photos with coloured borders, tilted phones playing behind-the-scenes clips, pull quotes in serif, and 'REMEMBER, IT'S NOT A MARATHON' to close. Type: Telidon Bold, ABC Gravity Variable, A-OTF Midashi Min MA31 Pro MA31, Telidon Italic.
Ground and ink from the measured palette (#000000, #BCEBFF, #825E3D). Motion carries the page through
tilted phones playing clips on a yellow ground beside an interview. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — editorial photography, video

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: editorial photography, video

## Reference lock

Primary reference/direction: i-D - Margaret Qualley interview — A magazine feature: 'LIGHTS!!! CAMERA!!! MARGARET!!!' in heavy condensed caps over cover photos, the interview in mono caps body text on grounds that change colour per chapter (black, light blue, yellow, pink), framed photos with coloured borders, tilted phones playing behind-the-scenes clips, pull quotes in serif, and 'REMEMBER, IT'S NOT A MARATHON' to close.
Preserve (3-5 traits): heavy condensed caps headline; ground colour per chapter; mono caps body; tilted phones with clips; coloured photo borders.
Borrow only (1-2): Change the ground colour at each chapter of a long read; Tilted phones playing behind-the-scenes clips
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: editorial photography, video
Reject: All-caps mono body is tiring
Token commitments: palette #000000, #BCEBFF, #825E3D, #A19B81, #411F10, #CAD5D6; type Telidon Bold, ABC Gravity Variable, A-OTF Midashi Min MA31 Pro MA31, Telidon Italic; engine GSAP + Lenis linked (never vendored).
