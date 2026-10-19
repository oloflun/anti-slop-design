---
title: "Tesoro - The Rewards Platform for the Gaming Economy"
url: http://tesoroxp.com/
source_url: http://tesoroxp.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: "playful"
family: color-flip-fintech-gaming
dna: "Gaming rewards fintech x full-screen colour flips and 3D icons"
register: other
grammar: chaptered editorial
lane: "A rewards platform: the giant 'TESORO' wordmark stays at the bottom while the screen flips through a gamer video, a coral card, a mustard thumbs-up, then a black octagon with a toggle, a four-step Connect/Activate/Spend/Reward row in coloured dice, and full-colour chapters (mint, cream, lilac) each with a phone-card demo and in-game currencies, ending in a footer of floating coloured octagons."
mode: persuade
traits: ["wordmark fixed while backgrounds flip", "full-screen colour per chapter", "3D card and hand icons", "dice-like step tiles", "octagon motif", "floating octagons footer"]
palette: ["#FEF8F3", "#C8FAD4", "#E6AD3C", "#433B2A", "#92D095"]
type: ["Polymath Display", "Systemia"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Each chapter owns a colour and the octagon recurs from the toggle to the footer, so a fintech flow feels like a game's level select.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Hold the wordmark still while the colour world behind it changes
- One geometric motif from hero to footer

## What to leave

- Small demo text
- Many similar demo cards

## Signature move

The 'TESORO' wordmark held still while full-screen colours and 3D icons flip behind it.

## Motion

Intro: the video hero with the wordmark (~1 s). Wheel (Lenis ~110 px glide, 1 pin): the background flips to coral with a 3D card, then mustard with a thumbs-up; an octagon drops in and the toggle slides; dice tiles roll in; each chapter's colour floods up; demo cards step through 1-2-3; currencies drop in; octagons tumble in the footer.

Measured (`motion/probe.json`): GSAP 3.15.0; 27 ScrollTriggers; 1 pinned sections; Lenis; 2 video; split text; smoothed scroll (median 111 px still travelling after input stops); entry gate: Skip to main content. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a rewards platform: the giant 'TESORO' wordmark stays at the bottom while the screen flips through a gamer video, a coral card, a mustard thumbs-up, then a black octagon with a toggle, a four-step Connect/Activate/Spend/Reward row in coloured dice, and full-colour chapters (mint, cream, lilac) each with a phone-card demo and in-game currencies, ending in a footer of floating coloured octagons. Type: Polymath Display, Systemia.
Ground and ink from the measured palette (#FEF8F3, #C8FAD4, #E6AD3C). Motion carries the page through
the 'TESORO' wordmark held still while full-screen colours and 3D icons flip behind it. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D icons, gamer video, UI cards

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D icons, gamer video, UI cards

## Reference lock

Primary reference/direction: Tesoro - The Rewards Platform for the Gaming Economy — A rewards platform: the giant 'TESORO' wordmark stays at the bottom while the screen flips through a gamer video, a coral card, a mustard thumbs-up, then a black octagon with a toggle, a four-step Connect/Activate/Spend/Reward row in coloured dice, and full-colour chapters (mint, cream, lilac) each with a phone-card demo and in-game currencies, ending in a footer of floating coloured octagons.
Preserve (3-5 traits): wordmark fixed while backgrounds flip; full-screen colour per chapter; 3D card and hand icons; dice-like step tiles; octagon motif.
Borrow only (1-2): Hold the wordmark still while the colour world behind it changes; One geometric motif from hero to footer
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D icons, gamer video, UI cards
Reject: Small demo text; Many similar demo cards
Token commitments: palette #FEF8F3, #C8FAD4, #E6AD3C, #433B2A, #92D095; type Polymath Display, Systemia; engine GSAP + Lenis linked (never vendored).
