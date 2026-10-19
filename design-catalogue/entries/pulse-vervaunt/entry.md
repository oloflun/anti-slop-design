---
title: "Pulse eCommerce Summit '26"
url: http://pulse.vervaunt.com/
source_url: http://pulse.vervaunt.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "editorial"
family: event-summit-green-black
dna: "eCommerce conference x neon green on black with a tilted ticket marquee"
register: cinematic dark
grammar: chaptered editorial
lane: "A conference site: the 'pulse.' logo glowing green on black, a statement, a white panel 'Hear from the most impressive brands', a collage of fashion brand imagery, venue video, a green stats panel with a tilted 'get your tickets now' marquee, speakers grid, special guests, sponsors, a repeated pulse logo poster, the app and an FAQ."
mode: persuade
traits: ["neon green on near-black", "tilted ticket marquee", "fashion brand collage", "green stats panel", "repeated logo poster", "speaker logo grid"]
palette: ["#000000", "#02EA41", "#FDFBFB", "#A2C09B", "#544A42"]
type: ["Syne"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The green panel with the tilted marquee is the call to action that recurs, and the brand collage sells the calibre of speakers fast.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A tilted marquee as the recurring ticket CTA

## What to leave

- Generic sponsor and FAQ blocks
- Long page

## Signature move

A tilted 'get your tickets now' marquee across a neon green stats panel.

## Motion

Intro: black, the logo fades from grey to green (~1.5 s). Wheel (ScrollSmoother, 8 pins): the white panel slides up; the brand collage assembles in layers; the venue video rises; the green panel floods in and the marquee slides at a tilt; speaker tiles stagger; the repeated logo poster scrolls; the app phone rotates in.

Measured (`motion/probe.json`): GSAP 3.13.0; 8 pinned sections; ScrollSmoother; 2 video; split text. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a conference site: the 'pulse.' logo glowing green on black, a statement, a white panel 'Hear from the most impressive brands', a collage of fashion brand imagery, venue video, a green stats panel with a tilted 'get your tickets now' marquee, speakers grid, special guests, sponsors, a repeated pulse logo poster, the app and an FAQ. Type: Syne.
Ground and ink from the measured palette (#000000, #02EA41, #FDFBFB). Motion carries the page through
a tilted 'get your tickets now' marquee across a neon green stats panel. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — fashion campaign photography, event photos

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: fashion campaign photography, event photos

## Reference lock

Primary reference/direction: Pulse eCommerce Summit '26 — A conference site: the 'pulse.' logo glowing green on black, a statement, a white panel 'Hear from the most impressive brands', a collage of fashion brand imagery, venue video, a green stats panel with a tilted 'get your tickets now' marquee, speakers grid, special guests, sponsors, a repeated pulse logo poster, the app and an FAQ.
Preserve (3-5 traits): neon green on near-black; tilted ticket marquee; fashion brand collage; green stats panel; repeated logo poster.
Borrow only (1-2): A tilted marquee as the recurring ticket CTA
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: fashion campaign photography, event photos
Reject: Generic sponsor and FAQ blocks; Long page
Token commitments: palette #000000, #02EA41, #FDFBFB, #A2C09B, #544A42; type Syne; engine GSAP + Lenis linked (never vendored).
