---
title: "Project Aperture"
url: https://www.project-aperture.com/
source_url: https://www.project-aperture.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: strip-index-travel-photo
dna: "Travel photography archive x five vertical strips"
register: cinematic dark
grammar: gallery/catalog
lane: "A dark photography archive that opens as five narrow vertical photo strips with coloured underlines, black-and-white until one is selected, which tints it in its trip's colour."
mode: experience
traits: ["five vertical photo strips", "colour underline per trip", "black-and-white until active", "tiny chrome labels", "dark charcoal ground"]
palette: ["#231D21", "#797977", "#535353", "#B3B397", "#DADAD8"]
type: ["Cormorant Garamond", "Satoshi"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The index is five slivers of photographs, like aperture blades; only the active trip gets colour, so the archive is calm until you choose. Everything else is withheld.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Isaak De Coninck).

## What to borrow (principle)

- Show a set of trips as narrow strips, monochrome until active
- A colour key per collection (underline) that becomes the active tint

## What to leave

- Nothing scrolls on the index
- Strips are too narrow to judge photos

## Signature move

Five black-and-white photo strips where the active one takes its trip's colour.

## Motion

Intro: dark frame, the five strips rise in with coloured underlines (~1.5 s). Interaction (Lenis, WebGL): the active strip tints (olive), the rest stay monochrome; wheel did not move the index.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the gallery/catalog grammar: a dark photography archive that opens as five narrow vertical photo strips with coloured underlines, black-and-white until one is selected, which tints it in its trip's colour. Type: Cormorant Garamond, Satoshi.
Ground and ink from the measured palette (#231D21, #797977, #535353). Motion carries the page through
five black-and-white photo strips where the active one takes its trip's colour. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — travel photography, architecture and landscapes, shot in black and white

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: travel photography, architecture and landscapes, shot in black and white

## Reference lock

Primary reference/direction: Project Aperture — A dark photography archive that opens as five narrow vertical photo strips with coloured underlines, black-and-white until one is selected, which tints it in its trip's colour.
Preserve (3-5 traits): five vertical photo strips; colour underline per trip; black-and-white until active; tiny chrome labels; dark charcoal ground.
Borrow only (1-2): Show a set of trips as narrow strips, monochrome until active; A colour key per collection (underline) that becomes the active tint
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: travel photography, architecture and landscapes, shot in black and white
Reject: Nothing scrolls on the index; Strips are too narrow to judge photos
Token commitments: palette #231D21, #797977, #535353, #B3B397, #DADAD8; type Cormorant Garamond, Satoshi; engine GSAP + Lenis linked (never vendored).
