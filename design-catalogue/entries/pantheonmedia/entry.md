---
title: "Pantheon Media Group"
url: http://www.pantheonmedia.com/
source_url: http://www.pantheonmedia.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: giant-wordmark-film-reel
dna: "Production company x a full-width wordmark over a fast reel"
register: cinematic dark
grammar: filmic one-shot
lane: "A production company: 'PANTHEON' full-width at the bottom of a white screen that flips to black and moves to the top, then a fast reel of their shoots (dance battles, concerts, boats, helicopters, bars) plays full bleed behind the wordmark with a city list at the bottom."
mode: experience
traits: ["full-width wordmark", "wordmark moves from bottom to top", "fast full-bleed reel", "city list footer", "white to black flip", "no scroll content"]
palette: ["#0A0C16", "#74787D", "#323443", "#F5F6F5", "#ADB3A4", "#85A7C2"]
type: ["PPMori", "DMMono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

One move (the wordmark rising) then the reel: a confident, minimal home for a company that only needs to show footage.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: ToyFight).

## What to borrow (principle)

- Move the wordmark from bottom to top as the intro

## What to leave

- Reel repeats
- Nothing else to read

## Signature move

'PANTHEON' across the full width over a fast reel of shoots.

## Motion

Intro: white with the wordmark at the bottom (~1.5 s), the screen flips to black as it rises to the top. The reel then plays with quick cuts; scroll does not move the page.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the filmic one-shot grammar: a production company: 'PANTHEON' full-width at the bottom of a white screen that flips to black and moves to the top, then a fast reel of their shoots (dance battles, concerts, boats, helicopters, bars) plays full bleed behind the wordmark with a city list at the bottom. Type: PPMori, DMMono.
Ground and ink from the measured palette (#0A0C16, #74787D, #323443). Motion carries the page through
'PANTHEON' across the full width over a fast reel of shoots. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — commercial and music video footage

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: commercial and music video footage

## Reference lock

Primary reference/direction: Pantheon Media Group — A production company: 'PANTHEON' full-width at the bottom of a white screen that flips to black and moves to the top, then a fast reel of their shoots (dance battles, concerts, boats, helicopters, bars) plays full bleed behind the wordmark with a city list at the bottom.
Preserve (3-5 traits): full-width wordmark; wordmark moves from bottom to top; fast full-bleed reel; city list footer; white to black flip.
Borrow only (1-2): Move the wordmark from bottom to top as the intro
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: commercial and music video footage
Reject: Reel repeats; Nothing else to read
Token commitments: palette #0A0C16, #74787D, #323443, #F5F6F5, #ADB3A4, #85A7C2; type PPMori, DMMono; engine GSAP + Lenis linked (never vendored).
