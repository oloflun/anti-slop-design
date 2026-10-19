---
title: "DICH Fashion - futuristic fashion"
url: https://dich-fashion.webflow.io/
source_url: https://dich-fashion.webflow.io/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "playful"
family: futuristic-fashion-alien-type
dna: "Futuristic fashion concept x alien display type, a 3D rock and pastel chapters"
register: other
grammar: chaptered editorial
lane: "A fashion concept site: a circular gradient loader with percent and HUD lines, 'Dich future new era' in an alien display face sliced over a figure in pink clouds, a peach 'Organic' section with a circle portrait, a lilac 'Our mission' with a rotating 3D rock and orbit lines numbered .001/.002/.003, a pink 'Drop' with circular portraits, a dark runway of models and 'Into the future'."
mode: experience
traits: ["alien custom display face", "3D rotating rock with orbits", "pastel chapter grounds", "circle portraits", "HUD frame lines", "numbered values"]
palette: ["#FEDFC3", "#CFB8FE", "#131213", "#A894AA", "#DD978A", "#A46560"]
type: ["Fkrastergrotesktrial Rounded", "Nbarchitektstd", "Spacegrotesk", "T 012"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The alien typeface and pastel chapters give a concept brand a complete world; the rock is the recurring object of the mission section.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A custom display face as the whole brand voice
- One 3D object carrying a numbered values section

## What to leave

- Type hard to read

## Signature move

A rotating 3D rock with orbit lines on lilac under alien type.

## Motion

Intro: black HUD with a gradient ring filling to 100% (~3 s), the title slices in. Wheel (111 triggers): clouds roll; panels change colour; the rock rotates as the values tick .001 to .003; portraits slide in circles; the runway pans.

Measured (`motion/probe.json`): GSAP 3.13.0; 111 ScrollTriggers; Lenis; WebGL canvas x2 (three.js); split text; smoothed scroll (median 83 px still travelling after input stops); entry gate: DISCOVER. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a fashion concept site: a circular gradient loader with percent and HUD lines, 'Dich future new era' in an alien display face sliced over a figure in pink clouds, a peach 'Organic' section with a circle portrait, a lilac 'Our mission' with a rotating 3D rock and orbit lines numbered .001/.002/.003, a pink 'Drop' with circular portraits, a dark runway of models and 'Into the future'. Type: Fkrastergrotesktrial Rounded, Nbarchitektstd, Spacegrotesk, T 012.
Ground and ink from the measured palette (#FEDFC3, #CFB8FE, #131213). Motion carries the page through
a rotating 3D rock with orbit lines on lilac under alien type. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — AI fashion imagery, 3D rock

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: AI fashion imagery, 3D rock

## Reference lock

Primary reference/direction: DICH Fashion - futuristic fashion — A fashion concept site: a circular gradient loader with percent and HUD lines, 'Dich future new era' in an alien display face sliced over a figure in pink clouds, a peach 'Organic' section with a circle portrait, a lilac 'Our mission' with a rotating 3D rock and orbit lines numbered .001/.002/.003, a pink 'Drop' with circular portraits, a dark runway of models and 'Into the future'.
Preserve (3-5 traits): alien custom display face; 3D rotating rock with orbits; pastel chapter grounds; circle portraits; HUD frame lines.
Borrow only (1-2): A custom display face as the whole brand voice; One 3D object carrying a numbered values section
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: AI fashion imagery, 3D rock
Reject: Type hard to read
Token commitments: palette #FEDFC3, #CFB8FE, #131213, #A894AA, #DD978A, #A46560; type Fkrastergrotesktrial Rounded, Nbarchitektstd, Spacegrotesk, T 012; engine GSAP + Lenis linked (never vendored).
