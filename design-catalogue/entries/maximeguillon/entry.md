---
title: "Maxime Guillon - Creative Developer"
url: https://maximeguillon.com/
source_url: https://maximeguillon.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: island-house-skills-tour
dna: "Creative developer x an island house you walk through to find skills on objects"
register: illustrated dark
grammar: continuous world
lane: "A 3D folio: a ship icon loader 'Land in sight', 'Maxime's world' with an island and a pink house, the camera walks up to the door, it opens, and you move through the rooms where each skill is printed on an object (React on a mug, Symfony and three.js on cups, Blender on a board, Python and HTML on bathroom bottles)."
mode: experience
traits: ["island with a house", "door opening into rooms", "skills on household objects", "warm pastel low-poly", "walk-through camera", "condensed italic labels"]
palette: ["#667B91", "#592019", "#8399A8", "#120604", "#853B34", "#AF845F"]
type: ["MedievalSharp"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Hiding the tech stack on everyday objects in a home makes a skill list a playful tour.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Put each skill on an object in a room the camera walks through

## What to leave

- Long walk for little content

## Signature move

A mug labelled REACT on a kitchen counter in a low-poly island house.

## Motion

Intro: a ship icon and 'Land in sight' (~2 s), the island. Wheel: the camera approaches the house; the door swings open; the camera moves room to room; skill labels pop beside objects.

Measured (`motion/probe.json`): GSAP 3.12.5; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the continuous world grammar: a 3D folio: a ship icon loader 'Land in sight', 'Maxime's world' with an island and a pink house, the camera walks up to the door, it opens, and you move through the rooms where each skill is printed on an object (React on a mug, Symfony and three.js on cups, Blender on a board, Python and HTML on bathroom bottles). Type: MedievalSharp.
Ground and ink from the measured palette (#667B91, #592019, #8399A8). Motion carries the page through
a mug labelled REACT on a kitchen counter in a low-poly island house. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D low-poly scene

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D low-poly scene

## Reference lock

Primary reference/direction: Maxime Guillon - Creative Developer — A 3D folio: a ship icon loader 'Land in sight', 'Maxime's world' with an island and a pink house, the camera walks up to the door, it opens, and you move through the rooms where each skill is printed on an object (React on a mug, Symfony and three.js on cups, Blender on a board, Python and HTML on bathroom bottles).
Preserve (3-5 traits): island with a house; door opening into rooms; skills on household objects; warm pastel low-poly; walk-through camera.
Borrow only (1-2): Put each skill on an object in a room the camera walks through
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D low-poly scene
Reject: Long walk for little content
Token commitments: palette #667B91, #592019, #8399A8, #120604, #853B34, #AF845F; type MedievalSharp; engine GSAP + Lenis linked (never vendored).
