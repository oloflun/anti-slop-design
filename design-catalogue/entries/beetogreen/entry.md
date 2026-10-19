---
title: "Beetogreen"
url: https://beetogreen.com/
source_url: https://beetogreen.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: ""
family: lime-loop-bike-benefit
dna: "Company bike benefit x lime loop logo and stacking cards"
register: modern clean
grammar: chaptered editorial
lane: "A company-bike-benefit site that opens with a lime loop drawing itself into the wordmark on dark green, then explains through colour cards that stack and swap as you scroll (Santé, Absentéisme, CO2), a CO2 calculator and a big green loop that winds through the page."
mode: persuade
traits: ["lime loop logo drawn with DrawSVG", "stacking colour cards per benefit", "big green loop graphic crossing sections", "rounded grotesque (Parkinsans)", "CO2 calculator with sliders", "5 pinned sections"]
palette: ["#0B1E17", "#F4F0E3", "#D7AF81", "#4C3E2C", "#5F906A"]
type: ["Parkinsans", "Instrument Sans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

A B2B benefit could be dry; the loop from the logo is used as a ribbon that winds through the page, and benefits come as a deck of coloured cards that stack on top of each other while pinned, one statistic per card. The page stays practical (calculator, FAQ) but every section is entered through a physical motion.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Draw the logo mark in the intro and reuse its stroke as a ribbon later in the page
- Stack benefit cards on top of each other in a pin, one statistic per card
- An interactive calculator as the proof section

## What to leave

- Hero is a generic office photo
- Heavy smoothing (~180 px glide)

## Signature move

A lime loop that draws the logo, then winds through the page as a ribbon.

## Motion

Intro: dark green, a lime loop draws itself and the wordmark 'Beetogreen' writes in (~1.5 s). Scroll (Lenis, ~180 px glide, 5 pins, DrawSVG, SplitText, Observer): office hero with sticky dots; logo marquee; green loop crossing a lavender section; three tabbed colour cards; pinned stack where Santé, Absentéisme, Bien-être and CO2 cards slide up over each other; marketplace card; calculator; map of France; testimonials; closing with a cyclist and the loop.

Measured (`motion/probe.json`): GSAP 3.15.0; 5 pinned sections; Lenis; 1 video; smoothed scroll (median 155 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a company-bike-benefit site that opens with a lime loop drawing itself into the wordmark on dark green, then explains through colour cards that stack and swap as you scroll (Santé, Absentéisme, CO2), a CO2 calculator and a big green loop that winds through the page. Type: Parkinsans, Instrument Sans.
Ground and ink from the measured palette (#0B1E17, #F4F0E3, #D7AF81). Motion carries the page through
a lime loop that draws the logo, then winds through the page as a ribbon. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — natural office and commuting photography, people on bikes

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: natural office and commuting photography, people on bikes

## Reference lock

Primary reference/direction: Beetogreen — A company-bike-benefit site that opens with a lime loop drawing itself into the wordmark on dark green, then explains through colour cards that stack and swap as you scroll (Santé, Absentéisme, CO2), a CO2 calculator and a big green loop that winds through the page.
Preserve (3-5 traits): lime loop logo drawn with DrawSVG; stacking colour cards per benefit; big green loop graphic crossing sections; rounded grotesque (Parkinsans); CO2 calculator with sliders.
Borrow only (1-2): Draw the logo mark in the intro and reuse its stroke as a ribbon later in the page; Stack benefit cards on top of each other in a pin, one statistic per card
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: natural office and commuting photography, people on bikes
Reject: Hero is a generic office photo; Heavy smoothing (~180 px glide)
Token commitments: palette #0B1E17, #F4F0E3, #D7AF81, #4C3E2C, #5F906A; type Parkinsans, Instrument Sans; engine GSAP + Lenis linked (never vendored).
