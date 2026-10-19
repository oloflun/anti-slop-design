---
title: "Ricky - AI joke companion"
url: https://www.whoisricky.lol/
source_url: https://www.whoisricky.lol/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "playful"
family: device-in-clouds-ai-gadget
dna: "AI gadget x a 3D device floating in clouds that plays videos"
register: cinematic dark
grammar: continuous world
lane: "A product page for a joke-telling AI device: a blue-black loader with jokey messages and a percent, a chrome device with a blue screen floating, 'Not just another boring AI companion', 'Made for ___' swapping words in a blue chip (compulsive buyers, overthinkers), '...made for those who aren't funny, but want to be' among stars, then the device in clouds playing video clips on its screen as steps (Turn ON your Ricky, Brief Ricky, Tell this joke), award stickers and a feature grid."
mode: persuade
traits: ["chrome 3D device with screen", "clouds and stars", "word chip swapping", "video on the device screen", "joke loader messages", "sticker badges"]
palette: ["#09101A", "#0B1777", "#354592"]
type: ["Spacegrotesk", "Spacemono", "Instrumentserif", "Open Sans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The device is the stage: every step plays on its screen while it turns in the clouds, so the product is always in view.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Play each step on the product's own screen as it rotates
- Swap the audience word in a chip

## What to leave

- Very dark blue text contrast

## Signature move

A chrome device floating in clouds with video clips on its screen.

## Motion

Intro: loader with jokes and percent (~5 s). Wheel (Lenis, 27 triggers): the device rotates in; the headline reveals; the chip scrambles to new words; clouds part; the screen plays clips as steps; the device turns sideways; stickers slap on.

Measured (`motion/probe.json`): GSAP 3.12.5; 27 ScrollTriggers; Lenis; WebGL canvas x3 (three.js); 1 video; smoothed scroll (median 119 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the continuous world grammar: a product page for a joke-telling AI device: a blue-black loader with jokey messages and a percent, a chrome device with a blue screen floating, 'Not just another boring AI companion', 'Made for ___' swapping words in a blue chip (compulsive buyers, overthinkers), '...made for those who aren't funny, but want to be' among stars, then the device in clouds playing video clips on its screen as steps (Turn ON your Ricky, Brief Ricky, Tell this joke), award stickers and a feature grid. Type: Spacegrotesk, Spacemono, Instrumentserif, Open Sans.
Ground and ink from the measured palette (#09101A, #0B1777, #354592). Motion carries the page through
a chrome device floating in clouds with video clips on its screen. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D device, video

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D device, video

## Reference lock

Primary reference/direction: Ricky - AI joke companion — A product page for a joke-telling AI device: a blue-black loader with jokey messages and a percent, a chrome device with a blue screen floating, 'Not just another boring AI companion', 'Made for ___' swapping words in a blue chip (compulsive buyers, overthinkers), '...made for those who aren't funny, but want to be' among stars, then the device in clouds playing video clips on its screen as steps (Turn ON your Ricky, Brief Ricky, Tell this joke), award stickers and a feature grid.
Preserve (3-5 traits): chrome 3D device with screen; clouds and stars; word chip swapping; video on the device screen; joke loader messages.
Borrow only (1-2): Play each step on the product's own screen as it rotates; Swap the audience word in a chip
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D device, video
Reject: Very dark blue text contrast
Token commitments: palette #09101A, #0B1777, #354592; type Spacegrotesk, Spacemono, Instrumentserif, Open Sans; engine GSAP + Lenis linked (never vendored).
