---
title: "Ashley Brooke CS - creative studio"
url: https://ashleybrookecs.com/
source_url: https://ashleybrookecs.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: bold-caps-red-studio
dna: "Creative studio x white page, a red serif monogram, heavy extended caps and red rule bars marking chapters"
register: editorial print
grammar: typographic poster
lane: "A studio site: a red panel wipes up to the 'ABCS' monogram in red serif, a short positioning line, chapters marked by numbered red bars ('The first thing you should know about us 01'), 'We grew for nine years without a website because we didn't need one' with photos tucked between the lines, a black note card, 'Numbers vendors business plans scopes', 'Most of our client work comes from trusted' with a red scribble, a client list in large type with one name in red, 'We are multilingual, we speak emotion, film', 'What we do' blurring behind service cards that stack."
mode: persuade
traits: ["red serif monogram", "heavy extended caps", "numbered red chapter bars", "photos tucked between headline lines", "client list with one red name", "service cards stacking over blurred type"]
palette: ["#FFFFFF", "#13120E", "#D0CBC4", "#B69891", "#777875", "#E24025"]
type: ["Universo", "Mosvita", "The Patience"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Admitting nine years without a website, in the largest type on the page, does the trust work that a case-study grid usually tries to do.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Ethan Suero).

## What to borrow (principle)

- Say the surprising fact in the biggest type

## What to leave

- Tiny mono labels

## Signature move

'We grew for nine years without a website because we didn't need one' with photos slotted between the words.

## Motion

Intro: red panel wipe (~1 s). Wheel (Lenis, barba, 80 triggers): headlines rise by line; photos slide into the gaps; red bars draw; the scribble draws; type blurs behind stacking cards.

Measured (`motion/probe.json`): GSAP 3.15.0/3.13.0; 80 ScrollTriggers; Lenis; Barba page transitions; split text; smoothed scroll (median 94 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the typographic poster grammar: a studio site: a red panel wipes up to the 'ABCS' monogram in red serif, a short positioning line, chapters marked by numbered red bars ('The first thing you should know about us 01'), 'We grew for nine years without a website because we didn't need one' with photos tucked between the lines, a black note card, 'Numbers vendors business plans scopes', 'Most of our client work comes from trusted' with a red scribble, a client list in large type with one name in red, 'We are multilingual, we speak emotion, film', 'What we do' blurring behind service cards that stack. Type: Universo, Mosvita, The Patience.
Ground and ink from the measured palette (#FFFFFF, #13120E, #D0CBC4). Motion carries the page through
'We grew for nine years without a website because we didn't need one' with photos slotted between the words. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — documentary and set photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: documentary and set photography

## Reference lock

Primary reference/direction: Ashley Brooke CS - creative studio — A studio site: a red panel wipes up to the 'ABCS' monogram in red serif, a short positioning line, chapters marked by numbered red bars ('The first thing you should know about us 01'), 'We grew for nine years without a website because we didn't need one' with photos tucked between the lines, a black note card, 'Numbers vendors business plans scopes', 'Most of our client work comes from trusted' with a red scribble, a client list in large type with one name in red, 'We are multilingual, we speak emotion, film', 'What we do' blurring behind service cards that stack.
Preserve (3-5 traits): red serif monogram; heavy extended caps; numbered red chapter bars; photos tucked between headline lines; client list with one red name.
Borrow only (1-2): Say the surprising fact in the biggest type
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: documentary and set photography
Reject: Tiny mono labels
Token commitments: palette #FFFFFF, #13120E, #D0CBC4, #B69891, #777875, #E24025; type Universo, Mosvita, The Patience; engine GSAP + Lenis linked (never vendored).
