---
title: "Calyx"
url: file:///C:/Users/Anton%20L/anti-slop-design/sites/calyx.html
captured: 2026-09-03
family: paper-atelier
dna: "Print catalogue x mono ledger"
register: editorial print
grammar: gallery/catalog
lane: "Full-bleed photographic overture, then a quiet paper column that scrolls as a numbered, priced catalogue and closes on one dark panel"
mode: persuade
traits: ["cream paper ground", "Cardo display italic", "PT Mono kickers", "12-col editorial grid", "numbered priced index rows", "rust drop caps", "full-bleed photo plates", "dark closing panel", "fixed multiply grain"]
palette: ["#F7F3EB", "#ECE7DE", "#12120B", "#24251D", "#585951", "#893F28", "#5D7A66", "#1A4129"]
type: ["Cardo", "PT Mono"]
kind: example
source: claude
origin: example-site
extract: none
category: editorial
category2: "luxury-craft"
status: ready
---

## Why it works

The page behaves like a printed commission catalogue, not a website. One typeface
pair does all the work: Cardo carries every voice — roman for the hero, italic for
headlines, pull quotes and product names — and PT Mono, tracked out at 0.22em and
never larger than 11px, carries every label, caption, counter and address. Because
the mono is reserved strictly for metadata, the reader learns the code in one
screen: serif is the studio talking, mono is the ledger.

The photography is never decorative filler. The hero is a single full-bleed
bouquet with the headline set straight onto it; every subsequent image is a plate
with a commission number, a location and a `02 / 14` counter beneath it. Images
are made to look like documentation, which is exactly what a florist selling
site-specific work needs to prove.

The economic centre of the page is the boldest move: an index of eleven cuttings
with real names, real ingredient lists and real prices in SEK, ruled like a
catalogue. Nothing on the page persuades harder than showing the price.

The 12-column grid is used asymmetrically and honestly — labels sit in columns 1-3,
content in 4-12, with a hairline rule under each kicker. The empty left column is
the luxury signal; nothing is centred to fill it.

## What to borrow (principle)

- **One serif, one mono, a hard rule between them.** Serif = voice, mono = record.
  Never let the mono grow past caption size, never let the serif carry a label.
- **Price the work in public.** A ruled index of named items with numbers, spec
  line and price does more selling than any hero claim.
- **Caption every image like an archive.** `CMSN. 0211 — HOTEL PIGALLE,
  DROTTNINGGATAN` plus a `02 / 14` counter converts a stock photo into evidence.
- **Reserve exactly one accent.** Rust `#893F28` appears only on drop caps and one
  product title; everything else is ink on paper.
- **End on inversion, once.** A single dark panel at the close makes the
  commission CTA feel like a different room, not a louder button.

## What to leave

- The fixed `mix-blend-mode: multiply` grain overlay at 0.5 opacity — it costs a
  full-screen composited layer for a texture most viewers never consciously see,
  and it dulls photography that was already muted.
- The blanket reveal: `document.querySelectorAll('section, h1, h2, h3, blockquote,
  figure, li')` all get a 1.2s transition. Everything animating means nothing is
  emphasised, and long index lists stagger awkwardly.
- Copy that overwrites its own restraint ("The eleventh is a wedding.", "smells
  like a memory"). One or two of these read as craft; four in a row read as
  costume.
- Text set directly on a busy bouquet, held up only by a drop shadow. It survives
  here because the crop happens to be dark on the left — it would fail on a lighter
  photo. Use a scrim or a dedicated plate.

## Signature move

The commission counter. Every image plate carries a mono caption on the left and a
`NN / 14` counter on the right, so the page reads as a numbered run of real jobs
with a finite capacity — reinforced by the copy ("We accept eleven commissions a
week"). Scarcity stated as bookkeeping, not as a badge.

## Brief

Build a cream-paper editorial catalogue for a small studio that sells finite,
named, site-specific work. Set everything in one old-style serif (Cardo) — roman
for display, italic for headlines and product names — with a single tracked-out
monospace at caption size for all labels, numbers and addresses. Ground is warm
off-white `#F7F3EB`; ink is a near-black olive `#12120B`; exactly one accent, a
rust `#893F28`, used only for drop caps and one title. Open on a full-bleed
photograph with the headline in cream serif set into it, mixing roman and italic
lines. Below the fold, drop to a 12-column grid where mono kickers sit in columns
1-3 under a hairline rule and content runs 4-12; keep the left column empty. Show
work as captioned plates with commission numbers and an `NN / total` counter.
Centre the page on a ruled index of named items with ingredient lines, spec and
price. Close on one full-width dark panel with the contact address and nothing
else.

## Image recipe

Documentary still life of [SUBJECT], shot on medium format film, natural north
window light, shallow depth of field with one plane crisp and the rest falling
soft, muted desaturated colour with warm cream highlights and cool green shadows,
no styling props, no studio strobe, no gradient background — the object as
delivered, photographed where it will live. Slight overexposure in the highlights,
grain retained.

## Photo search

Unsplash first, Pexels second.
- "florist bouquet natural light film"
- "flowers in vase window light muted"
- "wildflowers close up shallow depth of field"
- "wedding table arrangement documentary"

## Reference lock

Primary reference/direction: Calyx — cream paper atelier catalogue, Cardo + PT Mono, priced index as centrepiece.
Preserve (3-5 traits): warm cream ground `#F7F3EB` with near-black olive ink `#12120B`; Cardo for all voice, PT Mono at caption size for all metadata; 12-col grid with empty left column and hairline rules under kickers; numbered/priced index rows as the page's centre; captioned image plates with `NN / total` counters.
Borrow only (1-2): rust `#893F28` drop caps; the single dark closing panel.
Role rules: serif never labels, mono never speaks; mono capped at 11px and 0.22em tracking; accent rust on at most two elements per page; headline mixes roman and italic lines only in the hero.
Media strategy: photo:unsplash — documentary stills of real work, always captioned with a reference number and counter; never a generic hero stock frame.
Reject: fixed grain overlays; blanket scroll reveals on every element; centred layouts; a second accent colour; sans-serif of any kind; drop-shadowed text over busy photography without a scrim.
Token commitments: bg `#F7F3EB`, bg-tint `#ECE7DE`, ink `#12120B`, ink-soft `#24251D`, stone `#585951`, rust `#893F28`, green-mid `#5D7A66`, green-deep `#1A4129`; display `Cardo`, mono `PT Mono`; display leading 0.92-1.04, display tracking -0.02em, kicker tracking 0.22em; grid 12-col, max-width 1480px, gutter 32px.
