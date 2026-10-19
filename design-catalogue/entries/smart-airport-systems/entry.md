---
title: "Smart Airport Systems - Zero Ground Emissions"
url: https://www.smart-airport-systems.com/
source_url: https://www.smart-airport-systems.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "product-focused"
family: aviation-sustainability-blue
dna: "Ground-power aviation company x a jet engine close-up and line-drawn aircraft toggles"
register: modern clean
grammar: chaptered editorial
lane: "An aviation sustainability company in royal blue: an arctic photo in a blue frame, the logo, a jet engine close-up behind 'Zero Ground Emissions', 'Our journey to ZERO', an APU-off diagram, 'What is the impact of our solutions on CO2 reduction?', a line-drawn aircraft where engine and APU toggles switch off with fans stopping, a giant outline counter of CO2 saved, news, a glacier-and-plane photo for 2050 objectives and a blue arc footer with penguins."
mode: persuade
traits: ["royal blue and white", "line-drawn aircraft diagram with toggles", "giant outline counter", "jet engine close-up", "arctic photography", "mono blue highlights"]
palette: ["#FFFFFF", "#1C1B1C", "#908C86", "#C2C1BD", "#66605C", "#AAA49D"]
type: ["DM Mono", "Bricolage Grotesque"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The aircraft diagram with on/off toggles explains the product (switching engines off on the ground) as an interaction, and the giant counter makes the impact concrete.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Explain the product as toggles on a line diagram
- A giant ticking counter for the impact number

## What to leave

- Small mono body text
- Long news section

## Signature move

A line-drawn aircraft whose engine and APU toggles switch off as you scroll.

## Motion

Intro: blue frame with an arctic photo shrinking to the logo (~2 s), then the engine. Wheel (Lenis): the headline lifts; the white panel rises; the aircraft diagram pins as toggles flip and fan icons stop; the counter rolls up; photos slide; the blue arc rises with penguins.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; 7 video; split text; smoothed scroll (median 144 px still travelling after input stops); entry gate: Enter. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: an aviation sustainability company in royal blue: an arctic photo in a blue frame, the logo, a jet engine close-up behind 'Zero Ground Emissions', 'Our journey to ZERO', an APU-off diagram, 'What is the impact of our solutions on CO2 reduction?', a line-drawn aircraft where engine and APU toggles switch off with fans stopping, a giant outline counter of CO2 saved, news, a glacier-and-plane photo for 2050 objectives and a blue arc footer with penguins. Type: DM Mono, Bricolage Grotesque.
Ground and ink from the measured palette (#FFFFFF, #1C1B1C, #908C86). Motion carries the page through
a line-drawn aircraft whose engine and APU toggles switch off as you scroll. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — aviation and arctic photography, line drawings

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: aviation and arctic photography, line drawings

## Reference lock

Primary reference/direction: Smart Airport Systems - Zero Ground Emissions — An aviation sustainability company in royal blue: an arctic photo in a blue frame, the logo, a jet engine close-up behind 'Zero Ground Emissions', 'Our journey to ZERO', an APU-off diagram, 'What is the impact of our solutions on CO2 reduction?', a line-drawn aircraft where engine and APU toggles switch off with fans stopping, a giant outline counter of CO2 saved, news, a glacier-and-plane photo for 2050 objectives and a blue arc footer with penguins.
Preserve (3-5 traits): royal blue and white; line-drawn aircraft diagram with toggles; giant outline counter; jet engine close-up; arctic photography.
Borrow only (1-2): Explain the product as toggles on a line diagram; A giant ticking counter for the impact number
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: aviation and arctic photography, line drawings
Reject: Small mono body text; Long news section
Token commitments: palette #FFFFFF, #1C1B1C, #908C86, #C2C1BD, #66605C, #AAA49D; type DM Mono, Bricolage Grotesque; engine GSAP + Lenis linked (never vendored).
