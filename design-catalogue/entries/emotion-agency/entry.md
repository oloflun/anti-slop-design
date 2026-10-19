---
title: "Emotion Agency"
url: https://emotion-agency.com/
source_url: https://emotion-agency.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: violet-particle-landscape-agency
dna: "Interface agency x WebGL particle landscape"
register: illustrated dark
grammar: continuous world
lane: "A violet WebGL landscape of rocks and still water where a particle swirl grows into a glowing cloud as you scroll, while serif-and-caps statements change underneath."
mode: experience
traits: ["WebGL landscape scene", "particle swirl that morphs and grows", "italic serif word plus light caps statements", "audio entry gate", "mono label chips", "single violet hue"]
palette: ["#F4EFFE", "#D5CCE4", "#BCB1CD"]
type: ["IBM Plex Mono", "PP Neue Montreal", "Emotion Serif"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The page commits to one world (violet light, rocks, water) and lets one object, a particle form, change with the reader: a swirl, then a cube of particles, then a cloud that fills the sky. Statements are set in a light condensed caps face with one italic serif word, and they swap at each stage, so the object and the copy move together.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Emotion Agency).

## What to borrow (principle)

- One particle object that morphs per section as the thread through a scene
- Statements that swap with a glitch/scramble while the scene keeps continuity
- A single hue for the whole world so the motion carries all the contrast

## What to leave

- Audio gate and a long blank loader before anything appears
- Statements are thin and small against a busy particle field

## Signature move

A particle swirl that becomes a cube and then a glowing cloud over a violet lake as you scroll.

## Motion

Gate: 'Enter with audio' after a pale loader with a progress line (~3 s). Scroll (virtual, Lenis, WebGL/three.js): camera holds on the lake; particle swirl rotates; 'Where AMBITIOUS IDEAS BECOME INTERFACES PEOPLE REMEMBER' glitches out; particles reform as a cube beside 'We BUILD MORE THAN WEBSITES AND PRODUCTS'; the cloud grows over the rocks for 'TECHNOLOGY AS EMOTION'. MorphSVG on small marks, SplitText on statements.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; WebGL canvas x1 (three.js); 2 video; split text; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Enter with audio Enter with audio. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the continuous world grammar: a violet WebGL landscape of rocks and still water where a particle swirl grows into a glowing cloud as you scroll, while serif-and-caps statements change underneath. Type: IBM Plex Mono, PP Neue Montreal, Emotion Serif.
Ground and ink from the measured palette (#F4EFFE, #D5CCE4, #BCB1CD). Motion carries the page through
a particle swirl that becomes a cube and then a glowing cloud over a violet lake as you scroll. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D landscape in one hue, soft fog, particle forms

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D landscape in one hue, soft fog, particle forms

## Reference lock

Primary reference/direction: Emotion Agency — A violet WebGL landscape of rocks and still water where a particle swirl grows into a glowing cloud as you scroll, while serif-and-caps statements change underneath.
Preserve (3-5 traits): WebGL landscape scene; particle swirl that morphs and grows; italic serif word plus light caps statements; audio entry gate; mono label chips.
Borrow only (1-2): One particle object that morphs per section as the thread through a scene; Statements that swap with a glitch/scramble while the scene keeps continuity
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D landscape in one hue, soft fog, particle forms
Reject: Audio gate and a long blank loader before anything appears; Statements are thin and small against a busy particle field
Token commitments: palette #F4EFFE, #D5CCE4, #BCB1CD; type IBM Plex Mono, PP Neue Montreal, Emotion Serif; engine GSAP + Lenis linked (never vendored).
