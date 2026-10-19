---
title: "Studio Direction - product design and brand"
url: https://studiodirection.com/
source_url: https://studiodirection.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: spotlight-reel-studio
dna: "Design studio x a spotlit figure reel with giant type cuts"
register: cinematic dark
grammar: filmic one-shot
lane: "A studio's home: 'Find the feels, make them transform.' over a dark stage with a pool of light and a figure, then a reel of their brand film (close-ups, a woman in a chair, a synth, a tennis player, figures on red) with giant words ('HARD', 'STARGAZER') cutting in."
mode: experience
traits: ["spotlight pool on dark stage", "brand film reel", "giant word cuts", "small player controls", "red and blue grading"]
palette: ["#010102", "#1E2E3B", "#76A9CC", "#111820", "#4C82A4"]
type: ["Suisseintl", "Suisseintlmono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The opening spotlight sets a cinematic tone; the reel does the rest.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A spotlight pool on an empty stage as the hero

## What to leave

- Nothing beyond the reel

## Signature move

A figure stepping into a pool of light on a dark stage.

## Motion

Intro: dark stage with the light pool (~2 s), the headline. Then the reel plays with word cuts.

Measured (`motion/probe.json`): GSAP 3.15.0; 23 ScrollTriggers; Lenis; 12 video; split text; entry gate: Play video. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the filmic one-shot grammar: a studio's home: 'Find the feels, make them transform.' over a dark stage with a pool of light and a figure, then a reel of their brand film (close-ups, a woman in a chair, a synth, a tennis player, figures on red) with giant words ('HARD', 'STARGAZER') cutting in. Type: Suisseintl, Suisseintlmono.
Ground and ink from the measured palette (#010102, #1E2E3B, #76A9CC). Motion carries the page through
a figure stepping into a pool of light on a dark stage. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — brand film

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: brand film

## Reference lock

Primary reference/direction: Studio Direction - product design and brand — A studio's home: 'Find the feels, make them transform.' over a dark stage with a pool of light and a figure, then a reel of their brand film (close-ups, a woman in a chair, a synth, a tennis player, figures on red) with giant words ('HARD', 'STARGAZER') cutting in.
Preserve (3-5 traits): spotlight pool on dark stage; brand film reel; giant word cuts; small player controls; red and blue grading.
Borrow only (1-2): A spotlight pool on an empty stage as the hero
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: brand film
Reject: Nothing beyond the reel
Token commitments: palette #010102, #1E2E3B, #76A9CC, #111820, #4C82A4; type Suisseintl, Suisseintlmono; engine GSAP + Lenis linked (never vendored).
