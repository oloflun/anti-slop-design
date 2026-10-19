---
title: "Doomicus - Designer and Developer"
url: https://doomicus.com/
source_url: https://doomicus.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: butter-serif-giant-letters
dna: "Designer-developer x giant serif letters sliding past on butter yellow"
register: editorial print
grammar: typographic poster
lane: "A folio intro on butter yellow: a giant high-contrast serif 'PRO' sliding past the screen, the name 'Pedro' in script, then 'Designer & Developer' with swash letters and a small intro in two columns."
mode: read
traits: ["giant serif letters sliding past", "butter yellow ground", "swash capitals inside the headline", "script name", "two-column small intro", "Barba transitions"]
palette: ["#FFECA7", "#C9BC89", "#807657"]
type: ["Migra ExtraLight", "Migra Regular", "Migra Italic", "Neue Haas Display"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The giant letters passing like a camera move make a one-screen folio intro feel cinematic.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Slide giant letters past the camera as the intro

## What to leave

- Capture stops at the hero
- Very small intro text

## Signature move

Giant serif 'PRO' sliding past on butter yellow before 'Designer & Developer'.

## Motion

Intro: butter yellow, enormous serif letters slide past left to right (~3 s), the script name writes, the headline settles. Wheel: no change captured beyond the hero.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; Barba page transitions; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the typographic poster grammar: a folio intro on butter yellow: a giant high-contrast serif 'PRO' sliding past the screen, the name 'Pedro' in script, then 'Designer & Developer' with swash letters and a small intro in two columns. Type: Migra ExtraLight, Migra Regular, Migra Italic, Neue Haas Display.
Ground and ink from the measured palette (#FFECA7, #C9BC89, #807657). Motion carries the page through
giant serif 'PRO' sliding past on butter yellow before 'Designer & Developer'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — none, type only

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: none, type only

## Reference lock

Primary reference/direction: Doomicus - Designer and Developer — A folio intro on butter yellow: a giant high-contrast serif 'PRO' sliding past the screen, the name 'Pedro' in script, then 'Designer & Developer' with swash letters and a small intro in two columns.
Preserve (3-5 traits): giant serif letters sliding past; butter yellow ground; swash capitals inside the headline; script name; two-column small intro.
Borrow only (1-2): Slide giant letters past the camera as the intro
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: none, type only
Reject: Capture stops at the hero; Very small intro text
Token commitments: palette #FFECA7, #C9BC89, #807657; type Migra ExtraLight, Migra Regular, Migra Italic, Neue Haas Display; engine GSAP + Lenis linked (never vendored).
