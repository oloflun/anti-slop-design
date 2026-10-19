---
title: "SOZO21 - Film Production Company"
url: https://www.sozo21.co/
source_url: https://www.sozo21.co/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: film-studio-marquee-stack
dna: "Film production company x giant marquee headline and stacked client films"
register: cinematic dark
grammar: rhythmic cutlist
lane: "A film company site: black, a mono intro line, then a giant 'Cinematic Storytelling for Platforms and Brands' headline that scrolls sideways across several screens, followed by stacking full-width project cards (Amazon Prime, Netflix, Mercedes-AMG F1, Pinterest, DAZN, Apple TV+) and a list of further films."
mode: persuade
traits: ["giant headline scrubbed sideways", "stacking full-bleed project cards", "platform name as card title", "mono descriptions", "black and white only", "hover list of more films"]
palette: ["#000000", "#1C171B", "#4F4645", "#132B4E", "#560316", "#B4B1B0"]
type: ["Inter Variable", "IBM Plex Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The sideways headline turns the tagline into an opening title sequence, and the stacked cards make each film a chapter that slides over the last, which suits a company whose product is films.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Tagline scrubbed sideways as an opening title
- Project cards that stack over each other with the platform as the title

## What to leave

- Long black wait before anything shows
- Mono body text over busy stills

## Signature move

A tagline scrolling sideways across black before the client films stack up.

## Motion

Intro: black with nav only for ~2 s, a mono paragraph fades in over a dim still. Wheel (Lenis ~110 px glide, 1 pin): the giant headline is pinned and scrubbed right to left across ~3 screens, ending as the ground flips to white; project cards then stack, each sliding up over the previous with its still darkening; the list of more films fades in on white.

Measured (`motion/probe.json`): GSAP 3.15.0; 11 ScrollTriggers; 1 pinned sections; Lenis; split text; smoothed scroll (median 106 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the rhythmic cutlist grammar: a film company site: black, a mono intro line, then a giant 'Cinematic Storytelling for Platforms and Brands' headline that scrolls sideways across several screens, followed by stacking full-width project cards (Amazon Prime, Netflix, Mercedes-AMG F1, Pinterest, DAZN, Apple TV+) and a list of further films. Type: Inter Variable, IBM Plex Mono.
Ground and ink from the measured palette (#000000, #1C171B, #4F4645). Motion carries the page through
a tagline scrolling sideways across black before the client films stack up. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — film stills and key art

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: film stills and key art

## Reference lock

Primary reference/direction: SOZO21 - Film Production Company — A film company site: black, a mono intro line, then a giant 'Cinematic Storytelling for Platforms and Brands' headline that scrolls sideways across several screens, followed by stacking full-width project cards (Amazon Prime, Netflix, Mercedes-AMG F1, Pinterest, DAZN, Apple TV+) and a list of further films.
Preserve (3-5 traits): giant headline scrubbed sideways; stacking full-bleed project cards; platform name as card title; mono descriptions; black and white only.
Borrow only (1-2): Tagline scrubbed sideways as an opening title; Project cards that stack over each other with the platform as the title
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: film stills and key art
Reject: Long black wait before anything shows; Mono body text over busy stills
Token commitments: palette #000000, #1C171B, #4F4645, #132B4E, #560316, #B4B1B0; type Inter Variable, IBM Plex Mono; engine GSAP + Lenis linked (never vendored).
