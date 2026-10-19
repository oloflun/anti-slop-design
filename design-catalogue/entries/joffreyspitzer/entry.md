---
title: "Joffrey Spitzer - Creative Front-end Developer"
url: https://joffreyspitzer.com/
source_url: https://joffreyspitzer.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: quiet-column-folio-3d-rock
dna: "Creative front-end developer x quiet image column and 3D rock"
register: modern clean
grammar: gallery/catalog
lane: "A minimal folio: a framed loader counts up, then a light grey page with a large 'Cases' label fixed bottom left while a narrow column of project images scrolls past and the case name highlights in a list at right; a black 3D rock with 'Code, Design, Motion' ends the page."
mode: read
traits: ["framed loading screen with counter", "fixed 'Cases' label", "narrow image column scrolling past", "active case highlighted in side list", "3D black rock as closing object", "tiny type everywhere else"]
palette: ["#F7F7F7", "#0D0E0D", "#64695C", "#D0D1CE"]
type: ["PP Neue Montreal"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The fixed label and side list hold still while the images move, so the page reads like a contact sheet being pulled past a viewer; the rock gives the quiet page one heavy object to land on.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Joffrey Spitzer).

## What to borrow (principle)

- Fix the section label and list, scroll only the image column
- End a quiet page on one heavy 3D object

## What to leave

- Very small type
- Rock frame repeated at the end

## Signature move

A narrow column of project images sliding past a fixed 'Cases' label.

## Motion

Intro: a framed white loader counts 14 to 100, the frame then opens to the page (~2 s). Wheel (Lenis, ~140 px glide): images scroll at different widths in one column; the case name in the right list switches as each image passes; the rock rises from below and rotates slowly. Swup page transitions.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; Swup page transitions; 1 video; smoothed scroll (median 143 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the gallery/catalog grammar: a minimal folio: a framed loader counts up, then a light grey page with a large 'Cases' label fixed bottom left while a narrow column of project images scrolls past and the case name highlights in a list at right; a black 3D rock with 'Code, Design, Motion' ends the page. Type: PP Neue Montreal.
Ground and ink from the measured palette (#F7F7F7, #0D0E0D, #64695C). Motion carries the page through
a narrow column of project images sliding past a fixed 'Cases' label. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project photography and a 3D rock render

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project photography and a 3D rock render

## Reference lock

Primary reference/direction: Joffrey Spitzer - Creative Front-end Developer — A minimal folio: a framed loader counts up, then a light grey page with a large 'Cases' label fixed bottom left while a narrow column of project images scrolls past and the case name highlights in a list at right; a black 3D rock with 'Code, Design, Motion' ends the page.
Preserve (3-5 traits): framed loading screen with counter; fixed 'Cases' label; narrow image column scrolling past; active case highlighted in side list; 3D black rock as closing object.
Borrow only (1-2): Fix the section label and list, scroll only the image column; End a quiet page on one heavy 3D object
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project photography and a 3D rock render
Reject: Very small type; Rock frame repeated at the end
Token commitments: palette #F7F7F7, #0D0E0D, #64695C, #D0D1CE; type PP Neue Montreal; engine GSAP + Lenis linked (never vendored).
