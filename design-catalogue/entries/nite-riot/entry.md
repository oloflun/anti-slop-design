---
title: "Nite Riot - creative agency"
url: https://www.nite-riot.com/
source_url: https://www.nite-riot.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: triptych-fan-client-ticker
dna: "LA creative agency x three fanned cards per client and a client-name ticker"
register: modern clean
grammar: rhythmic cutlist
lane: "An agency: a dark index of projects and directors, then on cream each client appears as three fanned tilted cards (centre straight, sides tilted) with a client-name ticker along the bottom highlighting the active one (Genesis, Lenny Kravitz, Converse Skate, Your Turn, Tinder, Culligan, JLo Beauty)."
mode: experience
traits: ["three fanned cards per client", "client name ticker with highlight", "cream ground", "condensed caps", "tilted side cards", "dark project index"]
palette: ["#FCFAF6", "#000000", "#2B1D19", "#68786F", "#E4E5DF"]
type: ["Fixture", "ATF Demi", "ATF Book"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The fanned triptych shows three moments of each campaign at once and the ticker makes the reel navigable.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Fan three images per project with the centre one straight

## What to leave

- Repeats without variation

## Signature move

Three fanned campaign cards above a client-name ticker.

## Motion

Intro: black logo, then a project index (~2 s). Scroll: each step swaps the three cards (sides slide out, new ones fan in) and the ticker moves to the next client.

Measured (`motion/probe.json`): GSAP 3.12.5; Barba page transitions; 10 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the rhythmic cutlist grammar: an agency: a dark index of projects and directors, then on cream each client appears as three fanned tilted cards (centre straight, sides tilted) with a client-name ticker along the bottom highlighting the active one (Genesis, Lenny Kravitz, Converse Skate, Your Turn, Tinder, Culligan, JLo Beauty). Type: Fixture, ATF Demi, ATF Book.
Ground and ink from the measured palette (#FCFAF6, #000000, #2B1D19). Motion carries the page through
three fanned campaign cards above a client-name ticker. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — campaign photography and video

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: campaign photography and video

## Reference lock

Primary reference/direction: Nite Riot - creative agency — An agency: a dark index of projects and directors, then on cream each client appears as three fanned tilted cards (centre straight, sides tilted) with a client-name ticker along the bottom highlighting the active one (Genesis, Lenny Kravitz, Converse Skate, Your Turn, Tinder, Culligan, JLo Beauty).
Preserve (3-5 traits): three fanned cards per client; client name ticker with highlight; cream ground; condensed caps; tilted side cards.
Borrow only (1-2): Fan three images per project with the centre one straight
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: campaign photography and video
Reject: Repeats without variation
Token commitments: palette #FCFAF6, #000000, #2B1D19, #68786F, #E4E5DF; type Fixture, ATF Demi, ATF Book; engine GSAP + Lenis linked (never vendored).
