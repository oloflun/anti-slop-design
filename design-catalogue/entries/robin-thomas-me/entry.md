---
title: "Robin Thomas"
url: https://www.robin-thomas.me/
source_url: https://www.robin-thomas.me/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: ufo-lightbeam-dev-folio
dna: "French creative developer x UFO on a dark runway"
register: cinematic dark
grammar: filmic one-shot
lane: "A dark folio that loads 1% → 66% beside a small UFO icon, then hovers a camera over a dark runway with a light beam while a few lines of intro text scroll by, ending on huge 'Come v…' type as the UFO lands."
mode: experience
traits: ["percentage loader with UFO icon", "3D dark runway lit by one beam", "short intro lines that dissolve", "huge cropped closing words", "scroll progress bar bottom-left"]
palette: ["#0C0D0A", "#444545", "#272828", "#A39C7D"]
type: ["Sansita", "Mattone"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

A single 3D scene and a single light do all the atmosphere: the camera slides along a dark strip and the UFO waits; the copy is three short lines, then the scene holds, which makes the closing word huge by contrast.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One light beam in a dark 3D scene as the entire atmosphere
- Keep intro copy to three short lines that dissolve as the camera moves

## What to leave

- Long stretch of nearly identical dark frames
- Closing words cropped at the edge

## Signature move

A UFO waiting at the end of a dark runway lit by a single beam.

## Motion

Intro: 'WAIT' and 1% → 30% → 66% with a growing line to a UFO icon (~2.5 s), 'START'. Wheel (virtual, WebGL): 'Hi! I am Robin…' fades, 'Freelance or permanent job / Remote' fades, 'Scroll to continue'; camera slides along the runway; 'Come v…' huge type rises as the UFO lights.

Measured (`motion/probe.json`): GSAP 3.13.0; WebGL canvas x1 (three.js); split text; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: START. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the filmic one-shot grammar: a dark folio that loads 1% → 66% beside a small UFO icon, then hovers a camera over a dark runway with a light beam while a few lines of intro text scroll by, ending on huge 'Come v…' type as the UFO lands. Type: Sansita, Mattone.
Ground and ink from the measured palette (#0C0D0A, #444545, #272828). Motion carries the page through
a UFO waiting at the end of a dark runway lit by a single beam. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — dark 3D scene with one hard light

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: dark 3D scene with one hard light

## Reference lock

Primary reference/direction: Robin Thomas — A dark folio that loads 1% → 66% beside a small UFO icon, then hovers a camera over a dark runway with a light beam while a few lines of intro text scroll by, ending on huge 'Come v…' type as the UFO lands.
Preserve (3-5 traits): percentage loader with UFO icon; 3D dark runway lit by one beam; short intro lines that dissolve; huge cropped closing words; scroll progress bar bottom-left.
Borrow only (1-2): One light beam in a dark 3D scene as the entire atmosphere; Keep intro copy to three short lines that dissolve as the camera moves
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: dark 3D scene with one hard light
Reject: Long stretch of nearly identical dark frames; Closing words cropped at the edge
Token commitments: palette #0C0D0A, #444545, #272828, #A39C7D; type Sansita, Mattone; engine GSAP + Lenis linked (never vendored).
