# Process — SlopMonster loop on `draft.md`

Working dir for all commands: `C:\Users\Anton L\anti-slop-design\tests\ab\11-slopmonster\B-slopmonster`.
Tool paths: `C:\Users\Anton L\.agents\skills\slopmonster\tools\{deslop.py,cleanse.sh}`.

## 1 · SCORE — `python deslop.py draft.md`

```
python "C:/Users/Anton L/.agents/skills/slopmonster/tools/deslop.py" draft.md
```

```
485 words of visible copy

  AI constructions:
    · the 'whether you're X or Y' opener  (1)
    · 'say goodbye to'  (1)
  AI vocabulary:
    · leverage  (1)
    · seamless  (1)
    · elevate  (1)
    · unlock  (1)
    · empower  (1)
    · game-changing  (1)
    · effortless  (1)
  punctuation cadence:
    · two or more em-dashes in one sentence  (Capture every request and response your app makes … headers, bodies, t)
  rule-of-three rhythm:
    · rule-of-three list  (effortlessly, reliably, and locally)

  score 1/5  needs a cleanse
```

**Every hit above came from the English (Kvist) half of the file.** To confirm the vocabulary
catalogue is genuinely English-only, I isolated the Swedish half (`# Florhuset Majorna` onward)
and scored it alone:

```
python "C:/Users/Anton L/.agents/skills/slopmonster/tools/deslop.py" draft_sv_only.md
→ 274 words of visible copy
  score 5/5  CLEAN
```

The Swedish draft — full of AI tells — comes back **CLEAN**. See "Swedish coverage" below.

## 2 · REWRITE — three passes, by hand

Applied to every section of both pages at once (English and Swedish), per `references/signs-of-ai-writing.md`
and `references/principles.md`.

