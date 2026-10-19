---
title: "Siena Film Foundation"
url: https://www.siena.film/
source_url: https://www.siena.film/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "editorial"
family: film-foundation-stripes-intro
dna: "Film foundation x striped wordmark intro and film-poster hero"
register: cinematic dark
grammar: filmic one-shot
lane: "A film foundation: vertical stripes that close into the 'SIENA' wordmark, an Enter button, then a film-poster hero ('My Project X') over a still with review stars, director credits and a small preview window cycling clips, with the title glitching."
mode: experience
traits: ["stripes closing into the wordmark", "film-poster hero", "review stars as typography", "preview window", "title glitch", "Enter gate"]
palette: ["#482416", "#0A0A09", "#5A4535", "#81644E", "#C0B5A8"]
type: ["Neue Brucke", "P22 Parrish Roman", "NB International"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The stripe intro is like a film leader, and the poster hero sells a film the way a festival would.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Stripes closing into the wordmark as a film-leader intro

## What to leave

- Capture stays on the hero

## Signature move

Vertical stripes closing into 'SIENA'.

## Motion

Intro: white stripes thin to black stripes and resolve to the wordmark (~3 s), Enter. Scroll: the hero holds; the preview cycles clips; the title glitches.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; Taxi page transitions; WebGL canvas x1; 1 video; split text; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: ENTER. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the filmic one-shot grammar: a film foundation: vertical stripes that close into the 'SIENA' wordmark, an Enter button, then a film-poster hero ('My Project X') over a still with review stars, director credits and a small preview window cycling clips, with the title glitching. Type: Neue Brucke, P22 Parrish Roman, NB International.
Ground and ink from the measured palette (#482416, #0A0A09, #5A4535). Motion carries the page through
vertical stripes closing into 'SIENA'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — film stills

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: film stills

## Reference lock

Primary reference/direction: Siena Film Foundation — A film foundation: vertical stripes that close into the 'SIENA' wordmark, an Enter button, then a film-poster hero ('My Project X') over a still with review stars, director credits and a small preview window cycling clips, with the title glitching.
Preserve (3-5 traits): stripes closing into the wordmark; film-poster hero; review stars as typography; preview window; title glitch.
Borrow only (1-2): Stripes closing into the wordmark as a film-leader intro
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: film stills
Reject: Capture stays on the hero
Token commitments: palette #482416, #0A0A09, #5A4535, #81644E, #C0B5A8; type Neue Brucke, P22 Parrish Roman, NB International; engine GSAP + Lenis linked (never vendored).
