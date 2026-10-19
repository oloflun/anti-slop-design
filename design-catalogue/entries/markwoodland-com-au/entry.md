---
title: "Mark Woodland - Transforming industries"
url: https://markwoodland.com.au/
source_url: https://markwoodland.com.au/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: illustrated-impact-story-founder
dna: "Tech founder x painted illustration scenes for each venture"
register: illustrated dark
grammar: continuous world
lane: "A founder's personal site: a blue condensed 'LOADING 081' counter, the name in huge condensed caps over a portrait, a short belief statement, then a sequence of warm painted illustration scenes, one per venture (a mother and child outside a school for Xplor, a man with a moving box at a new home for a property venture, a family in a living room for Kismet), linked by a paper plane that flies between scenes."
mode: read
traits: ["condensed blue loader", "painted illustration per venture", "paper plane linking scenes", "warm sunset palette", "one-line impact statement per scene", "skip animation control"]
palette: ["#040E16", "#7D5C55", "#EEDBCE", "#C59585", "#1F3040"]
type: ["f37Judge", "PPNeueMontreal"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Turning each company into a human scene (who it helps) and linking them with a paper plane makes a founder bio into a story with one through-line.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Uncommon Studio).

## What to borrow (principle)

- Show each venture as the human moment it changes
- A small travelling object (paper plane) that links the scenes

## What to leave

- Small statement text over busy art
- Long loader

## Signature move

A paper plane flying between painted scenes of the people each venture helps.

## Motion

Intro: navy, condensed bars grow into 'LOADING' and a counter (~3 s). Wheel (Lenis): the name scales off; the bio slides; the first scene fades in and the statement types; a paper plane flies from the child's hand through a dissolve into the next scene; a cloud wipe leads into the living room scene.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; 11 video; split text. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the continuous world grammar: a founder's personal site: a blue condensed 'LOADING 081' counter, the name in huge condensed caps over a portrait, a short belief statement, then a sequence of warm painted illustration scenes, one per venture (a mother and child outside a school for Xplor, a man with a moving box at a new home for a property venture, a family in a living room for Kismet), linked by a paper plane that flies between scenes. Type: f37Judge, PPNeueMontreal.
Ground and ink from the measured palette (#040E16, #7D5C55, #EEDBCE). Motion carries the page through
a paper plane flying between painted scenes of the people each venture helps. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — painted illustration, portrait

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: painted illustration, portrait

## Reference lock

Primary reference/direction: Mark Woodland - Transforming industries — A founder's personal site: a blue condensed 'LOADING 081' counter, the name in huge condensed caps over a portrait, a short belief statement, then a sequence of warm painted illustration scenes, one per venture (a mother and child outside a school for Xplor, a man with a moving box at a new home for a property venture, a family in a living room for Kismet), linked by a paper plane that flies between scenes.
Preserve (3-5 traits): condensed blue loader; painted illustration per venture; paper plane linking scenes; warm sunset palette; one-line impact statement per scene.
Borrow only (1-2): Show each venture as the human moment it changes; A small travelling object (paper plane) that links the scenes
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: painted illustration, portrait
Reject: Small statement text over busy art; Long loader
Token commitments: palette #040E16, #7D5C55, #EEDBCE, #C59585, #1F3040; type f37Judge, PPNeueMontreal; engine GSAP + Lenis linked (never vendored).
