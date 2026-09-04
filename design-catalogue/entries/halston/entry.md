---
title: "Halston (architecture template)"
url: https://halston-architecture-template.webflow.io/
source_url: https://halston-architecture-template.webflow.io/
captured: 2026-09-04
origin: raw-url
extract: ok
raw: raw/8e5e088cd4e61aae-screenshot.webp
category: portfolio
category2: ""
family: stone-ledger-atelier
dna: "Architect portrait photography x achievement ledger rows"
register: editorial print
grammar: chaptered editorial
lane: "A stone-grey ground opens on a two-line all-caps claim, drops into a full-bleed portrait of the architect at work with the wordmark overlaid, then a ruled ledger of achievement statistics"
mode: persuade
traits: ["stone-grey ground", "two-line all-caps headline", "small vertical service list", "giant wordmark overlaid on portrait photo", "recognition/award tag", "ruled achievement stat rows with thumbnails", "warm interior/portrait photography", "red accent CTA"]
palette: ["#C9C4BA", "#6B4A33", "#EDE8DD", "#201C18", "#9B2E22"]
type: ["General Sans"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
---

## Why it works

The page opens with restraint before it opens with a photo: a stone-grey band
carries a two-line all-caps claim ("BESPOKE LIVING DEFINED BY CLARITY"), a
short vertical service list (Architecture / Interior Design / Renovation), and
a small "Recognition — DAM Preis 2026" tag, all in plain type with no imagery.
Only after that quiet statement does the page drop into a full-bleed portrait
of the architect at his desk, with the studio's wordmark set giant across the
bottom of the photograph.

Putting the founder's portrait in the hero, rather than a finished building,
reframes the whole studio around a person rather than a product — the desk, the
sketches, the plant, the warm light all read as "here is who makes the
decisions," which is a different trust claim than a glossy exterior shot would
make.

The achievement section is the page's ledger: five stats (`96% Satisfaction`,
`48+ Awards`, `2012 Since`, `180+ Projects`, `12 Countries`) each get their own
ruled row with a small project thumbnail, so the numbers aren't a bare stat
strip — every claim is anchored to a piece of visible work. It reads like a
firm's own internal scorecard made public.

## What to borrow (principle)

- **State your headline claim in plain type before showing any photography** —
  a text-only opening beat lets the claim land without competing with an image.
- **Use a portrait of the person, not the product, as your hero photo** when the
  studio's decision-maker is part of the sell.
- **Overlay the wordmark at giant scale on the hero photograph** rather than in
  a fixed header, so the name and the image read as one composition.
- **Pair every achievement statistic with a small thumbnail of real work**,
  never a bare number, so each claim has visible evidence beside it.

## What to leave

- A "Recognition" tag naming a single, fairly generic-sounding award ("DAM Preis
  2026") without context or a link reads as filler credibility rather than
  earned credibility — it needs a real, checkable reference.
- Five achievement stats in a row risks numeric fatigue; the strongest two or
  three (Awards, Projects) would carry more weight isolated than diluted among
  five.

## Signature move

The portrait-as-hero with the wordmark overlaid: rather than a finished
building or an abstract texture, the founder at his desk — sketches, warm lamp
light, a stool, a laptop — becomes the full-bleed hero image, with the studio
name set giant across the bottom third.

## Motion

(from designlang extract) Feel is "mixed" with scroll-linked motion confirmed.
The captured transitions are quick and plain — `200ms` colour, background and
border-colour changes on hover states, no eased curves beyond the default —
plus one `1ms` allow-discrete overflow transition (a framework artifact, not
content motion). Only one keyframe exists, a generic loading spinner. That
thinness reads consistent with the entry's "text-first, then one photograph"
structure: little UI needs animating, so what the extract captures is state
transitions (link/button colour on hover) rather than the staggered ledger
reveal the layout implies, which — if present — is likely driven by
scroll-triggered JS the static extract can't see.

| token | value | role |
|---|---|---|
| `instant` | 1ms | framework overflow transition |
| `sm` | 200ms | hover/colour state changes |

## Brief

Build a stone-grey architecture-studio page anchored by the founder's portrait.
Open on a text-only band: a two-line all-caps claim, a short vertical service
list, a small recognition tag and a CTA — no imagery yet. Drop into one
full-bleed portrait photograph of the founder at work, with the studio wordmark
set giant across the bottom third and a small "based in [city]" tag in the
corner. Below, build a ruled achievement ledger: 3-5 stat rows, each paired
with a small thumbnail of real project work, dividers between rows. Keep the
palette to stone, warm brown and near-black ink, one small red accent for the
primary CTA only.

## Image recipe

A documentary portrait of a person at [SUBJECT] — a considered desk with warm
lamp light, sketches, natural materials nearby (wood, paper, plants), shot at
a candid three-quarter angle, warm neutral colour grade, shallow depth of field
keeping the subject and immediate desk sharp.

## Photo search

Unsplash first, Pexels second.
- "architect desk sketching warm light portrait"
- "designer studio workspace candid documentary"
- "creative professional at desk natural light"

## Reference lock

Primary reference/direction: Halston — text-first stone-grey opening beat, founder portrait as hero with wordmark overlaid, ruled achievement ledger with thumbnails.
Preserve (3-5 traits): a text-only opening band (headline, service list, recognition tag) before any photography appears; the founder's portrait, not a building, as the full-bleed hero image; studio wordmark overlaid at giant scale on the hero photograph; every achievement statistic paired with a small thumbnail of real work.
Borrow only (1-2): the "based in [city]" location tag; the small vertical service list.
Role rules: red accent reserved for the primary CTA only, never body text or headings; achievement rows always paired with a thumbnail, never a bare number; wordmark overlay used once per page (the hero).
Media strategy: photo:unsplash — warm, candid, documentary portrait photography of a person at work; project thumbnails may be separate interior/exterior shots but must share the hero's warm colour grade.
Reject: a finished-building hero in place of the founder portrait; more than one accent colour; achievement stats presented as a bare number strip with no supporting thumbnail.
Token commitments: stone `#C9C4BA`, warm-brown `#6B4A33`, paper `#EDE8DD`, ink `#201C18`, red-accent `#9B2E22`; `General Sans` for all type, headline in two-line all-caps.
