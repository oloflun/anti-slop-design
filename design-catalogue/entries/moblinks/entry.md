---
title: "Moblinks - dreamwear"
url: https://moblinks.fr/
source_url: https://moblinks.fr/
captured: 2026-10-03
origin: raw-url
extract: none
category: consumer-brand
category2: "playful"
family: melting-yellow-dream-merch
dna: "Streetwear brand x melting yellow topographic rings, a 3D river dive and puzzle pieces"
register: other
grammar: chaptered editorial
lane: "A merch brand: a melting yellow ring pattern around the M logo, the rings opening like a hole into a 3D river that the camera dives along, 'Latest arrivals' cards, a navy band with photos of people in the pieces and 'It will make sense' repeating in colour, a crowd shot, 'Grab the uniform' with product cut-outs, a manifesto in condensed brown caps on a yellow wave, signpost arrows to social links and puzzle pieces filling the screen for the newsletter."
mode: persuade
traits: ["melting topographic rings", "hole into a 3D river dive", "condensed brown caps", "wavy section edges", "puzzle pieces close"]
palette: ["#FFCD04", "#EEDDA8", "#84C3CB", "#769D94", "#B2A16B", "#031A58"]
type: ["Ringold"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Diving through the logo's rings into a dreamlike river sells 'dreamwear' before any product appears.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Antonin Wieczorek, Benjamin Robinet).

## What to borrow (principle)

- Open the hero as a hole the camera dives through

## What to leave

- Tiny product labels

## Signature move

A yellow ring pattern opening into a dive along a 3D river.

## Motion

Wheel (Lenis, smoothed): rings scale into a portal; a scrubbed 3D dive; wave edges morph; the repeating word slides; puzzle pieces fall in.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; 3 video; smoothed scroll (median 143 px still travelling after input stops); entry gate: X. Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a merch brand: a melting yellow ring pattern around the M logo, the rings opening like a hole into a 3D river that the camera dives along, 'Latest arrivals' cards, a navy band with photos of people in the pieces and 'It will make sense' repeating in colour, a crowd shot, 'Grab the uniform' with product cut-outs, a manifesto in condensed brown caps on a yellow wave, signpost arrows to social links and puzzle pieces filling the screen for the newsletter. Type: Ringold.
Ground and ink from the measured palette (#FFCD04, #EEDDA8, #84C3CB). Motion carries the page through
a yellow ring pattern opening into a dive along a 3D river. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D render, fashion photography, cut-outs

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D render, fashion photography, cut-outs

## Reference lock

Primary reference/direction: Moblinks - dreamwear — A merch brand: a melting yellow ring pattern around the M logo, the rings opening like a hole into a 3D river that the camera dives along, 'Latest arrivals' cards, a navy band with photos of people in the pieces and 'It will make sense' repeating in colour, a crowd shot, 'Grab the uniform' with product cut-outs, a manifesto in condensed brown caps on a yellow wave, signpost arrows to social links and puzzle pieces filling the screen for the newsletter.
Preserve (3-5 traits): melting topographic rings; hole into a 3D river dive; condensed brown caps; wavy section edges; puzzle pieces close.
Borrow only (1-2): Open the hero as a hole the camera dives through
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D render, fashion photography, cut-outs
Reject: Tiny product labels
Token commitments: palette #FFCD04, #EEDDA8, #84C3CB, #769D94, #B2A16B, #031A58; type Ringold; engine GSAP + Lenis linked (never vendored).
