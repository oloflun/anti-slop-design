---
title: "Pocket Island"
url: https://pocket-island.webflow.io/
source_url: https://pocket-island.webflow.io/
captured: 2026-10-02
origin: raw-url
extract: none
category: playful
category2: "product-focused"
family: draggable-toy-island
dna: "Webflow showcase toy x draggable illustrated volcano island"
register: illustrated dark
grammar: live surface
lane: "A single-screen toy: a flat illustrated volcano island with palms and birds floats on pale sea inside a rounded frame, with speed and day/night dials and a credits panel at left; you drag the island and it swings with inertia."
mode: experience
traits: ["one draggable illustrated object", "speed and day/night dials", "Draggable with inertia", "soft cream and sea-green palette", "clone-it button", "birds and smoke idle loop"]
palette: ["#DDE6E3", "#99A88E"]
type: ["Satoshi", "Space Grotesk"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The whole site is one object with physics; the dials invite play and the inertia makes the island feel weighty, which is all a template showcase needs to sell its interactions.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Pierre Louis Labonne).

## What to borrow (principle)

- One object you can drag with inertia as the whole hero
- Dials that change the scene state

## What to leave

- No scroll content at all
- Tiny panel text

## Signature move

A little volcano island you can fling around a pale sea.

## Motion

Intro: cream screen, a palm icon loader with a bar, the panel and island fade in (~1.5 s). No scroll: the island bobs, birds circle, the volcano smokes; drag throws it with inertia and it settles back.

Measured (`motion/probe.json`): GSAP 3.15.0; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the live surface grammar: a single-screen toy: a flat illustrated volcano island with palms and birds floats on pale sea inside a rounded frame, with speed and day/night dials and a credits panel at left; you drag the island and it swings with inertia. Type: Satoshi, Space Grotesk.
Ground and ink from the measured palette (#DDE6E3, #99A88E). Motion carries the page through
a little volcano island you can fling around a pale sea. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — flat vector illustration

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: flat vector illustration

## Reference lock

Primary reference/direction: Pocket Island — A single-screen toy: a flat illustrated volcano island with palms and birds floats on pale sea inside a rounded frame, with speed and day/night dials and a credits panel at left; you drag the island and it swings with inertia.
Preserve (3-5 traits): one draggable illustrated object; speed and day/night dials; Draggable with inertia; soft cream and sea-green palette; clone-it button.
Borrow only (1-2): One object you can drag with inertia as the whole hero; Dials that change the scene state
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: flat vector illustration
Reject: No scroll content at all; Tiny panel text
Token commitments: palette #DDE6E3, #99A88E; type Satoshi, Space Grotesk; engine GSAP + Lenis linked (never vendored).
