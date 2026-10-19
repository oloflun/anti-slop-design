---
title: "RoiHeads - iGaming performance marketing"
url: https://roiheads.com/
source_url: https://roiheads.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: stone-head-graffiti-agency
dna: "Marketing agency x carved stone heads, graffiti script and casino props on black with violet and yellow glow"
register: illustrated dark
grammar: chaptered editorial
lane: "A loud agency: a violet loader, 'Delivering high-quality traffic' in condensed caps, 3D stone letters (ASO, UAC, PPC, SEO) tumbling past, a graffiti 'RoiHeads' tag sprayed over a carved stone head, playing cards and casino chips spinning in a violet halo, '01 02 03' giant numerals for values, polaroid team photos, a vacancies list with a scribbled 'Top expert', event polaroids, a yellow halo for the group, and a final 'We don't make drama' where 'drama' is struck and 'traffic' is sprayed in."
mode: persuade
traits: ["3D stone heads and letters", "graffiti script overlays", "casino props in a glow ring", "condensed caps", "polaroids", "struck word replaced by spray"]
palette: ["#0D0C0F", "#DBD5CB", "#948194", "#5403BD", "#563778"]
type: ["Manrope", "Caveat", "Alfredino"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The struck-out 'drama' rewritten as 'traffic' ends a loud page with a joke that is also the positioning.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Tisami).

## What to borrow (principle)

- Close on a sentence that corrects itself

## What to leave

- Too many glows

## Signature move

'We don't make drama' with 'drama' struck and 'traffic' sprayed in violet.

## Motion

Intro: violet panel (~1.5 s). Wheel (Lenis, 72 triggers): stone letters rotate in depth; the graffiti tag draws; cards spin in the halo; numerals slide; the strike and spray draw on scroll.

Measured (`motion/probe.json`): GSAP 3.15.0; 72 ScrollTriggers; Lenis; WebGL canvas x1 (three.js); 29 video; split text; smoothed scroll (median 99 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the chaptered editorial grammar: a loud agency: a violet loader, 'Delivering high-quality traffic' in condensed caps, 3D stone letters (ASO, UAC, PPC, SEO) tumbling past, a graffiti 'RoiHeads' tag sprayed over a carved stone head, playing cards and casino chips spinning in a violet halo, '01 02 03' giant numerals for values, polaroid team photos, a vacancies list with a scribbled 'Top expert', event polaroids, a yellow halo for the group, and a final 'We don't make drama' where 'drama' is struck and 'traffic' is sprayed in. Type: Manrope, Caveat, Alfredino.
Ground and ink from the measured palette (#0D0C0F, #DBD5CB, #948194). Motion carries the page through
'We don't make drama' with 'drama' struck and 'traffic' sprayed in violet. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D stone renders, team photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D stone renders, team photography

## Reference lock

Primary reference/direction: RoiHeads - iGaming performance marketing — A loud agency: a violet loader, 'Delivering high-quality traffic' in condensed caps, 3D stone letters (ASO, UAC, PPC, SEO) tumbling past, a graffiti 'RoiHeads' tag sprayed over a carved stone head, playing cards and casino chips spinning in a violet halo, '01 02 03' giant numerals for values, polaroid team photos, a vacancies list with a scribbled 'Top expert', event polaroids, a yellow halo for the group, and a final 'We don't make drama' where 'drama' is struck and 'traffic' is sprayed in.
Preserve (3-5 traits): 3D stone heads and letters; graffiti script overlays; casino props in a glow ring; condensed caps; polaroids.
Borrow only (1-2): Close on a sentence that corrects itself
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D stone renders, team photography
Reject: Too many glows
Token commitments: palette #0D0C0F, #DBD5CB, #948194, #5403BD, #563778; type Manrope, Caveat, Alfredino; engine GSAP + Lenis linked (never vendored).
