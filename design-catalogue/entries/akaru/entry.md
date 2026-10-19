---
title: "Akaru - Lyon web agency"
url: https://akaru.fr/en/
source_url: https://akaru.fr/en/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: colour-column-agency-giant-name
dna: "Web agency x colour columns, cut images and a giant condensed wordmark footer"
register: editorial print
grammar: chaptered editorial
lane: "An agency: thin vertical bars on black, 'AKARU' in condensed black on cream with a photo panel sliding in, a cat photo over a pink strip (Pikko case), colour columns (sage, mauve, orange) sliding beside 'Projects', 'Expertise' lists, a prize object on black, an agency section and a giant 'AKARU' wordmark filling the footer."
mode: persuade
traits: ["colour columns sliding", "condensed black wordmark", "photos cut by columns", "prize object on black", "giant footer wordmark", "cream and black"]
palette: ["#F0EFEB", "#0E0E0E", "#C4C2C7", "#3A404C"]
type: ["Alliance Neue", "Alliance Platt"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The columns are the layout and the transition: every section slides in as a stack of coloured panels.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase.

## What to borrow (principle)

- Use coloured columns as the device that brings each section in

## What to leave

- Small list text

## Signature move

'AKARU' in condensed black filling the footer edge to edge.

## Motion

Intro: bars grow on black (~1.5 s). Wheel: the photo panel slides; columns slide in from the right; images move inside the columns; the prize rotates; the wordmark rises.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x1 (three.js); 1 video; split text; smoothed scroll (median 377 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: an agency: thin vertical bars on black, 'AKARU' in condensed black on cream with a photo panel sliding in, a cat photo over a pink strip (Pikko case), colour columns (sage, mauve, orange) sliding beside 'Projects', 'Expertise' lists, a prize object on black, an agency section and a giant 'AKARU' wordmark filling the footer. Type: Alliance Neue, Alliance Platt.
Ground and ink from the measured palette (#F0EFEB, #0E0E0E, #C4C2C7). Motion carries the page through
'AKARU' in condensed black filling the footer edge to edge. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — case photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: case photography

## Reference lock

Primary reference/direction: Akaru - Lyon web agency — An agency: thin vertical bars on black, 'AKARU' in condensed black on cream with a photo panel sliding in, a cat photo over a pink strip (Pikko case), colour columns (sage, mauve, orange) sliding beside 'Projects', 'Expertise' lists, a prize object on black, an agency section and a giant 'AKARU' wordmark filling the footer.
Preserve (3-5 traits): colour columns sliding; condensed black wordmark; photos cut by columns; prize object on black; giant footer wordmark.
Borrow only (1-2): Use coloured columns as the device that brings each section in
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: case photography
Reject: Small list text
Token commitments: palette #F0EFEB, #0E0E0E, #C4C2C7, #3A404C; type Alliance Neue, Alliance Platt; engine GSAP + Lenis linked (never vendored).
