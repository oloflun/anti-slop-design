---
title: "Share Bien"
url: https://www.sharebien.com/
source_url: https://www.sharebien.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: teal-glow-influencer-agency
dna: "Influencer marketing agency x teal glow and hover-revealed talent"
register: cinematic dark
grammar: chaptered editorial
lane: "An influencer agency on charcoal: a squiggle mark morphs through a counter loader, creator names stream down the hero beside a portrait, services list with photos, campaign cards, a client list lit one name at a time, and a teal glow rising behind the contact address."
mode: persuade
traits: ["morphing squiggle logo loader", "streaming list of creator names", "teal glow ground at the close", "grey-to-white active item in a long client list", "PP Neue Montreal", "Taxi transitions"]
palette: ["#151515", "#495453", "#68817D", "#8FA49F"]
type: ["PP Neue Montreal"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Restraint everywhere except two moments: the logo squiggle morphing through the loader, and a teal light that rises from the bottom at the end like a stage light behind the contact. In between, lists (creators, clients) are the content, lit one name at a time.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Beaucoup).

## What to borrow (principle)

- A colour glow rising from the bottom as the closing light
- A long name list with one name lit per scroll step
- Morph the logo mark during the loader

## What to leave

- Scrambled placeholder text visible mid-animation
- Services section text is very small

## Signature move

A teal glow rising from the bottom of the page behind the contact address.

## Motion

Intro: counter '061 / 100' while the squiggle mark morphs (~2 s). Scroll (Lenis, ~145 px glide, Taxi, SplitText, WebGL): hero with streaming creator names; services list with photo and scrambling labels; campaign cards on a white band; client list where the active brand lights; teal radial glow rises behind the contact email, which scrambles into place; 'Share Bien' outline wordmark at the base.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; Taxi page transitions; WebGL canvas x1 (three.js); 9 video; split text; smoothed scroll (median 146 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: an influencer agency on charcoal: a squiggle mark morphs through a counter loader, creator names stream down the hero beside a portrait, services list with photos, campaign cards, a client list lit one name at a time, and a teal glow rising behind the contact address. Type: PP Neue Montreal.
Ground and ink from the measured palette (#151515, #495453, #68817D). Motion carries the page through
a teal glow rising from the bottom of the page behind the contact address. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — creator portraits and phone-filming moments, cool teal grade

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: creator portraits and phone-filming moments, cool teal grade

## Reference lock

Primary reference/direction: Share Bien — An influencer agency on charcoal: a squiggle mark morphs through a counter loader, creator names stream down the hero beside a portrait, services list with photos, campaign cards, a client list lit one name at a time, and a teal glow rising behind the contact address.
Preserve (3-5 traits): morphing squiggle logo loader; streaming list of creator names; teal glow ground at the close; grey-to-white active item in a long client list; PP Neue Montreal.
Borrow only (1-2): A colour glow rising from the bottom as the closing light; A long name list with one name lit per scroll step
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: creator portraits and phone-filming moments, cool teal grade
Reject: Scrambled placeholder text visible mid-animation; Services section text is very small
Token commitments: palette #151515, #495453, #68817D, #8FA49F; type PP Neue Montreal; engine GSAP + Lenis linked (never vendored).
