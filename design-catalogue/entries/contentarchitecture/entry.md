---
title: "Content Architecture - Sanity kit for Next.js"
url: https://www.contentarchitecture.dev/
source_url: https://www.contentarchitecture.dev/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: ""
family: ascii-sphere-dev-kit
dna: "Developer kit x an ASCII sphere and a hours-lost counter"
register: modern clean
grammar: chaptered editorial
lane: "A developer product on paper white: 'The stack agents don't reinvent' beside a dark panel, an ASCII text sphere spinning, 'The page builder alone costs you days' with a counter '~00' to '~24' hours and a day-by-day ledger, a dark section where the ASCII sphere becomes a face with numbered decisions, a code editor, showcase names, 'Two editions. One architecture.' and 'Before you buy' FAQ."
mode: persuade
traits: ["ASCII sphere and face", "hours counter", "mono ledger", "paper white and ink", "code editor panel", "numbered decisions"]
palette: ["#F2EEE9", "#232323", "#3D3D3D", "#C0BEBA"]
type: ["GeistMono", "GeistSans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The counter that ticks up the hours lost is the argument; the ASCII sphere is the one ornament and it is made of the product's material.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Edoardo Lunardi).

## What to borrow (principle)

- Let a counter tick up the cost as the reader scrolls

## What to leave

- Dense mono text

## Signature move

A spinning sphere made of ASCII text.

## Motion

Intro: the hero with the ASCII sphere spinning. Wheel: the counter rolls; ledger rows appear; the dark panel rises and the sphere resolves into a face; the editor types; rows fill.

Measured (`motion/probe.json`): Lenis; WebGL canvas x22; smoothed scroll (median 157 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a developer product on paper white: 'The stack agents don't reinvent' beside a dark panel, an ASCII text sphere spinning, 'The page builder alone costs you days' with a counter '~00' to '~24' hours and a day-by-day ledger, a dark section where the ASCII sphere becomes a face with numbered decisions, a code editor, showcase names, 'Two editions. One architecture.' and 'Before you buy' FAQ. Type: GeistMono, GeistSans.
Ground and ink from the measured palette (#F2EEE9, #232323, #3D3D3D). Motion carries the page through
a spinning sphere made of ASCII text. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — ASCII render, code

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: ASCII render, code

## Reference lock

Primary reference/direction: Content Architecture - Sanity kit for Next.js — A developer product on paper white: 'The stack agents don't reinvent' beside a dark panel, an ASCII text sphere spinning, 'The page builder alone costs you days' with a counter '~00' to '~24' hours and a day-by-day ledger, a dark section where the ASCII sphere becomes a face with numbered decisions, a code editor, showcase names, 'Two editions. One architecture.' and 'Before you buy' FAQ.
Preserve (3-5 traits): ASCII sphere and face; hours counter; mono ledger; paper white and ink; code editor panel.
Borrow only (1-2): Let a counter tick up the cost as the reader scrolls
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: ASCII render, code
Reject: Dense mono text
Token commitments: palette #F2EEE9, #232323, #3D3D3D, #C0BEBA; type GeistMono, GeistSans; engine GSAP + Lenis linked (never vendored).
