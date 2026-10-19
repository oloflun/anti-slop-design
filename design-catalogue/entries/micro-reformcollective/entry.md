---
title: "Micro - organised workspace"
url: https://micro.reformcollective.com/
source_url: https://micro.reformcollective.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: ""
family: pill-window-landscape-saas
dna: "Productivity app x pastel landscape painting seen through a pill-shaped window, chrome spheres and a serif statement"
register: cinematic dark
grammar: chaptered editorial
lane: "A productivity app: a pill-outlined wordmark loader with a counter, a pastel painted landscape with pines widening from a card to full screen ('Organized.'), shrinking into a pill-shaped window as chrome spheres float, 'Working hard just got easy' in serif, the app UI rising out of the landscape, cards of synced items, a white pill that grows to fill the screen into a cream section with line-drawn icons, a quote in a dark pill and the landscape returning under a huge wordmark."
mode: persuade
traits: ["pill-shaped window", "painted landscape", "floating chrome spheres", "serif statements", "pill grows to full screen as a transition"]
palette: ["#0F1014", "#FDDDBB", "#474139", "#97ADAD", "#D0D8CF"]
type: ["haffer", "tobias", "fraktion"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The pill shape is the window, the transition and the quote frame, so one form ties a SaaS page together.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Reform Collective).

## What to borrow (principle)

- Use one shape as window, transition and frame

## What to leave

- Very small UI text

## Signature move

A painted pine landscape seen through a pill-shaped window with chrome spheres drifting past.

## Motion

Intro: wordmark counter (~2 s). Wheel (Lenis, 3 pins): the landscape scales into the pill; spheres drift with parallax; UI rises; the white pill expands to a full-screen wipe; the landscape returns.

Measured (`motion/probe.json`): GSAP 3.12.7; 3 pinned sections; Lenis; 7 video; split text; smoothed scroll (median 122 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a productivity app: a pill-outlined wordmark loader with a counter, a pastel painted landscape with pines widening from a card to full screen ('Organized.'), shrinking into a pill-shaped window as chrome spheres float, 'Working hard just got easy' in serif, the app UI rising out of the landscape, cards of synced items, a white pill that grows to fill the screen into a cream section with line-drawn icons, a quote in a dark pill and the landscape returning under a huge wordmark. Type: haffer, tobias, fraktion.
Ground and ink from the measured palette (#0F1014, #FDDDBB, #474139). Motion carries the page through
a painted pine landscape seen through a pill-shaped window with chrome spheres drifting past. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — painted landscape illustration, 3D spheres, UI

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: painted landscape illustration, 3D spheres, UI

## Reference lock

Primary reference/direction: Micro - organised workspace — A productivity app: a pill-outlined wordmark loader with a counter, a pastel painted landscape with pines widening from a card to full screen ('Organized.'), shrinking into a pill-shaped window as chrome spheres float, 'Working hard just got easy' in serif, the app UI rising out of the landscape, cards of synced items, a white pill that grows to fill the screen into a cream section with line-drawn icons, a quote in a dark pill and the landscape returning under a huge wordmark.
Preserve (3-5 traits): pill-shaped window; painted landscape; floating chrome spheres; serif statements; pill grows to full screen as a transition.
Borrow only (1-2): Use one shape as window, transition and frame
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: painted landscape illustration, 3D spheres, UI
Reject: Very small UI text
Token commitments: palette #0F1014, #FDDDBB, #474139, #97ADAD, #D0D8CF; type haffer, tobias, fraktion; engine GSAP + Lenis linked (never vendored).
