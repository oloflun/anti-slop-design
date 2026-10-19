---
title: "EKLO-Verse"
url: https://ekloverse.com/
source_url: https://ekloverse.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: playful
category2: "editorial"
family: neon-astronaut-scifi-world
dna: "Nepali sci-fi film universe x neon blue HUD and robot mascot"
register: illustrated dark
grammar: chaptered editorial
lane: "A sci-fi film universe behind an 'ENTER THE EKLO-VERSE' neon gate: a 3D rusty robot astronaut stays in frame while 'TWO RETURN. ONE REMAINS. HE AWAKENS.' and chapters (About, The Casts, The Company, The Auteur) set in mono with blue glitch highlights, cast faces orbiting a planet."
mode: experience
traits: ["neon blue glitch title words", "3D robot mascot persistent in frame", "mono typewriter body", "cast avatars orbiting a planet", "dark navy ground with grain", "5 pinned chapters"]
palette: ["#04060A", "#372A27", "#63636B"]
type: ["Inter Variable", "JetBrains Mono Variable", "Noto Serif Devanagari"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

One 3D character stays in frame through every chapter, so the page feels like a guide walking you through the universe. Chapter words glitch in blue like a terminal, and the cast becomes an orbit of faces around a planet.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Qriousco Tech).

## What to borrow (principle)

- Keep one 3D character in frame as a guide across all chapters
- Arrange a cast as avatars orbiting a central planet
- Glitch-highlight the key word of each chapter title

## What to leave

- Gate before content
- Mono body text is dense

## Signature move

A rusty robot astronaut that stays beside the reader through every chapter.

## Motion

Gate: 'ENTER THE EKLO-VERSE' neon with 'Start the journey'. Then a film still with 'TWO RETURN. ONE REMAINS. HE AWAKENS.'; the robot rises and stays. Scroll (5 pins, WebGL): 'ABOUT EKLO-VERSE' frame draws and fills with text; 'THE CASTS' with avatars orbiting a planet; 'THE COMPANY' logo panel; 'THE AUTEUR' portrait; 'NEXT TRANSMISSION' glitch.

Measured (`motion/probe.json`): GSAP 3.15.0; 5 pinned sections; WebGL canvas x1 (three.js); 1 video; smoothed scroll (median 120 px still travelling after input stops); entry gate: Start the journey. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the chaptered editorial grammar: a sci-fi film universe behind an 'ENTER THE EKLO-VERSE' neon gate: a 3D rusty robot astronaut stays in frame while 'TWO RETURN. ONE REMAINS. HE AWAKENS.' and chapters (About, The Casts, The Company, The Auteur) set in mono with blue glitch highlights, cast faces orbiting a planet. Type: Inter Variable, JetBrains Mono Variable, Noto Serif Devanagari.
Ground and ink from the measured palette (#04060A, #372A27, #63636B). Motion carries the page through
a rusty robot astronaut that stays beside the reader through every chapter. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D character render, film stills, neon UI

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D character render, film stills, neon UI

## Reference lock

Primary reference/direction: EKLO-Verse — A sci-fi film universe behind an 'ENTER THE EKLO-VERSE' neon gate: a 3D rusty robot astronaut stays in frame while 'TWO RETURN. ONE REMAINS. HE AWAKENS.' and chapters (About, The Casts, The Company, The Auteur) set in mono with blue glitch highlights, cast faces orbiting a planet.
Preserve (3-5 traits): neon blue glitch title words; 3D robot mascot persistent in frame; mono typewriter body; cast avatars orbiting a planet; dark navy ground with grain.
Borrow only (1-2): Keep one 3D character in frame as a guide across all chapters; Arrange a cast as avatars orbiting a central planet
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D character render, film stills, neon UI
Reject: Gate before content; Mono body text is dense
Token commitments: palette #04060A, #372A27, #63636B; type Inter Variable, JetBrains Mono Variable, Noto Serif Devanagari; engine GSAP + Lenis linked (never vendored).
