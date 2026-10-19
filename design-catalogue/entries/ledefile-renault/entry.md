---
title: "Le Défilé Renault"
url: https://ledefile.renault.com/
source_url: https://ledefile.renault.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: consumer-brand
category2: "hospitality"
family: neon-road-brand-space
dna: "Car-brand venue x a synthwave neon road the loader drives down, then white rounded cards for events, café and store"
register: other
grammar: chaptered editorial
lane: "Renault's flagship space: a language and cookie gate, then a neon synthwave road with a glowing wireframe car driving into the city and the event mark, 'from September 24th' with a neon art car, a line-up carousel, 'plan your visit' with an isometric floor plan, 'more than a century on the Champs' with archive photos, 'le café', 'the Originals store' with fashion photos, 'cars for life lovers' and services."
mode: persuade
traits: ["neon synthwave road intro", "wireframe car", "rounded white cards", "isometric floor plan", "archive photo strip"]
palette: ["#FFFFFF", "#695562", "#02050D", "#AEA69E", "#231931", "#651A32"]
type: ["NouvelR"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

A neon drive into the venue frames a showroom as a destination worth a trip.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: 60fps, LNR).

## What to borrow (principle)

- Arrive at the venue by a short drive in the intro

## What to leave

- Two gates before the intro

## Signature move

A glowing wireframe car driving down a neon road.

## Motion

Intro: gates, then a scrubbed neon drive (~3 s). Wheel: cards rise; carousels drag; archive strip scrolls sideways.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; 6 video; smoothed scroll (median 127 px still travelling after input stops); entry gate: reject cookies, skip the introduction. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: renault's flagship space: a language and cookie gate, then a neon synthwave road with a glowing wireframe car driving into the city and the event mark, 'from September 24th' with a neon art car, a line-up carousel, 'plan your visit' with an isometric floor plan, 'more than a century on the Champs' with archive photos, 'le café', 'the Originals store' with fashion photos, 'cars for life lovers' and services. Type: NouvelR.
Ground and ink from the measured palette (#FFFFFF, #695562, #02050D). Motion carries the page through
a glowing wireframe car driving down a neon road. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D neon render, photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D neon render, photography

## Reference lock

Primary reference/direction: Le Défilé Renault — Renault's flagship space: a language and cookie gate, then a neon synthwave road with a glowing wireframe car driving into the city and the event mark, 'from September 24th' with a neon art car, a line-up carousel, 'plan your visit' with an isometric floor plan, 'more than a century on the Champs' with archive photos, 'le café', 'the Originals store' with fashion photos, 'cars for life lovers' and services.
Preserve (3-5 traits): neon synthwave road intro; wireframe car; rounded white cards; isometric floor plan; archive photo strip.
Borrow only (1-2): Arrive at the venue by a short drive in the intro
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D neon render, photography
Reject: Two gates before the intro
Token commitments: palette #FFFFFF, #695562, #02050D, #AEA69E, #231931, #651A32; type NouvelR; engine GSAP + Lenis linked (never vendored).
