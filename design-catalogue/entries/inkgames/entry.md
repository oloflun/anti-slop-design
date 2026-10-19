---
title: "INK Games"
url: https://inkgames.com/
source_url: https://inkgames.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "playful"
family: mobile-game-studio-tilted-panels
dna: "Mobile game studio x 3D game characters bursting around a condensed headline"
register: other
grammar: chaptered editorial
lane: "A game studio: an octopus logo loader, 'Join the new era of gaming' in heavy condensed type with coins, dice and game characters bursting around it, tilted video panels of the team, a magenta 'Explore the world of prize kingdoms' with floating game tiles, 'Play. Win. Earn.' with three game cards rising, news and a tilted HQ video before a white footer."
mode: persuade
traits: ["heavy condensed uppercase", "3D game assets bursting around the headline", "tilted video panels", "magenta chapter", "three cards rising from colour blocks", "octopus mascot"]
palette: ["#0A0E11", "#C74FFE", "#DBE1D8", "#8E8184", "#4A245B", "#88509E"]
type: ["RuderPlakatLL", "PPNeueMontreal", "PPNeueMontrealMono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The burst of game objects around the headline sells the product's playfulness in one frame, and the tilted panels keep a corporate studio page energetic.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: ToyFight).

## What to borrow (principle)

- Burst the product's objects around the hero headline
- Tilt video panels slightly as they pass

## What to leave

- Generic news section
- White footer feels detached

## Signature move

Coins, dice and game characters bursting around 'Join the new era of gaming'.

## Motion

Intro: black with the octopus mark (~1.5 s), cookie denied; the headline slides in at a skew and objects pop out around it. Wheel (Lenis + ScrollSmoother ~110 px glide, 1 pin): the headline lifts as a tilted video panel rises; the magenta panel slides up with tiles orbiting; coloured blocks rise and become game cards; the HQ video tilts in.

Measured (`motion/probe.json`): GSAP 3.12.7/3.14.2; 1 pinned sections; Lenis; ScrollSmoother; WebGL canvas x1 (three.js); 1 video; smoothed scroll (median 118 px still travelling after input stops); entry gate: Deny Deny, Skip to content. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a game studio: an octopus logo loader, 'Join the new era of gaming' in heavy condensed type with coins, dice and game characters bursting around it, tilted video panels of the team, a magenta 'Explore the world of prize kingdoms' with floating game tiles, 'Play. Win. Earn.' with three game cards rising, news and a tilted HQ video before a white footer. Type: RuderPlakatLL, PPNeueMontreal, PPNeueMontrealMono.
Ground and ink from the measured palette (#0A0E11, #C74FFE, #DBE1D8). Motion carries the page through
coins, dice and game characters bursting around 'Join the new era of gaming'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D game art, team video

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D game art, team video

## Reference lock

Primary reference/direction: INK Games — A game studio: an octopus logo loader, 'Join the new era of gaming' in heavy condensed type with coins, dice and game characters bursting around it, tilted video panels of the team, a magenta 'Explore the world of prize kingdoms' with floating game tiles, 'Play. Win. Earn.' with three game cards rising, news and a tilted HQ video before a white footer.
Preserve (3-5 traits): heavy condensed uppercase; 3D game assets bursting around the headline; tilted video panels; magenta chapter; three cards rising from colour blocks.
Borrow only (1-2): Burst the product's objects around the hero headline; Tilt video panels slightly as they pass
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D game art, team video
Reject: Generic news section; White footer feels detached
Token commitments: palette #0A0E11, #C74FFE, #DBE1D8, #8E8184, #4A245B, #88509E; type RuderPlakatLL, PPNeueMontreal, PPNeueMontrealMono; engine GSAP + Lenis linked (never vendored).
