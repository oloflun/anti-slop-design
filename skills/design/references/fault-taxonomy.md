# Fault taxonomy — what the owner rejects, and why

**Read this before you review, and read it before you build.** `design-catalogue/FEEDBACK.md`
is the *log*: one verdict, one rule, in the order he gave them. This file is the *analysis*:
every pushback from the Alunix run (2026-09-15 → 09-21, ~34 orders and 18 verdicts) sorted by
**cause**, because the cause is what a reviewer has to recognise before the owner has to say it
again.

The distinction that matters most, and the reason this file exists:

> **Almost none of the owner's pushbacks are taste.** Sorting them by cause, they land in
> eleven classes. Ten of them are *measurable* — a ratio, a seam, an overlap, a scale step, a
> cadence, a second reading, a control that does not do what it says. Only one class is
> exploration, and treating exploration as a defect is its own failure mode.

A reviewer who reports "this feels off" has done the owner's job for him. A reviewer who
reports *which class* and *what it measures* has done theirs.

---

## 1 · Balance and proportion

Something occupies too much or too little space **relative to its neighbour**. Never an
absolute size — always a ratio.

- *"minska även den överdrivna storleken som adressen har just nu"*
- *"förstorar hela rutan för ritningen och låter Calyx ta upp större plats i rutan, utan lika
  mycket luft runt om"*
- *"Exempelcase-rubriken ligger för ensamt och tar alldeles för stor plats"*
- *"'Första steget är ett samtal om vad du gör.' är så litet att det försvinner helt mellan det
  andra"*
- *"texten för 'Pris vid förfrågan' och Kontakt är alldeles för stor och blir malplacerad"*

**Detect.** For each element, name the element it is competing with and give the ratio. "The
address is 2,4× the ledger numerals" is a finding. "The address feels big" is not. A list
where one item is at a different weight than its siblings is always this class — either match
it or promote it deliberately.

**Also here:** one authority per page (TASTE § 1). Two elements fighting for the same
attention is balance, not style.

## 2 · Transition and seam

The join between two acts is wrong — a hard edge where two grounds meet, or the frames *in
between* carry nothing.

- *"övergången från den blå sektionen till ritningen är fortfarande för trubbig med stora
  fyrkantiga block i flera scroll-lägen"*
- *"Fixa även övergången mellan det blå blocket och ritningen … nu är det extremt platt"*
- *"övergången till exempelcase är även väldigt dåligt gjord med en mörk ruta"*
- *"testa … skapa en snygg övergång från bilden med prissektionen"*

**Detect.** Two separate checks, and both are required:
1. **The seam itself.** Do two grounds meet at a visible line? Sweep the boundary in wheel
   scroll and read it. A tonal inversion must *blend* or be a *deliberate* hard edge — never
   an accidental one.
2. **The frames between.** Sweep the whole act at 20 px and count frames below the text
   floor. Measured on this run: **46 of 121 frames under 18 % text, lowest 1,5 %.** An empty
   frame is not a pause, it is the fault.

**Never fix a transition with a translucent overlay.** A veil at partial opacity has a
mid-state, and the mid-state is grey. This was diagnosed twice on this run — once on
`.chapter-plate`, once again when the same shape was reintroduced. A gradient has no
mid-state; a clocked veil does.

## 3 · Collision, clipping, fit

Elements touch, overlap, or are cut. Purely measurable.

- *"siffrorna går ihop med texterna"* — the step number and the small-caps label, on every step
- *"undersidan av 'Från samtal till lanserad sida.' klipps i underkant"* — the heading cut by
  its own stamp box
- *"Innehållet ryms inte heller på helsida utan klipps"*
- *"Lös även problemet med utrymmet på bokningssidan av Hōrai för att allt ska rymmas på
  enklast möjliga sätt"*
- *"Observera även kanterna på sidramarna, där det syns en tunn färgkant, lös det helt och
  hållet"*

