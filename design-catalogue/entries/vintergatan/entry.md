---
title: "Vintergatan"
url: file:///C:/Users/Anton%20L/anti-slop-design/sites/vintergatan.html
captured: 2026-09-03
family: paper-atelier
dna: "Antiquarian ledger x scroll-scrubbed setpiece"
register: editorial print
grammar: chaptered editorial
lane: "Warm paper column carrying a photographic overture, a priced weekly acquisitions ledger and a numbered bindery process, interrupted once by a dark workshop setpiece scrubbed word by word, closing on hours and address"
mode: persuade
traits: ["warm paper ground", "Cormorant Garamond display", "IBM Plex Mono labels", "oxblood + gold accents", "priced ledger rows with FÖRV numbers", "roman-numeral process steps", "dark scrubbed setpiece", "documentary book photography", "Swedish copy"]
palette: ["#F4F0E4", "#F0EBDD", "#E9E3D2", "#211712", "#201610", "#5D5349", "#842A24", "#B45249", "#C8A65F"]
type: ["Cormorant Garamond", "EB Garamond", "IBM Plex Mono"]
kind: example
source: claude
origin: example-site
extract: none
category: editorial
category2: "consumer-brand"
status: ready
---

## Why it works

The page speaks the shop's own vocabulary and refuses to translate it. Acquisitions
carry `FÖRV. 2 311` numbers, a shelf is `HYLLA XIV, TOPOGRAFI OCH RESOR`, a status
is `UNDER BESKRIVNING`, and Monday in the opening-hours table is not a time at all
but the word `verkstadsdag`. None of that is explained. A visitor who knows the
trade is recognised; one who does not learns the trade from the page. That is what
makes it read as a real shop rather than a template with a books photo.

Type is split three ways and never crossed: Cormorant Garamond for display,
EB Garamond for reading, IBM Plex Mono for every label, catalogue number, price
unit and caption. The mono is what carries the ledger feeling — set small, in caps,
letter-spaced, it looks typed rather than designed, which is exactly right for a
record kept at a counter.

Italics are used as a punctuation mark, not as emphasis. Each headline ends with
one italic word in gold — *kvar*, *förvärv*, *till*, *skriv* — always the last
word, always the only coloured thing in the line. One rule, applied four times, and
the page has a voice.

The weekly acquisitions section is the commercial engine and it is set as a plain
ruled table: `.01` index, title in display serif, two lines of condition prose,
catalogue number and status in mono, price at the right with `SEK` in mono beneath.
Five rows, real prices from 340 kr to 48 000 kr. The range is the argument — it
says this is a shop you can walk into, not only a dealer's showroom.

The one dark chapter is placed exactly where a page like this gets tiring, and it
is about the workshop rather than the shop. Ground flips to `#211712`, the labels
stay mono, and three verbs stack — Syr. Lagar. Förgyller. — scrubbed in by scroll
position rather than triggered once. The interruption is earned because the
content genuinely changes rooms.

## What to borrow (principle)

- **Use the trade's own words as UI.** Catalogue numbers, shelf marks, status
  strings and a non-time entry in the hours table do more for credibility than any
  "about us" paragraph.
- **Three faces, three jobs.** Display serif for headlines, text serif for reading,
  mono for every label and number. Mono is what makes a page feel like a record.
- **One italic word per headline, in the accent colour, always last.** A single
  repeatable typographic gesture beats varied emphasis.
- **Price the full range.** Showing 340 kr next to 48 000 kr tells the reader who
  the shop is for; showing only the top price tells them to leave.
- **Guard your reveals.** This page adds the reveal class in JS (so a
  no-JS reader sees everything), marks anything already on screen as revealed at
  mount, and then runs two timeouts — 1.8s for near-viewport elements, 6s for
  everything — that force the un-revealed visible. A scroll animation that cannot
  strand content is the only kind worth shipping.

## What to leave

- The fixed `mix-blend-mode: multiply` grain at 0.45 opacity. Same objection as
  every other page in this family: a permanent composited full-screen layer that
  mostly just dulls the photographs.
