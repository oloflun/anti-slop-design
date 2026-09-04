# Alunix r4 · M2 — Kapitel · pinnad scen — build notes

Written before code, per Step 2b / contract.md's own requirement. Task: `tests/alunix-concepts-r4/contract.md`
§M2, binding; `tests/alunix-concepts-r4/brief.md` binding for the shared concept. Copy is taken
verbatim from `tests/alunix-concepts-r3/build/index.html` (read in full); reordered and regrouped,
never rewritten. No sub-agents used for this build.

## Reference lock

**Primary references (Tier 2 — the r3 page + these catalogue sources ARE the direction):**

- `tests/alunix-concepts-r3/build/index.html` — the finished split-stage page. Every headline,
  sub-text, price line and `kontakt@alunix.se` is lifted verbatim from here. Rejected from r3:
  the two-column split-stage structure itself, the seam-hairline-from-logo signature move
  (explicitly forbidden to reuse, brief/contract), the simultaneous Calyx-frame + price-box
  double close, the two-columns-side-by-side hero.
- `design-catalogue/entries/vinterspelen/entry.md` — chaptered editorial + the pinned stage
  machine (six wing flats sliding aside as a working model of real 1777 stage machinery,
  scroll-driven, cued by `--sc-p`-equivalent progress). Borrowed: the idea of a **pinned scene
  as a stage that changes what's on it while the frame itself holds still** (their flats sliding,
  my three iframes wiping in turn); the "ground or greet" cue discipline; "two states, not five"
  (this build alternates dark/blue/paper/dark, restrained). Rejected: their letter-spacing/blur
  per-frame scrub (forbidden by devices.md anyway), their multi-viewport-per-image sticky scrub
  (mine is one held frame, span 3.2, not "several viewport-heights per single image swap").
- `design-catalogue/entries/sanity/entry.md` — numbered Swiss-editorial section rhythm
  (01–05 in mono, left-column labels beside right-column content) and its dark-hero-then-white-
  sections chapter alternation. Borrowed: the **numbered folio-in-margin convention** (01/05,
  IBM-Plex-Mono-style tracked numerals) as this build's folio, and "show the actual product as
  marketing proof" (already Alunix's own move via the three live iframes, confirmed as the
  right instinct by this source). Rejected: Sanity's own orange accent (Alunix blue already
  fills that single-accent role; a second saturated colour is forbidden by TASTE.md §4.4), the
  112px display headline (r3's own giant headline size is kept, not re-derived).
- `design-catalogue/entries/not-real/entry.md` — the rotated 90° running-text strip pinned to
  the right viewport edge, project codes and timestamps, "a printed-magazine running header that
  persists independent of scroll content." Borrowed directly: the **mechanism** (rotated,
  edge-pinned, persistent) for this build's chapter-name rail — but not its content (their
  project reference codes) or its three-colour vellum palette (this page keeps R5+R6 tokens).
- `design-catalogue/entries/shelby-kay/entry.md` — the rotated secondary-wordmark fragment
  ("KAY") pinned to the right margin as "a second half of the wordmark functioning as a
  persistent spatial anchor." Borrowed: pairing the rotated running strip with the **logo mark**
  fixed at one point along it (their KAY fragment sits at a fixed rotated position; this build's
  logo sits fixed beside the rail, and the rail's own content moves past it — the inversion of
  their move, which is what makes it a genuinely different signature, not a copy of either
  source).
- `design-catalogue/TASTE.md` §1 (one authority per screen — read, applied: the pinned stage's
  authority is the changing frame itself, everything else recedes; the price box's authority is
  the two prices, set as bold discrete facts, nothing else competing) and §4 (decision rules —
  applied: one accent colour doing one job — Alunix blue, thesis block only; sections change
  material, not just background, between every chapter; depth via hairlines/ton-sur-ton, never
  shadow, kept from r3 verbatim).

