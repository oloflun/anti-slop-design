---
title: "Joseph Santamaria"
url: https://joseph-san.com/
source_url: https://joseph-san.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: underwater-glitch-3d-folio
dna: "Creative software engineer x underwater teal glitch world"
register: illustrated dark
grammar: continuous world
lane: "A dark-teal folio that loads a 3D experience, offers 'dive into the experience' or 'enter without audio', then sinks through a glitching underwater world of drifting blocks and a diver figure while short lines set in, ending with projects as floating objects."
mode: experience
traits: ["teal underwater 3D world", "glitch/streak transitions", "diver figure", "floating monolith blocks", "two-tone grey-white headline lines", "sound gate"]
palette: ["#07171B", "#18464C"]
type: ["PPNeueMontreal", "ModernEraMono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The camera 'dives': each scroll beat sinks deeper through teal water, with glitch streaks smearing the frame between depths. Projects appear as objects floating past, so the folio is a descent rather than a list.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Joseph Santamaria).

## What to borrow (principle)

- Frame the scroll as a descent (diving) with depth cues
- Glitch streaks as the transition between depths

## What to leave

- Gate before content
- Long glitch frames where nothing is legible

## Signature move

A dive through a teal underwater world past a lone diver and floating blocks.

## Motion

Gate: 'loading 3D experience' bar, 'dive into the experience' / 'enter without audio' (~3 s). Scroll (virtual, WebGL): particles rise; 'Architect of immersive dimensions' line sets in; glitch streaks; 'Creative Software Engineer' line with blocks and a diver; project objects (Bright AI, The Good News) float up.

Measured (`motion/probe.json`): GSAP 3.13.0; WebGL canvas x1 (three.js); split text; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: ENTER WITHOUT AUDIO. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the continuous world grammar: a dark-teal folio that loads a 3D experience, offers 'dive into the experience' or 'enter without audio', then sinks through a glitching underwater world of drifting blocks and a diver figure while short lines set in, ending with projects as floating objects. Type: PPNeueMontreal, ModernEraMono.
Ground and ink from the measured palette (#07171B, #18464C). Motion carries the page through
a dive through a teal underwater world past a lone diver and floating blocks. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D underwater scenes, teal haze, glitch textures

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D underwater scenes, teal haze, glitch textures

## Reference lock

Primary reference/direction: Joseph Santamaria — A dark-teal folio that loads a 3D experience, offers 'dive into the experience' or 'enter without audio', then sinks through a glitching underwater world of drifting blocks and a diver figure while short lines set in, ending with projects as floating objects.
Preserve (3-5 traits): teal underwater 3D world; glitch/streak transitions; diver figure; floating monolith blocks; two-tone grey-white headline lines.
Borrow only (1-2): Frame the scroll as a descent (diving) with depth cues; Glitch streaks as the transition between depths
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D underwater scenes, teal haze, glitch textures
Reject: Gate before content; Long glitch frames where nothing is legible
Token commitments: palette #07171B, #18464C; type PPNeueMontreal, ModernEraMono; engine GSAP + Lenis linked (never vendored).
