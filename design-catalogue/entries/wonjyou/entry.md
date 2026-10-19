---
title: "Won J You Studios - Design Coaching"
url: https://wonjyou.studio/
source_url: https://wonjyou.studio/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: giant-letter-mask-coach
dna: "Design coach x giant letters masking photos and campaign images"
register: cinematic dark
grammar: chaptered editorial
lane: "A coach and consultant: 'Educator Coach Mentor Consultant' in heavy red condensed type on black, a portrait sliding in, 'After years of designing solutions...', then giant letters 'MEET WON' acting as masks over campaign images and the portrait, a video intro, 'Over 20 years helping startups disrupt markets & Fortune 500s innovate at scale' with image cards, a brand list and a cream 'PROFESSOR' repeat."
mode: persuade
traits: ["heavy red condensed type", "giant letters as image masks", "black and white portrait", "video intro", "brand name list", "repeated outline word"]
palette: ["#050505", "#BE866D", "#312F2D"]
type: ["avantt"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Using 'MEET WON' as a window onto his work and face is a strong personal device that ties name and portfolio.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Spell the name in giant letters that mask the work

## What to leave

- Very long page
- Cookie bar at start

## Signature move

Giant letters 'MEET WON' revealing campaign images and a portrait.

## Motion

Intro: black with a cookie bar, the red titles stack in (~2 s). Wheel (Lenis ~130 px glide, 2 pins): the portrait slides; the paragraph fills; giant letters pin and the images inside them change; the portrait fills the screen; the stat headline stacks with cards popping in; the cream panel rises with the repeated word.

Measured (`motion/probe.json`): GSAP 3.13.0; 2 pinned sections; Lenis; 6 video; split text; smoothed scroll (median 130 px still travelling after input stops); entry gate: Decline. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a coach and consultant: 'Educator Coach Mentor Consultant' in heavy red condensed type on black, a portrait sliding in, 'After years of designing solutions...', then giant letters 'MEET WON' acting as masks over campaign images and the portrait, a video intro, 'Over 20 years helping startups disrupt markets & Fortune 500s innovate at scale' with image cards, a brand list and a cream 'PROFESSOR' repeat. Type: avantt.
Ground and ink from the measured palette (#050505, #BE866D, #312F2D). Motion carries the page through
giant letters 'MEET WON' revealing campaign images and a portrait. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — portrait, campaign imagery

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: portrait, campaign imagery

## Reference lock

Primary reference/direction: Won J You Studios - Design Coaching — A coach and consultant: 'Educator Coach Mentor Consultant' in heavy red condensed type on black, a portrait sliding in, 'After years of designing solutions...', then giant letters 'MEET WON' acting as masks over campaign images and the portrait, a video intro, 'Over 20 years helping startups disrupt markets & Fortune 500s innovate at scale' with image cards, a brand list and a cream 'PROFESSOR' repeat.
Preserve (3-5 traits): heavy red condensed type; giant letters as image masks; black and white portrait; video intro; brand name list.
Borrow only (1-2): Spell the name in giant letters that mask the work
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: portrait, campaign imagery
Reject: Very long page; Cookie bar at start
Token commitments: palette #050505, #BE866D, #312F2D; type avantt; engine GSAP + Lenis linked (never vendored).
