---
title: "Sublimio - Brand strategy and design"
url: https://www.sublimio.com/
source_url: https://www.sublimio.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "luxury-craft"
family: quiet-dark-brand-studio
dna: "Italian brand studio x a quiet black page with projects rising in a monitor"
register: cinematic dark
grammar: chaptered editorial
lane: "A brand studio on black: 'Ciao, we are Sublimio' types in, a case photo rises inside a monitor, cases (a Japanese hand-care brand, The Missing Element, Sakari sake) with small text, 'Want to see more?' over tilted cards, 'beautiful thinking' with a dark 3D flower, a craft photo of hands drawing and a map of studios."
mode: persuade
traits: ["typed greeting", "case inside a monitor", "black ground", "tilted project cards", "dark 3D flower", "craft photography"]
palette: ["#000000", "#A49F9A", "#202523"]
type: ["TT Hoves Regular", "TT Hoves DemiBold", "TT Hoves Medium"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Calm, dark and minimal; the dark flower is a nice emblem but the motion is modest.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Type the greeting as the intro

## What to leave

- Very small text

## Signature move

A dark 3D flower beside 'beautiful thinking'.

## Motion

Intro: black, the greeting types line by line (~2 s). Wheel (smoothed): the case rises inside a monitor and fills; cases fade; cards tilt in; the flower rotates; the craft photo scales.

Measured (`motion/probe.json`): GSAP 3.9.1/3.9.1; Locomotive; Swup page transitions; 3 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a brand studio on black: 'Ciao, we are Sublimio' types in, a case photo rises inside a monitor, cases (a Japanese hand-care brand, The Missing Element, Sakari sake) with small text, 'Want to see more?' over tilted cards, 'beautiful thinking' with a dark 3D flower, a craft photo of hands drawing and a map of studios. Type: TT Hoves Regular, TT Hoves DemiBold, TT Hoves Medium.
Ground and ink from the measured palette (#000000, #A49F9A, #202523). Motion carries the page through
a dark 3D flower beside 'beautiful thinking'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — case photography, 3D flower

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: case photography, 3D flower

## Reference lock

Primary reference/direction: Sublimio - Brand strategy and design — A brand studio on black: 'Ciao, we are Sublimio' types in, a case photo rises inside a monitor, cases (a Japanese hand-care brand, The Missing Element, Sakari sake) with small text, 'Want to see more?' over tilted cards, 'beautiful thinking' with a dark 3D flower, a craft photo of hands drawing and a map of studios.
Preserve (3-5 traits): typed greeting; case inside a monitor; black ground; tilted project cards; dark 3D flower.
Borrow only (1-2): Type the greeting as the intro
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: case photography, 3D flower
Reject: Very small text
Token commitments: palette #000000, #A49F9A, #202523; type TT Hoves Regular, TT Hoves DemiBold, TT Hoves Medium; engine GSAP + Lenis linked (never vendored).
