---
title: "Morten Stig Uemichi-Christensen"
url: https://www.mschristensen.com/
source_url: https://www.mschristensen.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: horizontal-case-strip-designer
dna: "Digital designer folio x endless horizontal case strip"
register: modern clean
grammar: gallery/catalog
lane: "A designer folio whose intro tilts a device mockup through three grounds (light, green, dark), then lays every case as a continuous horizontal strip of tall image panels with titles above, sliding sideways under the wheel."
mode: experience
traits: ["device mockup intro through colour grounds", "endless horizontal strip of case panels", "titles above each panel", "small pill nav (Selected, Archive, Published)", "Barba transitions"]
palette: ["#F8F8F8", "#587462", "#2E302D", "#B3B0A5", "#E3E3DB"]
type: ["PP Neue Montreal"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

All cases are one long strip that slides sideways forever, so the folio reads like a contact sheet of the whole career. The intro changes the ground colour three times behind one tilting device, a compact way to show range.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One continuous horizontal strip of tall case panels as the folio
- Cycle the ground colour behind a single object in the intro

## What to leave

- Cookie panel on every frame
- No sense of the strip's length

## Signature move

An endless horizontal strip of tall case panels sliding sideways.

## Motion

Intro: name, then a device mockup that tilts while the ground changes (light → green → dark) (~2.5 s). Wheel (Barba): the strip of case panels slides left; titles above update; panels show device and brand photography.

Measured (`motion/probe.json`): GSAP 3.15.0; Barba page transitions; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the gallery/catalog grammar: a designer folio whose intro tilts a device mockup through three grounds (light, green, dark), then lays every case as a continuous horizontal strip of tall image panels with titles above, sliding sideways under the wheel. Type: PP Neue Montreal.
Ground and ink from the measured palette (#F8F8F8, #587462, #2E302D). Motion carries the page through
an endless horizontal strip of tall case panels sliding sideways. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — device mockups and brand photography per case

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: device mockups and brand photography per case

## Reference lock

Primary reference/direction: Morten Stig Uemichi-Christensen — A designer folio whose intro tilts a device mockup through three grounds (light, green, dark), then lays every case as a continuous horizontal strip of tall image panels with titles above, sliding sideways under the wheel.
Preserve (3-5 traits): device mockup intro through colour grounds; endless horizontal strip of case panels; titles above each panel; small pill nav (Selected, Archive, Published); Barba transitions.
Borrow only (1-2): One continuous horizontal strip of tall case panels as the folio; Cycle the ground colour behind a single object in the intro
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: device mockups and brand photography per case
Reject: Cookie panel on every frame; No sense of the strip's length
Token commitments: palette #F8F8F8, #587462, #2E302D, #B3B0A5, #E3E3DB; type PP Neue Montreal; engine GSAP + Lenis linked (never vendored).
