---
title: "Flowstack (before / AI slop control)"
url: file:///C:/Users/Anton%20L/anti-slop-design/sites/before-ai-slop.html
captured: 2026-09-03
family: saas-default
dna: "Tailwind defaults x pitch deck"
register: modern clean
grammar: none
lane: "Floating pill nav, split hero with a fake dashboard card, three icon cards, a four-number stat band, a centred CTA and a one-line footer — the default vertical stack, nothing else"
mode: persuade
traits: ["floating pill nav", "indigo-to-violet gradient", "Inter everything", "split hero with dashboard mock", "three icon feature cards", "unsourced stat band", "greyed fake logo row", "centred closing CTA", "made with love footer"]
palette: ["#FBFAF7", "#FFFFFF", "#6366F1", "#8B5CF6", "#EC4899", "#F59E0B", "#1E40AF", "#1F2937"]
type: ["Inter"]
kind: antipattern
source: claude
origin: example-site
extract: none
category: product-focused
category2: ""
status: ready
---

## Why it works

It is included as the control, not as a target — but it is worth being honest about
what it gets right, because that is what makes it the default.

The information order is correct: what it is, who trusts it, what it does, what it
produced, what to do next. Every element is legible, the hierarchy is
unambiguous, contrast passes, the tap targets are large, and it will render
identically in every browser on every device. A team with no designer ships this in
an afternoon and it will not embarrass them.

That is the whole of the case. Everything competent here is competence available
from a template; nothing on the page could only have come from this company.

## What to borrow (principle)

- **The section order.** Promise → proof → capability → result → ask. The sequence
  is right; it is the content poured into it that is empty.
- **One typeface, sized properly.** Inter at 16/1.6 for body and a heavy weight for
  display is a legitimate, boring, working system.
- **A visible primary action in the nav and again at the close.** Two asks, same
  words, no third.

## What to leave

Nearly all of it. Catalogued here so the specific tells are nameable:

- **Claims with no referent.** "10x faster shipping", "50% cost reduction", "10,000+
  teams", "99.99% uptime SLA" — four numbers, no source, no customer, no method. A
  reader who believes them learns nothing; a reader who doesn't discounts the whole
  page. Compare with the entries in this catalogue that print real prices and real
  inventory numbers.
- **The greyed logo row of invented companies.** ACME, NEXUS, QUANTUM, HORIZON.
  Social proof that proves nothing, in the exact grey-at-40 % treatment every SaaS
  page uses.
- **The indigo-to-violet gradient** on the logo mark, the icon tiles and the chart
  fill. It is the single most over-used colour move of the period and it carries no
  meaning here — nothing is indigo about this product.
- **Three icon cards in a row.** Lightning bolt, link, rocket; "Lightning fast",
  "Seamless integrations", "Next-gen automation". The icons illustrate the adjective,
  not the product, and the adjectives are interchangeable with any competitor's.
- **The fake dashboard card.** A screenshot-shaped rectangle with plausible metrics
  and a smooth two-line area chart. It shows the product's chrome and none of its
  work.
- **Language that could describe anything.** "All-in-one platform for modern teams",
  "elevate", "unleash", "transform your workflow", "ship faster". Delete the logo and
  no reader could name the category.
- **Everything centred.** Section heading centred, subhead centred, stat band
  centred, CTA centred, footer centred. Centring is the layout you get when no
  decision has been made about where the reader's eye should start.
- **`Made with ❤️ in San Francisco`.** The last line of the page is a stock
  sentiment.

## Signature move

There isn't one, and that is the finding. Every element on the page is the highest-
probability element for its slot: the pill nav, the badge above the headline, the
gradient word inside the headline, the two-button hero, the avatar cluster, the
logo row, the icon triptych, the stat band, the centred CTA. Nothing was chosen
against the average. Keep this entry as the measuring stick: if a new page can be
described entirely by naming its slots, it has landed here.

## Brief

Reproduce only as a control. Build a single-column SaaS landing page on near-white
`#FBFAF7`, everything in Inter. Floating white pill nav with six links, a text
"Sign in" and a dark "Start free" pill. Split hero: small pill badge, a three-line
headline at ~4rem/1.05 with one phrase in indigo `#6366F1`, a two-line grey
subhead, a dark primary button and a ghost "Watch demo", an avatar cluster with
"Trusted by 10,000+ teams"; on the right a white rounded card with four metric
labels and a soft indigo area chart. Then a greyed row of six invented company
names, three white icon cards with gradient tiles, a four-figure stat band in
indigo, a centred CTA section, and a one-line footer. Centre every section
heading. Do not name a real customer, cite a source or show the product working.

## Image recipe

None — the page contains no photography, and that is part of the diagnosis. Its
only "image" is a rounded rectangle mocking a dashboard, drawn in CSS with a
gradient area chart. If you must reproduce it: flat white card, 16px radius, soft
shadow, four label/number pairs in a row, one smooth two-series area chart in
indigo and amber, no axis labels, no gridlines, no real data.

## Photo search

Not applicable — the control page uses no photography. Any entry in this catalogue
that does is a better source of direction.

## Reference lock

Primary reference/direction: NEGATIVE reference. Flowstack — the default AI-generated SaaS landing page. Never use as direction; use to detect drift toward it.
Preserve (3-5 traits): nothing.
Borrow only (1-2): the section order (promise → proof → capability → result → ask); one typeface used consistently.
Role rules: if a page under construction acquires a pill nav, a gradient word in the headline, an icon triptych, an unsourced stat band or a greyed row of invented logos, it has drifted here and the direction must be re-derived from the brand's own evidence.
Media strategy: placeholder — the control has no real imagery, which is the point.
Reject: indigo-to-violet gradients; unsourced metrics; invented customer logos; icon cards illustrating adjectives; fake dashboard mocks; centred everything; "all-in-one", "seamless", "next-gen", "elevate", "unleash", "transform"; "Made with ❤️ in <city>".
Token commitments: none — this entry commits no tokens. Recorded palette (`#FBFAF7`, `#6366F1`, `#8B5CF6`, `#EC4899`, `#F59E0B`, `#1F2937`) exists so the combination can be recognised and avoided.
