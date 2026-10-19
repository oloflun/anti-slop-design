---
title: "Fantik Studio"
url: http://fantik.studio/
source_url: http://fantik.studio/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: pixel-wordmark-smoke-field
dna: "Branding and motion studio x pixel wordmark over a smoky WebGL field"
register: cinematic dark
grammar: live surface
lane: "A studio home on one WebGL stage: percent loader, a pixel-bitmap 'fantik' wordmark over a dark smoky field with floating blobs, the wordmark scales and breaks up, an about line appears, then project titles (MODUS, TRINITY) take the centre one at a time while devices and badges float around them."
mode: experience
traits: ["pixel bitmap wordmark", "dark smoke field with floating blobs", "project title as centre object", "devices floating around the title", "rotating year badge", "virtual scroll steps"]
palette: ["#060606", "#2A2A2A", "#5D5D5D"]
type: ["Inter var", "InterDisplay-Regular", "HelveticaRegular", "HelveticaOblique"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The smoke field holds the whole site in one world and the pixel face gives the studio a voice; projects arrive as the same centred title, which reads clean but repeats.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Fantik Studio).

## What to borrow (principle)

- One WebGL field under the whole site
- Pixel bitmap wordmark that breaks up on scroll

## What to leave

- Same title-swap for every project
- Small grey about text

## Signature move

A pixel 'fantik' wordmark breaking up over a dark smoky field.

## Motion

Intro: black, a pixel mark and a percent counter 1 to 100 (~2 s), then the field and wordmark. Wheel (virtual): the wordmark scales up and pixelates away; the about line fades; each project title fades in centre with device mockups drifting in from the edges and a rotating badge; the smoke field flows the whole time.

Measured (`motion/probe.json`): GSAP 3.12.7; Lenis; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the live surface grammar: a studio home on one WebGL stage: percent loader, a pixel-bitmap 'fantik' wordmark over a dark smoky field with floating blobs, the wordmark scales and breaks up, an about line appears, then project titles (MODUS, TRINITY) take the centre one at a time while devices and badges float around them. Type: Inter var, InterDisplay-Regular, HelveticaRegular, HelveticaOblique.
Ground and ink from the measured palette (#060606, #2A2A2A, #5D5D5D). Motion carries the page through
a pixel 'fantik' wordmark breaking up over a dark smoky field. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL smoke, device mockups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL smoke, device mockups

## Reference lock

Primary reference/direction: Fantik Studio — A studio home on one WebGL stage: percent loader, a pixel-bitmap 'fantik' wordmark over a dark smoky field with floating blobs, the wordmark scales and breaks up, an about line appears, then project titles (MODUS, TRINITY) take the centre one at a time while devices and badges float around them.
Preserve (3-5 traits): pixel bitmap wordmark; dark smoke field with floating blobs; project title as centre object; devices floating around the title; rotating year badge.
Borrow only (1-2): One WebGL field under the whole site; Pixel bitmap wordmark that breaks up on scroll
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL smoke, device mockups
Reject: Same title-swap for every project; Small grey about text
Token commitments: palette #060606, #2A2A2A, #5D5D5D; type Inter var, InterDisplay-Regular, HelveticaRegular, HelveticaOblique; engine GSAP + Lenis linked (never vendored).
