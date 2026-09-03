# Photo sources — licenses and the contact-sheet method

Load when Step 5b's photo pipeline is in play. Corrects a license error in
[`assets.md`](assets.md) **without editing that file** — `assets.md` is a
byte-identical upstream port and stays untouched; read this instead for licensing.

**The correction.** `assets.md`'s Photography table lists Unsplash as "CC0." It
is not, and hasn't been since 2017. Unsplash photos ship under the **Unsplash
License**: free for commercial and noncommercial use, no attribution required —
but you may not sell unmodified copies, and you may not compile Unsplash photos
into a competing stock-photo or wallpaper service. That's narrower than CC0, which
places work fully in the public domain with no such restrictions.

## Licenses, per source

| Source | License | Notes |
|---|---|---|
| **Unsplash** | Unsplash License (since 2017) | Free commercial use, no attribution required. Banned: reselling unmodified copies; compiling into a competing service. |
| **Pexels** | Pexels License | Similar shape to Unsplash's — free commercial use, no attribution required. Banned: reselling/redistributing unmodified; building a competing stock service; depicting identifiable people in a demeaning or sensitive context. |
| **Nappy** | CC0, per Nappy's own stated terms | Verify per-photo before vendoring rather than assuming blanket CC0 — Nappy states its own terms and they should be read, not inferred from other free-stock sites. |
| **Humaaans** | CC0 | Pablo Stanley's mix-and-match illustrated people. |
| **Open Peeps** | CC0 | Hand-drawn character library. |

## Order of preference for this skill

1. **The product's own surface** — a real screenshot beats any stock photo.
2. **Unsplash**
3. **Pexels**
4. **Nappy** — reach for it specifically when the brief needs diverse representation Unsplash/Pexels search doesn't surface without effort.
5. **A drawn system** — hand-built SVG, when photography doesn't fit the register.
6. **Generated** — only via the image recipe in [`assets.md`](assets.md) § Generated illustration, and only through the design catalog's own image recipe, never a bare prompt.

## The contact-sheet method

Search candidates for the slot, render them as a contact sheet, **look at every
candidate** rather than picking the first result, verify each one actually loads,
pick the strongest, then judge that pick under the real scrim or overlay it will
sit behind and swap it if it fights the type — a bright, high-contrast photo that
reads fine alone can still crush the headline set over it. Downsize the winner to
roughly 2200px on the longest edge, re-encode to WebP, vendor the file into the
repo, and credit the photographer. No step is optional, and no step substitutes
for looking at the actual image.

## Photo-search field format

The catalog's photo-search fields take **2–4 phrases plus a source**, not a
sentence: `warm harbour dusk, wooden jetty, coastal terrace — unsplash`. Specific
phrases return specific photos; a single vague keyword returns un-curated
stock-photo-ish noise.

## Hotlinking

The skill's own example sites use verified Unsplash photo IDs, confirmed through
the contact-sheet method above rather than guessed. Hotlinking
`images.unsplash.com` directly is acceptable for demos and worked examples —
it's fast, and the IDs are pinned and verified. **Production vendors the file**
into the repo instead: the hero image is the largest contentful paint and must
not depend on another company's CDN uptime.
