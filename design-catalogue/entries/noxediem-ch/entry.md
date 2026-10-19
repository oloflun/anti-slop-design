---
title: "Noxediem - Video Production Agency Lausanne"
url: https://noxediem.ch/en/
source_url: https://noxediem.ch/en/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: lime-accent-production-studio
dna: "Lausanne production studio x lime accent words and stacking project films"
register: modern clean
grammar: chaptered editorial
lane: "A video production studio on warm white: 'Creative & production STUDIO' with the last word in lime serif, underlined links in the intro, stacking full-width project films (UEFA, Artemis the Lost Temple, Nestle InGenius with a '50 solutions coming to market' title, Cantonal museums), 'The right format to connect with your AUDIENCE', format cards, a services accordion with a lime highlight, the team and clients."
mode: persuade
traits: ["lime accent word in serif", "stacking full-width films", "project titles over film", "services accordion with lime row", "warm white ground", "team photos"]
palette: ["#2B331E", "#F7F8F3", "#A4A37A", "#100D0B", "#777A6E", "#C3C5B9"]
type: ["Everett Bold", "Everett Medium", "Everett Regular", "Ghost"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Stacking films with a title each gives the reel structure, and the single lime accent ties the page together.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: No graphism).

## What to borrow (principle)

- One accent colour used only for the key word of each heading
- Stack project films with the title on each

## What to leave

- Small captions
- Long accordion

## Signature move

Full-width project films stacking under a 'Creative & production STUDIO' headline.

## Motion

Intro: white with the headline (~1 s). Wheel (ScrollSmoother, 4 pins): each film panel slides up over the last and its title moves; the '50 solutions' title scales; the audience heading pins with the lime word; format cards slide in; accordion rows highlight in lime; team photos scroll.

Measured (`motion/probe.json`): GSAP 3.14.2/3.14.2/3.14.2/3.14.2; 4 pinned sections; ScrollSmoother; 19 video; split text. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a video production studio on warm white: 'Creative & production STUDIO' with the last word in lime serif, underlined links in the intro, stacking full-width project films (UEFA, Artemis the Lost Temple, Nestle InGenius with a '50 solutions coming to market' title, Cantonal museums), 'The right format to connect with your AUDIENCE', format cards, a services accordion with a lime highlight, the team and clients. Type: Everett Bold, Everett Medium, Everett Regular, Ghost.
Ground and ink from the measured palette (#2B331E, #F7F8F3, #A4A37A). Motion carries the page through
full-width project films stacking under a 'Creative & production STUDIO' headline. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — commercial and documentary film stills

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: commercial and documentary film stills

## Reference lock

Primary reference/direction: Noxediem - Video Production Agency Lausanne — A video production studio on warm white: 'Creative & production STUDIO' with the last word in lime serif, underlined links in the intro, stacking full-width project films (UEFA, Artemis the Lost Temple, Nestle InGenius with a '50 solutions coming to market' title, Cantonal museums), 'The right format to connect with your AUDIENCE', format cards, a services accordion with a lime highlight, the team and clients.
Preserve (3-5 traits): lime accent word in serif; stacking full-width films; project titles over film; services accordion with lime row; warm white ground.
Borrow only (1-2): One accent colour used only for the key word of each heading; Stack project films with the title on each
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: commercial and documentary film stills
Reject: Small captions; Long accordion
Token commitments: palette #2B331E, #F7F8F3, #A4A37A, #100D0B, #777A6E, #C3C5B9; type Everett Bold, Everett Medium, Everett Regular, Ghost; engine GSAP + Lenis linked (never vendored).
