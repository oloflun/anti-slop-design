---
title: "Guillaume Tomasi - devfolio"
url: https://dev.guillaumetomasi.com/
source_url: https://dev.guillaumetomasi.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: blue-paper-sheets-devfolio
dna: "Developer folio x blue paper sheets shifting behind a faint name"
register: modern clean
grammar: live surface
lane: "A developer folio: a blue screen where translucent paper-like sheets drift and overlap behind a faint 'GUILLAUME TOMASI' with small corner nav."
mode: experience
traits: ["blue paper sheets", "faint large name", "corner nav", "single screen", "WebGL sheets"]
palette: ["#193A78"]
type: ["PPPierSans-Regular", "PPPierSans-Bold", "PPSupplyMono-Medium"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

One quiet material effect; the capture shows nothing beyond the hero.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A single soft material field as a quiet hero

## What to leave

- Name nearly invisible
- Nothing beyond the hero

## Signature move

Blue translucent sheets drifting behind a faint name.

## Motion

Intro: white to blue (~1 s). Scroll: the sheets drift; nothing else captured.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the live surface grammar: a developer folio: a blue screen where translucent paper-like sheets drift and overlap behind a faint 'GUILLAUME TOMASI' with small corner nav. Type: PPPierSans-Regular, PPPierSans-Bold, PPSupplyMono-Medium.
Ground and ink from the measured palette (#193A78). Motion carries the page through
blue translucent sheets drifting behind a faint name. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL

## Reference lock

Primary reference/direction: Guillaume Tomasi - devfolio — A developer folio: a blue screen where translucent paper-like sheets drift and overlap behind a faint 'GUILLAUME TOMASI' with small corner nav.
Preserve (3-5 traits): blue paper sheets; faint large name; corner nav; single screen; WebGL sheets.
Borrow only (1-2): A single soft material field as a quiet hero
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL
Reject: Name nearly invisible; Nothing beyond the hero
Token commitments: palette #193A78; type PPPierSans-Regular, PPPierSans-Bold, PPSupplyMono-Medium; engine GSAP + Lenis linked (never vendored).
