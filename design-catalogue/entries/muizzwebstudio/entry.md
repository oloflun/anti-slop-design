---
title: "Muizz Web Studio"
url: https://muizzwebstudio.com/
source_url: https://muizzwebstudio.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: freelancer-tag-cloud-folio
dna: "Webflow freelancer x falling tool tags and pill shapes"
register: cinematic dark
grammar: chaptered editorial
lane: "A freelancer's sales folio: a circular loader, black and white column wipe, a toggle under the pitch, then tilted rows of tool tags (Framer, GSAP, Webflow, Spline 3D) sliding sideways, an About Me portrait, stat cards, a pill-pattern interlude and a case list with live-site buttons."
mode: persuade
traits: ["column wipe intro", "tilted tool-tag marquees", "giant About Me headline", "stat cards with line art", "pill pattern with 'keep scrolling' badge", "case rows with circular live-site button"]
palette: ["#0C0C0C", "#272523", "#695950", "#FBFBFB", "#BCB9B5"]
type: ["Great Vibes", "Lato", "Playfair Display", "Varela Round"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The tag marquees answer 'what can you build with' in one moving frame, and the column wipe gives a freelancer folio an agency-grade entrance.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Muizz Web Studio).

## What to borrow (principle)

- Tool tags as tilted marquee rows
- Column wipe from loader to page

## What to leave

- Generic stat cards
- Long empty pill interlude

## Signature move

Tilted rows of tool tags sliding sideways across black.

## Motion

Intro: circular loader fills, white columns drop away in a stepped wipe to reveal the pitch (~2 s). Wheel (Lenis ~55 px glide, 2 pins): tag rows slide opposite ways at a tilt; About Me scales down as the portrait rises; stat cards stack; the pill pattern pins with a rotating badge; case rows slide in with circular buttons. Barba page transitions.

Measured (`motion/probe.json`): GSAP 3.12.2; 30 ScrollTriggers; 2 pinned sections; Lenis; Barba page transitions; WebGL canvas x4 (three.js); split text; smoothed scroll (median 55 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a freelancer's sales folio: a circular loader, black and white column wipe, a toggle under the pitch, then tilted rows of tool tags (Framer, GSAP, Webflow, Spline 3D) sliding sideways, an About Me portrait, stat cards, a pill-pattern interlude and a case list with live-site buttons. Type: Great Vibes, Lato, Playfair Display, Varela Round.
Ground and ink from the measured palette (#0C0C0C, #272523, #695950). Motion carries the page through
tilted rows of tool tags sliding sideways across black. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — portrait, line art and site screenshots

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: portrait, line art and site screenshots

## Reference lock

Primary reference/direction: Muizz Web Studio — A freelancer's sales folio: a circular loader, black and white column wipe, a toggle under the pitch, then tilted rows of tool tags (Framer, GSAP, Webflow, Spline 3D) sliding sideways, an About Me portrait, stat cards, a pill-pattern interlude and a case list with live-site buttons.
Preserve (3-5 traits): column wipe intro; tilted tool-tag marquees; giant About Me headline; stat cards with line art; pill pattern with 'keep scrolling' badge.
Borrow only (1-2): Tool tags as tilted marquee rows; Column wipe from loader to page
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: portrait, line art and site screenshots
Reject: Generic stat cards; Long empty pill interlude
Token commitments: palette #0C0C0C, #272523, #695950, #FBFBFB, #BCB9B5; type Great Vibes, Lato, Playfair Display, Varela Round; engine GSAP + Lenis linked (never vendored).
