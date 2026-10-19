---
title: "NEWPEACE - visioning company"
url: https://newpeace.jp/
source_url: https://newpeace.jp/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: line-crowd-illustration-agency
dna: "Japanese brand-vision agency x a dense black line illustration of people in neon yellow and pink, a script signature drawn over photos"
register: illustrated dark
grammar: continuous world
lane: "A visioning company: a yellow loader with a hand-drawn heart mark, 'Empowering New Value' in serif over a dense line drawing of people with music, devices and hearts highlighted in neon yellow and pink, the camera travelling through the drawing as a pink line and a yellow heart loop across it, 'Empowering Society' with Japanese copy, an approach diagram of three circles (research, direction, action), services in a dark band with photos, 'We are Newpeace' written in a yellow script across a photo collage, a blog strip and contact cards."
mode: persuade
traits: ["dense black line illustration", "neon yellow and pink highlights", "looping drawn line", "yellow script signature over photos", "serif headlines with Japanese body"]
palette: ["#FFFFFF", "#C9CCBD", "#7F8171", "#B1B2A7", "#423F3B", "#F2FF47"]
type: ["century-old-style-std", "aktiv-grotesk"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Travelling through one huge drawing of people at work gives an abstract 'visioning' company a crowd and a mood.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: STUDIO DETAILS Inc.).

## What to borrow (principle)

- Travel through one large drawing as the page's first chapters

## What to leave

- Floating mail button

## Signature move

A neon yellow line looping through a dense black line drawing of a crowd.

## Motion

Intro: heart mark draws (~1.5 s). Wheel (Lenis): the illustration pans; lines draw along scroll; headlines rise; the script writes itself over the collage.

Measured (`motion/probe.json`): GSAP 3.11.4; Lenis; 7 video; split text; smoothed scroll (median 140 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the continuous world grammar: a visioning company: a yellow loader with a hand-drawn heart mark, 'Empowering New Value' in serif over a dense line drawing of people with music, devices and hearts highlighted in neon yellow and pink, the camera travelling through the drawing as a pink line and a yellow heart loop across it, 'Empowering Society' with Japanese copy, an approach diagram of three circles (research, direction, action), services in a dark band with photos, 'We are Newpeace' written in a yellow script across a photo collage, a blog strip and contact cards. Type: century-old-style-std, aktiv-grotesk.
Ground and ink from the measured palette (#FFFFFF, #C9CCBD, #7F8171). Motion carries the page through
a neon yellow line looping through a dense black line drawing of a crowd. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — line illustration, team photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: line illustration, team photography

## Reference lock

Primary reference/direction: NEWPEACE - visioning company — A visioning company: a yellow loader with a hand-drawn heart mark, 'Empowering New Value' in serif over a dense line drawing of people with music, devices and hearts highlighted in neon yellow and pink, the camera travelling through the drawing as a pink line and a yellow heart loop across it, 'Empowering Society' with Japanese copy, an approach diagram of three circles (research, direction, action), services in a dark band with photos, 'We are Newpeace' written in a yellow script across a photo collage, a blog strip and contact cards.
Preserve (3-5 traits): dense black line illustration; neon yellow and pink highlights; looping drawn line; yellow script signature over photos; serif headlines with Japanese body.
Borrow only (1-2): Travel through one large drawing as the page's first chapters
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: line illustration, team photography
Reject: Floating mail button
Token commitments: palette #FFFFFF, #C9CCBD, #7F8171, #B1B2A7, #423F3B, #F2FF47; type century-old-style-std, aktiv-grotesk; engine GSAP + Lenis linked (never vendored).
