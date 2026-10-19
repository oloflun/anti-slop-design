---
title: "Ponpon Mania - Interactive Comic"
url: https://ponpon-mania.com/
source_url: https://ponpon-mania.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: playful
category2: "editorial"
family: interactive-comic-cover
dna: "Web comic x a flat-colour cover scene with balloons floating up"
register: illustrated dark
grammar: live surface
lane: "An interactive comic's front page: a mascot-face loader on cream, then a bold flat-colour cover in a cloud-shaped frame: a smug sheep on a box above a city at sunset with a rhino and a dinosaur in the foreground, balloons floating up, a spinning record badge and a 'read now' button."
mode: experience
traits: ["cloud-shaped frame", "flat saturated comic colours", "floating balloons", "spinning record badge", "characters in foreground", "read now CTA"]
palette: ["#F997AE", "#FEB322", "#7F7EFE", "#E05125", "#5B535F", "#70AB66"]
type: ["Libre Franklin"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The cover is the hook: a single dense illustration with small idle motions (balloons, badge) invites you to start reading.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Justine SOULIE, Justine Soulié, Patrick HENG, Patrick Heng).

## What to borrow (principle)

- Small idle motions on an otherwise still illustration

## What to leave

- Nothing beyond the cover on scroll

## Signature move

A smug sheep on a box at sunset with balloons drifting up.

## Motion

Intro: cream with a mascot-face loader (~2 s), cookie declined, the cover scene fills. Scroll: nothing moves except balloons drifting and the badge spinning.

Measured (`motion/probe.json`): GSAP 3.13.0; WebGL canvas x1; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: decline. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the live surface grammar: an interactive comic's front page: a mascot-face loader on cream, then a bold flat-colour cover in a cloud-shaped frame: a smug sheep on a box above a city at sunset with a rhino and a dinosaur in the foreground, balloons floating up, a spinning record badge and a 'read now' button. Type: Libre Franklin.
Ground and ink from the measured palette (#F997AE, #FEB322, #7F7EFE). Motion carries the page through
a smug sheep on a box at sunset with balloons drifting up. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — flat comic illustration

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: flat comic illustration

## Reference lock

Primary reference/direction: Ponpon Mania - Interactive Comic — An interactive comic's front page: a mascot-face loader on cream, then a bold flat-colour cover in a cloud-shaped frame: a smug sheep on a box above a city at sunset with a rhino and a dinosaur in the foreground, balloons floating up, a spinning record badge and a 'read now' button.
Preserve (3-5 traits): cloud-shaped frame; flat saturated comic colours; floating balloons; spinning record badge; characters in foreground.
Borrow only (1-2): Small idle motions on an otherwise still illustration
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: flat comic illustration
Reject: Nothing beyond the cover on scroll
Token commitments: palette #F997AE, #FEB322, #7F7EFE, #E05125, #5B535F, #70AB66; type Libre Franklin; engine GSAP + Lenis linked (never vendored).
