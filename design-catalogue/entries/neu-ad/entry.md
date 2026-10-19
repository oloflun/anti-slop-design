---
title: "Neu Inc - ad agency (Japan)"
url: https://neu-ad.jp/
source_url: https://neu-ad.jp/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: electric-blue-ribbon-type-agency
dna: "Japanese ad agency x electric blue on white, a 3D ribbon of Japanese slogans twisting through space, a pixel wordmark and blob-framed team photos"
register: other
grammar: chaptered editorial
lane: "An ad agency: electric blue loader with one line of Japanese, then a 3D ribbon printed with slogans ('love and logic', 'hack to win') twisting across white behind the headline in blue boxes, the ribbon breaking into blue blocks, a statement on blue, 'Neu.Inc' in a pixel font that flips and rotates, services on white, team photos in rounded blob frames floating at different depths with illustrated and bear-headed members, 'VIEW' in pixel caps with a spinning badge, news rows with blue bars, and a contact card tumbling over a marquee of slogans."
mode: persuade
traits: ["3D ribbon of slogans", "electric blue and white", "pixel-font wordmark that flips", "blob-framed team photos", "slogan marquee footer"]
palette: ["#FFFFFF", "#1D01FE", "#C7C7E8", "#392EEF"]
type: ["Figtree", "Zen Kaku Gothic New", "BestTen-CRT Bold", "Zen Kaku Gothic New Placeholder"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Printing the agency's own slogans on a twisting ribbon makes its copy the hero image.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: FunTech Inc.).

## What to borrow (principle)

- Turn the brand's own lines into the hero object

## What to leave

- Tiny body copy

## Signature move

A 3D ribbon printed with Japanese ad slogans twisting behind the headline.

## Motion

Intro: blue panel with one line (~2 s). Wheel (Lenis): the ribbon twists and breaks into blocks; the wordmark flips; photos float in parallax; the contact card rotates over the marquee.

Measured (`motion/probe.json`): Lenis; 12 video; smoothed scroll (median 170 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: an ad agency: electric blue loader with one line of Japanese, then a 3D ribbon printed with slogans ('love and logic', 'hack to win') twisting across white behind the headline in blue boxes, the ribbon breaking into blue blocks, a statement on blue, 'Neu.Inc' in a pixel font that flips and rotates, services on white, team photos in rounded blob frames floating at different depths with illustrated and bear-headed members, 'VIEW' in pixel caps with a spinning badge, news rows with blue bars, and a contact card tumbling over a marquee of slogans. Type: Figtree, Zen Kaku Gothic New, BestTen-CRT Bold, Zen Kaku Gothic New Placeholder.
Ground and ink from the measured palette (#FFFFFF, #1D01FE, #C7C7E8). Motion carries the page through
a 3D ribbon printed with Japanese ad slogans twisting behind the headline. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D type ribbon, team photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D type ribbon, team photography

## Reference lock

Primary reference/direction: Neu Inc - ad agency (Japan) — An ad agency: electric blue loader with one line of Japanese, then a 3D ribbon printed with slogans ('love and logic', 'hack to win') twisting across white behind the headline in blue boxes, the ribbon breaking into blue blocks, a statement on blue, 'Neu.Inc' in a pixel font that flips and rotates, services on white, team photos in rounded blob frames floating at different depths with illustrated and bear-headed members, 'VIEW' in pixel caps with a spinning badge, news rows with blue bars, and a contact card tumbling over a marquee of slogans.
Preserve (3-5 traits): 3D ribbon of slogans; electric blue and white; pixel-font wordmark that flips; blob-framed team photos; slogan marquee footer.
Borrow only (1-2): Turn the brand's own lines into the hero object
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D type ribbon, team photography
Reject: Tiny body copy
Token commitments: palette #FFFFFF, #1D01FE, #C7C7E8, #392EEF; type Figtree, Zen Kaku Gothic New, BestTen-CRT Bold, Zen Kaku Gothic New Placeholder; engine GSAP + Lenis linked (never vendored).
