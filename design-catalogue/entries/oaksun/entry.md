---
title: "OAKSUN Studio - Web design and development"
url: https://www.oaksun.studio/
source_url: https://www.oaksun.studio/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: freelance-studio-images-in-words
dna: "Freelance web studio x giant words with images inside and a striped finale"
register: modern clean
grammar: chaptered editorial
lane: "A freelance studio: 'OAKSUN' blurring in, a red gradient with a flowing ribbon, 'PREMIUM WORK' huge on black, case cards stacking, 'SERVICES' with a 3D object inside the word, service cards with 3D renders sliding, 'FEATURED WORK' with an object in the O, an about with a mountain photo, FAQ, an orange call card and a striped 'LET'S WORK' finale."
mode: persuade
traits: ["giant words with objects inside letters", "stacking case cards", "3D service renders", "red gradient ribbon", "striped type finale", "orange call card"]
palette: ["#0F0F0F", "#E4E5E0", "#FFFFFF", "#B69FA5"]
type: ["HKGrotesk", "OsFont"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Putting a 3D object inside each giant word is a consistent device across sections.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Place an object inside the giant section word

## What to leave

- Many familiar devices

## Signature move

'LET'S WORK' in sliced horizontal stripes.

## Motion

Intro: white with the name blurring in (~2 s). Wheel (8 pins): giant words slide sideways; cards stack; service cards slide with renders; the about photo scales; the finale words slice into stripes.

Measured (`motion/probe.json`): GSAP 3.12.7; 8 pinned sections; ScrollSmoother; WebGL canvas x1; 9 video; split text. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a freelance studio: 'OAKSUN' blurring in, a red gradient with a flowing ribbon, 'PREMIUM WORK' huge on black, case cards stacking, 'SERVICES' with a 3D object inside the word, service cards with 3D renders sliding, 'FEATURED WORK' with an object in the O, an about with a mountain photo, FAQ, an orange call card and a striped 'LET'S WORK' finale. Type: HKGrotesk, OsFont.
Ground and ink from the measured palette (#0F0F0F, #E4E5E0, #FFFFFF). Motion carries the page through
'LET'S WORK' in sliced horizontal stripes. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D renders, case screenshots

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D renders, case screenshots

## Reference lock

Primary reference/direction: OAKSUN Studio - Web design and development — A freelance studio: 'OAKSUN' blurring in, a red gradient with a flowing ribbon, 'PREMIUM WORK' huge on black, case cards stacking, 'SERVICES' with a 3D object inside the word, service cards with 3D renders sliding, 'FEATURED WORK' with an object in the O, an about with a mountain photo, FAQ, an orange call card and a striped 'LET'S WORK' finale.
Preserve (3-5 traits): giant words with objects inside letters; stacking case cards; 3D service renders; red gradient ribbon; striped type finale.
Borrow only (1-2): Place an object inside the giant section word
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D renders, case screenshots
Reject: Many familiar devices
Token commitments: palette #0F0F0F, #E4E5E0, #FFFFFF, #B69FA5; type HKGrotesk, OsFont; engine GSAP + Lenis linked (never vendored).