**Detect.** Bounding boxes, not eyeballs. Minimum gap between adjacent elements; every text
block fully inside its container (watch descenders — a clipped descender is the classic);
nothing overflowing its section at any width. **Check the pair he actually named:** on this
run a probe measured number→paragraph (59 px, passing) while the collision was
number→*label*, which nothing measured. Measure the pair that is visually adjacent, not the
pair that was easy to select.

## 4 · Scale and hierarchy

Something sits at the wrong level, so the eye is not drawn where it should be.

- *"ögonen ska dras dit och läsa texten automatisk"*
- *"texten under texten lika stor"* — a sub-line should match the line it belongs to
- *"Gör även texten 'Berätta om er verksamhet' större och mer Impactful"*

**Detect.** TASTE § 4.6 is the rule and it is exact: **display at least 5× body; subheads are
either small kickers (tracking, 11–13 px) or display size — never the 32 px middle.** A
heading that is neither is in the forbidden zone, whatever it looks like. With 16 px body the
display floor is 80 px. Name the step; do not describe the feeling.

## 5 · Copy voice — the AI register

The writing reads as generated. This is the class he has had to repeat **three times**, which
makes it the most expensive one in the log.

- *"det verkar helt hjärndött, helt självklara saker som skriker AI eftersom att man antar att
  kunden är helt IQ-befriad"*
- *"är återigen helt hjärndött, och precis samma AI-slop som jag reagerade på tidigare,
  bekräfta att du förstår varför"*
- *"texten under rubriken är fortfarande fruktansvärd AI-slop, bekräfta att du förstått vad jag
  menar, det är väldigt tydligt"*
- *"rubrikerna för de båda casen lite roligare, nu känns de väldigt platta och intetsägande"*

**Detect — and this is the part that is always missed: the fault is the CADENCE, not the
words.** Rewriting the vocabulary while keeping the shape reproduces it exactly, which is what
happened on the second and third attempt. The shapes:

- **The roadmap.** A sentence describing the section's own disposition — what follows, in what
  order, and why. *"Vi går igenom vad vi valde i dem och varför."*
- **The disclaimer.** A caveat about the material's status, placed before the material.
  *"Ingen av dem finns."*
- **Setup → caveat → roadmap**, in that order. The default shape of "introduce a section".
- **The obvious stated.** Telling the reader something they already know, which reads as
  contempt for them.
- **The page narrating itself** (F-018). Any sentence whose subject is the page, the section,
  the example or the selection.

**Run the test, not the vibe:** `skills/design/scripts/self_reference_scan.py` — four
categories, with a `--selftest` that must pass first. A prose rule with no test gets broken by
the next fluent paragraph; that is measured, not theoretical.

## 6 · Ambiguity — the line that can be misread

- *"'Hōrai serverar bokningen sist.' är lätt att feltolka, serverar de bokningar i andra hand,
  är det bättre med 'serverar bokningen först' eller vad är motiveringen bakom?"*

**Detect.** Read the line as a stranger with no context, and write down the **second reading**.
If a plausible reading is wrong or embarrassing, the line is a finding — and the fix is to
state the intended meaning directly, not to add a clarifying clause. He asks for the
reasoning, so give it: *why* this wording and not the other.

## 7 · Broken affordance and semantic mismatch

A control, a state, or a label does not do what it says.

- *"Gör även så att man kommer till kontaktsidan om man klickar på 'Boka möte' på visitkortet
  längst upp"* — the CTA opened a mail client instead of reaching the section
- *"Calyx ska inte vara svartvit, den kan vara det under ritningsprocessen, men ska få sin färg
  i den färdiga versionen i sista steget"* — colour as a function of progress, wrongly mapped
- *"Hōrai är ett fönster i fasaden, inte en ruta utanpå den"* (F-010) — a compositing
  relationship the build got wrong

**Detect.** Trace every interactive element to its **actual effect**, not its label: click it
and watch where it goes. Trace every time-varying property to the state it encodes: is the
value mapped to the right thing at the right moment? This class is invisible in a static
screenshot and must be walked.

