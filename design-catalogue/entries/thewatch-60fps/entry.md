---
title: "FS 60P - automatic watch by 60fps"
url: https://thewatch.60fps.fr/
source_url: https://thewatch.60fps.fr/
captured: 2026-10-03
origin: raw-url
extract: none
category: luxury-craft
category2: "product-focused"
family: silver-studio-watch-film
dna: "Watch launch x one 3D watch turned, exploded and orbited on a soft grey studio sweep, with a black interlude for the movement"
register: modern clean
grammar: filmic one-shot
lane: "A product film for one watch: a hairline circle loader on pale grey, '60mm automatic watch /' in thin and bold extended caps with the watch tumbling through the type, the watch upright with the name 'FS-60P' rising vertically past it, the case exploded into dial, movement and caseback along an axis, a drop to black where the movement floats in a ribbon of particles ('Mechanical heart', '23''), back to grey for close studies (elegant contours, slim profile, a bracelet filling the width), 'Silver steel' ghosted behind the watch, a spec sheet 'Model 146GR', and a closing line-up of four finishes."
mode: experience
traits: ["hairline circle loader", "extended caps, thin and bold mixed", "3D watch tumbling through the type", "exploded view along an axis", "black particle interlude for the movement", "macro crops filling the frame", "colourway line-up close"]
palette: ["#0A0A0A", "#A2A2A2", "#E9E9E9", "#CECECE", "#555454", "#B9B8B8"]
type: ["Nekst", "Inter"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The camera never leaves the object: every chapter is a new distance or angle on the same watch, so the page feels like handling it rather than reading about it.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: 60fps).

## What to borrow (principle)

- Keep one object and change only distance and angle per chapter
- Drop to black for the one technical chapter

## What to leave

- Tiny grey body copy on grey

## Signature move

The watch case exploding into dial, movement and caseback along one axis.

## Motion

Intro: hairline circle loader (~3 s). Wheel (Lenis, smoothed, no pins): the WebGL watch rotates and translates with scroll; type slides past it vertically; the explode is scrubbed; a cut to black with particles flowing around the movement; macro zooms; a ghost word scrubs behind; the line-up fades in.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; WebGL canvas x1 (three.js); split text; smoothed scroll (median 270 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the filmic one-shot grammar: a product film for one watch: a hairline circle loader on pale grey, '60mm automatic watch /' in thin and bold extended caps with the watch tumbling through the type, the watch upright with the name 'FS-60P' rising vertically past it, the case exploded into dial, movement and caseback along an axis, a drop to black where the movement floats in a ribbon of particles ('Mechanical heart', '23''), back to grey for close studies (elegant contours, slim profile, a bracelet filling the width), 'Silver steel' ghosted behind the watch, a spec sheet 'Model 146GR', and a closing line-up of four finishes. Type: Nekst, Inter.
Ground and ink from the measured palette (#0A0A0A, #A2A2A2, #E9E9E9). Motion carries the page through
the watch case exploding into dial, movement and caseback along one axis. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL product model, particles

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL product model, particles

## Reference lock

Primary reference/direction: FS 60P - automatic watch by 60fps — A product film for one watch: a hairline circle loader on pale grey, '60mm automatic watch /' in thin and bold extended caps with the watch tumbling through the type, the watch upright with the name 'FS-60P' rising vertically past it, the case exploded into dial, movement and caseback along an axis, a drop to black where the movement floats in a ribbon of particles ('Mechanical heart', '23''), back to grey for close studies (elegant contours, slim profile, a bracelet filling the width), 'Silver steel' ghosted behind the watch, a spec sheet 'Model 146GR', and a closing line-up of four finishes.
Preserve (3-5 traits): hairline circle loader; extended caps, thin and bold mixed; 3D watch tumbling through the type; exploded view along an axis; black particle interlude for the movement.
Borrow only (1-2): Keep one object and change only distance and angle per chapter; Drop to black for the one technical chapter
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL product model, particles
Reject: Tiny grey body copy on grey
Token commitments: palette #0A0A0A, #A2A2A2, #E9E9E9, #CECECE, #555454, #B9B8B8; type Nekst, Inter; engine GSAP + Lenis linked (never vendored).
