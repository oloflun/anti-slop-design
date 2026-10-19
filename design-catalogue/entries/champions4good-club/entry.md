---
title: "Champions for Good Club"
url: https://www.champions4good.club/
source_url: https://www.champions4good.club/
captured: 2026-10-03
origin: raw-url
extract: none
category: institutional
category2: "playful"
family: pictogram-athlete-club
dna: "Athletes' network x deep plum, condensed caps in lilac, cut-paper athlete pictograms that move between chapters"
register: illustrated dark
grammar: chaptered editorial
lane: "A club for athletes and executives: 'Network of game changers' in condensed lilac caps on plum, 'No boring networking' assembling on white while a cut-paper basketball player jumps, 'Sondern' with a teal climber, a video 'Voices' quote, an orange archer whose arrow flies to a target that fills the screen ('Neue Chancen für Athleten'), a mission paragraph in huge condensed type with coloured tiles, a lilac cyclist, membership cards fanned, a teal runner and a final golfer pictogram."
mode: persuade
traits: ["cut-paper athlete pictograms", "condensed caps in lilac", "one sport per chapter", "arrow flight transition", "tiles inside a giant paragraph"]
palette: ["#012529", "#22002B", "#F6FBFB", "#2B1808", "#C89CE1", "#613E6D"]
type: ["Neue Montreal", "Druk Condensed Super Desktop"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Each chapter has its own athlete pictogram, so the network's variety is shown as a sequence of sports rather than logos.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Double Play).

## What to borrow (principle)

- Give each chapter its own figure doing one action

## What to leave

- Tiny body copy in caps

## Signature move

An orange archer whose arrow flies into a target that fills the screen.

## Motion

Wheel (Lenis): pictograms animate their action per chapter; type assembles letter by letter; the arrow travels and the target scales; cards fan.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; 2 video; split text; smoothed scroll (median 80 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the chaptered editorial grammar: a club for athletes and executives: 'Network of game changers' in condensed lilac caps on plum, 'No boring networking' assembling on white while a cut-paper basketball player jumps, 'Sondern' with a teal climber, a video 'Voices' quote, an orange archer whose arrow flies to a target that fills the screen ('Neue Chancen für Athleten'), a mission paragraph in huge condensed type with coloured tiles, a lilac cyclist, membership cards fanned, a teal runner and a final golfer pictogram. Type: Neue Montreal, Druk Condensed Super Desktop.
Ground and ink from the measured palette (#012529, #22002B, #F6FBFB). Motion carries the page through
an orange archer whose arrow flies into a target that fills the screen. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — vector pictograms, video

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: vector pictograms, video

## Reference lock

Primary reference/direction: Champions for Good Club — A club for athletes and executives: 'Network of game changers' in condensed lilac caps on plum, 'No boring networking' assembling on white while a cut-paper basketball player jumps, 'Sondern' with a teal climber, a video 'Voices' quote, an orange archer whose arrow flies to a target that fills the screen ('Neue Chancen für Athleten'), a mission paragraph in huge condensed type with coloured tiles, a lilac cyclist, membership cards fanned, a teal runner and a final golfer pictogram.
Preserve (3-5 traits): cut-paper athlete pictograms; condensed caps in lilac; one sport per chapter; arrow flight transition; tiles inside a giant paragraph.
Borrow only (1-2): Give each chapter its own figure doing one action
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: vector pictograms, video
Reject: Tiny body copy in caps
Token commitments: palette #012529, #22002B, #F6FBFB, #2B1808, #C89CE1, #613E6D; type Neue Montreal, Druk Condensed Super Desktop; engine GSAP + Lenis linked (never vendored).
