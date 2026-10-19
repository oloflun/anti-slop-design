---
title: "Tech Redux - Design Beyond The Screen"
url: https://techredux.co/
source_url: https://techredux.co/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: water-reflection-3d-agency
dna: "3D web studio x giant condensed words rising out of a reflective sea"
register: cinematic dark
grammar: continuous world
lane: "A 3D web studio: a logo with Start on a grid, then a night sea where giant condensed words ('Tech Redux', 'Design', 'Beyond', 'The Screen', 'Studio Showcase') rise and pass over the water with rippling reflections, project laptops floating over the sea with names, then a bento about, testimonials and a contact form."
mode: persuade
traits: ["reflective night sea", "giant condensed words on the water", "rippling reflections", "laptops floating over the sea", "logo prism", "bento about"]
palette: ["#020615", "#273B5D", "#536A7F", "#7891A1", "#ADC8D1", "#142348"]
type: ["Montserrat", "Roboto"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The sea is the stage for every chapter; words and projects pass over it like boats, which unifies a long page.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One reflective ground that every chapter passes over

## What to leave

- Generic bento after the sea

## Signature move

Giant words rising out of a night sea with rippling reflections.

## Motion

Intro: logo on a grid, Start (unlocked) (~2 s). Wheel (Lenis, 1 pin): the camera glides over the water; words rise, slide past and sink; the logo prism hovers; laptops float in with names; the sea fades to the bento.

Measured (`motion/probe.json`): GSAP 3.12.7; 1 pinned sections; Lenis; WebGL canvas x1 (three.js); 1 video; split text; smoothed scroll (median 77 px still travelling after input stops); entry gate: START. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the continuous world grammar: a 3D web studio: a logo with Start on a grid, then a night sea where giant condensed words ('Tech Redux', 'Design', 'Beyond', 'The Screen', 'Studio Showcase') rise and pass over the water with rippling reflections, project laptops floating over the sea with names, then a bento about, testimonials and a contact form. Type: Montserrat, Roboto.
Ground and ink from the measured palette (#020615, #273B5D, #536A7F). Motion carries the page through
giant words rising out of a night sea with rippling reflections. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL water, device mockups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL water, device mockups

## Reference lock

Primary reference/direction: Tech Redux - Design Beyond The Screen — A 3D web studio: a logo with Start on a grid, then a night sea where giant condensed words ('Tech Redux', 'Design', 'Beyond', 'The Screen', 'Studio Showcase') rise and pass over the water with rippling reflections, project laptops floating over the sea with names, then a bento about, testimonials and a contact form.
Preserve (3-5 traits): reflective night sea; giant condensed words on the water; rippling reflections; laptops floating over the sea; logo prism.
Borrow only (1-2): One reflective ground that every chapter passes over
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL water, device mockups
Reject: Generic bento after the sea
Token commitments: palette #020615, #273B5D, #536A7F, #7891A1, #ADC8D1, #142348; type Montserrat, Roboto; engine GSAP + Lenis linked (never vendored).
