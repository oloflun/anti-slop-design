---
title: "Magnify Capital Partners"
url: http://magnify.partners/
source_url: http://magnify.partners/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "luxury-craft"
family: red-dahlia-fund-showcase
dna: "Portuguese investment funds x a red dahlia that stays pinned while fund cards fly past"
register: cinematic dark
grammar: split stage
lane: "A fund manager for Golden Visa investors: black, a red dahlia blooms from the dark, 'Magnifying your investments', then the dahlia stays pinned centre while each fund category (Private Equity, Venture Capital, Open-ended, Private Syndicate, Real Estate) is written huge across the bottom and cream fund cards fly up past the flower; it ends in black-and-white architecture and a funds comparison table."
mode: persuade
traits: ["one red dahlia pinned through the whole page", "giant category word sliding across the bottom", "cream fund cards flying past", "red and black only", "Flip between card states", "comparison table finale"]
palette: ["#000000", "#FFFDF6", "#B90911", "#6B0507", "#A2928F", "#6F2428"]
type: ["TT Norms"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The dahlia is the signature object and the only colour: it stays still while the funds move around it, which reads as stability in a finance pitch and makes a long product list one composition.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Co.Design).

## What to borrow (principle)

- Pin one object and fly the product cards past it
- Write each category huge along the bottom edge

## What to leave

- Card text very small
- Comparison table is dense

## Signature move

A red dahlia pinned on black while fund cards fly past it.

## Motion

Intro: black for ~2 s, a single stem then the dahlia fades and grows in (~3 s). Wheel (Lenis ~110 px glide, 7 pins): the headline rises over the flower; the flower pins; each category word slides in huge from the right as cards rise from below and exit upward; the flower drifts left for the Golden Visa section; architecture photos slide in; the table rises.

Measured (`motion/probe.json`): GSAP 3.13.0; 7 pinned sections; Lenis; WebGL canvas x1 (three.js); 1 video; smoothed scroll (median 136 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the split stage grammar: a fund manager for Golden Visa investors: black, a red dahlia blooms from the dark, 'Magnifying your investments', then the dahlia stays pinned centre while each fund category (Private Equity, Venture Capital, Open-ended, Private Syndicate, Real Estate) is written huge across the bottom and cream fund cards fly up past the flower; it ends in black-and-white architecture and a funds comparison table. Type: TT Norms.
Ground and ink from the measured palette (#000000, #FFFDF6, #B90911). Motion carries the page through
a red dahlia pinned on black while fund cards fly past it. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — dahlia photography, black and white architecture

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: dahlia photography, black and white architecture

## Reference lock

Primary reference/direction: Magnify Capital Partners — A fund manager for Golden Visa investors: black, a red dahlia blooms from the dark, 'Magnifying your investments', then the dahlia stays pinned centre while each fund category (Private Equity, Venture Capital, Open-ended, Private Syndicate, Real Estate) is written huge across the bottom and cream fund cards fly up past the flower; it ends in black-and-white architecture and a funds comparison table.
Preserve (3-5 traits): one red dahlia pinned through the whole page; giant category word sliding across the bottom; cream fund cards flying past; red and black only; Flip between card states.
Borrow only (1-2): Pin one object and fly the product cards past it; Write each category huge along the bottom edge
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: dahlia photography, black and white architecture
Reject: Card text very small; Comparison table is dense
Token commitments: palette #000000, #FFFDF6, #B90911, #6B0507, #A2928F, #6F2428; type TT Norms; engine GSAP + Lenis linked (never vendored).
