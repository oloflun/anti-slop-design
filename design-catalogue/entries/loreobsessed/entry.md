---
title: "Lore - fandom app"
url: https://loreobsessed.com/
source_url: https://loreobsessed.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "playful"
family: glowing-green-myth-token
dna: "Fandom platform x deep green mist, a glowing 3D 'Lore' wordmark that dissolves into sparks, a coin token that turns through a myth-like manifesto"
register: cinematic dark
grammar: filmic one-shot
lane: "A fandom app pre-launch: 'Loading...' with a sound prompt, a glowing green 3D 'Lore' logo in mist that burns away into sparks, 'Lore is going to fix it', then a single 3D coin token turning through green light shafts while a manifesto steps ('And something inside us awakened', 'It's in our DNA', 'This is what it means to be human'), the token carrying the founders' faces as their names appear, and a sign-up form ('Fandom at your fingertips')."
mode: experience
traits: ["glowing 3D wordmark", "wordmark burns into sparks", "one turning token as the thread", "myth-like manifesto lines", "green light shafts"]
palette: ["#0A1605", "#435F30", "#2B401C", "#63824C"]
type: ["ceraph", "oracle"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

One coin token carries the whole manifesto and then the founders, so the page has a single object to watch while reading.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase.

## What to borrow (principle)

- Let one object carry the text from line to line

## What to leave

- Sound prompt on load

## Signature move

A glowing green 'Lore' wordmark burning away into sparks.

## Motion

Intro: loader with sound prompt (~3 s). Wheel (WebGL): the logo dissolves; the token rotates and travels; lines fade in on either side; light shafts sweep.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; WebGL canvas x1 (three.js); smoothed scroll (median 69 px still travelling after input stops); entry gate: off. Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the filmic one-shot grammar: a fandom app pre-launch: 'Loading...' with a sound prompt, a glowing green 3D 'Lore' logo in mist that burns away into sparks, 'Lore is going to fix it', then a single 3D coin token turning through green light shafts while a manifesto steps ('And something inside us awakened', 'It's in our DNA', 'This is what it means to be human'), the token carrying the founders' faces as their names appear, and a sign-up form ('Fandom at your fingertips'). Type: ceraph, oracle.
Ground and ink from the measured palette (#0A1605, #435F30, #2B401C). Motion carries the page through
a glowing green 'Lore' wordmark burning away into sparks. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL 3D

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL 3D

## Reference lock

Primary reference/direction: Lore - fandom app — A fandom app pre-launch: 'Loading...' with a sound prompt, a glowing green 3D 'Lore' logo in mist that burns away into sparks, 'Lore is going to fix it', then a single 3D coin token turning through green light shafts while a manifesto steps ('And something inside us awakened', 'It's in our DNA', 'This is what it means to be human'), the token carrying the founders' faces as their names appear, and a sign-up form ('Fandom at your fingertips').
Preserve (3-5 traits): glowing 3D wordmark; wordmark burns into sparks; one turning token as the thread; myth-like manifesto lines; green light shafts.
Borrow only (1-2): Let one object carry the text from line to line
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL 3D
Reject: Sound prompt on load
Token commitments: palette #0A1605, #435F30, #2B401C, #63824C; type ceraph, oracle; engine GSAP + Lenis linked (never vendored).
