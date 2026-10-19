---
title: "TKS"
url: https://www.tks.world/
source_url: https://www.tks.world/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: ""
family: cinematic-youth-accelerator
dna: "Youth innovation program x cinematic photos and big statements"
register: warm photographic
grammar: chaptered editorial
lane: "A youth accelerator page that opens on backlit cinematic portraits of students, overlays huge words ('10 Months', 'Ages 13-17', 'Future Ready') on full-bleed classroom photos, lists stats and program elements in large type, and scatters skill cards around 'Skills for the Future'."
mode: persuade
traits: ["backlit cinematic portrait hero", "huge words over full-bleed photos", "marquee band", "stat list in large type", "skill cards scattered around a heading", "green CTA"]
palette: ["#F2F2F2", "#9D9D93", "#0B0E11", "#4E413B", "#8A8278", "#C6CAB8"]
type: ["Ppneuemontreal"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

A program for teenagers is pitched with film-poster photography: backlit silhouettes, big words laid across real classroom shots. Each key fact gets its own full-bleed frame, so facts read as moments.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Izum Digital).

## What to borrow (principle)

- Give each key program fact its own full-bleed photo with one huge word
- Scatter small skill cards around a central heading

## What to leave

- 60 ScrollTriggers for a fairly simple page
- Small grey body text

## Signature move

Huge program facts ('10 Months', 'Ages 13-17') laid over full-bleed classroom photos.

## Motion

Intro: backlit silhouettes cut between three portraits (~2 s) with a marquee band. Scroll (Lenis, ~150 px glide, 60 ScrollTriggers): intro text with images; '10 Months', 'Ages 13-17', 'Future Ready' over photos that scale; stats list; alumni photo; 'Skills for the Future' with cards drifting in; testimonial; financial aid; 'FAQ PAGE' marquee; 'READY TO JOIN THE NEXT WAVE OF INNOVATORS?'.

Measured (`motion/probe.json`): GSAP 3.15.0; 60 ScrollTriggers; Lenis; 1 video; smoothed scroll (median 152 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a youth accelerator page that opens on backlit cinematic portraits of students, overlays huge words ('10 Months', 'Ages 13-17', 'Future Ready') on full-bleed classroom photos, lists stats and program elements in large type, and scatters skill cards around 'Skills for the Future'. Type: Ppneuemontreal.
Ground and ink from the measured palette (#F2F2F2, #9D9D93, #0B0E11). Motion carries the page through
huge program facts ('10 Months', 'Ages 13-17') laid over full-bleed classroom photos. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — cinematic documentary photos of teenagers learning, backlit

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: cinematic documentary photos of teenagers learning, backlit

## Reference lock

Primary reference/direction: TKS — A youth accelerator page that opens on backlit cinematic portraits of students, overlays huge words ('10 Months', 'Ages 13-17', 'Future Ready') on full-bleed classroom photos, lists stats and program elements in large type, and scatters skill cards around 'Skills for the Future'.
Preserve (3-5 traits): backlit cinematic portrait hero; huge words over full-bleed photos; marquee band; stat list in large type; skill cards scattered around a heading.
Borrow only (1-2): Give each key program fact its own full-bleed photo with one huge word; Scatter small skill cards around a central heading
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: cinematic documentary photos of teenagers learning, backlit
Reject: 60 ScrollTriggers for a fairly simple page; Small grey body text
Token commitments: palette #F2F2F2, #9D9D93, #0B0E11, #4E413B, #8A8278, #C6CAB8; type Ppneuemontreal; engine GSAP + Lenis linked (never vendored).
