---
title: "Revelatio"
url: https://revelatio.studio/
source_url: https://revelatio.studio/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: dot-cursor-studio-index
dna: "Brazilian design-and-code studio x dot-matrix team photo"
register: modern clean
grammar: chaptered editorial
lane: "A black-and-white studio page that opens on a dot-matrix team photo, passes a long city list where only the current city lights up, and counts its numbers on rolling digit columns."
mode: persuade
traits: ["dot-matrix halftone video hero", "city list highlighted one name at a time", "rolling digit counters (2020, 40+)", "single small dot cursor", "vertical red side tab", "logo grid"]
palette: ["#000000", "#FFFFFF", "#252320", "#844931", "#C3CAA6"]
type: ["Neue Haas Grotesk Text Pro 55 Roman"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The studio is shown through its people and places rather than work first: a halftone team photo, then a list of thirty cities in grey with one name lit per scroll step, then numbers that roll like odometers. Each device makes a list into a reading with tempo.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Revelatio Studio).

## What to borrow (principle)

- Light one item of a long list at a time with scroll so a list becomes a reading
- Odometer digit columns for key numbers instead of a count-up tween
- Halftone/dot treatment on video for a hero that is texture rather than picture

## What to leave

- Cookie modal over the captured frames
- Very small type in the services lists

## Signature move

Thirty city names in grey where scroll lights one at a time.

## Motion

Intro: black with small corner labels, then the dot-matrix team video fades up with 'Branding, Product Design & Code' (~2 s). Scroll (Lenis, ~170 px glide, Observer, SplitText): the hero video zooms and darkens; services columns reveal per line; red gradient case cards; city list where the active name turns white per step; digits roll for 2020 / 9+ / 0+ / 40+; testimonial; logo grid; news cards; contact. ScrambleText on small labels.

Measured (`motion/probe.json`): GSAP 3.15.0; 1 ScrollTriggers; Lenis; WebGL canvas x1; 1 video; split text; smoothed scroll (median 185 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a black-and-white studio page that opens on a dot-matrix team photo, passes a long city list where only the current city lights up, and counts its numbers on rolling digit columns. Type: Neue Haas Grotesk Text Pro 55 Roman.
Ground and ink from the measured palette (#000000, #FFFFFF, #252320). Motion carries the page through
thirty city names in grey where scroll lights one at a time. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — team and studio photography, high grain, black and white or one warm tint

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: team and studio photography, high grain, black and white or one warm tint

## Reference lock

Primary reference/direction: Revelatio — A black-and-white studio page that opens on a dot-matrix team photo, passes a long city list where only the current city lights up, and counts its numbers on rolling digit columns.
Preserve (3-5 traits): dot-matrix halftone video hero; city list highlighted one name at a time; rolling digit counters (2020, 40+); single small dot cursor; vertical red side tab.
Borrow only (1-2): Light one item of a long list at a time with scroll so a list becomes a reading; Odometer digit columns for key numbers instead of a count-up tween
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: team and studio photography, high grain, black and white or one warm tint
Reject: Cookie modal over the captured frames; Very small type in the services lists
Token commitments: palette #000000, #FFFFFF, #252320, #844931, #C3CAA6; type Neue Haas Grotesk Text Pro 55 Roman; engine GSAP + Lenis linked (never vendored).
