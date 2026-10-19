---
title: "Harsh Dayal"
url: https://harshdayal.dev/
source_url: https://harshdayal.dev/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: black-hole-two-path-folio
dna: "AI engineer folio x black-hole WebGL"
register: cinematic dark
grammar: split stage
lane: "A dark folio that asks you to choose: the screen splits into 'Brief Read' with a cold blue disc and 'My Story' with a glowing red black hole, each an entry into a different length of the same CV."
mode: experience
traits: ["two-path split landing", "WebGL black hole with accretion glow", "pixel/terminal font (VT323) labels", "cold vs warm halves", "name fade-in intro"]
palette: ["#020203", "#44070B", "#7D6D65", "#261B1F"]
type: ["Geist", "VT323"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The page admits that visitors want different lengths and offers both up front, each half with its own light. The black hole on the 'story' side is the bigger, warmer image, which steers without forcing.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Harsh Dayal).

## What to borrow (principle)

- Offer two entry paths of different depth as the landing itself
- Give the two choices different temperature so the hierarchy is felt

## What to leave

- Nothing scrolls before a choice is made
- Small terminal-font labels are hard to read

## Signature move

A landing split between a cold short path and a glowing black-hole long path.

## Motion

Intro: 'HARSH DAYAL' fades from grey to white on near-black (~1.5 s), then the screen divides into the two panels and the black hole spins up on the right (WebGL, useGSAP). The wheel does not move the page; the accretion disc turns continuously.

Measured (`motion/probe.json`): GSAP 3.15.0; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the split stage grammar: a dark folio that asks you to choose: the screen splits into 'Brief Read' with a cold blue disc and 'My Story' with a glowing red black hole, each an entry into a different length of the same CV. Type: Geist, VT323.
Ground and ink from the measured palette (#020203, #44070B, #7D6D65). Motion carries the page through
a landing split between a cold short path and a glowing black-hole long path. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL space render, one warm and one cold field

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL space render, one warm and one cold field

## Reference lock

Primary reference/direction: Harsh Dayal — A dark folio that asks you to choose: the screen splits into 'Brief Read' with a cold blue disc and 'My Story' with a glowing red black hole, each an entry into a different length of the same CV.
Preserve (3-5 traits): two-path split landing; WebGL black hole with accretion glow; pixel/terminal font (VT323) labels; cold vs warm halves; name fade-in intro.
Borrow only (1-2): Offer two entry paths of different depth as the landing itself; Give the two choices different temperature so the hierarchy is felt
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL space render, one warm and one cold field
Reject: Nothing scrolls before a choice is made; Small terminal-font labels are hard to read
Token commitments: palette #020203, #44070B, #7D6D65, #261B1F; type Geist, VT323; engine GSAP + Lenis linked (never vendored).
