# What actually made the difference — the full causal model

Written 2026-07-31, from six parallel readers over: the Snajp /goal session (8c02f3a1),
the hardening/deploy session (d2aecc19), the v2 rework session (f2fc9ec2), the v1 system
and its git history, the full source of Calyx/Horai/Hyperborea, and the live hook chain.
Own-eyes captures of all three demo sites and the shipped Snajp page confirmed the claims.

## The one-paragraph diagnosis

v1 one-shotted reference-grade sites because **the taste was resident in context at write
time** (the model had just read five opinionated craft skills in the same session), because
**every build began by naming an aesthetic lane** ("unnamed ambition becomes beige"), and
because **every ban was paired with named positive alternatives**. v2 fixed v1's two real
mechanical failures (hooks that didn't fire, specialists that repainted brands) but never
analyzed why v1's output was *good* — it replaced taste-in-context with 120 on-demand
reference files the model samples and averages, demoted the direction-giving specialists,
and built a success metric (route-vs-invocation gap) that measures process compliance, not
output. Every quality gate in the chain is negative; a flat, on-palette, generic page
passes all 88 of them untouched. The Snajp and Alunix sessions only reached quality when
the user *manually* re-imposed v1's exit bar: iterate until genuinely better than named
references, verify with your own eyes, never judge from code.

## The ten load-bearing factors

1. **Context density, not dispatch.** At v1 build time all craft content was resident.
   Nothing was "loaded on demand". The current dispatcher's craft lives in ~120 files;
   telemetry proves routed skills go unloaded (route gap ≠ 0 in the Snipra session).
2. **A named aesthetic lane before code.** "Liquid Death acid-green drench", "Editorial
   luxury minimalism". Pre-flight item in v1; absent in v2. The tier gate asks where
   direction comes FROM but never forces the direction to be NAMED.
3. **Bans paired with named alternatives.** v1: "no 3-col icon cards → Bento 2.0,
   zig-zag, horizontal scroll, masonry, single spread". Detection alone yields
   compliant-but-flat. (Also proven by the Snajp flat page: prohibition-only DESIGN.md
   ⇒ "a fully compliant page was necessarily empty".)
4. **Imagery is the design.** Real verified Unsplash photos or a bespoke inline-SVG
   identity system. Contact sheet → choose with eyes → verify loads → judge against the
   actual scrim → swap what fights the type. "Demosidorna visar att fotot ofta är
   designen." Nothing in v2 blocks a first render review without imagery.
5. **House physics — exact shared values.** Across all three sites: kicker
   10.5px/0.22em/uppercase mono; 8–10 oklch tokens with exactly ONE saturated accent
   deployed at display scale and never on small controls; buttons barely exist (CTAs are
   typeset mailtos at 3–4xl); palette-tinted feTurbulence grain (multiply on light,
   screen on dark); display clamp() up to 15rem at leading 0.9–0.95; label-rail (kicker +
   hairline + meta) beside wide content on a 12-col grid; every list/pricing surface is a
   hairline ledger, never a card grid; paired columns never top-align (mt-12/24/44
   staggers); measure capped in ch. Scattered today across 45 files; needs to be one page.
6. **Copy is worldbuilding with a density floor.** Invented editorial apparatus
   (Cmsn. 0211, plate 02/14, Vol. IX · spring, roman-numeral dates), real street
   addresses, cross-referenced fictional entities, self-aware colophons ("Set in Cardo &
   PT Mono"). Copy pipeline: copywriting → copy-editing → humanizer + humanizer-svenska,
   humanizers LAST, diff-audited so they never rewrite facts.
7. **In-situ negation + an antagonist.** Section comments name the slop default being
   replaced ("INDEX: a typeset ledger — NOT a card row"). v1's session rendered a
   deliberately generic antagonist page first, so "not that" was a rendered artifact.
8. **One signature motion set-piece per page** on top of a shared reveal system
   (translateY 28px, 1.2–1.4s, cubic-bezier(.16,1,.3,1)) — Horai's scroll-scrubbed quote
   (lerp+smoothstep, animating blur AND letter-spacing, both directions). Always
   prefers-reduced-motion. Reveal systems fail toward visible (4 guards). The artifact
   ships verification affordances (`?preview=quote` forces the formed state for
   screenshots).
9. **Eyes on pixels inside the build loop.** "A screenshot you didn't read doesn't
   count." References captured full-page in slices BEFORE code (fold-only capture missed
   Alunix's rhythm failure). Render → Read PNG → fix → render, until a full pass finds
   nothing. Diagnosis with numbers (measure.py: hairlines 106→2, ochre-at-display 30→0…)
   turns "looks generic" into a fix list. Verify the verifier against a known-broken case.
10. **A reference-beating exit bar, mechanically enforced.** v1: "a high-end studio
    reviewer would defend it". Snajp only recovered under a /goal Stop-block. Six real
    defects were found AFTER the page already "looked done". The round that finds nothing
    is the stopping signal — and the Stop hook is the right place to enforce it.

## The hook-chain defects (from the audit)

- design-stop.py never blocks — the exact event where "not done until better than
  references" could be mechanical. It also judges from code (detect.mjs) at Stop.
- design-verify-gate.py points AWAY from vision ("prefer read_page over screenshot",
  "two rounds maximum") — both rules contradict the winning recipe.
- Stale state: `.once-*` and `.design-verb` are never cleared per session → the
  inspection floor injected once on jul 28 and never again; same-verb sessions get zero
  intent injection. No SessionStart hook exists.
- Stop-report dedup hashes a per-minute timestamp → 48 spam reports; the dedups that DO
  hold are the ones suppressing needed injections. Backwards.
- DESIGN_GATE_BLOCKING unset → the only hard enforcement point is advisory in practice.
- Greenfield (no DESIGN.md) = zero pre-write enforcement — the Alunix case.
- No hook records whether vision happened, so no report can flag its absence.
- Bypass routes: Bash-written files skip gate+route; mcp__claude-in-chrome__* skips the
  verify gate.

## What the rebuild must do

A. Make the craft floor resident: fold house physics + positive moves + lane naming +
   composition contract into SKILL.md itself, and require reading ONE demo-site source
   end-to-end before any marketing build (the sites are the executed spec).
B. Enforce the exit bar mechanically: Stop-block for design sessions until renders were
   captured AND read after the last UI edit, with the reason restating the goal (beat the
   named references; a full clean pass, said out loud).
C. Track vision: a PostToolUse hook records PNG/image Reads into the ledger.
D. SessionStart hygiene: clear .once-*, .design-verb, .stop-signature; rotate the ledger.
E. Fix the stop-report dedup (hash content, not timestamp). Invert the verify-gate text
   (vision-first, no round cap). Set DESIGN_GATE_BLOCKING=1.
F. Imagery-first gate: no first render review without sourced imagery or an explicit
   user waiver; for tech/SaaS surfaces, 21st.dev-style component sourcing is a named
   alternative. Contact-sheet method canonized.
G. Anti-convergence: never converge on the same choices across generations; a named lane
   per artifact.
