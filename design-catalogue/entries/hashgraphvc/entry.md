---
title: "Hashgraph Ventures - venture capital"
url: https://hashgraphvc.com/
source_url: https://hashgraphvc.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: institutional
category2: "portfolio"
family: deep-ocean-webgl-crystal
dna: "Venture fund x a glowing crystal hovering over a night ocean that dives through the surface and breaks into a particle stream"
register: cinematic dark
grammar: continuous world
lane: "A fund's site as one dive: a sound gate, the wordmark assembling letter by letter on black, a night ocean fading up with a lit crystal hovering above the swell, 'The next wave of venture capital' decoding at the foot, a diagonal wipe that cuts below the surface into a glowing crater where the crystal shatters into a column of particles, 'Capital with conviction' beside it, another diagonal cut deeper, and the particles forming a drifting figure among dark shards with 'Early access, permanent advantage' and a short manifesto."
mode: experience
traits: ["sound gate", "letter-by-letter wordmark", "WebGL night ocean", "floating lit crystal", "diagonal wipe cuts between depths", "crystal shattering into particles", "decoding headlines"]
palette: ["#010208", "#282B32", "#66676B"]
type: ["HashgraphWeb", "NeueMontrealWeb", "ParaboleWeb"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Each chapter is a step deeper under the same water, so the fund's thesis (get in early, go deep) is built into the camera path, not stated.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Glenn Catteeuw, Kurt Drubbel, Paul-Guilhem Repaux, Rogier de Boevé, Romain Rope, Thomas Aufresne).

## What to borrow (principle)

- Cut between chapters with a diagonal wipe that goes one layer deeper
- Let the hero object break apart into the next chapter's material

## What to leave

- Small body copy over busy WebGL

## Signature move

A lit crystal hovering above a night ocean, then shattering into a particle column under the surface.

## Motion

Intro: gate, wordmark letters scramble in (~2 s), ocean fades up. Wheel (Lenis, no pins): the camera holds on the crystal while the headline decodes; a diagonal clip-path wipe drops below the surface; the crystal fractures into particles; a second diagonal cut; headlines decode per chapter.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; WebGL canvas x1 (three.js); split text; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: ENTER WITHOUT AUDIO. Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the continuous world grammar: a fund's site as one dive: a sound gate, the wordmark assembling letter by letter on black, a night ocean fading up with a lit crystal hovering above the swell, 'The next wave of venture capital' decoding at the foot, a diagonal wipe that cuts below the surface into a glowing crater where the crystal shatters into a column of particles, 'Capital with conviction' beside it, another diagonal cut deeper, and the particles forming a drifting figure among dark shards with 'Early access, permanent advantage' and a short manifesto. Type: HashgraphWeb, NeueMontrealWeb, ParaboleWeb.
Ground and ink from the measured palette (#010208, #282B32, #66676B). Motion carries the page through
a lit crystal hovering above a night ocean, then shattering into a particle column under the surface. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL ocean, particles, 3D crystal

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL ocean, particles, 3D crystal

## Reference lock

Primary reference/direction: Hashgraph Ventures - venture capital — A fund's site as one dive: a sound gate, the wordmark assembling letter by letter on black, a night ocean fading up with a lit crystal hovering above the swell, 'The next wave of venture capital' decoding at the foot, a diagonal wipe that cuts below the surface into a glowing crater where the crystal shatters into a column of particles, 'Capital with conviction' beside it, another diagonal cut deeper, and the particles forming a drifting figure among dark shards with 'Early access, permanent advantage' and a short manifesto.
Preserve (3-5 traits): sound gate; letter-by-letter wordmark; WebGL night ocean; floating lit crystal; diagonal wipe cuts between depths.
Borrow only (1-2): Cut between chapters with a diagonal wipe that goes one layer deeper; Let the hero object break apart into the next chapter's material
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL ocean, particles, 3D crystal
Reject: Small body copy over busy WebGL
Token commitments: palette #010208, #282B32, #66676B; type HashgraphWeb, NeueMontrealWeb, ParaboleWeb; engine GSAP + Lenis linked (never vendored).
