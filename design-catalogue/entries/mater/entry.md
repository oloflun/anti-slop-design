---
title: "mater.agency - born digital"
url: http://mater.agency/
source_url: http://mater.agency/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: agency-dark-teal-case-wall
dna: "Croatian digital agency x a wall of floating case cards on dark teal"
register: cinematic dark
grammar: chaptered editorial
lane: "An agency: a typing line 'Friday. The weekend's opening act...', a light page 'You say jump, we dance' with floating device cards, a statement typing in, stat and case cards (40, 34, 23 degrees, Masters of Telco) floating in two columns, a 'villas' card, then dark teal 'Our latest projects' with case renders floating at different depths, 'Behind the screens' articles, client logos and a yellow CTA."
mode: persuade
traits: ["typing first line", "floating case cards at different depths", "dark teal and lime yellow", "stat cards with big numbers", "phone renders", "client logo row"]
palette: ["#EBECE7", "#7D7B78", "#15181A", "#AEAFAA", "#42403E"]
type: ["Inter", "Plain ExtraBold"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Case cards floating at different speeds give a dense agency page depth, and the typing intro gives it a personality.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Open with a typed line of personality, not a headline

## What to leave

- Too many card styles
- Small text

## Signature move

Case renders floating at different depths on dark teal.

## Motion

Intro: a line types and deletes (~3 s). Wheel (ScrollSmoother, 3 pins): device cards drift; the statement types letter by letter; stat cards float at different speeds; the page turns dark teal; renders float past; articles slide in; logos fade.

Measured (`motion/probe.json`): GSAP 3.11.4; 3 pinned sections; ScrollSmoother; WebGL canvas x1 (three.js); 14 video; split text; entry gate: Deny. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: an agency: a typing line 'Friday. The weekend's opening act...', a light page 'You say jump, we dance' with floating device cards, a statement typing in, stat and case cards (40, 34, 23 degrees, Masters of Telco) floating in two columns, a 'villas' card, then dark teal 'Our latest projects' with case renders floating at different depths, 'Behind the screens' articles, client logos and a yellow CTA. Type: Inter, Plain ExtraBold.
Ground and ink from the measured palette (#EBECE7, #7D7B78, #15181A). Motion carries the page through
case renders floating at different depths on dark teal. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — device renders, campaign photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: device renders, campaign photography

## Reference lock

Primary reference/direction: mater.agency - born digital — An agency: a typing line 'Friday. The weekend's opening act...', a light page 'You say jump, we dance' with floating device cards, a statement typing in, stat and case cards (40, 34, 23 degrees, Masters of Telco) floating in two columns, a 'villas' card, then dark teal 'Our latest projects' with case renders floating at different depths, 'Behind the screens' articles, client logos and a yellow CTA.
Preserve (3-5 traits): typing first line; floating case cards at different depths; dark teal and lime yellow; stat cards with big numbers; phone renders.
Borrow only (1-2): Open with a typed line of personality, not a headline
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: device renders, campaign photography
Reject: Too many card styles; Small text
Token commitments: palette #EBECE7, #7D7B78, #15181A, #AEAFAA, #42403E; type Inter, Plain ExtraBold; engine GSAP + Lenis linked (never vendored).
