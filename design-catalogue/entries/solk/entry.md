---
title: "SOLK - Swiss engineered footwear"
url: https://solk.com/
source_url: https://solk.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "luxury-craft"
family: sustainable-shoe-quiet-commerce
dna: "Biocircular footwear x quiet white editorial and process photography"
register: modern clean
grammar: chaptered editorial
lane: "A footwear brand on white: a full-width shoe close-up 'Made to fade', a two-up of models on volcanic rock, a centred statement about compostable shoes, three cards (materials, back to earth, our system), a sneaker on grey, factory process shots and a press logo row before a black footer with the 'S/LK' wordmark."
mode: read
traits: ["white editorial ground", "small centred statements", "two-up campaign photos", "process photography", "press logo row", "black footer wordmark"]
palette: ["#FFFFFF", "#C8C7C2", "#2A2926", "#A19D98", "#534D45", "#E7E5E1"]
type: ["SuisseIntl Regular", "SuisseWorks Regular", "GTStandard-M"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Quiet, well-photographed and restrained; the motion is limited to calm reveals.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Small centred statements between large photos for a calm luxury pace

## What to leave

- Little motion beyond reveals

## Signature move

A shoe close-up under 'Made to fade'.

## Motion

Intro: the hero with a cookie card (declined). Wheel (Lenis): images rise in pairs; statements fade in; cards slide; the black footer rises.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; 4 video; smoothed scroll (median 116 px still travelling after input stops); entry gate: Decline. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a footwear brand on white: a full-width shoe close-up 'Made to fade', a two-up of models on volcanic rock, a centred statement about compostable shoes, three cards (materials, back to earth, our system), a sneaker on grey, factory process shots and a press logo row before a black footer with the 'S/LK' wordmark. Type: SuisseIntl Regular, SuisseWorks Regular, GTStandard-M.
Ground and ink from the measured palette (#FFFFFF, #C8C7C2, #2A2926). Motion carries the page through
a shoe close-up under 'Made to fade'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product and campaign photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product and campaign photography

## Reference lock

Primary reference/direction: SOLK - Swiss engineered footwear — A footwear brand on white: a full-width shoe close-up 'Made to fade', a two-up of models on volcanic rock, a centred statement about compostable shoes, three cards (materials, back to earth, our system), a sneaker on grey, factory process shots and a press logo row before a black footer with the 'S/LK' wordmark.
Preserve (3-5 traits): white editorial ground; small centred statements; two-up campaign photos; process photography; press logo row.
Borrow only (1-2): Small centred statements between large photos for a calm luxury pace
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product and campaign photography
Reject: Little motion beyond reveals
Token commitments: palette #FFFFFF, #C8C7C2, #2A2926, #A19D98, #534D45, #E7E5E1; type SuisseIntl Regular, SuisseWorks Regular, GTStandard-M; engine GSAP + Lenis linked (never vendored).
