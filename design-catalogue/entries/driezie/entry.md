---
title: "Driezie Studio"
url: https://driezie.studio/
source_url: https://driezie.studio/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: bent-screen-studio
dna: "Accessibility-first studio x 3D curved device renders"
register: modern clean
grammar: split stage
lane: "A warm off-white studio page where each case is a stack of bent, cylinder-curved screens that rotate in 3D as the case text alternates sides, closing on a giant wordmark."
mode: persuade
traits: ["Instrument Serif italic mixed into a grotesque headline", "curved 3D screen renders per case", "alternating left/right case text", "orange micro accents", "mono metadata labels", "giant wordmark footer"]
palette: ["#F3F1EB", "#DAD6D1", "#806D63"]
type: ["Instrument Sans", "Instrument Serif", "Geist Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The studio sells accessible, quiet websites, and the page is quiet: off-white ground, small grotesque, one italic word per headline. The single loud device is the case render, screens bent around a cylinder and spinning slowly, which makes flat website screenshots into objects without any extra colour.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Driezie Studio).

## What to borrow (principle)

- Turn flat screenshots into objects (curved, stacked, rotating) so cases read as products
- One italic serif word inside a sans headline as the only typographic flourish
- Alternate the text column side per case so a long list keeps a rhythm

## What to leave

- The hero render starts blurred and grey for the first second, a soft opening
- Services list is a plain stack after the rich cases

## Signature move

Case screenshots bent into curved 3D panels that rotate as each case scrolls past.

## Motion

Intro: the hero render fades in from a blur while the headline settles (~1.2 s). Scroll (Lenis, ~110 px glide): each case's curved screen stack rotates and drifts up as the case text fades in on the opposite side; sections exchange with simple rises. A horizontal strip of case thumbnails passes near the end; the footer wordmark sits still.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; WebGL canvas x1 (three.js); smoothed scroll (median 113 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the split stage grammar: a warm off-white studio page where each case is a stack of bent, cylinder-curved screens that rotate in 3D as the case text alternates sides, closing on a giant wordmark. Type: Instrument Sans, Instrument Serif, Geist Mono.
Ground and ink from the measured palette (#F3F1EB, #DAD6D1, #806D63). Motion carries the page through
case screenshots bent into curved 3D panels that rotate as each case scrolls past. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — device or screen renders curved and stacked, soft studio light on warm white

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: device or screen renders curved and stacked, soft studio light on warm white

## Reference lock

Primary reference/direction: Driezie Studio — A warm off-white studio page where each case is a stack of bent, cylinder-curved screens that rotate in 3D as the case text alternates sides, closing on a giant wordmark.
Preserve (3-5 traits): Instrument Serif italic mixed into a grotesque headline; curved 3D screen renders per case; alternating left/right case text; orange micro accents; mono metadata labels.
Borrow only (1-2): Turn flat screenshots into objects (curved, stacked, rotating) so cases read as products; One italic serif word inside a sans headline as the only typographic flourish
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: device or screen renders curved and stacked, soft studio light on warm white
Reject: The hero render starts blurred and grey for the first second, a soft opening; Services list is a plain stack after the rich cases
Token commitments: palette #F3F1EB, #DAD6D1, #806D63; type Instrument Sans, Instrument Serif, Geist Mono; engine GSAP + Lenis linked (never vendored).
