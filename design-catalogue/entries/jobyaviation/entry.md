---
title: "Joby Aviation"
url: https://www.jobyaviation.com/
source_url: https://www.jobyaviation.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "consumer-brand"
family: air-taxi-dusk-to-sky
dna: "Electric air taxi x dusk cabin photography, the aircraft taking off over a city, cream editorial chapters and a hand-drawn sky close"
register: warm photographic
grammar: chaptered editorial
lane: "An air-taxi company: a blue loader, a passenger silhouetted against a city at dusk through the cabin window, the camera moving out past the wing and propeller to the aircraft lifting off a pad, a blue panel rising with 'Nowhere to go but up', cream chapters with cabin portraits and a passenger beside the aircraft, a statement where words fade from grey, 'Technology that makes the dream possible' over a wing, news, partner categories with the aircraft, 'The sky was never the limit', then 'Dream of flight' on blue with drawn clouds and an illustrated city skyline with people on a terrace."
mode: persuade
traits: ["cabin-window dusk photography", "camera pull-out from window to aircraft", "blue panel rising", "drawn clouds and illustrated city close"]
palette: ["#423E3C", "#060404", "#D9C8BA", "#695B52", "#007BE5", "#C5AE9F"]
type: ["jobyText", "jobyDisplay"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Starting inside the cabin and pulling out to the aircraft shows the passenger's experience before the machine.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Bruno Arizio, TinyWins).

## What to borrow (principle)

- Start inside the experience, then reveal the machine

## What to leave

- Cookie bar on every frame

## Signature move

A passenger silhouetted at a cabin window above a dusk skyline.

## Motion

Intro: blue loader (~2 s). Wheel (Lenis): video scrubbed from cabin to takeoff; the blue panel rises; text lights by word; clouds drift.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; 1 video; split text; smoothed scroll (median 213 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: an air-taxi company: a blue loader, a passenger silhouetted against a city at dusk through the cabin window, the camera moving out past the wing and propeller to the aircraft lifting off a pad, a blue panel rising with 'Nowhere to go but up', cream chapters with cabin portraits and a passenger beside the aircraft, a statement where words fade from grey, 'Technology that makes the dream possible' over a wing, news, partner categories with the aircraft, 'The sky was never the limit', then 'Dream of flight' on blue with drawn clouds and an illustrated city skyline with people on a terrace. Type: jobyText, jobyDisplay.
Ground and ink from the measured palette (#423E3C, #060404, #D9C8BA). Motion carries the page through
a passenger silhouetted at a cabin window above a dusk skyline. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — cinematic photography, illustration

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: cinematic photography, illustration

## Reference lock

Primary reference/direction: Joby Aviation — An air-taxi company: a blue loader, a passenger silhouetted against a city at dusk through the cabin window, the camera moving out past the wing and propeller to the aircraft lifting off a pad, a blue panel rising with 'Nowhere to go but up', cream chapters with cabin portraits and a passenger beside the aircraft, a statement where words fade from grey, 'Technology that makes the dream possible' over a wing, news, partner categories with the aircraft, 'The sky was never the limit', then 'Dream of flight' on blue with drawn clouds and an illustrated city skyline with people on a terrace.
Preserve (3-5 traits): cabin-window dusk photography; camera pull-out from window to aircraft; blue panel rising; drawn clouds and illustrated city close.
Borrow only (1-2): Start inside the experience, then reveal the machine
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: cinematic photography, illustration
Reject: Cookie bar on every frame
Token commitments: palette #423E3C, #060404, #D9C8BA, #695B52, #007BE5, #C5AE9F; type jobyText, jobyDisplay; engine GSAP + Lenis linked (never vendored).
