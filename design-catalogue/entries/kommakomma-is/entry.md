---
title: "Komma Komma"
url: http://kommakomma.is/
source_url: http://kommakomma.is/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: quote-mark-reykjavik-studio
dna: "Reykjavik web studio x quotation-mark identity"
register: modern clean
grammar: chaptered editorial
lane: "A pale studio page whose loader builds a quotation mark from blocks, then a project cover floats over a moss photograph, 'You only quote what's important' assembles word by word, featured projects tilt in 3D, and services list dims all but the active line."
mode: persuade
traits: ["quotation-mark logo built from blocks", "project cover over moss photo", "statement words assembling from scattered positions", "3D tilted project card", "service list with active line", "giant wordmark footer with a slashed O"]
palette: ["#E9E9E9", "#18220B", "#BEBBBC", "#514A31"]
type: ["BDO Grotesk"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The name (comma comma, a quotation mark in Icelandic) becomes the loader: blocks fall into the two marks. The statement 'You only quote what's important' then gathers its words from across the screen, so the identity, the line and the motion are the same idea.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Build the logo glyph from blocks as the loader
- Gather a statement's words from scattered positions into the line
- Dim all but the active row in a services list

## What to leave

- Pale grey on grey lowers contrast
- Featured project shown as one floating card

## Signature move

Blocks dropping into place to form a pair of quotation marks.

## Motion

Intro: two blocks, then a bracket, then the full quotation mark (~1.5 s). Scroll (Lenis, ~125 px glide, Barba, three.js): moss photo with a project cover; words of the statement drift into place; 'Featured Projects' with a 3D-tilted cover that rotates; services list activating per line; award laurels; dotted '„' graphic; wordmark footer.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; Barba page transitions; WebGL canvas x1 (three.js); smoothed scroll (median 131 px still travelling after input stops); entry gate: REJECT. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a pale studio page whose loader builds a quotation mark from blocks, then a project cover floats over a moss photograph, 'You only quote what's important' assembles word by word, featured projects tilt in 3D, and services list dims all but the active line. Type: BDO Grotesk.
Ground and ink from the measured palette (#E9E9E9, #18220B, #BEBBBC). Motion carries the page through
blocks dropping into place to form a pair of quotation marks. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — nature textures (moss, forest) with printed project covers

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: nature textures (moss, forest) with printed project covers

## Reference lock

Primary reference/direction: Komma Komma — A pale studio page whose loader builds a quotation mark from blocks, then a project cover floats over a moss photograph, 'You only quote what's important' assembles word by word, featured projects tilt in 3D, and services list dims all but the active line.
Preserve (3-5 traits): quotation-mark logo built from blocks; project cover over moss photo; statement words assembling from scattered positions; 3D tilted project card; service list with active line.
Borrow only (1-2): Build the logo glyph from blocks as the loader; Gather a statement's words from scattered positions into the line
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: nature textures (moss, forest) with printed project covers
Reject: Pale grey on grey lowers contrast; Featured project shown as one floating card
Token commitments: palette #E9E9E9, #18220B, #BEBBBC, #514A31; type BDO Grotesk; engine GSAP + Lenis linked (never vendored).
