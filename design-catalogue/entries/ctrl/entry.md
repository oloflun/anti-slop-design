---
title: "Ctrl - multichain wallet"
url: https://ctrl.xyz/
source_url: https://ctrl.xyz/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: ""
family: pastel-card-wallet
dna: "Crypto wallet x pale grey page, a phone in the centre with pastel cards sliding around it, green pill buttons"
register: modern clean
grammar: chaptered editorial
lane: "A wallet (with a shutdown notice pinned at the top): 'Take Ctrl.' with the logo inside the type, a phone in the centre while pastel cards (blue, yellow, pink) slide in on both sides with features (create a wallet with Google, gas fees in USDC, one wallet for all your crypto), a list of chains scrolling under '2,500+ chains. One wallet.', 'Capture every opportunity on every chain', asset and NFT cards, trust cards with ratings, 'The secure way to Web3' with security features, FAQ and 'Level up.'."
mode: persuade
traits: ["phone fixed in the centre", "pastel cards sliding beside it", "logo inside the headline", "scrolling chain list", "green pill CTAs"]
palette: ["#E7F2E8", "#B1C0AC"]
type: ["Tomato Grotesk"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Keeping the phone fixed while feature cards slide around it shows every feature in the context of the same screen.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Le Fruit Studio, Ludmilla Maury).

## What to borrow (principle)

- Hold the product screen still and slide features around it

## What to leave

- Shutdown banner over every frame

## Signature move

Pastel feature cards sliding in around a fixed phone.

## Motion

Wheel (Lenis): the phone pins while cards translate in; the chain list scrolls; cards stack.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; 14 video; smoothed scroll (median 157 px still travelling after input stops); entry gate: Close. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a wallet (with a shutdown notice pinned at the top): 'Take Ctrl.' with the logo inside the type, a phone in the centre while pastel cards (blue, yellow, pink) slide in on both sides with features (create a wallet with Google, gas fees in USDC, one wallet for all your crypto), a list of chains scrolling under '2,500+ chains. One wallet.', 'Capture every opportunity on every chain', asset and NFT cards, trust cards with ratings, 'The secure way to Web3' with security features, FAQ and 'Level up.'. Type: Tomato Grotesk.
Ground and ink from the measured palette (#E7F2E8, #B1C0AC). Motion carries the page through
pastel feature cards sliding in around a fixed phone. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — UI, 3D icons

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: UI, 3D icons

## Reference lock

Primary reference/direction: Ctrl - multichain wallet — A wallet (with a shutdown notice pinned at the top): 'Take Ctrl.' with the logo inside the type, a phone in the centre while pastel cards (blue, yellow, pink) slide in on both sides with features (create a wallet with Google, gas fees in USDC, one wallet for all your crypto), a list of chains scrolling under '2,500+ chains. One wallet.', 'Capture every opportunity on every chain', asset and NFT cards, trust cards with ratings, 'The secure way to Web3' with security features, FAQ and 'Level up.'.
Preserve (3-5 traits): phone fixed in the centre; pastel cards sliding beside it; logo inside the headline; scrolling chain list; green pill CTAs.
Borrow only (1-2): Hold the product screen still and slide features around it
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: UI, 3D icons
Reject: Shutdown banner over every frame
Token commitments: palette #E7F2E8, #B1C0AC; type Tomato Grotesk; engine GSAP + Lenis linked (never vendored).
