---
title: "Daoism Systems"
url: https://daoism.systems/
source_url: https://daoism.systems/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: "portfolio"
family: signal-grid-loader-gate
dna: "Web3/AI engineering studio x red signal-grid terminal"
register: cinematic dark
grammar: filmic one-shot
lane: "A black engineering-studio page whose loader is a red signal grid raining down a dark screen with terse status lines ('please stand by', 'creating the scene'), ending at a circular HUD gate offering 'enter with sound' or 'enter in silence'."
mode: experience
traits: ["red dotted signal grid loader", "status-line copy during load", "circular HUD frame with crosshairs", "sound / silence gate", "mono type (IBM Plex Mono)"]
palette: ["#030303", "#201717"]
type: ["IBM Plex Mono", "KH Interference TRIAL"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The wait is staged as a machine booting: a progress tag in the corner, a grid of red signal dots sweeping down, and status lines that narrate the build. The gate is drawn as a HUD reticle, so even the choice screen belongs to the same instrument panel.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Lynksen).

## What to borrow (principle)

- Narrate a long load with short status lines instead of a bare percentage
- Draw the entry gate as part of the interface world (reticle, crosshairs)

## What to leave

- Captured only to the gate; the scene behind it was not reached
- Very long load before any content

## Signature move

A red signal grid raining down a black screen while status lines narrate the scene being built.

## Motion

Intro: tiny status text and a loading tag, then a red dot grid sweeps down from the top over ~3 s with 'please stand by' → 'creating the scene'; a circular HUD frame draws in with 'ENTER WITH SOUND / ENTER IN SILENCE'. Beyond the gate: a three.js scene with SplitText (not captured).

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; split text; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Sound off, Start, Enter with sound. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the filmic one-shot grammar: a black engineering-studio page whose loader is a red signal grid raining down a dark screen with terse status lines ('please stand by', 'creating the scene'), ending at a circular HUD gate offering 'enter with sound' or 'enter in silence'. Type: IBM Plex Mono, KH Interference TRIAL.
Ground and ink from the measured palette (#030303, #201717). Motion carries the page through
a red signal grid raining down a black screen while status lines narrate the scene being built. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — generative signal/data graphics in one red on black

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: generative signal/data graphics in one red on black

## Reference lock

Primary reference/direction: Daoism Systems — A black engineering-studio page whose loader is a red signal grid raining down a dark screen with terse status lines ('please stand by', 'creating the scene'), ending at a circular HUD gate offering 'enter with sound' or 'enter in silence'.
Preserve (3-5 traits): red dotted signal grid loader; status-line copy during load; circular HUD frame with crosshairs; sound / silence gate; mono type (IBM Plex Mono).
Borrow only (1-2): Narrate a long load with short status lines instead of a bare percentage; Draw the entry gate as part of the interface world (reticle, crosshairs)
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: generative signal/data graphics in one red on black
Reject: Captured only to the gate; the scene behind it was not reached; Very long load before any content
Token commitments: palette #030303, #201717; type IBM Plex Mono, KH Interference TRIAL; engine GSAP + Lenis linked (never vendored).
