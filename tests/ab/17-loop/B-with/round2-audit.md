# Round 2 accessibility audit — Florhuset Majorna (B-with/index.html)

Procedure: `a11y-audit/SKILL.md` passes 2–6 (POUR, COGA, Content, Adaptive,
Interaction), applied to the file as it stood after Round 1's critique fixes.
Pass 1 (mechanical) tooling was run first and re-run after every fix; passes
7–8 (persona walkthrough, full legal-map report) are out of scope for this
loop per the brief — this document is the findings table + verdict only.

## Coverage

| Input | Verified | Inferred / Not verified |
|---|---|---|
| `file://…/index.html`, driven by real Playwright/Chromium | Mechanical scripts (axe, tab-walk, reflow), keyboard path, focus order/visibility, measured contrast (token math in Round 1 + axe's rendered-pixel check here), reflow at 320px/200% zoom, reduced-motion behaviour, console output | — |
| Screen-reader announcement phrasing | Accessible names / roles / heading structure verified via axe + DOM inspection | Not run through an actual AT (NVDA/VoiceOver) — phrasing itself is inferred from correct semantics, not heard |
| `forced-colors` (Windows High Contrast) | — | Not verified — no emulation tool available in this pass |

## Mechanical pass, before → after

| Script | Before | After |
|---|---|---|
| `a11y_scan.py` (axe, 1440×900 + 390×844) | 1 violation: `color-contrast`, serious, WCAG 1.4.3 — different `.ledger__row` node flagged each run (390×844 only), 41 passes | **0 violations**, 41 passes, across 3 repeated confirmation runs |
| `tab_walk.py` (≤60 stops) | 11 stops, 0 issues | 11 stops, 0 issues (unchanged — was already clean) |
| `reflow.py` | `overflow320: [img]`, `overflowZoom200: [img]`, `hiddenUnderReducedMotion: 1 [li]` | Same 2 flags remain, both **investigated and confirmed false positives** (see findings 6–7); the `li` flag's one genuinely on-screen case is resolved (see finding 2) |
| `detect.mjs` | 1 warning: `overused-font` (Fraunces) | Unchanged — deliberate, documented choice (see finding 8) |

## Findings

| Severity | Location | Before | After | Why | WCAG | Who |
|---|---|---|---|---|---|---|
| HIGH | 3 of 4 `<img>` alt attributes (hero right panel; wedding aisle; ateljékvällar bouquet) | Alt text described a flat-lay of cut flowers, a set table, and hands mid-binding — none of which match the actual photographed content (verified by fetching each source image directly) | Alt text rewritten to describe what is actually shown | Alt text that actively misdescribes an image is worse than none for a screen-reader/no-images user trying to understand the page | 1.1.1 (A) | Blind/low-vision screen-reader users; users with images disabled or on slow connections |
| HIGH | `.ledger reveal--stagger` children (Buketter section) | axe flagged `color-contrast` (serious) at 390×844, on a different ledger row's text each run — a transient mid-fade opacity blend, not the settled token colour | 0 violations across 3 repeat runs | Mount-time immediate-reveal threshold (1.1×viewport-height) didn't cover the ledger, so it depended on IntersectionObserver + a 1.2s/90ms-stepped transition an axe snapshot could sample mid-fade; fixed by raising the threshold to 3.0× and shortening the stagger (1.2s→0.5s, 90ms→40ms steps) | 1.4.3 (AA) | Low-vision users, and any user or tool reading the page in its first ~1–2s |
| MEDIUM | `#wedFacts li` (Bröllop section) | Only 1 of 3 practicality facts visible at the genuinely on-screen scroll checkpoint (thresholds 0.15/0.4/0.65 → full set visible for only ~29% of the 220vh pin range) | All 3 facts simultaneously visible at the same checkpoint (thresholds tightened to 0.05/0.12/0.20 → full set visible for ~74% of the range) | A reduced-motion user who pauses mid-scroll (no lerp smoothing to carry them past a partial state) could rest on a list that looks incomplete | 2.3.3-adjacent / readability under reduced motion | Users with vestibular/motion sensitivity who scroll in short bursts and pause |
| MEDIUM | `.hours-table` (Besök oss) | Scoped row headers (`th scope="row"`) but no `<caption>` | `<caption class="sr-only">Öppettider</caption>` added | A screen-reader user jumping table-to-table gets no programmatic label for what it lists | 1.3.1 (A) | Screen-reader users navigating by table/landmark shortcuts |
| MEDIUM | `.close-section` (Besök oss) | No heading element anywhere in the section (`<p class="close-address">…`) | Promoted to `<h2 class="close-address">` — zero visual change, styling is class-based | A screen-reader user navigating by headings jumps from "Ateljékvällar" straight past the whole close section with no announcement | 2.4.6 / 1.3.1 (AA/A) | Screen-reader users using heading-navigation (a very common AT pattern) |
| MEDIUM | 10 mono micro-label selectors sitewide (kicker, ledger meta/currency, split-list `dt`, wed-facts, knot caption, hours-table cells, close-foot, site-nav, brand place) | `font-size` set in raw px (10px/10.5px/11px/12px) | Converted to rem equivalents (0.625/0.65625/0.6875/0.75rem) | Px-locked text doesn't scale when a user raises their browser's *base* font-size preference (distinct from pinch/ctrl-zoom, which already passed reflow.py's 200% check) — these labels would shrink relative to the rest of the rem/clamp-based page | 1.4.4 (AA, spirit — zoom itself already conformed) | Low-vision users who set a larger default text size rather than using page zoom |
| LOW — verified false positive, no fix | `.hero-stage__panel--daisies img` | `reflow.py` flags `img` overflow at 320px and 200% zoom | Investigated: `document.documentElement.scrollWidth === clientWidth` at both 320px and 720×2 zoom — no real horizontal scroll exists. The flag is the post-`transform:scale(2.05)` bounding rect exceeding the viewport while the parent's `overflow:hidden` clips it visually; the script's geometry check doesn't walk up for a clipping ancestor | n/a | n/a |
| LOW — verified false positive, no fix | `#wedFacts li` | `reflow.py`'s `hiddenUnderReducedMotion` flag persists after the MEDIUM fix above | Investigated at all 3 checkpoints: the flag now only fires at scroll fraction 0.0 and 1.0, where the wedding section is genuinely off-screen (`wedTop` 2448px below / −3393px above viewport) — the script excludes horizontally off-canvas elements but not vertically off-screen ones | n/a | n/a |
| LOW — accepted, not fixed | Google Fonts Fraunces | `detect.mjs`: `overused-font`, severity warning | Unchanged | A deliberate, explicitly reasoned choice documented in the file's own header comment (named departure #2 from the Cardo-based AI default) — not a defect any critique or a11y pass flagged, only a structural popularity heuristic | n/a | n/a |
| LOW — accepted, not fixed | `.site-bar` (nav) | Static, non-sticky header; no persistent wayfinding once scrolled past it on a 6741px single page | Unchanged | Explicit, documented registry-differentiation decision (the file's own fingerprint-gate table names "static non-sticky bar" as one of the dimensions this page deliberately differs on) — no WCAG SC requires persistent navigation | — | — |
| LOW — accepted, not fixed | `.hero-plate` scrim | `color-mix(…, 88%, transparent)` doesn't fall back to solid under `prefers-reduced-transparency` | Unchanged | Already 88% opaque (near-solid); the text inside measures 15.66:1/9.91:1 independent of the residual 12% transparency | — | — |
| LOW — accepted, not fixed | Whole page | No `prefers-color-scheme` fork | Unchanged | The palette is the page's fixed brand identity (cold fog/petrol + one deliberate dark inversion), not a light-mode UI meant to fork; not a cited WCAG SC | — | — |

## Verdict

**Approve.** Both HIGH findings and all four MEDIUM findings are fixed and
confirmed by re-running the full mechanical suite three times (0 axe
violations, 0 tab-walk issues). The two remaining `reflow.py` flags were
investigated and are verified false positives (documented above, not
silently dropped). Coverage gaps are named rather than assumed clean:
`forced-colors` was not verified (no tool available this pass) and
screen-reader announcement phrasing was not heard through an actual AT —
both listed as "Not reviewed," not folded into the Approve.

## Legal map

Every fixed and accepted finding above maps to WCAG 2.2 AA (cited per-row).
EAA / EN 301 549 align with WCAG 2.2 AA directly. No ADA/Section 508-specific
gap beyond the WCAG mapping was identified.

## SEO flag

Two of the fixed findings are SEO-relevant by the same structural signal
search crawlers and screen readers both depend on: the corrected alt text
(3 images) and the restored heading structure (`close-address` → `h2`) both
improve how a crawler, not just an AT, parses the page's content and outline.
