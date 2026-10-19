---
title: "Ten Years Away (375 Studio)"
url: https://ten.375.studio/en
source_url: https://ten.375.studio/en
captured: 2026-10-02
origin: raw-url
extract: none
category: editorial
category2: "playful"
family: year-flip-graphic-novel
dna: "Graphic novel launch x year counter 2015 → 2025"
register: illustrated dark
grammar: filmic one-shot
lane: "A graphic-novel site whose loader flips a year from 2015 to 2025 digit by digit, offers enter with or without sound, then presents the comic's cover floating in a navy cloud under the title 'TEN YEARS AWAY' with the two years outlined at the corners."
mode: experience
traits: ["year counter as loader (2015 → 2025)", "sound gate", "comic cover as the hero object", "navy cloudy ground", "outlined years in corners", "wide heavy caps title"]
palette: ["#21273E", "#373D50", "#505360", "#A9BABF"]
type: ["valve"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The title's idea (ten years) is the loader: the year flips digit by digit from 2015 to 2025 before you enter, so the gap the book is about has already passed on screen. The cover then floats alone as the only colour.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Studio375).

## What to borrow (principle)

- Make the loader count the subject (a span of years)
- Present a single product cover floating alone as the only colour on a dark ground

## What to leave

- Gate before the content
- 'Click anywhere to start' leaves the page static in captures

## Signature move

A year that flips digit by digit from 2015 to 2025 as the loader.

## Motion

Intro: '2015' with 'enable sound for a better experience', the last digits roll to '2025' (~2 s), enter with/without sound. Then: title 'TEN YEARS AWAY' and the comic cover float in a cloud with '2015' and '2025' outlined at the bottom corners; 'click anywhere to start' (WebGL).

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Mute, ENTER WITHOUT SOUND. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the filmic one-shot grammar: a graphic-novel site whose loader flips a year from 2015 to 2025 digit by digit, offers enter with or without sound, then presents the comic's cover floating in a navy cloud under the title 'TEN YEARS AWAY' with the two years outlined at the corners. Type: valve.
Ground and ink from the measured palette (#21273E, #373D50, #505360). Motion carries the page through
a year that flips digit by digit from 2015 to 2025 as the loader. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — comic book cover art, dense colourful illustration

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: comic book cover art, dense colourful illustration

## Reference lock

Primary reference/direction: Ten Years Away (375 Studio) — A graphic-novel site whose loader flips a year from 2015 to 2025 digit by digit, offers enter with or without sound, then presents the comic's cover floating in a navy cloud under the title 'TEN YEARS AWAY' with the two years outlined at the corners.
Preserve (3-5 traits): year counter as loader (2015 → 2025); sound gate; comic cover as the hero object; navy cloudy ground; outlined years in corners.
Borrow only (1-2): Make the loader count the subject (a span of years); Present a single product cover floating alone as the only colour on a dark ground
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: comic book cover art, dense colourful illustration
Reject: Gate before the content; 'Click anywhere to start' leaves the page static in captures
Token commitments: palette #21273E, #373D50, #505360, #A9BABF; type valve; engine GSAP + Lenis linked (never vendored).
