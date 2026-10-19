---
title: "12 Studio - digital experience studio"
url: https://www.12.studio/
source_url: https://www.12.studio/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: ""
family: glass-cube-blur-studio
dna: "Digital studio x a glass cube that refracts the work and a service list that sharpens from blur"
register: cinematic dark
grammar: chaptered editorial
lane: "A studio home: 'Loading...' with a percent, 'the digital product, branding, marketing studio' with a glass cube refracting the text, the cube passing over case screens (Seek, a purple isometric town 'Supercharged invoicing'), a brand guidelines strip, 'Pushing boundaries digitally' with letters sharpening from blur, a service list (Branding, Digital Strategy, Marketing Sites, SaaS apps, E-commerce, Experience Sites) whose items sharpen from blur as they arrive, and case cards on purple."
mode: persuade
traits: ["glass cube refraction", "letters sharpening from blur", "service list from blur", "purple accent", "case screens behind the cube", "loading counter"]
palette: ["#111111", "#524773", "#95979F", "#39295E"]
type: ["12 Studio Sans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The glass cube distorting each case as it passes makes the reel feel crafted; the blur-in list reads as focusing.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: 12 Studio).

## What to borrow (principle)

- Bring list items in from blur, letter by letter

## What to leave

- Generic case cards

## Signature move

A glass cube refracting 'the digital branding studio'.

## Motion

Intro: 'Loading...' with percent (~2 s). Wheel: the cube rotates over text and cases; cases scale behind it; letters sharpen from blur; list items sharpen in turn; cards slide.

Measured (`motion/probe.json`): GSAP 3.12.5; WebGL canvas x1 (three.js); 1 video; split text; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a studio home: 'Loading...' with a percent, 'the digital product, branding, marketing studio' with a glass cube refracting the text, the cube passing over case screens (Seek, a purple isometric town 'Supercharged invoicing'), a brand guidelines strip, 'Pushing boundaries digitally' with letters sharpening from blur, a service list (Branding, Digital Strategy, Marketing Sites, SaaS apps, E-commerce, Experience Sites) whose items sharpen from blur as they arrive, and case cards on purple. Type: 12 Studio Sans.
Ground and ink from the measured palette (#111111, #524773, #95979F). Motion carries the page through
a glass cube refracting 'the digital branding studio'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — case screenshots, WebGL glass

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: case screenshots, WebGL glass

## Reference lock

Primary reference/direction: 12 Studio - digital experience studio — A studio home: 'Loading...' with a percent, 'the digital product, branding, marketing studio' with a glass cube refracting the text, the cube passing over case screens (Seek, a purple isometric town 'Supercharged invoicing'), a brand guidelines strip, 'Pushing boundaries digitally' with letters sharpening from blur, a service list (Branding, Digital Strategy, Marketing Sites, SaaS apps, E-commerce, Experience Sites) whose items sharpen from blur as they arrive, and case cards on purple.
Preserve (3-5 traits): glass cube refraction; letters sharpening from blur; service list from blur; purple accent; case screens behind the cube.
Borrow only (1-2): Bring list items in from blur, letter by letter
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: case screenshots, WebGL glass
Reject: Generic case cards
Token commitments: palette #111111, #524773, #95979F, #39295E; type 12 Studio Sans; engine GSAP + Lenis linked (never vendored).
