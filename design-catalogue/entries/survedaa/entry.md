---
title: "SurVedaa"
url: https://survedaa.com/
source_url: https://survedaa.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: ""
family: violet-blur-music-studio-app
dna: "Music studio app x violet blur and serif italic"
register: cinematic dark
grammar: chaptered editorial
lane: "A music-studio app page on a deep violet blur where a serif problem statement is followed by a stack of photo cards that deal out one by one, a 'whole world of possibilities' grid, a sentence that blurs in and out, and a phone counting practice days."
mode: persuade
traits: ["deep violet/amber blurred ground", "serif + italic headline pairs", "photo cards dealt as a stack", "marquee nav strip in mono", "blur-in/blur-out statements", "phone mockup with a counting number"]
palette: ["#000000", "#17161D", "#3F3E41", "#9B9B9F"]
type: ["DM Mono", "DM Sans", "Denton"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The ground is smoke-like colour that shifts behind every section, so the plain layout always has atmosphere. Problems are shown as a stack of photo cards dealt across the screen one by one, and the app's promise is a single sentence that comes into focus from a blur.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Deal a stack of cards across the screen one per scroll beat to list problems
- Bring a key sentence into focus from a heavy blur
- A counting number on a phone mockup as the proof beat

## What to leave

- Very heavy smoothing (~150–175 px glide)
- Long blurred stretches with nothing to read

## Signature move

Photo cards dealt from a stack across a violet blur, one per problem.

## Motion

Intro: 'Survedaa' with a progress bar on a violet blur (~1.5 s). Scroll (Lenis, ~150 px glide, 2 pins, Observer): a problem statement sets in; photo cards slide out from a stack and fan across; 'Survedaa removes every single one of these' as the stack collapses; studio photos; 'One Studio, A whole world of possibilities.' grid; 'Book It. Learn It. Track It.' sharpens out of blur; a phone rises with a day counter 341 → 365.

Measured (`motion/probe.json`): GSAP 3.15.0; 2 pinned sections; Lenis; WebGL canvas x1; smoothed scroll (median 147 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a music-studio app page on a deep violet blur where a serif problem statement is followed by a stack of photo cards that deal out one by one, a 'whole world of possibilities' grid, a sentence that blurs in and out, and a phone counting practice days. Type: DM Mono, DM Sans, Denton.
Ground and ink from the measured palette (#000000, #17161D, #3F3E41). Motion carries the page through
photo cards dealt from a stack across a violet blur, one per problem. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — warm documentary photos of musicians and studios under violet light

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: warm documentary photos of musicians and studios under violet light

## Reference lock

Primary reference/direction: SurVedaa — A music-studio app page on a deep violet blur where a serif problem statement is followed by a stack of photo cards that deal out one by one, a 'whole world of possibilities' grid, a sentence that blurs in and out, and a phone counting practice days.
Preserve (3-5 traits): deep violet/amber blurred ground; serif + italic headline pairs; photo cards dealt as a stack; marquee nav strip in mono; blur-in/blur-out statements.
Borrow only (1-2): Deal a stack of cards across the screen one per scroll beat to list problems; Bring a key sentence into focus from a heavy blur
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: warm documentary photos of musicians and studios under violet light
Reject: Very heavy smoothing (~150–175 px glide); Long blurred stretches with nothing to read
Token commitments: palette #000000, #17161D, #3F3E41, #9B9B9F; type DM Mono, DM Sans, Denton; engine GSAP + Lenis linked (never vendored).
