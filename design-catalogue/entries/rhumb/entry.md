---
title: "Rhumb Studio - Design and development studio"
url: https://www.rhumb.co/
source_url: https://www.rhumb.co/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: serif-studio-stacked-cases
dna: "Design and dev studio x stacked full-width cases on warm grey with serif type"
register: editorial print
grammar: chaptered editorial
lane: "A studio site on warm grey: a black name loader, a blurred reveal, then full-width cases (Lumara, Jonathan Grado, Rose Island) that stack as you scroll with the case name at right and a short description at left, a serif statement, a numbered services list, a project mosaic, testimonials and articles."
mode: persuade
traits: ["warm grey ground", "serif headlines", "full-width cases stacking", "blur reveal intro", "numbered services", "project mosaic"]
palette: ["#101010", "#808A93", "#323634", "#435C6A", "#C4C8C9", "#6E6E68"]
type: ["editorialNew", "Switzer"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Stacked full-width cases with a calm serif give the studio an editorial pace.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Blur in the first frame instead of fading

## What to leave

- Small text
- Generic mosaic

## Signature move

Full-width case images stacking under small serif captions on warm grey.

## Motion

Intro: black name for ~2 s, a blurred frame sharpens into the first case. Wheel (Lenis ~90 px glide): cases slide up over each other; names swap; the statement fills; services highlight one by one; the mosaic drifts.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x1 (three.js); 1 video; smoothed scroll (median 101 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a studio site on warm grey: a black name loader, a blurred reveal, then full-width cases (Lumara, Jonathan Grado, Rose Island) that stack as you scroll with the case name at right and a short description at left, a serif statement, a numbered services list, a project mosaic, testimonials and articles. Type: editorialNew, Switzer.
Ground and ink from the measured palette (#101010, #808A93, #323634). Motion carries the page through
full-width case images stacking under small serif captions on warm grey. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — architectural renders, product photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: architectural renders, product photography

## Reference lock

Primary reference/direction: Rhumb Studio - Design and development studio — A studio site on warm grey: a black name loader, a blurred reveal, then full-width cases (Lumara, Jonathan Grado, Rose Island) that stack as you scroll with the case name at right and a short description at left, a serif statement, a numbered services list, a project mosaic, testimonials and articles.
Preserve (3-5 traits): warm grey ground; serif headlines; full-width cases stacking; blur reveal intro; numbered services.
Borrow only (1-2): Blur in the first frame instead of fading
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: architectural renders, product photography
Reject: Small text; Generic mosaic
Token commitments: palette #101010, #808A93, #323634, #435C6A, #C4C8C9, #6E6E68; type editorialNew, Switzer; engine GSAP + Lenis linked (never vendored).
