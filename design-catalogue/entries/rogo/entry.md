---
title: "Rogo"
url: https://rogo.com
source_url: https://rogo.ai
captured: 2026-09-04
origin: raw-url
raw: raw/32df109fbbb1e1bc-rogo-ai.webp
extract: ok
category: product-focused
category2: institutional
family: dusk-skyline-fintech
dna: "Wall Street dusk cinematography x white-paper product proof"
register: cinematic dark
grammar: filmic one-shot
lane: "A single cinematic dusk photograph of the Manhattan skyline carries a serif claim and a bank-logo wall of trust, then the page drops to a plain white section of paired screenshot tiles and short serif/sans claims"
mode: persuade
traits: ["full-bleed dusk skyline photograph", "serif headline over photo", "white pill CTA", "financial-institution logo wall", "top announcement bar with case-study link", "plain white product section", "paired screenshot-and-claim rows", "conservative serif for stat sentences"]
palette: ["#F7F7F7", "#151515", "#000000", "#737373", "#EEEDEC"]
type: ["ABC Arizona Mix Regular", "Inter"]
measured: designlang
kind: reference-style
source: claude
status: ready
---

## Why it works

The hero borrows the authority register of finance itself rather than SaaS convention: a
single cinematic photograph of Manhattan at dusk (Empire State Building lit, a flag in the
foreground, water in the frame) carries a serif headline ("The AI Platform for Finance")
in white, with no gradient beyond what's needed for legibility. Directly under it, a
row of real, recognisable investment-bank and advisory logos in their native typography
sits on the same dark photograph rather than a separate white strip — proof and pitch
share one frame, the same device the equity-fund and picnic entries in this set use with
photographs and logo walls.

The moment the page leaves the hero, it changes almost every register at once: dark to
white, cinematic to plain, wide serif claim to a two-column layout pairing a short serif
sentence with an actual product screenshot (deal tables, data-room integrations). Nothing
is illustrated or abstracted — every claim is followed immediately by a real interface
tile showing the claim in action, which is a more literal, harder-to-fake form of proof
than an icon or an illustration would be.

A single bold clause inside an otherwise grey sentence ("Rogo changes that.") functions
as this page's version of the italic-accent-word device seen elsewhere in this set —
except here the emphasis tool is weight, not style, keeping the serif consistent while
still marking exactly which words the sentence turns on.

## What to borrow (principle)

- **Put a client-logo wall on the same photographic frame as the hero claim**, not in a
  separate strip — proof arrives in the same breath as the pitch.
- **Follow every marketing claim immediately with an unedited product screenshot**, not an
  illustration or icon — for a credibility-sensitive audience, the real interface is the
  more convincing artifact.
- **Mark emphasis with weight inside one consistent typeface**, rather than switching
  fonts or styles, when the surrounding register (finance, serif, restraint) doesn't
  suit a decorative italic.
- **Change every register at once at the hero boundary** — colour, photography, and
  layout together — so the transition itself signals "now the proof begins."

## What to leave

- The top announcement bar (case-study link) and the cookie-settings panel both compete
  for attention with the primary CTA on first paint in this capture — worth sequencing so
  only one persistent overlay is visible at once.
- Font measurement could not complete live for this entry (the page never reached network
  idle within budget, twice); typeface identification here is read off the image only.
- The screenshot tiles are cropped tightly enough that supporting UI chrome (window
  frames, full context) is lost — convincing as texture, but a viewer can't actually parse
  the interface from the tile alone.

## Signature move

The logo wall on the photograph: trust marks (bank and advisory-firm names) sit directly
on the dusk skyline image rather than in a separate white proof strip, so the claim
("trusted by leading financial institutions") and its evidence occupy the same frame
instead of a claim-then-scroll-for-proof sequence.

## Motion

Motion reads as mixed and notably restrained: the extract confirms only one named
duration and one custom easing curve, both applied narrowly to colour transitions —
there is no fade, slide or scale keyframe in use anywhere. Scroll-linked: yes, though the
mechanism behind that (likely inline/JS-driven reveal rather than CSS `@keyframes`) isn't
directly visible in the extract, so the still-frame reading of a per-section fade-in
remains unconfirmed rather than disproven. The one easing curve in use,
`cubic-bezier(0.44, 0, 0.56, 1)`, is a steep, symmetric ease — slow at both ends, fast
through the middle — with no spring or overshoot. Two keyframes exist in the CSS bundle
(`react-loading-skeleton`, a shimmer sweep; `__framer-loading-spin`, a 360deg rotation)
but neither appears in the "in use" set — both read as loading-state UI, not page motion
(from designlang extract).

| Duration | Easing | Applies to |
|---|---|---|
| 300ms (`md`) | `cubic-bezier(0.44, 0, 0.56, 1)` (13 uses) | colour |

## Brief

Build a finance-sector AI product page opening on one full-bleed cinematic dusk cityscape
photograph, with a serif headline in white and a single white pill CTA. Place a row of
real client/partner logos directly on the same photograph, beneath the headline, rather
than in a separate proof section. Immediately below the fold, switch completely to a
plain white ground: pair every short serif claim sentence with an unedited, real product
screenshot beside it, alternating the image side left-right down the page. Use bold
weight, not italics or a second typeface, to mark the one clause per sentence that
matters most. Keep a persistent top announcement bar for one timely case-study link, but
avoid stacking it with other overlays (cookie banners, chat widgets) on first paint.

## Image recipe

Cinematic dusk or blue-hour cityscape photograph of [SUBJECT] — a financial-district
skyline, a harbour with an iconic building lit against the sky — shot with warm sky tones
fading to a cool dark foreground, a recognisable landmark silhouette, some foreground
texture (water, a flag, a railing) for depth, composed with a clear open band across the
middle third for headline type and a logo row beneath it.

## Photo search

Unsplash first, Pexels second.
- "Manhattan skyline dusk skyline blue hour"
- "financial district cityscape evening"
- "New York harbor dusk skyline"
- "city skyline golden hour water reflection"

## Reference lock

Primary reference/direction: Rogo — cinematic dusk-skyline fintech hero with an on-photo
logo wall, plain white claim-plus-screenshot proof section.
Preserve (3-5 traits): one full-bleed cinematic dusk cityscape photograph carrying the
hero claim in white serif type; a real client/partner logo wall placed on the same
photograph, not a separate strip; a hard register change (dark/photographic to
white/plain) at the fold; every marketing claim paired immediately with an unedited
product screenshot, alternating sides down the page; emphasis marked by bold weight
within one consistent serif, never a second typeface or italic.
Borrow only (1-2): the persistent top announcement bar for a single timely link; the
white pill CTA style against the dark hero.
Role rules: the hero photograph never carries more than headline, CTA and logo row —
no additional copy blocks; every claim below the fold requires a real screenshot beside
it, not an illustration; only one attention-competing overlay (announcement bar, cookie
panel, chat) is visible on first paint at a time.
Media strategy: photo:unsplash — cinematic dusk/blue-hour cityscape photography, warm
sky against cool dark foreground; never a daytime or flatly lit skyline.
Reject: illustrations or icons standing in for real product screenshots; a separate
"trusted by" strip disconnected from the hero photograph; italics or a second display
face for emphasis; multiple simultaneous overlay panels on load.
Token commitments: bg `#F7F7F7`, ink `#151515`, ink-soft `#302F2F`, warm-grey `#776D69`,
stone `#BBB8B6`; serif for headlines and stat sentences, sans for UI labels and body;
emphasis via bold weight only within the serif, never italic or a second face.
