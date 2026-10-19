---
title: "Scheme Engine"
url: https://www.schemeengine.com/
source_url: https://www.schemeengine.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: violet-gradient-production-reel
dna: "Culture-first production company x drifting film cards"
register: cinematic dark
grammar: rhythmic cutlist
lane: "A production company on a violet-to-amber gradient where film stills drift past in depth around a centred statement, then sort into labelled clusters (Commercial, Music, Film & TV, Live) before the closing line."
mode: persuade
traits: ["dark violet/amber gradient ground", "film stills drifting at depth", "centred small statements", "category clusters of stills with director credits", "wide extended caps headings", "Swup transitions"]
palette: ["#080015", "#535461", "#3C2229", "#A4A3A7"]
type: ["lil-gui", "Neuepower Ultra", "Champagne Cartel", "neue-haas-grotesk-display"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The stills never form a grid: they drift through a deep gradient space at different scales and speeds, like flotsam of a reel, and the statements sit still in the middle. When the page reaches the work, the same stills gather into clusters per category, so the drifting becomes an organised index without changing medium.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Let the same media drift loose first and then gather into categories: one move from mood to index
- Gradient ground that changes temperature with the section
- Credits set in small serif caps under each still

## What to leave

- Statement text is small for the space it is given
- Drift can make stills hard to click

## Signature move

Film stills drifting through a violet gradient that later gather into category clusters.

## Motion

Intro: black, then the gradient fades up with a slanted line of text 'from the… we live' sweeping (~3 s). Scroll (Lenis, ~110 px glide, 1 pin, three.js, Observer): stills fly past at varying depth around the statement; statement paragraphs swap with line reveals; 'COMMERCIAL & BRANDED', 'MUSIC', 'FILM & TV', 'LIVE' each pin a cluster of overlapping stills with credits; closing line centred on the gradient.

Measured (`motion/probe.json`): GSAP 3.15.0; 1 pinned sections; Lenis; Swup page transitions; WebGL canvas x1 (three.js); 1 video; smoothed scroll (median 98 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the rhythmic cutlist grammar: a production company on a violet-to-amber gradient where film stills drift past in depth around a centred statement, then sort into labelled clusters (Commercial, Music, Film & TV, Live) before the closing line. Type: lil-gui, Neuepower Ultra, Champagne Cartel, neue-haas-grotesk-display.
Ground and ink from the measured palette (#080015, #535461, #3C2229). Motion carries the page through
film stills drifting through a violet gradient that later gather into category clusters. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — music video and commercial film stills, saturated night colour

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: music video and commercial film stills, saturated night colour

## Reference lock

Primary reference/direction: Scheme Engine — A production company on a violet-to-amber gradient where film stills drift past in depth around a centred statement, then sort into labelled clusters (Commercial, Music, Film & TV, Live) before the closing line.
Preserve (3-5 traits): dark violet/amber gradient ground; film stills drifting at depth; centred small statements; category clusters of stills with director credits; wide extended caps headings.
Borrow only (1-2): Let the same media drift loose first and then gather into categories: one move from mood to index; Gradient ground that changes temperature with the section
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: music video and commercial film stills, saturated night colour
Reject: Statement text is small for the space it is given; Drift can make stills hard to click
Token commitments: palette #080015, #535461, #3C2229, #A4A3A7; type lil-gui, Neuepower Ultra, Champagne Cartel, neue-haas-grotesk-display; engine GSAP + Lenis linked (never vendored).
