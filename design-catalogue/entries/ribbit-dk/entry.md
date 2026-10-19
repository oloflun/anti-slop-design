---
title: "Ribbit"
url: http://ribbit.dk/
source_url: http://ribbit.dk/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: animation-studio-logo-reel
dna: "Danish animation studio x the logo re-animated in a different style every cut"
register: illustrated dark
grammar: rhythmic cutlist
lane: "An animation studio home that is a reel: a lilac intro with 'Howdy, we are' and an infinity mark, surreal 3D creatures around the name, then the 'ribbit' wordmark appears again and again in a new style per cut (neon sign in a dark room, chrome on silk, cosmic ring, flat illustration can, 3D clay room, retro desktop, crystal ball, dreamy lake)."
mode: experience
traits: ["the wordmark re-made per cut", "each cut a different medium", "lilac intro with 3D creatures", "video player chrome", "no conventional sections", "PLAY gate"]
palette: ["#2D2924", "#615559", "#5D88BF", "#E8BEE9", "#A19086", "#C1BAB5"]
type: ["FKGroteskNeue", "FKTEcho"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Showing the same logo in a dozen techniques is the studio's whole pitch in one loop: range proven on a single constant.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Frederik Hansen, Michael Vestergaard).

## What to borrow (principle)

- Re-render one constant (the logo) in every style you can do

## What to leave

- Nothing to read beyond the reel
- Player chrome feels unfinished

## Signature move

The 'ribbit' wordmark re-animated in a new medium every few seconds.

## Motion

Intro: lilac, 'Howdy we are' types, the infinity mark morphs into the wordmark surrounded by bobbing 3D creatures (~3 s). PLAY (unlocked) starts the reel; wheel (Lenis ~130 px glide) moves through cuts while each one plays: neon flicker, silk ripple, ring pulse, illustration bounce.

Measured (`motion/probe.json`): GSAP 3.13.0; 2 video; smoothed scroll (median 131 px still travelling after input stops); entry gate: PLAY. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the rhythmic cutlist grammar: an animation studio home that is a reel: a lilac intro with 'Howdy, we are' and an infinity mark, surreal 3D creatures around the name, then the 'ribbit' wordmark appears again and again in a new style per cut (neon sign in a dark room, chrome on silk, cosmic ring, flat illustration can, 3D clay room, retro desktop, crystal ball, dreamy lake). Type: FKGroteskNeue, FKTEcho.
Ground and ink from the measured palette (#2D2924, #615559, #5D88BF). Motion carries the page through
the 'ribbit' wordmark re-animated in a new medium every few seconds. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D animation, illustration, motion design

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D animation, illustration, motion design

## Reference lock

Primary reference/direction: Ribbit — An animation studio home that is a reel: a lilac intro with 'Howdy, we are' and an infinity mark, surreal 3D creatures around the name, then the 'ribbit' wordmark appears again and again in a new style per cut (neon sign in a dark room, chrome on silk, cosmic ring, flat illustration can, 3D clay room, retro desktop, crystal ball, dreamy lake).
Preserve (3-5 traits): the wordmark re-made per cut; each cut a different medium; lilac intro with 3D creatures; video player chrome; no conventional sections.
Borrow only (1-2): Re-render one constant (the logo) in every style you can do
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D animation, illustration, motion design
Reject: Nothing to read beyond the reel; Player chrome feels unfinished
Token commitments: palette #2D2924, #615559, #5D88BF, #E8BEE9, #A19086, #C1BAB5; type FKGroteskNeue, FKTEcho; engine GSAP + Lenis linked (never vendored).