## 8 · Calibration — the middle he can only recognise

He oscillates, and the oscillation is the information.

- process copy: 35–44 words → 18–22 → *"Texten blev även aningen för kortfattad, försök
  återigen hitta en balans mellan den ursprungliga versionen i v3C och den nuvarande"* → 28–34
- *"Försök förkorta texterna utan att de blir så kortfattade som tidigare"*

**Detect.** This class is **not a defect** and must not be reported as one. The target is a
band, and the band is found by reading what the *previous* version was and landing between the
two. Two things make it tractable:
- **When he supplies a target sentence, it is the spec.** He did twice (*"observera skillnaden
  och försök applicera det på de övriga med samma ton"*). His example is the tone; measure the
  difference he names — shorter, merged clauses, ends in an image — and apply it to the rest.
- **Count words.** "Aningen för kortfattad" against a numbered previous version is a number,
  not a mood.

## 9 · Emptiness — a column with no weight

- *"just nu är det som en rullande paragraf och läser uppnår inte den slående effekt som
  förväntas"*
- *"stora tomma ytor"* — recurring, in several rounds

**Detect.** Measure ink coverage per frame and per column. **Weight every column you open**:
a rail holding two whispered lines beside a large block is a hole, not a rail. Either give it
something with presence (a display numeral, an image, a full-height rule) or close it and give
the content the width.

## 10 · Exploration — NOT a fault

This is the class that produces noise when it is misread as a defect.

- *"Motivera den valet till den vita bakgrunden för ritningen. Jag vill att du ber om en
  inverterad variant"*
- *"Testa att invertera den sektionen till svart"*
- *"testa att lägga en bild undertill under texten, bredvid formuläret"*
- *"Jag vill att du testar lägga processbeskrivningarna på vänster sida om ritningen"*

**The signals are the words *testa* and *motivera*.** He is interrogating a decision, not
reporting a defect. What he wants is **the reasoning and the alternative**, and sometimes he
wants to see both to choose. A reviewer that flags an exploration request as a fault has
misread the job — and a builder that *argues instead of testing* has too.

**Corollary:** when a test is ordered, the deliverable is the comparison, named as such.
Present the two states side by side and say what each buys. Then let him pick.

## 11 · Process and tooling — the chain, not the page

- *"ALLT är fortfarande exakt likadant som innan den senaste rundan, är det ens något gjort?"*
- *"ändringarna dyker upp i preview först, INNAN du gör något annat"*
- *"jag förväntar mig att se större resultat utan lika många försök den här gången"*

**Detect.** Not a page fault. Enforced in [`chain-discipline.md`](chain-discipline.md) § V1
(a review surface never caches) and § V2 (verify in the render, not in the bytes). The owner
concluded nothing had been built because the board served him a cached round — twice. When the
owner says "nothing changed", **suspect the surface before the build.**

---

## How to use this in a review

1. **Name the class.** "This is class 3, collision" beats "this feels tight". Six of the eleven
   classes are pure measurement; three more are structural reads; only two need judgment.
2. **Give the number or the name of the pair.** Every class above has a unit — a ratio, a gap
   in px, a frame count, a word count, a scale step, a second reading, a destination URL.
3. **Check the pair he named, not the pair that was convenient.** The 59 px probe measured
   number→paragraph while the collision was number→label. A check that measures the wrong pair
   returns green forever.
4. **Never report class 10 as a fault.** If the order contains *testa* or *motivera*, the
   finding is a comparison, not a defect.
5. **The three classes he repeats are 2, 3 and 5** — the seam, the collision, and the AI
   register. If a round touches a transition, a heading, or a lede, check those three first;
   that is where his rejections have actually landed, three times each.

**The one-line version:** *almost every pushback is a measurable relationship between two
things — and the reviewer's job is to name the two things before he has to.*
