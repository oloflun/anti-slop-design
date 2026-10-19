---
title: "VWLAB Report - Web animation course"
url: https://vwlab.io/pages/report
source_url: https://vwlab.io/pages/report
captured: 2026-10-02
origin: raw-url
extract: none
category: editorial
category2: "product-focused"
family: course-report-giant-type
dna: "Web animation course x a giant 'REPORT' wordmark and demo lessons"
register: editorial print
grammar: chaptered editorial
lane: "A course report page: a cream-to-maroon loader, a giant maroon 'REPORT' wordmark with a pixel icon in the O, chapter icons, halftone discs, 'The monthly updates made since launching' list, demo lesson panels (infinite slider, gallery animation, kinetic page transition with red stretched type, drawer animation) and 'We're not just numbers' with counters."
mode: persuade
traits: ["giant maroon wordmark", "halftone disc shapes", "demo lesson panels", "red stretched kinetic type", "mono labels", "cream and maroon"]
palette: ["#BBA5A4", "#8E6257", "#E7DFD6", "#D2C1BD", "#13090A"]
type: ["IBM Plex Mono", "IBM Plex Sans Condensed"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Showing actual lesson demos inside framed panels sells the course by example.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Embed live demo panels of what the product teaches

## What to leave

- Very small labels

## Signature move

A giant maroon 'REPORT' with a pixel icon in the O.

## Motion

Intro: cream, then maroon with small text (~2 s), the wordmark rises. Wheel: discs slide; the list fills; each demo panel plays its own animation; counters tick.

Measured (`motion/probe.json`): virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: CLOSE. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a course report page: a cream-to-maroon loader, a giant maroon 'REPORT' wordmark with a pixel icon in the O, chapter icons, halftone discs, 'The monthly updates made since launching' list, demo lesson panels (infinite slider, gallery animation, kinetic page transition with red stretched type, drawer animation) and 'We're not just numbers' with counters. Type: IBM Plex Mono, IBM Plex Sans Condensed.
Ground and ink from the measured palette (#BBA5A4, #8E6257, #E7DFD6). Motion carries the page through
a giant maroon 'REPORT' with a pixel icon in the O. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — demo screenshots, halftone shapes

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: demo screenshots, halftone shapes

## Reference lock

Primary reference/direction: VWLAB Report - Web animation course — A course report page: a cream-to-maroon loader, a giant maroon 'REPORT' wordmark with a pixel icon in the O, chapter icons, halftone discs, 'The monthly updates made since launching' list, demo lesson panels (infinite slider, gallery animation, kinetic page transition with red stretched type, drawer animation) and 'We're not just numbers' with counters.
Preserve (3-5 traits): giant maroon wordmark; halftone disc shapes; demo lesson panels; red stretched kinetic type; mono labels.
Borrow only (1-2): Embed live demo panels of what the product teaches
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: demo screenshots, halftone shapes
Reject: Very small labels
Token commitments: palette #BBA5A4, #8E6257, #E7DFD6, #D2C1BD, #13090A; type IBM Plex Mono, IBM Plex Sans Condensed; engine GSAP + Lenis linked (never vendored).
