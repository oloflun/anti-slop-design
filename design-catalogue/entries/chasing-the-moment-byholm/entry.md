---
title: "Chasing the Moment (HOLM)"
url: https://chasing-the-moment.byholm.co/
source_url: https://chasing-the-moment.byholm.co/
captured: 2026-10-02
origin: raw-url
extract: none
category: playful
category2: ""
family: ticket-gate-webfilm
dna: "Web film x paper cinema ticket"
register: cinematic dark
grammar: filmic one-shot
lane: "A web film that opens on a printed cinema ticket; the stub tears off and turns into two choices, 'WITH SOUND' and 'WITHOUT SOUND', before the film begins."
mode: experience
traits: ["paper ticket as the loader", "stub that tears off", "two-choice sound gate as tickets", "condensed caps (Anton)", "smoky grey ground"]
palette: ["#242424", "#BABABA"]
type: ["Anton", "Archivo", "Caveat"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The gate is part of the fiction: you are handed a ticket, the stub tears, and the two halves become the sound choice. Even before the film plays, the object sets the tone.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Canberk Polat).

## What to borrow (principle)

- Make the entry gate an object from the story (a ticket) instead of a modal
- A tear or fold as the transition from loader to choice

## What to leave

- Captured only up to the gate: the gate is built so the automated click did not pass it
- Smoke texture ground is low contrast

## Signature move

A cinema ticket whose stub tears off and becomes the WITH SOUND / WITHOUT SOUND choice.

## Motion

Intro: smoky dark ground, the ticket slides in with a silhouette and 'ADMIT ONE' (~1.2 s), the stub tears and rotates away (~2.5 s), the two ticket halves stand as the sound choice. Beyond the gate (not captured): a scroll-driven web film (ScrollTrigger, WebGL x3).

Measured (`motion/probe.json`): GSAP 3.15.0; WebGL canvas x3 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the filmic one-shot grammar: a web film that opens on a printed cinema ticket; the stub tears off and turns into two choices, 'WITH SOUND' and 'WITHOUT SOUND', before the film begins. Type: Anton, Archivo, Caveat.
Ground and ink from the measured palette (#242424, #BABABA). Motion carries the page through
a cinema ticket whose stub tears off and becomes the WITH SOUND / WITHOUT SOUND choice. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — printed paper ephemera on a dark smoky ground

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: printed paper ephemera on a dark smoky ground

## Reference lock

Primary reference/direction: Chasing the Moment (HOLM) — A web film that opens on a printed cinema ticket; the stub tears off and turns into two choices, 'WITH SOUND' and 'WITHOUT SOUND', before the film begins.
Preserve (3-5 traits): paper ticket as the loader; stub that tears off; two-choice sound gate as tickets; condensed caps (Anton); smoky grey ground.
Borrow only (1-2): Make the entry gate an object from the story (a ticket) instead of a modal; A tear or fold as the transition from loader to choice
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: printed paper ephemera on a dark smoky ground
Reject: Captured only up to the gate: the gate is built so the automated click did not pass it; Smoke texture ground is low contrast
Token commitments: palette #242424, #BABABA; type Anton, Archivo, Caveat; engine GSAP + Lenis linked (never vendored).
