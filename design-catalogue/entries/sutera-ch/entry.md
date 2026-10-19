---
title: "Sutéra"
url: https://www.sutera.ch/
source_url: https://www.sutera.ch/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: inline-emoji-sticker-designer
dna: "Human-machine interaction designer x inline object stickers"
register: modern clean
grammar: chaptered editorial
lane: "A white portfolio whose sentences have small cut-out objects tucked between the words (a sparkle, a chain link, an eye, a sprout), surrounded by floating UI fragments, 3D rocks and hands, then a scattered cloud of project objects."
mode: persuade
traits: ["tiny cut-out objects inside sentences", "floating UI fragments and 3D objects", "large light sans statements", "scattered project-object cloud", "mono micro labels", "script logo"]
palette: ["#FFFFFF", "#7C7977", "#E9E9E8", "#C4BBB5", "#A0A1A2", "#3D3C39"]
type: ["NeueHaas", "PPNeueMontreal"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Sentences are illustrated inline: each key word sits next to a tiny object (a link for 'connect', an eye for 'work', a sprout for 'care'), so reading feels like a collage. Around them floats a cabinet of 3D objects and UI scraps that describe the practice.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Okey Studio).

## What to borrow (principle)

- Tuck small cut-out objects between words of a statement as inline illustration
- Show projects as a scattered cloud of their representative objects

## What to leave

- Busy margins with floating fragments
- Small mono labels

## Signature move

Small cut-out objects set between the words of each sentence.

## Motion

Intro: the script logo draws in with a loading line (~1.5 s). Scroll (Lenis, ~130 px glide, WebGL x5, SplitText): a mossy rock and UI fragments float in; statements set line by line with their inline objects popping in; lavender and hand objects drift; 'Some Project Examples' cloud of objects spreads; 'Lectures, Talks & Writing' list; contact with portrait.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x5 (three.js); split text; smoothed scroll (median 87 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a white portfolio whose sentences have small cut-out objects tucked between the words (a sparkle, a chain link, an eye, a sprout), surrounded by floating UI fragments, 3D rocks and hands, then a scattered cloud of project objects. Type: NeueHaas, PPNeueMontreal.
Ground and ink from the measured palette (#FFFFFF, #7C7977, #E9E9E8). Motion carries the page through
small cut-out objects set between the words of each sentence. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D cut-out objects (rocks, plants, devices) on white, UI fragments

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D cut-out objects (rocks, plants, devices) on white, UI fragments

## Reference lock

Primary reference/direction: Sutéra — A white portfolio whose sentences have small cut-out objects tucked between the words (a sparkle, a chain link, an eye, a sprout), surrounded by floating UI fragments, 3D rocks and hands, then a scattered cloud of project objects.
Preserve (3-5 traits): tiny cut-out objects inside sentences; floating UI fragments and 3D objects; large light sans statements; scattered project-object cloud; mono micro labels.
Borrow only (1-2): Tuck small cut-out objects between words of a statement as inline illustration; Show projects as a scattered cloud of their representative objects
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D cut-out objects (rocks, plants, devices) on white, UI fragments
Reject: Busy margins with floating fragments; Small mono labels
Token commitments: palette #FFFFFF, #7C7977, #E9E9E8, #C4BBB5, #A0A1A2, #3D3C39; type NeueHaas, PPNeueMontreal; engine GSAP + Lenis linked (never vendored).
