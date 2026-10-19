---
title: "Raine Architects"
url: https://rainearchitects.com/
source_url: https://rainearchitects.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: blue-accent-architect-studio
dna: "Texas architecture firm x blue accent words and corner-tick frames"
register: modern clean
grammar: chaptered editorial
lane: "An architecture firm on white: a corner-tick loader with a counter, 'Innovative timeless architecture design' with alternating blue words, a parametric facade photo, 3D viz renders, a founder portrait with 'Based in' cities in blue, experience/vision/diversity rows, project stats, a project carousel with spec sheets, an expertise list with a blue active row and a form."
mode: persuade
traits: ["blue accent words", "corner tick marks", "counter loader", "parametric facade photo", "stat grid", "blue highlighted list row"]
palette: ["#FFFFFF", "#3B4640", "#92A0AC", "#D5DDE7", "#888580", "#161C18"]
type: ["Gilroy", "Helvetica", "IvyStyle Sans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

A tidy firm site; the corner ticks and alternating blue words give it a technical, drawn feel.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Two Capitals Studio).

## What to borrow (principle)

- Corner tick marks as a framing motif

## What to leave

- Generic stats and form
- Long lists

## Signature move

Alternating blue words in 'Innovative timeless architecture design'.

## Motion

Intro: white with corner ticks and a counter 62 to 91 (~2 s). Wheel (Lenis ~150-190 px glide): the headline words slide in from alternate sides; images scale; city names rise; stats count; carousel slides; the list row highlights.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x1 (three.js); smoothed scroll (median 148 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: an architecture firm on white: a corner-tick loader with a counter, 'Innovative timeless architecture design' with alternating blue words, a parametric facade photo, 3D viz renders, a founder portrait with 'Based in' cities in blue, experience/vision/diversity rows, project stats, a project carousel with spec sheets, an expertise list with a blue active row and a form. Type: Gilroy, Helvetica, IvyStyle Sans.
Ground and ink from the measured palette (#FFFFFF, #3B4640, #92A0AC). Motion carries the page through
alternating blue words in 'Innovative timeless architecture design'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — architectural photography and renders, portrait

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: architectural photography and renders, portrait

## Reference lock

Primary reference/direction: Raine Architects — An architecture firm on white: a corner-tick loader with a counter, 'Innovative timeless architecture design' with alternating blue words, a parametric facade photo, 3D viz renders, a founder portrait with 'Based in' cities in blue, experience/vision/diversity rows, project stats, a project carousel with spec sheets, an expertise list with a blue active row and a form.
Preserve (3-5 traits): blue accent words; corner tick marks; counter loader; parametric facade photo; stat grid.
Borrow only (1-2): Corner tick marks as a framing motif
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: architectural photography and renders, portrait
Reject: Generic stats and form; Long lists
Token commitments: palette #FFFFFF, #3B4640, #92A0AC, #D5DDE7, #888580, #161C18; type Gilroy, Helvetica, IvyStyle Sans; engine GSAP + Lenis linked (never vendored).
