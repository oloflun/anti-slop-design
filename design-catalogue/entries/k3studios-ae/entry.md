---
title: "K3 Studios"
url: https://k3studios.ae/
source_url: https://k3studios.ae/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: orange-mono-dubai-agency
dna: "Dubai digital agency x orange stat bands and outline type"
register: cinematic dark
grammar: chaptered editorial
lane: "A dark agency page with orange stat bands, filled-plus-outline condensed headlines (SELECTED / WORK), a numbered case list with screens alternating sides, services and pricing tiers, and a 'LET'S BUILD TOGETHER' close over a marquee."
mode: persuade
traits: ["orange stat band", "filled + outlined condensed caps pairs", "mono numbering (01–07)", "alternating case screenshots", "pricing tiers", "service marquee"]
palette: ["#0C0C0C", "#FEFEFE", "#53392F", "#BCB2AD"]
type: ["JetBrains Mono", "Space Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

A conventional agency structure given rhythm by type: each section title is two lines, one filled and one outlined, and the orange stat bands slide across as breaks. Numbered cases alternate sides so a long list keeps moving.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: k3Studio).

## What to borrow (principle)

- Pair a filled and an outlined line for every section title
- An orange stat band sliding across as a section break

## What to leave

- Generic agency content
- Small grey mono text

## Signature move

Section titles set as a filled line over an outlined line (SELECTED / WORK).

## Motion

Intro: logo mark on black, then 'DIGITAL AGENCY IN DUBAI' (~2 s). Scroll (Lenis, ~140 px glide, 13 ScrollTriggers): orange stat band with counters; 'SELECTED WORK' pins while numbered cases slide in alternating sides; 'WHO WE WORK WITH' cards; services list activating; pricing tiers; marquee and 'LET'S BUILD TOGETHER'.

Measured (`motion/probe.json`): GSAP 3.12.7; 13 ScrollTriggers; Lenis; smoothed scroll (median 138 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a dark agency page with orange stat bands, filled-plus-outline condensed headlines (SELECTED / WORK), a numbered case list with screens alternating sides, services and pricing tiers, and a 'LET'S BUILD TOGETHER' close over a marquee. Type: JetBrains Mono, Space Mono.
Ground and ink from the measured palette (#0C0C0C, #FEFEFE, #53392F). Motion carries the page through
section titles set as a filled line over an outlined line (SELECTED / WORK). Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — case study screenshots on black

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: case study screenshots on black

## Reference lock

Primary reference/direction: K3 Studios — A dark agency page with orange stat bands, filled-plus-outline condensed headlines (SELECTED / WORK), a numbered case list with screens alternating sides, services and pricing tiers, and a 'LET'S BUILD TOGETHER' close over a marquee.
Preserve (3-5 traits): orange stat band; filled + outlined condensed caps pairs; mono numbering (01–07); alternating case screenshots; pricing tiers.
Borrow only (1-2): Pair a filled and an outlined line for every section title; An orange stat band sliding across as a section break
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: case study screenshots on black
Reject: Generic agency content; Small grey mono text
Token commitments: palette #0C0C0C, #FEFEFE, #53392F, #BCB2AD; type JetBrains Mono, Space Mono; engine GSAP + Lenis linked (never vendored).
