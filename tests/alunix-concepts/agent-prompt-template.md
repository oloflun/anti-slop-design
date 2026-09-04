# Prompt template — one concept builder (K1..K6)

Fill {{K}}, {{NAME}}, {{ROW}} (the K-row of contract.md pasted), {{LOCKS}} (slugs), {{VOICE}},
{{ASSETS}} (photo files allowed, or "inga foton").

---

You are building concept {{K}} "{{NAME}}" for Alunix's web-design service. Work in
`C:\Users\Anton L\anti-slop-design`. This is NOT a blind test: run the real design chain and
load skills with the Skill tool (they are logged; the log is part of the evaluation).

Read, in this order, nothing else first:
1. `tests/alunix-concepts/brief.md` (facts and the forbidden list, binding)
2. `tests/alunix-concepts/contract.md` (your row {{K}} and the fingerprint row; the other rows
   are what you must NOT resemble)
3. `design-catalogue/TASTE.md` sections 1, 4, 6
4. Your reference-lock entries: {{LOCKS}} — `design-catalogue/entries/<slug>/entry.md` as
   text and `fold.webp` (+ 2 slices) as images. Read them as pixels.
5. `Skill(design)` — then follow SKILL.md Steps 1b (write the reference lock + decision
   ledger as an HTML comment at the top of your file), 2b (grammar, feeling curve, signature
   move exactly as your contract row says; skip the bake-off, this IS a bake-off cell), 3, 4, 5.

Copy: `Skill(copywriting)` with this voice rule as CONTENT FUNDAMENTALS: "{{VOICE}}". Then
read `~/.agents/skills/design/references/copy-gate.md` in full (Pass 1b line-sources and the
structure rule) and apply it, then `Skill(humanizer-svenska)` on every Swedish string. Swedish
only in this concept. No em or en dashes anywhere in visible text. Every number must come from
brief.md. Pricing/delivery time are `[behövs pris]` / `[behövs leveranstid]` in visible text,
styled as a labelled placeholder, never a fake number.

Build: ONE file `tests/alunix-concepts/cells/{{K}}-chain/index.html` (inline CSS + JS, no
frameworks, no CDN except Google Fonts; fonts must be real Google Fonts or system). Fold +
three sections (proof = the three demos as real links with their screenshots copied from
`C:\Users\Anton L\alunix\public\demos\{calyx,horai,hyperborea}.webp` into
`tests/alunix-concepts/cells/{{K}}-chain/`; how it works with placeholders; close with
`hej@alunix.se` as text + mailto). ≤ 400 lines. Photos: {{ASSETS}}. Reveal system fails
toward visible (threshold 0, above-fold revealed at mount, 1.5 s failsafe, noscript).
`prefers-reduced-motion` removes the journey, not the content. Inputs never below 16 px.
The three demos must stay clearly legible as the page's proof.

Hard rules from the contract: your fingerprint row exactly; ≤ 2/6 shared with any other K row
and with your primary source; no palette, type pairing, section order or signature move copied
from a source; the decision ledger names what was borrowed (principle) and what was rejected.

Verify (Step 5), all from the repo root:
- `python "C:/Users/Anton L/.agents/skills/design/scripts/shoot.py" tests/alunix-concepts/cells/{{K}}-chain/shots "file:///C:/Users/Anton L/anti-slop-design/tests/alunix-concepts/cells/{{K}}-chain/index.html"` and READ both PNGs. Fix what you see. Iterate until a pass finds nothing.
- `python "C:/Users/Anton L/.agents/skills/design/scripts/scroll_verify.py" "file:///C:/Users/Anton L/anti-slop-design/tests/alunix-concepts/cells/{{K}}-chain/index.html"` → zero dead scroll, zero unrevealed, zero blankBands.
- `python "C:/Users/Anton L/.agents/skills/a11y-audit/scripts/a11y_scan.py" "file:///C:/Users/Anton L/anti-slop-design/tests/alunix-concepts/cells/{{K}}-chain/index.html"` → no serious/critical.
- `node "C:/Users/Anton L/.agents/skills/impeccable/scripts/detect.mjs" tests/alunix-concepts/cells/{{K}}-chain/index.html` if present; fix findings.

Deliver: the HTML, the shots, and `tests/alunix-concepts/cells/{{K}}-chain/NOTES.md` with:
the reference lock + decision ledger (copy of the header comment), the fingerprint row you
built, the six-line feeling curve, the full Swedish copy as plain text, the list of Skill(...)
calls you made in order, and the verification numbers. Report back in under 150 words.
