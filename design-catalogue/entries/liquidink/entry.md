---
title: "Liquidink Design - studio"
url: https://www.liquidink.design/
source_url: https://www.liquidink.design/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: ""
family: blur-scroll-studio-feed
dna: "Design studio x content that blurs as it leaves and sharpens as it arrives"
register: modern clean
grammar: chaptered editorial
lane: "A studio home: a logo loader, a travel app case ('Discover where to next'), 'Creating India's largest local community', a mission statement with a small diagram, recent project tiles, a GitHub community case, news cards, client logos, 'Play at Liquidink', a '2024 Review' video card on grey and black, and a newsletter."
mode: read
traits: ["blur on leaving content", "case tiles", "mission with a tiny diagram", "video review card", "white ground", "dense feed"]
palette: ["#FFFFFF", "#030006", "#554476", "#A5A7AD", "#161D4C", "#ECCEA5"]
type: ["Montserrat", "Literata"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The blur on content leaving the viewport is the only motion idea; the rest is a feed.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase.

## What to borrow (principle)

- Blur what leaves, sharpen what arrives

## What to leave

- Feed without hierarchy

## Signature move

Project tiles blurring as they scroll out of the viewport.

## Motion

Intro: logo on white (~1 s). Wheel: each block blurs as it exits and sharpens as it enters; tiles slide; the review card scales.

Measured (`motion/probe.json`): GSAP 3.15.0; 35 ScrollTriggers; 2 pinned sections; 3 video. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a studio home: a logo loader, a travel app case ('Discover where to next'), 'Creating India's largest local community', a mission statement with a small diagram, recent project tiles, a GitHub community case, news cards, client logos, 'Play at Liquidink', a '2024 Review' video card on grey and black, and a newsletter. Type: Montserrat, Literata.
Ground and ink from the measured palette (#FFFFFF, #030006, #554476). Motion carries the page through
project tiles blurring as they scroll out of the viewport. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — case screenshots

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: case screenshots

## Reference lock

Primary reference/direction: Liquidink Design - studio — A studio home: a logo loader, a travel app case ('Discover where to next'), 'Creating India's largest local community', a mission statement with a small diagram, recent project tiles, a GitHub community case, news cards, client logos, 'Play at Liquidink', a '2024 Review' video card on grey and black, and a newsletter.
Preserve (3-5 traits): blur on leaving content; case tiles; mission with a tiny diagram; video review card; white ground.
Borrow only (1-2): Blur what leaves, sharpen what arrives
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: case screenshots
Reject: Feed without hierarchy
Token commitments: palette #FFFFFF, #030006, #554476, #A5A7AD, #161D4C, #ECCEA5; type Montserrat, Literata; engine GSAP + Lenis linked (never vendored).
