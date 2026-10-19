---
title: "Sparkk - web agency, Nantes"
url: https://sparkk.fr/
source_url: https://sparkk.fr/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: green-voxel-agency
dna: "Web agency x a swarm of neon green voxels on bottle green that forms a lightning bolt, a floor and an arcade cabinet"
register: illustrated dark
grammar: continuous world
lane: "An agency site on bottle green: a wordmark and SK monogram loader, 'Play with your ideas' behind a WebGL swarm of glowing green cubes, a short agency intro that a pixel wipe clears, project cards (an app grid, a portrait, a pink illustration) carried past on a curve through the swarm, the cubes condensing into a pixel lightning bolt, scattering into a cloud and a 'see our work' tag, a floor of cubes rising under the team line, and finally an arcade cabinet built of the same voxels in front of a client logo wall."
mode: experience
traits: ["neon green voxel swarm", "pixel lightning bolt", "project cards on a curved track", "voxel floor", "arcade cabinet finale", "serif italic emphasis in body"]
palette: ["#06220F", "#50A447", "#DCF1BE", "#9BE865"]
type: ["Fraunces", "aspekta-bold", "aspekta-sm", "aspekta-med"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Every chapter is made of the same cubes regrouping, so a services page reads as one playful toy rather than a list.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Sparkk).

## What to borrow (principle)

- Build every chapter's image out of one recurring particle

## What to leave

- Small body copy over the swarm

## Signature move

Glowing green voxels condensing into a pixel lightning bolt.

## Motion

Intro: wordmark, then the monogram draws (~1.5 s). Wheel (Lenis, smoothed): the voxel swarm reforms per chapter; cards travel a curved path; a pixel wipe swaps panels; the floor rises; the cabinet assembles.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; WebGL canvas x2 (three.js); 1 video; smoothed scroll (median 108 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the continuous world grammar: an agency site on bottle green: a wordmark and SK monogram loader, 'Play with your ideas' behind a WebGL swarm of glowing green cubes, a short agency intro that a pixel wipe clears, project cards (an app grid, a portrait, a pink illustration) carried past on a curve through the swarm, the cubes condensing into a pixel lightning bolt, scattering into a cloud and a 'see our work' tag, a floor of cubes rising under the team line, and finally an arcade cabinet built of the same voxels in front of a client logo wall. Type: Fraunces, aspekta-bold, aspekta-sm, aspekta-med.
Ground and ink from the measured palette (#06220F, #50A447, #DCF1BE). Motion carries the page through
glowing green voxels condensing into a pixel lightning bolt. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL voxels, project screenshots

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL voxels, project screenshots

## Reference lock

Primary reference/direction: Sparkk - web agency, Nantes — An agency site on bottle green: a wordmark and SK monogram loader, 'Play with your ideas' behind a WebGL swarm of glowing green cubes, a short agency intro that a pixel wipe clears, project cards (an app grid, a portrait, a pink illustration) carried past on a curve through the swarm, the cubes condensing into a pixel lightning bolt, scattering into a cloud and a 'see our work' tag, a floor of cubes rising under the team line, and finally an arcade cabinet built of the same voxels in front of a client logo wall.
Preserve (3-5 traits): neon green voxel swarm; pixel lightning bolt; project cards on a curved track; voxel floor; arcade cabinet finale.
Borrow only (1-2): Build every chapter's image out of one recurring particle
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL voxels, project screenshots
Reject: Small body copy over the swarm
Token commitments: palette #06220F, #50A447, #DCF1BE, #9BE865; type Fraunces, aspekta-bold, aspekta-sm, aspekta-med; engine GSAP + Lenis linked (never vendored).
