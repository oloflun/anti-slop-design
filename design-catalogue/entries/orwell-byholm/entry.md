---
title: "What if George Orwell had a website"
url: https://orwell.byholm.co/
source_url: https://orwell.byholm.co/
captured: 2026-10-02
origin: raw-url
extract: none
category: editorial
category2: "playful"
family: red-propaganda-1984
dna: "1984 tribute x red propaganda poster"
register: cinematic dark
grammar: chaptered editorial
lane: "A tribute site that counts 19…84…100 on black, then turns blood red with a cut-out hand, speaker cones and the year 1984 arranged like a poster, newspaper clippings, a blindfolded face, and a 'THOUGHTCRIME DETECTED' close over walls of text."
mode: experience
traits: ["year count 19 → 84 → 100", "saturated red ground", "cut-out black-and-white collage", "condensed caps + EB Garamond", "newspaper clipping insert", "wall-of-text background"]
palette: ["#000000", "#D80202", "#E3E2E2", "#B05E5D", "#550001", "#8D1110"]
type: ["Bebas Neue", "EB Garamond"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The loader counts the title (19, 84) before reaching 100, so the number is the theme. After that the page is a propaganda poster in motion: one red, black-and-white cut-outs, condensed caps slogans. It ends on a joke that implicates the reader: 'THOUGHTCRIME DETECTED, this session has been recorded'.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A counter that spells the subject (19 → 84) before it reaches 100
- One saturated ground colour with black-and-white cut-out collage
- Close on a line that turns the reader into part of the story

## What to leave

- Wall-of-text sections are unreadable by design
- Long red stretches feel the same

## Signature move

A loader that counts 19, 84, then 100 before the red poster opens.

## Motion

Intro: 'what if George Orwell had a website' types in tiny serif on black, then 19 → 84 → 100 in condensed white then red (~2.5 s); the red poster scales in with the hand and speakers. Scroll (Lenis, DrawSVG, SplitText, WebGL x2): an eye mark watches as a quote sets in beside marching figures; newspaper page slides in; a blindfolded face draws; 'Who controls the past…' sets word by word; a black slab rotates over walls of text; 'THOUGHTCRIME DETECTED'.

Measured (`motion/probe.json`): GSAP 3.12.2; Lenis; WebGL canvas x2 (three.js); smoothed scroll (median 81 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a tribute site that counts 19…84…100 on black, then turns blood red with a cut-out hand, speaker cones and the year 1984 arranged like a poster, newspaper clippings, a blindfolded face, and a 'THOUGHTCRIME DETECTED' close over walls of text. Type: Bebas Neue, EB Garamond.
Ground and ink from the measured palette (#000000, #D80202, #E3E2E2). Motion carries the page through
a loader that counts 19, 84, then 100 before the red poster opens. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — black-and-white archival cut-outs on a single saturated red

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: black-and-white archival cut-outs on a single saturated red

## Reference lock

Primary reference/direction: What if George Orwell had a website — A tribute site that counts 19…84…100 on black, then turns blood red with a cut-out hand, speaker cones and the year 1984 arranged like a poster, newspaper clippings, a blindfolded face, and a 'THOUGHTCRIME DETECTED' close over walls of text.
Preserve (3-5 traits): year count 19 → 84 → 100; saturated red ground; cut-out black-and-white collage; condensed caps + EB Garamond; newspaper clipping insert.
Borrow only (1-2): A counter that spells the subject (19 → 84) before it reaches 100; One saturated ground colour with black-and-white cut-out collage
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: black-and-white archival cut-outs on a single saturated red
Reject: Wall-of-text sections are unreadable by design; Long red stretches feel the same
Token commitments: palette #000000, #D80202, #E3E2E2, #B05E5D, #550001, #8D1110; type Bebas Neue, EB Garamond; engine GSAP + Lenis linked (never vendored).
