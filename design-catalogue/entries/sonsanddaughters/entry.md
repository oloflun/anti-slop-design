---
title: "Sons and Daughters - Chinese-Canadian cafes"
url: https://sonsanddaughters.xyz/
source_url: https://sonsanddaughters.xyz/
captured: 2026-10-02
origin: raw-url
extract: none
category: editorial
category2: "institutional"
family: documentary-cafe-story
dna: "Documentary project x small-town cafe photographs and a 'GENERATIONS' title"
register: editorial print
grammar: chaptered editorial
lane: "A documentary about Chinese-Canadian cafes: 'SONS & DAUGHTERS' in heavy grotesk on cream with a small cafe door photo, 'Every town across Canada has a Chinese-Canadian cafe. Each has its own story.', a full photo of the Oxbow Restaurant, a list of dishes in serif, 'The Oxbow Cafe' with population, and 'GENERATIONS' with four portraits of the family."
mode: read
traits: ["heavy grotesk title", "cream ground", "documentary photography", "serif menu lines", "population data line", "family portraits row"]
palette: ["#ECE8DC", "#392F27", "#A2A39F", "#BFB8AD", "#74746E"]
type: ["Roboto", "new-spirit", "Founders Grotesk"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Plain editorial typography and real photographs let the stories carry the site; the door photo growing into the cafe is a quiet entrance.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Grow a small photo into the full scene as the entrance

## What to leave

- Short page captured

## Signature move

A small cafe door photo that grows into the Oxbow Restaurant.

## Motion

Intro: dark with a small icon (~2 s), the title page. Wheel: the door photo grows to the full cafe; dishes list fades in line by line; the section title rises; family portraits slide in above 'GENERATIONS'.

Measured (`motion/probe.json`): GSAP 3.12.4; Lenis; Taxi page transitions; smoothed scroll (median 415 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a documentary about Chinese-Canadian cafes: 'SONS & DAUGHTERS' in heavy grotesk on cream with a small cafe door photo, 'Every town across Canada has a Chinese-Canadian cafe. Each has its own story.', a full photo of the Oxbow Restaurant, a list of dishes in serif, 'The Oxbow Cafe' with population, and 'GENERATIONS' with four portraits of the family. Type: Roboto, new-spirit, Founders Grotesk.
Ground and ink from the measured palette (#ECE8DC, #392F27, #A2A39F). Motion carries the page through
a small cafe door photo that grows into the Oxbow Restaurant. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — documentary photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: documentary photography

## Reference lock

Primary reference/direction: Sons and Daughters - Chinese-Canadian cafes — A documentary about Chinese-Canadian cafes: 'SONS & DAUGHTERS' in heavy grotesk on cream with a small cafe door photo, 'Every town across Canada has a Chinese-Canadian cafe. Each has its own story.', a full photo of the Oxbow Restaurant, a list of dishes in serif, 'The Oxbow Cafe' with population, and 'GENERATIONS' with four portraits of the family.
Preserve (3-5 traits): heavy grotesk title; cream ground; documentary photography; serif menu lines; population data line.
Borrow only (1-2): Grow a small photo into the full scene as the entrance
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: documentary photography
Reject: Short page captured
Token commitments: palette #ECE8DC, #392F27, #A2A39F, #BFB8AD, #74746E; type Roboto, new-spirit, Founders Grotesk; engine GSAP + Lenis linked (never vendored).
