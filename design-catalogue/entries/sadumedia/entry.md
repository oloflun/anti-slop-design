---
title: "Sadu Media"
url: https://www.sadumedia.com/
source_url: https://www.sadumedia.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: condensed-reel-production
dna: "Saudi production house x poster-condensed type with inline video"
register: cinematic dark
grammar: rhythmic cutlist
lane: "A production house whose huge condensed headlines carry video inside the words, then cuts through full-bleed case films that stack over each other like a reel, alternating dark and light grounds."
mode: persuade
traits: ["ultra-condensed caps display", "inline video and thumbnails set inside lines of type", "full-bleed case films stacking on scroll", "dark/light ground alternation", "teal micro CTA", "mixed-size word lockups"]
palette: ["#ECEEEE", "#0D0D0E", "#4B5356", "#706D63", "#9C9989", "#2A2828"]
type: ["Inter", "Manuka"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The type is the frame: 'WE [video] ARE SADU MEDIA' puts a talking-head clip in the word gap, and 'PRODUCTION / STORYTELLING' lines carry rows of thumbnails between the words. When the page reaches the work it hands over to full-bleed films that slide up over each other, so the reel behaves like an edit, one cut per wheel step.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Beaucoup).

## What to borrow (principle)

- Set media inside the line of type (word gap, between words) so headline and reel are one object
- Stack full-bleed case films so each new one slides over the last: a cut per scroll step
- Grey-to-ink activation down a vertical list of services instead of a static list

## What to leave

- Cookie bar sits over every frame
- Light sections between dark ones flash on a fast scroll

## Signature move

Video playing inside the gap of a giant condensed headline.

## Motion

Intro: dark frame, then 'WE ARE SADU MEDIA' snaps in with the clip already playing in the word gap (~2.5 s). Scroll (Lenis, ~150 px glide): headline lines reveal letter by letter with thumbnail rows sliding in between; 'WE ARE SADU MEDIA' returns huge over a video; 'WORK THAT SPEAKS FOR ITSELF' mixed-size lockup; case films stack, each sliding over the previous with its title centred; logo scatter; PRE-/POST-PRODUCTION list greys out inactive items; closing split 'YOU BRING THE BRIEF / WE'LL BRING IT TO LIFE' around a centred image. Taxi page transitions.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; Taxi page transitions; 13 video; smoothed scroll (median 153 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the rhythmic cutlist grammar: a production house whose huge condensed headlines carry video inside the words, then cuts through full-bleed case films that stack over each other like a reel, alternating dark and light grounds. Type: Inter, Manuka.
Ground and ink from the measured palette (#ECEEEE, #0D0D0E, #4B5356). Motion carries the page through
video playing inside the gap of a giant condensed headline. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — production stills and BTS: cameras, sets, campaign frames, warm and saturated

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: production stills and BTS: cameras, sets, campaign frames, warm and saturated

## Reference lock

Primary reference/direction: Sadu Media — A production house whose huge condensed headlines carry video inside the words, then cuts through full-bleed case films that stack over each other like a reel, alternating dark and light grounds.
Preserve (3-5 traits): ultra-condensed caps display; inline video and thumbnails set inside lines of type; full-bleed case films stacking on scroll; dark/light ground alternation; teal micro CTA.
Borrow only (1-2): Set media inside the line of type (word gap, between words) so headline and reel are one object; Stack full-bleed case films so each new one slides over the last: a cut per scroll step
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: production stills and BTS: cameras, sets, campaign frames, warm and saturated
Reject: Cookie bar sits over every frame; Light sections between dark ones flash on a fast scroll
Token commitments: palette #ECEEEE, #0D0D0E, #4B5356, #706D63, #9C9989, #2A2828; type Inter, Manuka; engine GSAP + Lenis linked (never vendored).
