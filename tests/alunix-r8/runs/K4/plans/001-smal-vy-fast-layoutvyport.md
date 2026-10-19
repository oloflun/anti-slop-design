# 001 — Ge båda ramarna en fast layoutvyport på 1440 och en statisk skala under 640 px

- **Status**: TODO
- **Commit**: b2e1ecd
- **Severity**: HIGH
- **Category**: funktionsfel (F-007-avvikelse, s1 vid 390)
- **Estimated scope**: 1 fil (`tests/alunix-r8/runs/K4/index.html`), en mediafråga plus fyra rader i monteringsfunktionen

## Problem

Vid 390 px är varje halva av scenen 195 px bred, och båda ramarna lägger ut mot
390 px. Besökaren ser alltså **en halv telefonsida per sida**, inte två sidor.
Läst som pixlar i `tests/alunix-r8/review/r2/K4-fold-390.png`:

- Vänstra halvan: mallsidans navpost `Flowstack` skjuter över sömmen; rubriken
  bryts till `The all-` / `platform` / `modern` och varje fortsättning är klippt
  mitt i ord; brödtexten klipps mitt i rad (`Flowstack helps tea`,
  `AI-powered workflo`, `collaboration, and se`, `integrations across y`).
- Högra halvan: Calyx jätterubrik syns som fragmenten `re,` och `ockholm.`
  svävande över fotot, plus `ITION` och brödtext klippt mitt i rad.

Målbilden (`malbilder/K4.md`) säger *"vänster halva = en typisk mallsida (live),
höger halva = Calyx live"* och `concepts-K4.md` § (3) s1 säger att de två
sajterna står **helt stilla** medan besökaren läser rubriken. Vid 390 står de
inte stilla som två sidor; de står som två trasiga sidor bredvid varandra, och
cellens hela argument — *besökaren avgör själv* — kan inte fällas.

Nuvarande kod:

```css
/* tests/alunix-r8/runs/K4/index.html:171 — current */
.frames {
  position: absolute;
  inset: var(--head-h) 0 0 0;
  --head-h: 232px;
}

/* :203 — current */
.layer > iframe {
  display: block;
  width: 100%;
  height: 100%;
  border: 0;
  background: var(--paper);
}

/* :415 — current */
@media (max-width: 640px) {
  .frames { --head-h: 196px; }
  ...
}
```

`width: 100%` gör ramens layoutvyport lika bred som scenen, alltså 390 px på en
telefon. Det är den raden som skapar felet.

## Target

Under 640 px lägger båda ramarna ut mot **1440 px** och skalas med **en enda
statisk `scale()` satt vid montering**. Skalan ändras aldrig under akten.
Bandets höjd härleds ur skalan så att exakt samma bildutsnitt som vid 1440 syns,
och ingen död pappersyta blir kvar.

Måltal vid 390 × 844:

| Storhet | Målvärde |
|---|---|
| Ramens layoutbredd | `1440px` |
| Ramens layouthöjd | `668px` (samma som den synliga scenen vid 1440 × 900: `900 − 232`) |
| Skala | `390 / 1440 = 0.2708` |
| Utskriftsbandets renderade höjd | `668 × 0.2708 = 181px` (±2 px) |
| Papper ovanför bandet | rubrik + `Före`/`Efter` + mailto, som idag |
| Papper under bandet | resten, jämnt fördelat så att bandet står optiskt centrerat i arket |

```css
/* target — ersätter .layer > iframe:s width/height under 640 */
@media (max-width: 640px) {
  .frames {
    /* bandet är en liggande remsa, inte en helskärmsyta */
    inset: var(--head-h) 0 auto 0;
    height: var(--band-h);          /* skrivs av JS vid montering, se Steps */
  }
  .layer > iframe {
    width: 1440px;
    height: 668px;
    transform: scale(var(--frame-scale));
    transform-origin: 0 0;
  }
}
```

`--frame-scale` och `--band-h` sätts **en gång** vid montering och vid `resize`,
aldrig i akten och aldrig per bildruta.

## Repo conventions to follow

- Registrerade lokaler deklareras med `@property` överst i `<style>`; se
  `index.html:61` (`--split`) och `:68` (`--d`). `--frame-scale` registreras på
  samma sätt som `<number>` med `inherits: true`, `--band-h` som `<length>`.
- Värden som kommer ur mätning skrivs som en kommentar med talet, i samma stil
  som `:194` och `:411`.
- Alla `.sc-*`-selektorer är motorns; rör dem aldrig (AB06). Bandet är cellens
  egen `.frames`.
