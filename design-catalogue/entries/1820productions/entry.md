---
title: "1820 Productions - Video Production Dallas"
url: https://www.1820productions.com/
source_url: https://www.1820productions.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "consumer-brand"
family: production-house-reel-statements
dna: "Video production house x full-bleed reel with short punchy statements"
register: cinematic dark
grammar: rhythmic cutlist
lane: "A Dallas production company: a black logo intro, then full-bleed clips from their spots (Haggar, Dave's Killer Bread, a celebrity dip ad, a falling man in a suit) with a single condensed statement over each ('We listen. We craft. We deliver.', 'Stylish production. Seamless execution.', 'We're not a cult. But people do keep coming back.'), a reel section on bright product shots and 'Brands who swiped right' with client logos."
mode: persuade
traits: ["one condensed statement per full-bleed clip", "clips slide up over each other", "wry copy", "bright product shots in the reel", "black divider bands", "client logo row"]
palette: ["#171515", "#4A3727", "#9EA5A1", "#746E64", "#8C8B82", "#B6BCB9"]
type: ["Suisseintl Condensed", "Suisseintl"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Each clip carries one line of copy, so the reel is also the pitch; the wry lines keep a production house from sounding generic.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Balky Studio).

## What to borrow (principle)

- One short statement per full-bleed clip
- Let clips slide over each other as the section change

## What to leave

- Very small nav and labels
- Black gaps between clips

## Signature move

Full-bleed spots sliding up under one-line condensed statements.

## Motion

Intro: black with the 1820 logo (~1.5 s), the first clip opens. Wheel (Lenis ~120 px glide): each clip slides up over the previous one as a panel; the statement splits in line by line; the 'hype is reel' section cuts to product shots that scale up; logos fade in on black. Barba page transitions.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; Barba page transitions; Taxi page transitions; 4 video; split text; smoothed scroll (median 127 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the rhythmic cutlist grammar: a Dallas production company: a black logo intro, then full-bleed clips from their spots (Haggar, Dave's Killer Bread, a celebrity dip ad, a falling man in a suit) with a single condensed statement over each ('We listen. We craft. We deliver.', 'Stylish production. Seamless execution.', 'We're not a cult. But people do keep coming back.'), a reel section on bright product shots and 'Brands who swiped right' with client logos. Type: Suisseintl Condensed, Suisseintl.
Ground and ink from the measured palette (#171515, #4A3727, #9EA5A1). Motion carries the page through
full-bleed spots sliding up under one-line condensed statements. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — commercial video stills

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: commercial video stills

## Reference lock

Primary reference/direction: 1820 Productions - Video Production Dallas — A Dallas production company: a black logo intro, then full-bleed clips from their spots (Haggar, Dave's Killer Bread, a celebrity dip ad, a falling man in a suit) with a single condensed statement over each ('We listen. We craft. We deliver.', 'Stylish production. Seamless execution.', 'We're not a cult. But people do keep coming back.'), a reel section on bright product shots and 'Brands who swiped right' with client logos.
Preserve (3-5 traits): one condensed statement per full-bleed clip; clips slide up over each other; wry copy; bright product shots in the reel; black divider bands.
Borrow only (1-2): One short statement per full-bleed clip; Let clips slide over each other as the section change
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: commercial video stills
Reject: Very small nav and labels; Black gaps between clips
Token commitments: palette #171515, #4A3727, #9EA5A1, #746E64, #8C8B82, #B6BCB9; type Suisseintl Condensed, Suisseintl; engine GSAP + Lenis linked (never vendored).
