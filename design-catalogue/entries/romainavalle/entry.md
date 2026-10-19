---
title: "Romain Avalle - interactive developer"
url: https://romainavalle.dev/
source_url: https://romainavalle.dev/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: ""
family: scanline-blackletter-dev-portfolio
dna: "Developer portfolio x white page, a blackletter name rendered in horizontal scanlines that glitches, a dithered portrait and a project ledger"
register: editorial print
grammar: typographic poster
lane: "A developer's site: a black bar loader, the name in huge blackletter built from horizontal scanlines, glitching into pixel blocks and settling, a bio beside a dithered scanline portrait, award counts, 'Select Projects' in scanline blackletter, a numbered ledger of projects (client, role, city, awards, year) with a black marquee bar that scrolls the hovered project's awards, and 'Let's talk' in scanline blackletter on black."
mode: persuade
traits: ["blackletter in scanlines", "glitch to pixel blocks", "dithered portrait", "numbered project ledger", "marquee bar inside the ledger"]
palette: ["#FFFFFF", "#9D9D9D", "#373737", "#DDDDDD", "#BBBBBB", "#7A7A7A"]
type: ["RemusVariableVF", "andale-mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Rendering a blackletter name as scanlines joins old typography to screen texture, which is the developer's craft in one image.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Bastien Allard, Romain Avalle).

## What to borrow (principle)

- Render the display type in the medium's own texture

## What to leave

- Decoding characters hide some ledger text

## Signature move

A blackletter name built from horizontal scanlines glitching into pixel blocks.

## Motion

Intro: bar loader, glitch assembly (~2 s). Wheel (Lenis, WebGL): scanline type distorts with scroll; text decodes character by character; ledger rows reveal; the marquee runs.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x1 (three.js); smoothed scroll (median 72 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the typographic poster grammar: a developer's site: a black bar loader, the name in huge blackletter built from horizontal scanlines, glitching into pixel blocks and settling, a bio beside a dithered scanline portrait, award counts, 'Select Projects' in scanline blackletter, a numbered ledger of projects (client, role, city, awards, year) with a black marquee bar that scrolls the hovered project's awards, and 'Let's talk' in scanline blackletter on black. Type: RemusVariableVF, andale-mono.
Ground and ink from the measured palette (#FFFFFF, #9D9D9D, #373737). Motion carries the page through
a blackletter name built from horizontal scanlines glitching into pixel blocks. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL type, dithered photo

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL type, dithered photo

## Reference lock

Primary reference/direction: Romain Avalle - interactive developer — A developer's site: a black bar loader, the name in huge blackletter built from horizontal scanlines, glitching into pixel blocks and settling, a bio beside a dithered scanline portrait, award counts, 'Select Projects' in scanline blackletter, a numbered ledger of projects (client, role, city, awards, year) with a black marquee bar that scrolls the hovered project's awards, and 'Let's talk' in scanline blackletter on black.
Preserve (3-5 traits): blackletter in scanlines; glitch to pixel blocks; dithered portrait; numbered project ledger; marquee bar inside the ledger.
Borrow only (1-2): Render the display type in the medium's own texture
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL type, dithered photo
Reject: Decoding characters hide some ledger text
Token commitments: palette #FFFFFF, #9D9D9D, #373737, #DDDDDD, #BBBBBB, #7A7A7A; type RemusVariableVF, andale-mono; engine GSAP + Lenis linked (never vendored).
