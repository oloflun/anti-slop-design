---
title: "DRIMAGE - Company"
url: https://drimage.com/
source_url: https://drimage.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "product-focused"
family: bar-field-company-timeline
dna: "Korean entertainment-tech company x a field of yellow 3D bars"
register: cinematic dark
grammar: split stage
lane: "A games and entertainment company page: a click-to-enter logo screen, then a field of yellow 3D bars rises like a city or equaliser behind 'Shaping the future of entertainment, one dream at a time', and the bars tilt into a grid that sits at the right while a year-by-year history scrolls at left."
mode: read
traits: ["click to enter", "field of yellow 3D bars", "bars tilt into a side grid", "year-by-year timeline", "yellow accent on black", "sticky year headers"]
palette: ["#000000", "#3E3E15", "#B2B83F", "#1B1B16", "#8D913F"]
type: ["Pretendard", "Poppins"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

One abstract object changes role: it is a skyline behind the mission, then a grid that ticks along beside the history, so the timeline has motion without pictures.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One abstract 3D field that turns into a side panel
- Sticky year headings on a long timeline

## What to leave

- Small timeline text
- Bars repeat the same motion

## Signature move

A field of yellow 3D bars rising behind the mission statement.

## Motion

Intro: black logo with a 'click to enter' dot (Skip clicked), the bars fade up (~2 s). Wheel (Lenis ~130 px glide): bars rise and sway like an equaliser behind the headline; then they rotate into a tilted grid at right; the timeline scrolls at left with sticky years; the grid ripples as each year passes.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; WebGL canvas x1 (three.js); smoothed scroll (median 130 px still travelling after input stops); entry gate: Skip. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the split stage grammar: a games and entertainment company page: a click-to-enter logo screen, then a field of yellow 3D bars rises like a city or equaliser behind 'Shaping the future of entertainment, one dream at a time', and the bars tilt into a grid that sits at the right while a year-by-year history scrolls at left. Type: Pretendard, Poppins.
Ground and ink from the measured palette (#000000, #3E3E15, #B2B83F). Motion carries the page through
a field of yellow 3D bars rising behind the mission statement. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL 3D bars

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL 3D bars

## Reference lock

Primary reference/direction: DRIMAGE - Company — A games and entertainment company page: a click-to-enter logo screen, then a field of yellow 3D bars rises like a city or equaliser behind 'Shaping the future of entertainment, one dream at a time', and the bars tilt into a grid that sits at the right while a year-by-year history scrolls at left.
Preserve (3-5 traits): click to enter; field of yellow 3D bars; bars tilt into a side grid; year-by-year timeline; yellow accent on black.
Borrow only (1-2): One abstract 3D field that turns into a side panel; Sticky year headings on a long timeline
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL 3D bars
Reject: Small timeline text; Bars repeat the same motion
Token commitments: palette #000000, #3E3E15, #B2B83F, #1B1B16, #8D913F; type Pretendard, Poppins; engine GSAP + Lenis linked (never vendored).
