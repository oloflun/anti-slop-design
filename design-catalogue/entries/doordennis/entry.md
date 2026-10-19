---
title: "Door Dennis"
url: https://www.doordennis.nl/
source_url: https://www.doordennis.nl/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: frosted-glass-wordmark-studio
dna: "Dutch branding studio x frosted 3D glass logo"
register: modern clean
grammar: split stage
lane: "A pale studio page where a frosted-glass 3D version of the logo floats in a blue blur behind a serif-italic headline, and project photos enter through vertical-bar scan reveals while the blur follows the scroll."
mode: persuade
traits: ["frosted glass 3D logo in WebGL", "blue atmospheric blur ground", "serif caps headline with italic words", "vertical bar (venetian) image reveals", "orange micro CTA", "tabbed expertise grid"]
palette: ["#F0F0F0", "#C7D2DE", "#32292D", "#A19CA3"]
type: ["Instrument Serif", "Inter", "icomoon"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The ground is the motion: a soft blue refraction field with a glassy 3D logo drifting through it stays behind every section, so the plain white layout always has depth. Projects never just fade; they arrive behind vertical bars that resolve into the photo, a print-scan feel that matches the studio's branding work.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Dennis Janssen).

## What to borrow (principle)

- A continuous atmospheric WebGL ground (blur, refraction) behind a plain layout gives depth without decorating each section
- Reveal photographs through vertical bars that resolve, like a scan
- Mix italic serif words into an all-caps serif headline for voice

## What to leave

- Cookie banner sits over every captured frame
- Long blank stretches where only the blur moves

## Signature move

A frosted-glass logo floating in a blue refraction field behind the whole page.

## Motion

Intro: headline types/reveals line by line in serif with italic words, blur ground fades up (~1.5 s). Scroll (Lenis, ~40–130 px glide; 2 pins; Swup transitions; SplitText on ~1200 nodes): the glass logo drifts and rotates with scroll; a services marquee band; project photos arrive through vertical bar masks, alternating sides; the manifesto paragraph reveals per line and stays pinned while the blur shifts; expertise tabs.

Measured (`motion/probe.json`): GSAP 3.11.4; 14 ScrollTriggers; 2 pinned sections; Lenis; Swup page transitions; WebGL canvas x1 (three.js); 10 video; split text; smoothed scroll (median 105 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the split stage grammar: a pale studio page where a frosted-glass 3D version of the logo floats in a blue blur behind a serif-italic headline, and project photos enter through vertical-bar scan reveals while the blur follows the scroll. Type: Instrument Serif, Inter, icomoon.
Ground and ink from the measured palette (#F0F0F0, #C7D2DE, #32292D). Motion carries the page through
a frosted-glass logo floating in a blue refraction field behind the whole page. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — campaign portraits and branded objects, high contrast colour photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: campaign portraits and branded objects, high contrast colour photography

## Reference lock

Primary reference/direction: Door Dennis — A pale studio page where a frosted-glass 3D version of the logo floats in a blue blur behind a serif-italic headline, and project photos enter through vertical-bar scan reveals while the blur follows the scroll.
Preserve (3-5 traits): frosted glass 3D logo in WebGL; blue atmospheric blur ground; serif caps headline with italic words; vertical bar (venetian) image reveals; orange micro CTA.
Borrow only (1-2): A continuous atmospheric WebGL ground (blur, refraction) behind a plain layout gives depth without decorating each section; Reveal photographs through vertical bars that resolve, like a scan
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: campaign portraits and branded objects, high contrast colour photography
Reject: Cookie banner sits over every captured frame; Long blank stretches where only the blur moves
Token commitments: palette #F0F0F0, #C7D2DE, #32292D, #A19CA3; type Instrument Serif, Inter, icomoon; engine GSAP + Lenis linked (never vendored).
