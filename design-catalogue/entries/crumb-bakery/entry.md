---
title: "CRUMB Bakery"
url: https://crumb-bakery.vercel.app/
source_url: https://crumb-bakery.vercel.app/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "hospitality"
family: bread-chapter-colour-floods
dna: "Home bakery x one loaf per full-colour chapter"
register: illustrated dark
grammar: rhythmic cutlist
lane: "A small home bakery: a circular text loader 'Crumb Bakery', letters of CRUMB jumping, a loaf dropping onto a green wave, then each bread gets a full-screen colour chapter (Hulk spinach on green, rye on brown, white on tan, borsch beetroot on red, wholegrain, chocolate, baguette) with the loaf rolling in from the side over a repeated outline name and a price line, and a handwritten about with photos."
mode: persuade
traits: ["one loaf per colour chapter", "loaf rolls in from the side", "repeated outline name in the background", "handwriting font for the about", "price line per bread", "circular text loader"]
palette: ["#D4D4D4", "#B08C54", "#764E28", "#4E2E19"]
type: ["Gloria Hallelujah", "Luckiest Guy", "Londrina Outline"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Each loaf as its own colour world turns a short menu into a playful sequence; the rolling loaf is the same move every time but each colour makes it new.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Give every product its own background colour and the same entrance

## What to leave

- Handwriting font for body copy
- Thin price lines

## Signature move

Each loaf rolling in on its own full-screen colour.

## Motion

Intro: grey, circular text spins around 'CRUMB', the letters jump and scatter (~2 s), a loaf drops onto a green wave. Wheel (Lenis ~130 px glide, 2 pins): each chapter's colour slides in; the loaf rolls in rotating from the right while the outline name scrolls behind; the price line draws; the baguette falls; the about panel rises.

Measured (`motion/probe.json`): GSAP 3.13.0; 2 pinned sections; Lenis; WebGL canvas x1 (three.js); smoothed scroll (median 134 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the rhythmic cutlist grammar: a small home bakery: a circular text loader 'Crumb Bakery', letters of CRUMB jumping, a loaf dropping onto a green wave, then each bread gets a full-screen colour chapter (Hulk spinach on green, rye on brown, white on tan, borsch beetroot on red, wholegrain, chocolate, baguette) with the loaf rolling in from the side over a repeated outline name and a price line, and a handwritten about with photos. Type: Gloria Hallelujah, Luckiest Guy, Londrina Outline.
Ground and ink from the measured palette (#D4D4D4, #B08C54, #764E28). Motion carries the page through
each loaf rolling in on its own full-screen colour. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — bread cut-out photography, personal photos

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: bread cut-out photography, personal photos

## Reference lock

Primary reference/direction: CRUMB Bakery — A small home bakery: a circular text loader 'Crumb Bakery', letters of CRUMB jumping, a loaf dropping onto a green wave, then each bread gets a full-screen colour chapter (Hulk spinach on green, rye on brown, white on tan, borsch beetroot on red, wholegrain, chocolate, baguette) with the loaf rolling in from the side over a repeated outline name and a price line, and a handwritten about with photos.
Preserve (3-5 traits): one loaf per colour chapter; loaf rolls in from the side; repeated outline name in the background; handwriting font for the about; price line per bread.
Borrow only (1-2): Give every product its own background colour and the same entrance
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: bread cut-out photography, personal photos
Reject: Handwriting font for body copy; Thin price lines
Token commitments: palette #D4D4D4, #B08C54, #764E28, #4E2E19; type Gloria Hallelujah, Luckiest Guy, Londrina Outline; engine GSAP + Lenis linked (never vendored).