- Precedensen för en statisk skala satt vid montering står i
  `runs/K3/NOTES.md` § Öppet efter R2: *"En statisk skala satt vid montering är
  inte samma sak som att transformera en ram efter att den visats."* Skriv in
  samma mening som en rad i `BRIEF.md` § decision ledger.

## Steps

1. Registrera två lokaler direkt efter `@property --d` (`index.html:68`):
   `--frame-scale` (`<number>`, `inherits: true`, `initial-value: 1`) och
   `--band-h` (`<length>`, `inherits: true`, `initial-value: 0px`).
2. Lägg till en funktion `sizeFrames()` i sidans JS, anropad från samma ställe
   som `relayout()` (`index.html:754`) och från `resize`:
   - läs `stage.clientWidth`;
   - om bredden > 640: sätt `--frame-scale: 1`, ta bort `--band-h`, låt
     `.frames` behålla `inset: var(--head-h) 0 0 0`;
   - annars: `scale = width / 1440`, skriv `--frame-scale: scale.toFixed(4)` och
     `--band-h: Math.round(668 * scale) + 'px'` på `.split`.
   - Funktionen får aldrig anropas ur rAF-loopen och aldrig ur `paintSplit`.
3. Lägg reglerna ur § Target i den befintliga `@media (max-width: 640px)`-blocket
   (`index.html:415`).
4. Centrera bandet optiskt: sätt `--head-h` under 640 så att papperet över
   bandet och papperet under bandet skiljer sig med högst 15 %, mätt vid
   390 × 844. Skriv ut de två talen som en kommentar.
5. Kontrollera att `clip-path` på `.layer--before` (`:197`) fortfarande räknar
   mot `.layer`-boxen och inte mot den skalade ramen: klippet ska sitta på
   `.layer`, ramen inuti är skalad. Ändra ingenting om det redan stämmer.
6. Kontrollera att träffytan i `.seam` (`:283`, `:289`, `:318`) fortfarande
   följer `--split × 100%` av scenens bredd och inte av ramens 1440. Den ligger
   på `.seam`, alltså på scenen, och ska vara oförändrad.
7. Skriv in beslutet som en rad i `BRIEF.md` § decision ledger (Area: hero-device,
   Source: F-007-kontrollen R2, Source rule: PRODUCT.md princip 1) och som en rad
   i `NOTES.md` § Byggarens rader.

## Boundaries

- Rör INTE `sites/before-ai-slop.html` eller `sites/calyx.html`. Exempelsajterna
  redigeras aldrig.
- Rör INTE motorn eller `sc-smooth.js`, och restyla ingen `.sc-*`-klass.
- Använd INTE demo-bilderna i `assets/`. De står kvar som dokumenterad reserv och
  ska inte in i layouten.
- Skalan får INTE animeras, interpoleras eller skrivas per bildruta. En gång vid
  montering och vid `resize`, inget annat.
- Lägg INTE till ett handtag, en knopp, en ikon eller en `dra`-text (gate 88).
- Lägg INTE till en brytpunkt till som byter grammatik: sömmen är lodrät på alla
  bredder.

## Verification

- **Mekaniskt**:
  - `python scripts/design/scroll_verify.py --url http://127.0.0.1:3311/tests/alunix-r8/runs/K4/index.html --width 390` — `blankBands` får inte växa mot R2:s utfall.
  - Överflödessvep vid 320, 375, 390, 414, 768, 1440: `scrollWidth == clientWidth` på var och en.
  - `python ~/.claude/skills/design/scripts/motion_probe.py` mot `section.split:--split`, hjul `100:60` och `20:120`, 4× CPU: `staircase` ska vara **0** i båda, som i R2. Talet får inte försämras av ändringen.
- **Feel check**: ladda sidan vid 390 × 844 och kontrollera i pixlar:
  - vid ps = 0 syns mallsidans emblemrad, rubrikblock och båda knapparna **hela** i vänstra halvan, och Calyx fotografi fyller högra halvan — alltså samma objekt som i `review/r2/K4-fold-1440.png`, i miniatyr;
  - ingen textrad är avskuren av scenens vänster- eller högerkant. Bara sömmen får skära något;
  - dra i sömmen: delaren följer fingret 1:1, släpps och landar på scrollens värde, aldrig på 0,5;
  - vid ps = 1 fyller Calyx bandet helt och oskuret.
- **Done when**: en skärmbild vid 390 × 844 vid ps = 0 visar samma komposition som 1440-bilden i miniatyr, bandet är 181 ± 2 px högt, och ingen halva innehåller ett ord som är avskuret av en annan kant än sömmen.
