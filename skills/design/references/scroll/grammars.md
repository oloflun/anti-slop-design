# The eight page grammars

Condensed from `upstream/scroll-craft/.../references/uniqueness.md` §2 — read
that file for the full text, the worked "four sites, one template" finding,
and the reasoning behind each forbid. A grammar is the page's organising
logic, not its palette: two pages in the same grammar feel related no matter
how far apart their worlds are. Pick exactly one; never blend two.

| Grammar | Fits | Scroll feels like | Forbids | Nav / hero / close | Leans on | Bans |
|---|---|---|---|---|---|---|
| **Filmic one-shot** | Single linear emotional arc — launches, consumer products | A film pushing through, no seams | Visible sequence, hard cuts, more than one entry point | Fixed minimal bar; full-bleed scrub hero, corner headline; pinned spotlight close, magnetic CTA | `scrub`, `pin`, `drift`, `kinetic` | Nothing structural — carries a burden of proof instead |
| **Chaptered editorial** | Long-form substance — method, manifesto, founder story | Turning pages, hard cuts between chapters | Continuous `drift`, full-bleed scrub hero, magnetic CTA, centred hero copy | No fixed bar; folio in margin; title-page hero (no media); colophon close, CTA as running text | `flow`+`in`, `reveal` at boundaries, `parallax` in a column, `count` in prose | `scrub` beyond one chapter, `spotlight`, `magnet` |
| **Live surface** | Software, tools, dashboards — the demo IS the argument | Operating something, panels populate | Any marketing chrome, full-bleed photography, kinetic headlines | App chrome (sidebar/tabs) as nav; hero is the product mid-state; close is a real input field | `pin`, `count` on real telemetry, pointer devices in-product | `scrub`, `kinetic`, `spotlight`, `drift` past two stops |
| **Continuous world** | A journey with real geography — supply chain, a place, a build | Moving through one space that never cuts | Section boundaries, any act device, second stage, interpolated `drift` | Nav is a map/waypoint list; hero is an establishing position; close is arrival at a place | worldflight legs, `data-sc-linger`, `sc:waypoint` | Every act device, `flow`, `pan`, hard cuts, `src` swaps |
| **Typographic poster** | A brand whose asset is a sentence — manifestos, agencies | Words at wildly different weights, rhythm from scale | Photographic ground, scrims, cards, decorative motion | Wordmark at composition scale; hero is one word/line at extreme scale; close inverts to smallest type, plain link | `kinetic`, `pin` with `--sc-p`-driven scale, `reveal` as a wipe | `scrub`, `pan` rails, `tilt`, `parallax` on text |
| **Gallery / catalog** | A range — products, portfolio, menu, materials | Walking a room, objects at their own pace | Argument-shaped pinned type, single hero claim, persuasion copy | Nav is an index that jumps; hero is object one, already labelled; close is last object or inquiry-as-label | `pan` as the spine, `reveal` per object, `tilt`, `count` | `kinetic` headlines, `spotlight`, `magnet`, >1 `scrub` |
| **Split stage** | Any two-sided argument — before/after, manual vs automated | Watching a balance tip toward a resolve | Full-bleed before the resolve, centred copy, symmetric close | No bar; divider IS the chrome; hero shows the split 50/50; close is the collapse to one column | `pin` with divider from `--sc-p`, `reveal` per side, real `count` | `pan`, `spotlight`, `magnet`, >1 `scrub`, `drift` |
| **Rhythmic cutlist** | Energy brands — streetwear, sport, events, music | A cut every second, 12–20 short sections | Any act >~1.4vh, `dwell`>0.1, `pin`, overlapping cues | Loud/marquee bar; hero cuts to next in under a viewport; close is abrupt full bleed | `flow`+`in` at short stagger, `reveal` on nearly every section, hard `drift` steps | `pin`, `spotlight`, `magnet`, `dwell`, `parallax` |

Cutlist's peak problem — it bans the devices a peak normally wants — is
solved by moving the peak into the fixed chrome layer rather than breaking
the grammar; see uniqueness.md §2.8.

## Register × grammar fit

The six registers are `../../SKILL.md` § The craft floor's own list. Each row
below is 2–3 grammars that genuinely fit that register, plus one grammar that
reads as a mismatch and the one-line reason why.

| Register | Fits | Mismatch (and why) |
|---|---|---|
| **Editorial print** | Chaptered editorial (the register's native shape); Gallery/catalog (museum-label copy is already this register's voice); Typographic poster (a manifesto-led atelier) | Rhythmic cutlist — a loud marquee bar and hard-cut energy contradicts the register's restraint and apparatus |
| **Cinematic dark** | Filmic one-shot (linear narrative arc, hospitality/launch); Continuous world (atmosphere as geography — a restaurant, a hotel); Gallery/catalog (a menu as a walkable collection) | Typographic poster — the grammar bans photographic ground outright, and cinematic dark's whole effect is atmosphere built from photography |
| **Illustrated dark** | Typographic poster (strong verbal identity paired with drawn forms); Gallery/catalog (a set of speaker/object portraits as objects); Chaptered editorial (a programme read as chapters) | Live surface — the grammar bans marketing chrome and kinetic headlines, which is exactly the illustrated-identity apparatus this register is built from |
| **Modern clean** | Live surface (the subject is precision — an instrument, a technical firm); Split stage (a before/after comparison, cost vs saving); Typographic poster (minimal photography, the claim carries it) | Rhythmic cutlist — a loud, marqueed, cut-every-second page fights a register whose whole case is calm precision |
| **Warm photographic** | Filmic one-shot (a consumer/hospitality arc); Continuous world (a journey through a place — harbour, guesthouse); Gallery/catalog (rooms or dishes as a walkable range) | Typographic poster — same conflict as cinematic dark: the register's asset is the photograph, and the grammar has no photographic ground at all |
| **Historical art** | Gallery/catalog (museum labels are this grammar's literal copy schema); Chaptered editorial (an institution that plausibly publishes an edition or catalogue); Continuous world (a journey through a collection or a period) | Rhythmic cutlist — a loud, marqueed, energy-brand grammar reads as flippant against institutional gravitas |

Cite `upstream/scroll-craft/plugins/nateherk-design/skills/scroll-craft/references/uniqueness.md`
for the full grammar text, the fingerprint gate, and the signature-move rules
(the latter two are condensed separately in
[`feel-and-fingerprint.md`](feel-and-fingerprint.md)).