**Pass 1 — kill the vocabulary.** Removed `unlock`, `seamless`, `game-changing`, `empowers`,
`leverage`, `elevate`, `effortless`. English page lost "Unlock seamless API confidence",
"game-changing developer experience", "leverage real traffic", "elevate your workflow".
Swedish equivalents removed by hand (not linter-driven, since the catalogue can't see them):
`kurerar` (curated), `noggrant utvalt`, `upptäck glädjen i`.

**Pass 2 — kill the shapes.** Cut `Kvist is not just a proxy, it's a game-changing developer
experience` (the loudest tell, though the regex missed this exact instance because the subject
is "Kvist" rather than "it"), `whether you're a solo hacker or a fast-growing team`, `say goodbye
to flaky integration tests`, the "faster, ship smarter, and sleep better" tricolon, the
"effortlessly, reliably, and locally" tricolon, the double em-dash in the Record bullet, and
"you're not guessing, you're knowing" (a not-X-but-Y variant). By hand in Swedish: `inte bara en
blomsterbutik — det är en upplevelse` (the exact Swedish shape of "not just X, it's Y" —
undetectable to the English regex), `oavsett om du firar, sörjer eller...` (a whether-you're-X-
or-Y equivalent), `elegans möter naturlighet` (an "X meets Y" construction), the em-dash cadence
in the wedding step 3 and the subscription bullets.

**Pass 3 — put a person back in.** Removed the one invented-proof claim the linter's noun list
happens to miss — `Trusted by 10,000+ happy developers worldwide` — replacing it with a concrete,
checkable claim about the actual audience (no QA team → diff catches the break before a customer
does) instead of a borrowed number. Varied sentence length (short fragments: "Runs on your
laptop.", "Same input, different code."). Kept one rough edge per section rather than five. In
Swedish, replaced vague virtue-listing (`passion, precision och kärlek till hantverket`) with
specific, checkable claims (bouquets rebound weekly on what's actually in season; the Sunday
bouquet is explicitly "what was left over" — an admission a cautious writer would have cut, and
exactly the kind of texture the model draft has none of). No numbers, customers, or quotes were
invented anywhere in either language; every price and time in the draft (`495 kr`, `190 kr`,
`Onsdagar 18–20.30`, `Mariaplan 4`, opening hours) was carried over unchanged.

Result written to `rewritten.md`. Self-check before cleansing:

```
python deslop.py rewritten.md → 521 words, score 5/5 CLEAN
```

## 3 · CLEANSE — rival model

```
bash "C:/Users/Anton L/.agents/skills/slopmonster/tools/cleanse.sh" rewritten.md > cleansed.md
```

`codex` CLI was found and used (GPT-5.6 via `codex exec --skip-git-repo-check --sandbox
read-only`). Exit code 0, no stderr. It ran cleanly on both languages in one pass, despite the
draft mixing English and Swedish — worth flagging since `cleanse.sh`'s prompt gives no explicit
instruction about mixed-language input.

**Deviation from the tool's own contract:** the prompt (`prompts/cleanse.txt`) says "return only
the copy," but codex appended a five-line "what changed" bullet list after a `---` separator at
the end of `cleansed.md`. I rescored the file exactly as returned (see below — it still passed,
because the summary text itself happens to be plain, tell-free prose), then trimmed the trailing
summary before treating the file as source copy for `final.md`, since it is commentary, not page
content. This is the summary codex produced, kept here as the record of what it changed rather
than as page copy:

- Removed em dashes in English copy where they added AI-ish cadence, while keeping the existing markdown structure intact.
- Cut stacked setup language like "here's what setup actually looks like" and tightened the phrasing.
- Broke up same-length rhythm in both languages with shorter sentences, including "No mock that quietly stopped matching reality." and "Inte det som legat kvar i kylen."
- Kept all source claims and numbers only, including `190 kr`, `495 kr`, and `Onsdagar 18–20.30`.
- Left one rough edge with contractions and fragments, like "Here's" and "No mock that quietly stopped matching reality."

Verified against the actual diff — codex's real changes were narrower than its own summary
claims (no new sentence-length rewrite in the bouquets list, for instance): it converted the
remaining single em-dashes to periods/commas in six places (EN hero, EN "Why Kvist" bullet 3, EN
Code line, EN CTA, SV hero, SV Ateljékvällar), and trimmed a handful of words for rhythm ("months
ago", "actually", "you" in one spot). No facts, numbers, or claims were added or changed.

## 4 · RE-LINT

```
python deslop.py cleansed.md   (raw codex output, stray summary block included) → 609 words, score 5/5 CLEAN
python deslop.py final.md      (summary trimmed — final deliverable)            → 511 words, score 5/5 CLEAN
```

(A throwaway intermediate — `cleansed.md` with just the trailing summary sliced off, before it
was relabeled and saved as `final.md` — was also scored during the check and came back 511 words,
5/5 CLEAN; it wasn't kept as a separate file since `final.md` is that exact content.)

**Score history:** `draft.md` 1/5 → `rewritten.md` (hand rewrite) 5/5 → `cleansed.md` 5/5 →
`final.md` 5/5. One iteration of the loop was enough; no second cleanse pass was needed.

## Swedish coverage — what the linter did and did not catch

`deslop.py`'s five groups are English-pattern regex: the vocabulary list is English words
(`leverage`, `seamless`…), the construction phrases are English sentence shapes (`not just X, but
Y`, `whether you're X or Y`…), and the rule-of-three regex requires the literal word `and`
between items. None of that fires on Swedish text, so the AI-slop Swedish half of `draft.md`
scored a clean 5/5 on its own — proof the gate is not testing that language at all, not proof the
copy was clean.

**What it did catch, incidentally:** nothing Swedish-specific. The one punctuation rule that is
language-agnostic (two-or-more-em-dashes-in-one-sentence, and the compound-word-stacking rule) is
theoretically language-neutral, but none of the Swedish sentences happened to cross that threshold
(each Swedish em-dash instance is a single dash per sentence, not a stacked pair) so even the
one rule that could have caught something never fired.

**What it missed entirely**, confirmed by hand against `references/signs-of-ai-writing.md`:

- `Florhuset Majorna är inte bara en blomsterbutik — det är en upplevelse.` — the Swedish
  `inte bara X — det är Y` is a structural match for "the single loudest tell in English right
  now" (`not just X, it's Y`), invisible to the regex because the words are Swedish.
- `Vi skapar unika, handbundna buketter med passion, precision och kärlek till hantverket` —
  a rule-of-three (`passion, precision och kärlek`) joined by Swedish `och`, not English `and`,
  so the rhythm rule never fires.
- `oavsett om du firar, sörjer eller bara vill förgylla vardagen` — a whether-you're-X-or-Y
  opener in Swedish clothing.
- Vocabulary-tier tells with no Swedish entry in the catalogue: `kurerar` (curated),
  `noggrant utvalt` (meticulously curated), `en explosion av färg` / `en harmonisk symfoni`
  (purple-prose cliché pairing, the Swedish cousin of "myriad"/"tapestry"), `elegans möter
  naturlighet` ("X meets Y" construction), `enkelhet i sin renaste form` (superlative padding),
  `i hjärtat av` ("in the heart of" — a top-tier English cliché with an exact Swedish translation
  the linter has never heard of), `älskad mötesplats för blomsterälskare` (an unearned-affection
  claim — arguably invented proof, since nothing establishes the shop is "beloved" — that the
  PROOF regex cannot see because it looks for a number, not a sentiment), `upptäck glädjen i att
  binda själv` (an "imagine a…"-style invitation opener), `populära ateljékvällar` (an unproven
  popularity claim — same invented-proof shape as `Trusted by 10,000+ developers`, again invisible
  because there is no digit), `sömlöst och stressfritt` and `utan att du behöver lyfta ett finger`
  (idiom-cliché pairs).
- A second miss on the **English** side worth naming for completeness: `Trusted by 10,000+ happy
  developers worldwide` should have tripped the `proof` group (a number beside a noun), but the
  noun list (`users`, `customers`, `learners`, `students`, `teams`, `members`, `companies`,
  `businesses`, `homeowners`, `subscribers`, `clients`, `patients`, `readers`, `sites`,
  `projects`) does not include `developers`, so it passed silently. Same failure mode as the
  Swedish gaps — the catalogue is a finite word list, and anything outside it is invisible
  regardless of language.

**Fix applied:** since the tool can't be pointed at Swedish, I ran the exact three-pass method
from Step 2 by hand against the Swedish half, matching each Swedish sentence against the *shape*
of the English catalogue rather than its literal words (e.g. treating `inte bara X — det är Y` as
the same tell as `not just X, it's Y` because it's the same construction, not because a regex
caught it). The rewritten Swedish copy in `final.md` has none of the six items listed above; I
verified this by rereading each Swedish paragraph against the signs-of-ai-writing catalogue by
eye rather than by score, since no automated score exists for that language here.

## Files in this directory

- `draft.md` — original two-page AI-slop draft (given).
- `rewritten.md` — hand rewrite, three passes, both languages (score 5/5 on English half; Swedish
  verified by hand).
- `cleansed.md` — raw output of `cleanse.sh` (codex/GPT-5.6), including the stray "what changed"
  summary it appended below a `---` separator despite the "return only the copy" instruction.
- `final.md` — `cleansed.md` with the stray summary trimmed and section headers relabeled `final`
  instead of `rewritten`/`omskriven`. This is the deliverable; score 5/5 CLEAN.
- `process.md` — this file.
