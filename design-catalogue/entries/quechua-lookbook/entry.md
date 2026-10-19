---
title: "Quechua SS25 Lookbook"
url: https://quechua-lookbook.com/ss25/
source_url: https://quechua-lookbook.com/ss25/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: ""
family: outdoor-lookbook-film
dna: "Outdoor clothing lookbook x a photo stack loader and a hiking film"
register: warm photographic
grammar: filmic one-shot
lane: "A clothing lookbook: a stack of photos riffling with handwritten notes on cream, 'Feel alive in every footstep' over hikers on a mountain, and a full film of the collection in the Pyrenees (rocks, faces, hikers on ridges, mist) with a small play control."
mode: experience
traits: ["riffling photo stack loader", "handwritten notes", "full-bleed hiking film", "white serif headline", "small film controls", "cookie panel"]
palette: ["#8ABAC2", "#111513", "#2B342E", "#4B5144", "#FDFCFB", "#7E8E8F"]
type: ["Decathlon-Brand", "Decathlon-Display", "Decathlon-Text", "Casey"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The riffling stack is a nice analogue loader; the rest is the film.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Riffle a stack of photos as the loader

## What to leave

- Capture fell into the full film; cookie panel over frames

## Signature move

A stack of hiking photos riffling with handwritten notes.

## Motion

Intro: cream, photos riffle in a stack with scribbled arrows (~2 s), the hero film. Then the full film plays.

Measured (`motion/probe.json`): GSAP 3.12.2; Lenis; Taxi page transitions; 8 video; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Discover full video. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the filmic one-shot grammar: a clothing lookbook: a stack of photos riffling with handwritten notes on cream, 'Feel alive in every footstep' over hikers on a mountain, and a full film of the collection in the Pyrenees (rocks, faces, hikers on ridges, mist) with a small play control. Type: Decathlon-Brand, Decathlon-Display, Decathlon-Text, Casey.
Ground and ink from the measured palette (#8ABAC2, #111513, #2B342E). Motion carries the page through
a stack of hiking photos riffling with handwritten notes. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — outdoor film

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: outdoor film

## Reference lock

Primary reference/direction: Quechua SS25 Lookbook — A clothing lookbook: a stack of photos riffling with handwritten notes on cream, 'Feel alive in every footstep' over hikers on a mountain, and a full film of the collection in the Pyrenees (rocks, faces, hikers on ridges, mist) with a small play control.
Preserve (3-5 traits): riffling photo stack loader; handwritten notes; full-bleed hiking film; white serif headline; small film controls.
Borrow only (1-2): Riffle a stack of photos as the loader
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: outdoor film
Reject: Capture fell into the full film; cookie panel over frames
Token commitments: palette #8ABAC2, #111513, #2B342E, #4B5144, #FDFCFB, #7E8E8F; type Decathlon-Brand, Decathlon-Display, Decathlon-Text, Casey; engine GSAP + Lenis linked (never vendored).
