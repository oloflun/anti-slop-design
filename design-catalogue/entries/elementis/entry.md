---
title: "ELEMENTIS - wellness resorts and residences"
url: https://elementis.co/
source_url: https://elementis.co/
captured: 2026-10-03
origin: raw-url
extract: none
category: luxury-craft
category2: "hospitality"
family: wellness-resort-pinned-card
dna: "Wellness resort developer x a pinned beige card over architecture photos"
register: warm photographic
grammar: chaptered editorial
lane: "A wellness resort brand: sage blank (~2 s), a full-bleed film of a woman in a conical hat in a forest with 'Wellness · Innovation · Nature' marquee in thin type, a dark green welcome paragraph with orange highlights, a yoga photo beside 'Personalized wellness, innovation and nature meet in synergy', then a pinned beige card in the centre that changes title and photo (Innovation Culture, Exceptional Wood Construction, Innovative Glass Solutions, World First Climate Control, State-of-the-Art Design) while full-bleed architecture photos change behind it, 'Our story', a retreat marquee, a link list and a sign-up form."
mode: persuade
traits: ["thin type marquee", "pinned centre card over changing backdrops", "dark green and beige", "orange highlight words", "architecture photography at dusk", "link list rows"]
palette: ["#2B352F", "#495851", "#A5A99D", "#050D10"]
type: ["Basis Grotesque"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Pinning one card and swapping both card and backdrop makes five features feel like one calm walk through the building.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Pin a card in the centre and swap card and backdrop together

## What to leave

- Cookie bar in every frame

## Signature move

A beige card pinned centre while resort architecture changes behind it.

## Motion

Intro: sage (~2 s), the forest film with the marquee. Wheel (Lenis, Observer, 1 pin): the marquee slides; the welcome text colours word by word; photos scale; the card pins and its title and image swap while the backdrop crossfades; the retreat marquee runs; rows underline.

Measured (`motion/probe.json`): GSAP 3.12.5; 1 pinned sections; Lenis; 2 video; smoothed scroll (median 107 px still travelling after input stops); entry gate: close. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a wellness resort brand: sage blank (~2 s), a full-bleed film of a woman in a conical hat in a forest with 'Wellness · Innovation · Nature' marquee in thin type, a dark green welcome paragraph with orange highlights, a yoga photo beside 'Personalized wellness, innovation and nature meet in synergy', then a pinned beige card in the centre that changes title and photo (Innovation Culture, Exceptional Wood Construction, Innovative Glass Solutions, World First Climate Control, State-of-the-Art Design) while full-bleed architecture photos change behind it, 'Our story', a retreat marquee, a link list and a sign-up form. Type: Basis Grotesque.
Ground and ink from the measured palette (#2B352F, #495851, #A5A99D). Motion carries the page through
a beige card pinned centre while resort architecture changes behind it. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — resort architecture and wellness photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: resort architecture and wellness photography

## Reference lock

Primary reference/direction: ELEMENTIS - wellness resorts and residences — A wellness resort brand: sage blank (~2 s), a full-bleed film of a woman in a conical hat in a forest with 'Wellness · Innovation · Nature' marquee in thin type, a dark green welcome paragraph with orange highlights, a yoga photo beside 'Personalized wellness, innovation and nature meet in synergy', then a pinned beige card in the centre that changes title and photo (Innovation Culture, Exceptional Wood Construction, Innovative Glass Solutions, World First Climate Control, State-of-the-Art Design) while full-bleed architecture photos change behind it, 'Our story', a retreat marquee, a link list and a sign-up form.
Preserve (3-5 traits): thin type marquee; pinned centre card over changing backdrops; dark green and beige; orange highlight words; architecture photography at dusk.
Borrow only (1-2): Pin a card in the centre and swap card and backdrop together
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: resort architecture and wellness photography
Reject: Cookie bar in every frame
Token commitments: palette #2B352F, #495851, #A5A99D, #050D10; type Basis Grotesque; engine GSAP + Lenis linked (never vendored).
