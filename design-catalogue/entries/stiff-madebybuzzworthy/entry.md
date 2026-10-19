---
title: "Working Stiff Films"
url: https://stiff.madebybuzzworthy.com/
source_url: https://stiff.madebybuzzworthy.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: comedy-production-cartoon-mascots
dna: "Comedy commercial production x cartoon mascots and red slab type"
register: other
grammar: chaptered editorial
lane: "A comedy production company: a script 'S' loader on cream, 'We make LAUGHS that look damn GOOD' in red and cream slab type with a chattering teeth mascot in the O, a column of tilted project cards (Astrology, Rich, Running, Same day, Be your own hero) beside a 'Comedy gold' badge with cartoon eyes, 'In your FEED' with a film-reel mascot and news cards, and 'Hit us UP' with a cartoon car."
mode: persuade
traits: ["red slab display type", "cartoon mascots in the letters", "tilted project cards with titles", "rotating badge with eyes", "charcoal and cream", "news cards strip"]
palette: ["#2B3136", "#EEEBD8", "#A4564E", "#4D4D4C", "#B9B2A2"]
type: ["Grand Bold", "PP Neue Montreal"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The cartoon mascots make 'comedy' visible in every section, and the slab type keeps it bold enough for a production company.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Buzzworthy Studio).

## What to borrow (principle)

- A mascot set inside the headline letters
- A rotating badge as a section emblem

## What to leave

- Long card column
- Small news captions

## Signature move

Chattering teeth set into the O of 'GOOD'.

## Motion

Intro: cream with a script 'S' drawing (~1.5 s). Wheel (ScrollSmoother, 5 pins): the headline pins while project cards scroll up beside it; the badge rotates; cards tilt on hover; 'In your FEED' pins with the reel mascot bobbing; the car drives in at the end.

Measured (`motion/probe.json`): GSAP 3.11.5; 36 ScrollTriggers; 5 pinned sections; ScrollSmoother; 5 video; split text; entry gate: close. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a comedy production company: a script 'S' loader on cream, 'We make LAUGHS that look damn GOOD' in red and cream slab type with a chattering teeth mascot in the O, a column of tilted project cards (Astrology, Rich, Running, Same day, Be your own hero) beside a 'Comedy gold' badge with cartoon eyes, 'In your FEED' with a film-reel mascot and news cards, and 'Hit us UP' with a cartoon car. Type: Grand Bold, PP Neue Montreal.
Ground and ink from the measured palette (#2B3136, #EEEBD8, #A4564E). Motion carries the page through
chattering teeth set into the O of 'GOOD'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — commercial stills, cartoon mascots

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: commercial stills, cartoon mascots

## Reference lock

Primary reference/direction: Working Stiff Films — A comedy production company: a script 'S' loader on cream, 'We make LAUGHS that look damn GOOD' in red and cream slab type with a chattering teeth mascot in the O, a column of tilted project cards (Astrology, Rich, Running, Same day, Be your own hero) beside a 'Comedy gold' badge with cartoon eyes, 'In your FEED' with a film-reel mascot and news cards, and 'Hit us UP' with a cartoon car.
Preserve (3-5 traits): red slab display type; cartoon mascots in the letters; tilted project cards with titles; rotating badge with eyes; charcoal and cream.
Borrow only (1-2): A mascot set inside the headline letters; A rotating badge as a section emblem
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: commercial stills, cartoon mascots
Reject: Long card column; Small news captions
Token commitments: palette #2B3136, #EEEBD8, #A4564E, #4D4D4C, #B9B2A2; type Grand Bold, PP Neue Montreal; engine GSAP + Lenis linked (never vendored).
