---
title: "Graffico - Web, Software and AI"
url: https://graffico.it/
source_url: https://graffico.it/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "product-focused"
family: italian-dev-agency-ribbon
dna: "Italian software agency x a 3D ribbon through the wordmark and floating device mockups"
register: cinematic dark
grammar: chaptered editorial
lane: "A software agency: red logo intro, a cream shape wipe to black, a 3D ribbon looping through the giant 'GRAFFICO' wordmark, then black sections with italic serif accents (reviews, services in glowing cards), a cream projects section where laptops and phones float in pairs, articles and an FAQ with a dashed path."
mode: persuade
traits: ["3D ribbon through the wordmark", "italic red serif accents", "cream and black alternation", "floating laptop and phone pairs", "glowing service cards", "dashed path line"]
palette: ["#111111", "#E6D6C1", "#3F2C28", "#8A7A6D"]
type: ["Shrikhand", "Work Sans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The ribbon gives the name an object, and the floating device pairs make a project list feel physical.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Float device pairs at depth for case studies

## What to leave

- Cookie bar over every frame
- Many generic sections

## Signature move

A 3D ribbon looping through a giant 'GRAFFICO' wordmark.

## Motion

Intro: red with the logo (~1 s), a cream organic shape sweeps across to black and the wordmark lands with the ribbon. Wheel (native with ~120 px smoothing spikes): reviews and cards slide up; the ground flips to cream; device pairs drift in from the sides at different depths; articles stagger; the FAQ path draws.

Measured (`motion/probe.json`): GSAP 3.15.0; 36 video; smoothed scroll (median 120 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a software agency: red logo intro, a cream shape wipe to black, a 3D ribbon looping through the giant 'GRAFFICO' wordmark, then black sections with italic serif accents (reviews, services in glowing cards), a cream projects section where laptops and phones float in pairs, articles and an FAQ with a dashed path. Type: Shrikhand, Work Sans.
Ground and ink from the measured palette (#111111, #E6D6C1, #3F2C28). Motion carries the page through
a 3D ribbon looping through a giant 'GRAFFICO' wordmark. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D ribbon, device mockups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D ribbon, device mockups

## Reference lock

Primary reference/direction: Graffico - Web, Software and AI — A software agency: red logo intro, a cream shape wipe to black, a 3D ribbon looping through the giant 'GRAFFICO' wordmark, then black sections with italic serif accents (reviews, services in glowing cards), a cream projects section where laptops and phones float in pairs, articles and an FAQ with a dashed path.
Preserve (3-5 traits): 3D ribbon through the wordmark; italic red serif accents; cream and black alternation; floating laptop and phone pairs; glowing service cards.
Borrow only (1-2): Float device pairs at depth for case studies
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D ribbon, device mockups
Reject: Cookie bar over every frame; Many generic sections
Token commitments: palette #111111, #E6D6C1, #3F2C28, #8A7A6D; type Shrikhand, Work Sans; engine GSAP + Lenis linked (never vendored).
