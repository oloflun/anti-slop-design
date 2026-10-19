---
title: "Brandium Agency"
url: http://brandium.nl/
source_url: http://brandium.nl/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: two-up-case-agency-white
dna: "Dutch branding agency x two-up cases and a dot-grid stat card"
register: modern clean
grammar: gallery/catalog
lane: "A branding agency on white: name intro on black, 'brands disrupt the expected', then pairs of large case images (Loop Earplugs, GoodNews, Co Office, Metapsych) with a dot between them, philosophy, an Apostrophe case, a David Lloyd card, Instagram mockups, earplugs on mint, services list, lime and black stat cards with dot matrices and a client logo row."
mode: persuade
traits: ["two-up case images", "small dot as centre marker", "clean grotesk on white", "lime accent", "dot-matrix stat cards", "client logo row"]
palette: ["#FFFFFF", "#705F54", "#B7BFB5", "#BEA497", "#352A26", "#E7E7DA"]
type: ["TWKLausanne"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The two-up pairs give each case a before/after rhythm, and the dot-matrix stat cards add one crafted detail to a clean agency page.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Present cases in pairs with a shared centre marker
- Dot-matrix animation in stat cards

## What to leave

- Generic white agency layout
- Small text

## Signature move

Pairs of case images with a dot between them on white.

## Motion

Intro: black with the name typing (~1.5 s), a white panel rises. Wheel (Lenis ~110 px glide, 1 pin): case pairs slide up at different speeds; the dot follows the centre; the Apostrophe case scales in; services list reveals by column; dot matrices animate in the stat cards; logos fade in.

Measured (`motion/probe.json`): GSAP 3.13.0/3.13.0; 23 ScrollTriggers; 1 pinned sections; Lenis; WebGL canvas x3; 1 video; split text; smoothed scroll (median 94 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the gallery/catalog grammar: a branding agency on white: name intro on black, 'brands disrupt the expected', then pairs of large case images (Loop Earplugs, GoodNews, Co Office, Metapsych) with a dot between them, philosophy, an Apostrophe case, a David Lloyd card, Instagram mockups, earplugs on mint, services list, lime and black stat cards with dot matrices and a client logo row. Type: TWKLausanne.
Ground and ink from the measured palette (#FFFFFF, #705F54, #B7BFB5). Motion carries the page through
pairs of case images with a dot between them on white. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — brand case photography, mockups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: brand case photography, mockups

## Reference lock

Primary reference/direction: Brandium Agency — A branding agency on white: name intro on black, 'brands disrupt the expected', then pairs of large case images (Loop Earplugs, GoodNews, Co Office, Metapsych) with a dot between them, philosophy, an Apostrophe case, a David Lloyd card, Instagram mockups, earplugs on mint, services list, lime and black stat cards with dot matrices and a client logo row.
Preserve (3-5 traits): two-up case images; small dot as centre marker; clean grotesk on white; lime accent; dot-matrix stat cards.
Borrow only (1-2): Present cases in pairs with a shared centre marker; Dot-matrix animation in stat cards
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: brand case photography, mockups
Reject: Generic white agency layout; Small text
Token commitments: palette #FFFFFF, #705F54, #B7BFB5, #BEA497, #352A26, #E7E7DA; type TWKLausanne; engine GSAP + Lenis linked (never vendored).