- The reveal set is still broad — every `h1, h2, h3, figure, li` outside the
  setpiece. The failsafes make it safe, not necessary. Reveal section openings, not
  list items.
- The scrubbed setpiece is beautiful in place and unreadable in a screenshot, a
  print, a PDF export or a slow scroll — anything that captures a scroll position
  mid-way gets blurred type. If the content matters, it must be legible at every
  scroll offset, not only at the end of one.
- Four consecutive gold italic closers is one more than the device can carry. Two
  land as a signature; four start to read as a mannerism.

## Signature move

The workshop setpiece: at one point the paper ground flips to near-black, and three
verbs — Syr. Lagar. Förgyller. — are scrubbed in word by word as a function of
scroll position, with a hairline "thread" drawing itself down the left. Both
directions work, the CSS resting state is the finished state (so no-JS and
reduced-motion readers get the type outright), and `?preview=setpiece` locks it
open for capture. Ambition and a way out of it, shipped together.

## Brief

Build a Swedish antiquarian bookshop page on warm paper `#F4F0E4` with near-black
`#211712` ink. Set headlines in Cormorant Garamond, body in EB Garamond at
1.05rem/1.75, and every label, catalogue number, price unit and caption in IBM Plex
Mono at 11px, caps, 0.1em tracking. End each headline with one italic word in gold
`#C8A65F`. Open on a full-bleed documentary photograph of shelves with the headline
set into it and a small mono-labelled address block at the lower right. Present the
week's acquisitions as a ruled table: `.01` index, title, two lines of condition
prose, `FÖRV.` number and status in mono, price at the right with `SEK` beneath —
five rows spanning a wide price range. Interrupt once with a full-width near-black
workshop chapter carrying three stacked verbs and a hairline rule. Set the bindery
process as roman-numeraled rows: `i Brevet`, `ii Genomgången`, `iii Arbetet`, each
with one paragraph. Close on a two-column contact panel with an hours table where
one weekday is a word, not a time.

## Image recipe

Documentary photograph of [SUBJECT] in a working antiquarian shop, available light
from a shop window, warm tungsten fill, shallow depth of field with one shelf plane
crisp, muted colour with cream highlights and deep brown shadows, dust and wear
left in, no styling, no props arranged for the camera, no white background, shot at
standing eye level as a customer would see it.

## Photo search

Unsplash first, Pexels second.
- "antiquarian bookshop shelves warm light"
- "old books stacked spines close up"
- "bookbinding workshop hands tools"
- "fountain pen writing ledger paper"

## Reference lock

Primary reference/direction: Vintergatan — warm-paper Swedish antiquarian shop page, Cormorant + EB Garamond + IBM Plex Mono, priced acquisitions ledger, one dark workshop chapter.
Preserve (3-5 traits): warm paper `#F4F0E4` with near-black `#211712` ink; three-way type split (display serif / text serif / mono labels) never crossed; trade vocabulary as UI — catalogue numbers, shelf marks, status strings, a weekday that is a word; the ruled priced acquisitions table spanning a wide price range; exactly one dark full-width workshop chapter.
Borrow only (1-2): the single gold italic closing word per headline; the three-failsafe reveal guard.
Role rules: mono never sets a sentence and never exceeds 11px/0.1em; display serif never sets a label; gold `#C8A65F` only on the italic closing word; oxblood `#842A24` only on acquisition titles; at most two gold italic closers per page.
Media strategy: photo:unsplash — available-light documentary shots of the actual premises and stock, always captioned in mono with shelf mark or catalogue number.
Reject: fixed grain overlays; scroll-scrubbed type on content that must be readable in a screenshot; blanket reveals on list items; a third accent colour; sans-serif anywhere; centred layouts.
Token commitments: papper `#F4F0E4`, benvit `#F0EBDD`, benvit-djup `#E9E3D2`, mörk `#211712`, svart `#201610`, sten `#5D5349`, oxblod `#842A24`, oxblod-ljus `#B45249`, guld `#C8A65F`; display `Cormorant Garamond`, body `EB Garamond`, mono `IBM Plex Mono`; display tracking -0.015em, mono tracking 0.1em at 11px, body 1.05rem/1.75.
