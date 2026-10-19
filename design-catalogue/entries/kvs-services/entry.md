---
title: "KVS Studio"
url: https://www.kvs.services/
source_url: https://www.kvs.services/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: crt-blackletter-slide-gate
dna: "Product design studio x CRT screen and dot-matrix blackletter"
register: modern clean
grammar: filmic one-shot
lane: "A studio site framed as a rounded CRT screen: a percentage loader, then a horned dot-matrix blackletter logo dripping ink at the bottom, with an orange 'slide to enter' bar and 'headphones recommended'."
mode: experience
traits: ["rounded CRT screen frame on black", "dot-matrix blackletter logo", "ink drips below the logo", "slide-to-enter gate", "hazard tape corner"]
palette: ["#E0E0DF", "#000002", "#938580"]
type: ["SF Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The entry is a physical gesture (slide to enter) on a screen object, and the logo is a metal-band blackletter rendered in dots and dripping, a deliberately loud identity for a product studio.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A slide gesture as the gate when the site is an experience
- A screen-object frame (CRT) around the whole site

## What to leave

- Captured only the gate; the slide gesture was not performed
- Nothing readable before entering

## Signature move

A dripping dot-matrix blackletter logo inside a CRT frame with 'slide to enter'.

## Motion

Intro: CRT frame with 'loading' and percentage (~1 s), logo forms from dots and ink drips spread under it (~2 s). Gate: the orange slider waits; WebGL drips animate idly. Wheel does nothing before entering.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; WebGL canvas x4 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: click-anywhere. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the filmic one-shot grammar: a studio site framed as a rounded CRT screen: a percentage loader, then a horned dot-matrix blackletter logo dripping ink at the bottom, with an orange 'slide to enter' bar and 'headphones recommended'. Type: SF Mono.
Ground and ink from the measured palette (#E0E0DF, #000002, #938580). Motion carries the page through
a dripping dot-matrix blackletter logo inside a CRT frame with 'slide to enter'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — dot-matrix graphics, ink textures

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: dot-matrix graphics, ink textures

## Reference lock

Primary reference/direction: KVS Studio — A studio site framed as a rounded CRT screen: a percentage loader, then a horned dot-matrix blackletter logo dripping ink at the bottom, with an orange 'slide to enter' bar and 'headphones recommended'.
Preserve (3-5 traits): rounded CRT screen frame on black; dot-matrix blackletter logo; ink drips below the logo; slide-to-enter gate; hazard tape corner.
Borrow only (1-2): A slide gesture as the gate when the site is an experience; A screen-object frame (CRT) around the whole site
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: dot-matrix graphics, ink textures
Reject: Captured only the gate; the slide gesture was not performed; Nothing readable before entering
Token commitments: palette #E0E0DF, #000002, #938580; type SF Mono; engine GSAP + Lenis linked (never vendored).
