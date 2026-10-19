---
title: "Curse The League"
url: http://cursetheleague.com/
source_url: http://cursetheleague.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: playful
category2: "editorial"
family: sports-curse-mind-trick
dna: "ESPN sports story x a glowing-eyed skull helmet that reads your mind"
register: cinematic dark
grammar: live surface
lane: "An ESPN interactive: after PLAY, a skull in a football helmet with glowing red eyes floats among storm clouds and NFL team logos, asking you to 'Pick any 2 digit number' as the first step of a mind-reading trick, with a ticker of cursed-team trivia along the bottom."
mode: experience
traits: ["glowing-eyed skull helmet", "storm clouds and flying team logos", "step-by-step trick with NEXT", "condensed sports type", "news ticker", "sound toggle"]
palette: ["#24242C", "#130709", "#4A3F3D", "#4F0C09", "#ACABA9"]
type: ["Goldman", "SerifGothicStd", "Anybody_UltraCondensed", "Octal"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

A mind-reading trick is a clever hook for a story about sports curses; the skull and logos set the tone instantly.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Use a participatory trick as the entry to a story

## What to leave

- Nothing on scroll; you must click through
- Small ticker text

## Signature move

A glowing-eyed skull in a helmet asking you to pick a number.

## Motion

Intro: black, PLAY (unlocked), the skull fades in with red eyes lighting (~3 s). No scroll: logos tumble past, clouds drift, the eyes pulse; NEXT advances the trick.

Measured (`motion/probe.json`): GSAP 3.13.0; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: PLAY. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the live surface grammar: an ESPN interactive: after PLAY, a skull in a football helmet with glowing red eyes floats among storm clouds and NFL team logos, asking you to 'Pick any 2 digit number' as the first step of a mind-reading trick, with a ticker of cursed-team trivia along the bottom. Type: Goldman, SerifGothicStd, Anybody_UltraCondensed, Octal.
Ground and ink from the measured palette (#24242C, #130709, #4A3F3D). Motion carries the page through
a glowing-eyed skull in a helmet asking you to pick a number. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D skull helmet, team logos

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D skull helmet, team logos

## Reference lock

Primary reference/direction: Curse The League — An ESPN interactive: after PLAY, a skull in a football helmet with glowing red eyes floats among storm clouds and NFL team logos, asking you to 'Pick any 2 digit number' as the first step of a mind-reading trick, with a ticker of cursed-team trivia along the bottom.
Preserve (3-5 traits): glowing-eyed skull helmet; storm clouds and flying team logos; step-by-step trick with NEXT; condensed sports type; news ticker.
Borrow only (1-2): Use a participatory trick as the entry to a story
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D skull helmet, team logos
Reject: Nothing on scroll; you must click through; Small ticker text
Token commitments: palette #24242C, #130709, #4A3F3D, #4F0C09, #ACABA9; type Goldman, SerifGothicStd, Anybody_UltraCondensed, Octal; engine GSAP + Lenis linked (never vendored).