**Preserved verbatim (brief point 1, binding):** every headline — `ALUNIX / Digital byrå`,
`Er hemsida är nutidens visitkort` (from the Tidvatten iframe's own title, promoted to a
visible chapter heading per contract.md), `Webbdesign, design och system. Allt på ett ställe.`,
`Webbdesign` / `Design` / `System` (the three tjänst H3s), `Det första intrycket är digitalt.`,
`Vi bygger ert varumärke.`, `Design` / `Utveckling` / `System` (hero service list and ledger
titles), `Alla har rätt till bra design.` — plus every sub-text, the three price lines and
`kontakt@alunix.se`, character-for-character. Both source typefaces kept: Geist/Geist Mono for
the R5-toned chapters (01, 03, 04), Public Sans for the R6-toned material (chapter 02's tjänst
cues, chapter 05's price box). No third font added — neither Bodoni Moda/Newsreader (vinterspelen)
nor Waldenburg/IBM Plex Mono (sanity) carries structure here that Geist Mono doesn't already
supply for this build's own mono role (folio, rail, kickers).

**New construction, this build only:** the pinned three-frame stage (chapter 02) with its
bespoke `--sc-p`-driven inset wipe (never touches the iframe elements themselves, only their
wrapper divs — see Decision ledger); the folio (fixed, left margin, `0X/05`, updates on scroll);
the chapter rail (fixed, right edge, rotated chapter-name strip functioning as a scroll
playhead — the signature move, see below).

**Reject (binding, from brief.md + contract.md):** any new numbers beyond the two real prices;
customers beyond the three demo sites; Klova; en/em dashes in visible text (using `·` instead,
matching r3's own convention); "jag" first person; photos claimed as "our office/team"; pointer
effects on the three iframes; transform or opacity animation on an iframe element once opened
(only its wrapper's `clip-path` moves, per contract.md's own instruction); reuse of r3's seam
hairline / logo-dock signature move; a page-wide `pin` (only chapter 02 pins); more than one
`scrub` (this build uses zero — no scrub media exists in the source assets, and chaptered
editorial's own grammar row bans "full-bleed scrub hero" for anything but the very first
screen, which here is a static title page, not a scrub).

## Decision ledger

| Decision | Source | Role | Why |
|---|---|---|---|
| Single column, max 1100px, five numbered chapters + one pinned scene | contract.md M2, binding | layout | Literal instruction; chaptered editorial's own grammar row (`scroll/grammars.md`) prescribes "no fixed bar; folio in margin; title-page hero; colophon close" |
| `Er hemsida är nutidens visitkort` promoted from an iframe `title` attribute (invisible in r3) to a visible chapter heading | contract.md M2 structure list | copy | Contract explicitly assigns this exact string to chapter 02; it is real, unedited r3 text (an attribute value, not prose, but character-for-character verbatim), not new copy |
| Three iframes (Tidvatten, Hōrai, Calyx) consolidated into one pinned stage instead of spread across separate sections | contract.md M2 | structure | Binding instruction: "en pinnad scen... där Tidvatten, Hōrai och Calyx byter plats" |
| Frame swap is bespoke JS reading `--sc-p` off the pin act, driving `clip-path: inset()` on each frame's wrapper div only, never the `<iframe>` itself | brief.md ban on transform/opacity on an opened iframe; contract.md M2's own instruction ("låt scenen byta ram genom clip-path/opacity på ett omslag... `pointer-events` på när ramen är öppen") | mechanism | The kit's own `data-sc-reveal` only wipes IN once and never back out (confirmed by reading `scrollcraft.js` `read()`), so a scene that must open, then close again as the next frame opens, cannot be a plain kit reveal — it has to be bespoke, exactly as contract.md anticipates |
| Three R6 tjänst cues (Webbdesign/Design/System) are also bespoke-JS-driven (opacity + `translateX`), not `data-sc-cue` | found while building: `data-sc-cue` elements get their `transform` fully overwritten every frame by the engine (`translate3d(0,Yvh,0)`), which would silently erase any CSS-driven `translateX` on the same element | mechanism | Keeping the three cues on the same bespoke `--sc-p` read as the frame wipes (rather than fighting the engine for the `transform` property) keeps their timing and direction both exactly synced to the frame they caption, with no race |
| Text blocks entering via `data-sc-in` (chapter 03's thesis text, chapter 04's giant-sub) get a page-scoped CSS override: `transform: translateX(48px)` pre-reveal, `none` once `.sc-in` — instead of the engine's own default 14px Y-rise | M2's own direction row (contract.md, brief.md): "text glider in från höger" | motion / direction | `data-sc-in` fires its `.sc-in` class ONCE via IntersectionObserver, then the whole animation is a plain CSS transition (confirmed in `scrollcraft.css` lines 286-291) — unlike `data-sc-cue`, nothing here is rewritten by inline JS every frame, so a page-scoped selector with higher specificity than the engine's own `[data-sc-in]` rule overrides safely, without touching `.sc-in`/`.sc-*` as engine-wide classes (gate: never restyle the engine's classes) |
| Images wipe in via `data-sc-reveal="left"` (not `"right"`) | verified against `scrollcraft.js` `read()`: `dir === 'left'` produces `inset(0 pct% 0 0)`, whose visible region is anchored at the LEFT edge and grows rightward as `pct` falls from 100 to 0 — i.e. the image visibly wipes in starting at its own left edge | mechanism | Contract.md's own prose names `reveal="right"` for this effect, but reading the engine's actual math shows `"left"` is the value that produces "wipes in from the left" — verified directly in code rather than trusted from memory, then confirmed again on the five motion screenshots (see Verification) |
| Chapter rail (signature move) computed with a **1:1 scrollY mapping**, not a proportional-to-chapter-length track | design, this build | signature move | `translateY(-scrollY)` on the rail's inner track, with each chapter label's own `top` set once (on load/resize) to that chapter's real document-space midpoint, makes the label's position inside the fixed rail viewport mathematically identical to that chapter's own on-screen position — so "the label level with the logo is the active chapter" is exactly true by construction, not approximated with equal spacing |
| Folio and rail both hidden under 860px; a plain in-flow `0X/05` chip appears at the top of each mobile chapter instead | brief.md's mobile-verification requirement + no natural left/right margin exists at 390px for either device | responsive | A 1100px-column device with fixed marginal chrome has nowhere to put that chrome once the column is full viewport width; degrading to an in-flow marker (matching r3's own mobile-collapse precedent for its corner marks/nav) keeps the "always know your chapter" function without clipping |
| Chapter 05 (price box) carries no scroll device at all | r3's own precedent (its price box is deliberately still) + brief's "close" convention for chaptered editorial ("colofon close") | motion | The one deliberately static element on the page, same rule r3 already proved works: the close should rest, not perform |
| `.stage`/`.ch02`'s solid ground moved off `var(--sc-canvas)` onto a new `--stage-ground` token, same starting value | bug found in verification: `scrollcraft.js`'s `drift` feature writes the interpolated colour onto `--sc-canvas` **globally** (`docEl.style.setProperty`), not scoped to the drifting act — chapter 03's own `data-sc-drift="#123f68"` was bleeding blue into chapter 02's still-pinned stage background as the page approached the boundary (confirmed live: `getComputedStyle(stage).backgroundColor` read `rgb(18,63,104)`, chapter 03's blue, while still deep inside chapter 02) | bugfix | `--sc-canvas` is drift-managed engine-wide by design (any `[data-sc-drift]` act can retint it); a page-authored element that wants a fixed ground must never read that same token — verified after the fix: `rgb(12,11,8)` (the correct dark) held constant through the whole boundary crossing |
| Stage cue opacity/`translateX` given its **own** narrower timing windows (`cueLocal0/1/2`), separate from the frame wipe's `local0/1/2` | found in the first motion screenshots: reusing the frame's wide crossfade window for the caption text meant the outgoing and incoming captions were both partially opaque over the same ~0.37-of-act stretch, reading as two headlines ghosted on top of each other | bugfix / polish | Each cue now fully fades out before its neighbour's crossover point and fades in only after it — at most one caption is ever legible, while the images still cross-fade slowly underneath (the wipe stays a wipe, the caption cuts cleanly) |
| Stage-head and stage-cue text given a flat `rgba(6,5,3,.84)` panel (own CSS, additive; not a restyle of `.sc-scrim`) | found via `scroll_verify.py`'s `contrastUnderMedia` check: a directional gradient panel (my first attempt) left part of the text under-covered — measured worst case 1.8:1 against a 4.5:1 floor, inside the gradient's own faded tail; separately, Hōrai's own "A three sister restaurant" line was visible sitting directly under the stage-head text with only the engine's own `.sc-scrim` gradient behind it | bugfix | A uniform panel guarantees the whole text block clears the floor regardless of which of the three real, uncontrolled sites happens to be showing behind it; re-measured clean (`contrastUnderMedia: []`) |
| `.chip` (mobile chapter marker) opacity raised from `.6` to `.85` | `a11y_scan.py` flagged `color-contrast` on `#ch03 .chip` at 390×844 (white-on-Alunix-blue at 0.6 alpha computes to 3.51:1, below the 4.5:1 floor for 11px text) | bugfix | Recomputed by hand (`blend(white, blue, 0.85)` → 5.34:1) before applying; re-ran `a11y_scan.py`, 0 violations |
| Rail "active chapter" (and folio number) driven by **containment** (`target` falling inside a chapter's own `[top, bottom)` range), not by nearest-midpoint | found while checking the motion screenshots: folio read "01" for the first third of chapter 02's own scroll range, because chapter 01's short midpoint (~450px into the document) stayed numerically nearer to the scroll anchor than chapter 02's own midpoint (~2340px down), even though chapter 02's *content* was already the only thing on screen — chapter 02 (2880px) is more than triple the height of any other chapter, which nearest-midpoint cannot handle correctly | bugfix | Verified live via `getComputedStyle`/`classList` reads at several scroll positions: folio and the bold rail label agree with each other and with the chapter actually rendered on screen at every position checked |
| **FIX ROUND.** `.stage-head` (kicker + "Er hemsida är nutidens visitkort" H2 + lede, bottom-left panel on the stage) removed entirely. Kicker ("02 · Tjänster") + lede ("Webbdesign, design och system. Allt på ett ställe.", now an `<h2>`) moved into a new plain-flow block, `.ch02-lead`, placed immediately BEFORE `<section id="ch02">` in the DOM — same dark ground token (`--stage-ground`), `enter-right`+`data-sc-in` reveal (M2's own direction rule, same mechanism as ch03/ch04's flow text). The standalone "Er hemsida är nutidens visitkort" line is dropped, not moved anywhere. | Anton, pixel-measured on `my-M2-2.png`/`my-M2-3.png` (1440×900): the on-stage panel repeated a headline that Tidvatten's own frame (`tidvatten-hero.html`, out of scope) already carries in its own fold, so the line read twice on one screen — and the panel then rode along, unexplained, over Hōrai and Calyx too, which don't share that headline at all | bugfix (defect #1, this fix round) | `.ch02-lead` is deliberately NOT a `.chapter` element: `document.querySelectorAll('.chapter')` (five elements) indexes 1:1 against the five rail labels in `layoutRail()`/`updateRail()`; a sixth `.chapter` here would misalign every rail label after it. Confirmed post-fix: rail/folio still agree with the on-screen chapter at every position checked (see Verification) |
| **FIX ROUND.** Both `.sc-scrim` corner-gradient divs (`--lead`/`--trail`) dropped from the stage markup. The three tjänst cues no longer share one narrow, right-aligned, right-anchored `.stage-cues` column (`sc-copy sc-copy--trail`, `max-width:min(24rem,64vw)`, `text-align:right`); each `.stage-cue` is now its own bottom-anchored panel, `max-width:min(36ch, 100vw - 2×gutter)`, left-aligned. Cues 1/2 (Hōrai, Calyx) default bottom-left; cue 0 (Webbdesign/Tidvatten) gets `.stage-cue--right` (bottom-right on desktop) because Tidvatten's own headline lives bottom-left inside its own frame. `.stage-cues` needed an explicit `z-index:var(--sc-z-copy)` once it stopped using the kit's `.sc-copy` class — missed on the first pass, caught immediately by a live opacity/rect probe (`getComputedStyle` said opacity 1, rect on-screen, but nothing painted): without it the cue panels stacked *below* `.frame-wrap[data-frame="0"]`'s own `z-index:3` and were fully hidden behind the open frame | Anton, pixel-measured on `my-M2-2.png`/`my-M2-3.png`: the cue column read as a persistent ~150px-wide black band running the full frame height, ragged one/two-word lines, riding across all three frames regardless of what was showing | bugfix (defect #2, this fix round) | Kept the exact same flat `rgba(6,5,3,.84)` panel ground (already proven clean by `scroll_verify.py`'s `contrastUnderMedia` against Tidvatten's bright sky) — only its shape/position changed, not its color, so the earlier contrast proof still applies; re-verified after the fix (`contrastUnderMedia: []`, all five motion screenshots read by eye) |
| **FIX ROUND, mobile-only.** `.stage-cue--right` gets a `@media (max-width:640px)` override: `top:var(--gutter)` instead of `bottom:…`. | found while re-shooting mobile (390×844): even bottom-RIGHT still collided with Tidvatten's own headline there, because that headline wraps to 4–5 lines at 390px and grows tall enough to reach the bottom-right corner too — a screenshot caught the two texts genuinely overlapping | bugfix, mobile | Tidvatten's own hero has nothing in its top band at any width checked; cues 1/2 (Hōrai, Calyx) were already clean bottom-left on mobile (checked, no change made there) — re-shot after the fix, clean at 390×844 |
| **FIX ROUND.** `.ch02-lead-statement` set as an `<h2>` (was drafted as a `<p>`) | `a11y_scan.py` flagged `heading-order` (moderate) once `.stage-head`'s own H2 was removed: the stage's `<h3>` cues then jumped straight from ch01's `<h1>` with nothing in between | bugfix | Re-ran `a11y_scan.py`: 0 violations, back to the pre-fix-round baseline (35 passes, 2 incomplete) |
| **FIX ROUND.** Mobile `.chip` for chapter 02 trimmed from `"02 / 05 · Er hemsida är nutidens visitkort"` to `"02 / 05"` | consistency with every other chapter's chip (03/04/05 never repeat their own headline) now that the headline text itself no longer needs protecting from duplication — leaving the old extra text in would have been a second, smaller echo of the same fixed problem | polish, this fix round | Visual only, no functional role (`.chip` is decorative/marginal on mobile, matching folio+rail's role on desktop) |
| Verification's own full-page desktop capture: **no viewport-height resize trick**, plus a persistent `resize` listener re-applying a force-open (including `.sc-split__i` kinetic children directly, not just their parent `[data-sc-cue]`) after Playwright's internal `full_page` resize | found while shooting: r3's own desktop workaround (resize the *page* to full document height, screenshot without `full_page`) assumes every section scales by `cqw`/container width; this build's chapter 02 stage depends on the engine's own `.sc-stage{height:100vh}`, so resizing the viewport to ~6000px tall re-renders the WHOLE pin at that inflated 100vh and breaks it outright (confirmed: the Tidvatten iframe rendered scrolled deep into its own internal page, not its hero). Even with a normal-height `full_page` capture, the giant kinetic headline (chapter 04) still rendered blank on the first attempt — the same root cause r3's own NOTES.md already documented (`full_page`'s internal `resize` event clears `scrollcraft.js`'s cached kinetic-split units) | verification-tooling, not a page bug | This is a capture-tool limitation, not something a real visitor encounters (confirmed by the non-full-page, per-position screenshots throughout this file, all correct); documented here rather than worked around inside the page itself |

## Feeling curve (written before building)

1. **Threshold.** The console card states the byrå's name once, dead center on a grayscale
   desk photo, dark and quiet, nothing moving. Caused by: a title-page hero with zero scroll
   device — chaptered editorial's own opening convention, a cover rather than a pitch.
2. **The machine holds its breath.** The page locks; a stage opens where the sites will show
   themselves in turn, one already resting behind the fold. Caused by: the pin engaging,
   `--sc-p` starting at 0, the chapter's own heading ("Er hemsida är nutidens visitkort")
   arriving as the frame's first caption.
3. **Proof, three times over — the peak.** Tidvatten wipes open from the left, its own tjänst
   line sliding in from the right to name it; it closes and Hōrai does the same; then Calyx.
   Caused by: one held frame changing what's inside it three times, each swap captioned by the
   exact service it demonstrates, entirely inside a single pinned span.
4. **Conviction, stated flat.** The scene releases into Alunix blue: three short lines of fact,
   a black-and-white photograph of a real project wiping open beside them. Caused by: the one
   saturated colour on the page landing immediately after three quiet, mixed-tone frames.
5. **Scale.** The giant kinetic headline rises line by line, then the ledger (Design /
   Utveckling / System) reads out the process underneath it, unhurried. Caused by: the loudest
   type on the page landing right after the peak, followed by the calmest device (staggered
   flow) on the page.
6. **Resolve, no ceremony.** The page inverts a final time: philosophy line, two real prices,
   one contact address, nothing moving. Caused by: a still, dark close that mirrors chapter 1's
   own dark ground — the argument closes the loop it opened on.

**Peak:** act 3 / chapter 02, the pinned stage (`data-sc-span="3.2"`) — the only act where the
visitor watches three different, real, interactive sites take the same frame in turn, each
named by copy crossing in front of it. Largest span on the page, most scroll room, the one
place the R5 and R6 worlds' own texts literally cross paths on the same physical stage.

**Tell-someone sentence:** "It's the site where one frame in the middle of the page changes
which of three real client sites is playing inside it as you scroll — one wiping open as the
last one wipes shut — while a little rotated number on the right edge always tells you which
chapter you're actually standing in."

**Signature move:** the chapter rail — a vertical, rotated running strip along the right edge
reading `01 ALUNIX · 02 VISITKORT · 03 DIGITALT · 04 VARUMÄRKE · 05 DESIGN`, fixed beside the
logo mark, whose inner track is translated by exactly `-scrollY` every frame while each
chapter's label sits, once measured, at that chapter's real document-space vertical midpoint —
so the label mathematically level with the fixed logo is always, provably, the chapter actually
on screen (not an approximation). The nearest label is boosted in weight/opacity as the
"active" one. Distinct from r3's seam-hairline-from-logo (that page draws a growing line;
this page scrolls a list past a fixed point) and from any kit device (nothing in
`scrollcraft.js` produces this — it is entirely page-authored JS reading `window.scrollY` and
each chapter section's own layout, never touching `--sc-p` for this particular mechanism since
it spans the whole page, not one act).

## Devices per act (≥4 families, never the same one twice in a row)

| Chapter | Act | Primary device family | Notes |
|---|---|---|---|
| 01 — ALUNIX / Digital byrå | title page | *(none — static)* | Matches r3's own hero precedent: the first screen needs no scroll device |
| 02 — Er hemsida är nutidens visitkort | **pin** (`data-sc-span="3.2"`) | `pin` | Bespoke frame-wipe + bespoke tjänst-cue crossing, both `--sc-p`-driven, composed inside the one pinned act |
| 03 — Det första intrycket är digitalt. | flow | `reveal` (image, `left`) + `flow`+`in` (text, direction-overridden) | Two families composed; reveal is the reason the act exists (image and blue block declare the state) |
| 04 — Vi bygger ert varumärke. | flow | `kinetic` (headline) → `flow`+`in` (ledger, staggered) | Two beats in sequence, kinetic first (loud), flow+in after (calm) |
| 05 — Alla har rätt till bra design. | *(none — static)* | *(none)* | Deliberately still close, r3's own precedent |

Families used across the page: **pin, reveal, kinetic, flow+in** = 4 distinct families, plus
the bespoke signature move (chapter rail, outside the kit) and the bespoke stage mechanism
(chapter 02's frame wipe, also outside the kit, composed inside `pin`). No act repeats its
primary family immediately after another instance of the same family.

## Fingerprint row (vs. r3, brief's binding ≤2/6 ceiling)

| # | Dimension | r3 (`build/index.html`) | M2 (this build) | Shared? |
|---|---|---|---|---|
| 1 | Grammar | Split stage | Chaptered editorial | No |
| 2 | Nav | No bar; four fixed corner tick-marks (no text) | No bar; fixed folio (`0X/05`) + rotated chapter-name rail | Both "no traditional nav, persistent fixed marginal chrome" — **yes, loosely** |
| 3 | Hero device | Two heroes side by side (console card + Tidvatten iframe) | One title-page console card, alone, static | No |
| 4 | Act-sequence shape | Two parallel columns, `flow` acts only, no pin/scrub/pan | Five numbered chapters, single column, one `pin` act (span 3.2) | No |
| 5 | Close pattern | Dual simultaneous close (Calyx frame + price box, side by side) | Single close (price box alone; Calyx already spent inside chapter 02's stage) — same box, same tokens, but not simultaneous with another frame | **Yes** (same closing device, price box) |
| 6 | Signature move | Seam hairline drawn from a docked logo (`--seam-p`, `scaleY`) | Chapter rail: rotated running text scrolled `-scrollY`, playhead against the fixed logo | No |

**Shared: 2/6** (nav treatment's underlying "no bar, fixed marginal chrome" concept; the price-box
close device) — at the brief's own ≤2/6 ceiling, not over it.

## Skills loaded, in order

1. `Skill(design)` — front door, Steps 0 (page scope: full build, page/surface), 1 (pre-flight:
   `tests/alunix-concepts-r4/` has no `DESIGN.md`, no existing tokens — clean), 1b (reference
   lock, above; r3's own build read in full first, then the four catalogue entries and TASTE.md
   §1/§4), 2 (Tier 2 — r3 + the catalogue sources are the direction, stated), 2b (grammar
   pre-assigned by contract.md — chaptered editorial + one pinned scene — feeling curve/peak/
   signature move/device table above, bake-off skipped: task instruction, single assigned
   direction per contract), 4 (build), 5 (verify, this document, numbers appended below).
2. No copywriting/copy-editing/humanizer chain run — brief.md and contract.md both state the
   copy chain is not needed ("copyn är ordagrann ur r3... Ingen copy-kedja behövs" / "Ingen
   copy-kedja (copyn är ordagrann ur r3)"), and no new string was written anywhere on this page.

## Verification results

**Fix round (this pass).** Two pixel-measured defects on `my-M2-2.png`/`my-M2-3.png`
(1440×900, inside the pinned stage) — see the two FIX ROUND rows in the decision
ledger above for the full account:

1. Duplicated headline: the stage's own `.stage-head` panel repeated "Er hemsida är
   nutidens visitkort", already visible inside the Tidvatten frame's own fold.
   Removed; the kicker + lede that were left move into a new plain-flow `.ch02-lead`
   block ABOVE the pin (R6 typography, Public Sans 300, same `enter-right` direction
   rule as chapters 03/04).
2. Cramped cue column: the three tjänst cues shared one narrow (~150px), right-
   anchored, right-aligned black column running the full frame height. Replaced with
   one bottom-anchored panel per cue (`max-width: min(36ch, 100vw - 2×gutter)`,
   left-aligned); cue 0 (Webbdesign, plays over Tidvatten) anchors bottom-right on
   desktop / top-right under 640px, since Tidvatten's own headline lives bottom-left
   in its own frame; cues 1/2 (Hōrai, Calyx) stay bottom-left, where neither site puts
   its own text.

Both `.sc-scrim` corner-gradient divs dropped from the stage markup — with no
permanent on-stage caption left to protect, they had nothing to justify them and were
themselves part of what read as an unexplained dark band on the right. A z-index bug
introduced while de-coupling the cues from the kit's `.sc-copy` class (cue panels
briefly painted *behind* the open frame — see ledger) was caught by a live
`getComputedStyle`/`getBoundingClientRect` probe before it reached a screenshot, and
fixed (`z-index: var(--sc-z-copy)`, same numeric level the kit's own copy layer uses).
A `heading-order` a11y regression introduced by removing `.stage-head`'s own `<h2>`
was caught by `a11y_scan.py` and fixed by promoting the new lead-in statement to
`<h2>` (it already reads as the chapter's title line).

Re-verified after the fix round: `scroll_verify.py` — `deadScroll: []`,
`cuesNeverFull: []`, `unrevealed: []`, `contrastUnderMedia: []` (same flat
`rgba(6,5,3,.84)` panel ground as before, unchanged, only its shape/position moved).
`a11y_scan.py` — 0 violations, 35 passes, 2 incomplete (back to the pre-fix-round
baseline). No horizontal overflow at 1440 or 390
(`document.documentElement.scrollWidth === window.innerWidth` at both). No
`[scrollcraft]` console warnings at either breakpoint through a full scripted
scroll-through. Three iframes, real titles, unchanged. Reduced motion: frame 0 open
and static, frames 1/2 closed, identical state before and after scrolling to y=2000 —
unchanged by this fix round (its own CSS/JS untouched). Five fresh
`shots/motion-0..4.png` (scrollY 1155/1650/2016/2541/3036, sampled at `--sc-p` ≈
0/0.25/0.435/0.7/0.95 through the pin's own 1980px travel) read by eye: motion-0 shows
"01 Webbdesign" bottom-right with Tidvatten's own headline fully readable bottom-left,
no duplicate text anywhere on screen and no black column; motion-2 shows "02 Design"
as a single legible bottom-left panel over Hōrai; motion-4 shows "03 System" the same
way over Calyx; motion-1/motion-3 are mid-wipe (no cue lit, per the "no two cues lit
at once" rule) and show the stage's own dark ground in the not-yet-claimed region —
expected curtain behaviour, not the fixed defect (that defect was a *cue-bearing*
column, not the wipe's own transient ground). Also re-shot and read three mobile
frames (390×844, `mobile-cue0b/1b/2b.png`): cues 1/2 were already clean; cue 0 needed
the `@media (max-width:640px)` top-right override above to clear Tidvatten's own
headline there too (its wraps to 4–5 lines at that width).

Server: `python -m http.server 3091` from the repo root. Tested at
`http://127.0.0.1:3091/tests/alunix-concepts-r4/cells/M2-chain/index.html`.

**Original build's own verification (unchanged by this fix round, kept for record):**

- **`scroll_verify.py`** (1440×900, no-preference motion): `deadScroll: []`,
  `cuesNeverFull: []`, `unrevealed: []`, `contrastUnderMedia: []`. Clean —
  matches brief.md's own three named checks exactly. `blankBands` reports one
  band (document Y 1800–3883, 2083px) inside chapter 02's own pinned spacer
  in a `full_page=True` capture — a Playwright/sticky-position stitching
  limitation (the sticky stage only paints its own viewport-sized slice; the
  rest of a 2880px-tall pin spacer, off-screen at capture time, has nothing
  else drawn there), not something a real visitor scrolling normally ever
  sees — confirmed directly: `scroll_verify.py`'s own per-position captures
  (`00.png`–`24.png`, plain `scrollTo()` + `screenshot()`, no `full_page`)
  show the correct frame/cue at every one of the 18 sampled positions
  through that exact range, and the five `shots/motion-*.png` below confirm
  the same thing at finer resolution. Not fixed inside the page itself
  (nothing about the pin is wrong) — documented, matching r3's own
  precedent for the identical class of tooling limitation.
- **`a11y_scan.py`**: **0 violations, 35 passes, 2 incomplete** (axe's own
  "needs manual review" bucket, not a failure — same shape as r3's own
  baseline). One violation found and fixed mid-build (`.chip` contrast on
  mobile, see decision ledger) — re-run after the fix: 0 violations.
- **No horizontal overflow** at either breakpoint, checked after a full
  scripted scroll-through: desktop `document.documentElement.scrollWidth
  === window.innerWidth === 1440`; mobile `390 === 390`.
- **Three iframes, real titles, all loaded:**
  `/tests/alunix-concepts-r3/build/tidvatten-hero.html` → "Er hemsida är
  nutidens visitkort"; `/sites/horai.html` → "Hōrai, restaurang i
  Stockholm"; `/sites/calyx.html` → "Calyx, florist i Stockholm".
- **Console:** no `[scrollcraft]` warnings at either breakpoint through a
  full scripted scroll-through (checked via a `page.on('console', ...)`
  listener filtering for the literal string, both at 1440×900 and 390×844).
  The only console lines anywhere are the known `cdn.tailwindcss.com`
  notices originating inside the Hōrai/Calyx iframes' own pages, out of this
  build's scope (same as every prior round of this whole chain).
- **Reduced motion** (`prefers-reduced-motion: reduce`): the pinned stage
  shows the first frame (Tidvatten) open and static —
  `getComputedStyle(frameWrap[0]).clipPath === 'inset(0px 0% 0px 0px)'`
  (fully open) — with frames 1 and 2 held closed
  (`'inset(0px 100% 0px 0px)'`) and reachable instead as two plain text
  links (`.stage-links`, `display:flex` under reduced motion only). State
  is identical before and after scrolling to y=2000 — confirmed static, not
  a frozen mid-animation frame. `.sc-stage` itself is never touched by any
  reduced-motion override (only the wrapper clip-paths and cue opacities are
  set once), so no `[scrollcraft]` "will not pin" warning is ever risked.
- **Five motion screenshots**, 300px apart through the pinned stage's own
  wipe (`shots/motion-0.png`…`motion-4.png`, scrollY 950/1250/1550/1850/
  2150), read directly: `motion-0`/`motion-1` show the Tidvatten frame
  shrinking away from its own right edge while its visible region stays
  anchored to the left (the image wipes in/out from the left, per M2's own
  direction rule); `motion-2`–`motion-4` show Hōrai fully open, its own
  "02 Design" caption sitting at its resting position on the right after
  entering with a `translateX` from further right (confirmed by the
  pre-fix/post-fix screenshots: the caption starts offset right, ends at
  0). The chapter rail's "02 VISITKORT" label is visibly bold/white
  (active) throughout, matching the pin's own on-screen chapter.
- `wc -l index.html`: 658 lines.

## What I could not do / environment notes

- The Playwright `full_page=True` blank-band and kinetic-headline-reset
  issues (both described above and in the decision ledger) are capture-tool
  limitations already documented by r3's own NOTES.md for a related but not
  identical cause (r3's page had no `pin` act at all, so it only hit the
  kinetic-reset half of this; this build's chapter 02 pin adds the sticky-
  stitching half on top). Worked around for the verification screenshots
  themselves (a persistent `resize` listener re-applying the reveal
  failsafe, see decision ledger); not something that needed a change inside
  the shipped page, since a real visitor never triggers Playwright's
  internal resize event.
- Did not touch `sites/horai.html`, `sites/calyx.html`, or
  `tests/alunix-concepts-r3/build/tidvatten-hero.html` (out of scope,
  existing pages) — the `cdn.tailwindcss.com` console notice and each
  site's own on-page text (which chapter 02's stage-cue panels now sit in
  front of, see decision ledger) originate there, not in this build.
- **Fix round: resolved, not left as-is.** The previous round's own
  "minor, low-severity" note here described the stage-head panel's heading
  as a near-duplicate of Tidvatten's own on-page headline. Anton's own
  pixel measurement on `my-M2-2.png`/`my-M2-3.png` treated that as a real
  defect, not an acceptable structural consequence — fixed this round by
  dropping the standalone heading from this build's own copy entirely (see
  decision ledger, FIX ROUND rows). It no longer recurs anywhere on the
  page; Tidvatten's own on-frame headline is now the only place that exact
  sentence appears on screen at once.
