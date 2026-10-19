# 002 — Ge delaren tillbaka rollen som aktens displayelement mellan ps 0,10 och 0,68

- **Status**: TODO
- **Commit**: b2e1ecd
- **Severity**: HIGH
- **Category**: flöde och hierarki (F-007-avvikelse, s2 vid 1440 och 390)
- **Estimated scope**: 1 fil (`tests/alunix-r8/runs/K4/index.html`), ett värde och en kurva

## Problem

`concepts-K4.md` § (3) s2 låser skärmens displayelement:

> | s2 | a1, ps 0,10–0,68 | **Delaren** — den lodräta hårlinjen med `#1E5E9C`, på väg vänsterut | Rubrikens före-halva tunnas … mallsidans mättnad faller |

Läst som pixlar i `runs/K4/shots/r2/act-mid-1440.png` (ps ≈ 0,40, delaren vid
x = 400) är delaren **inte** vyns displayelement. Det som ögat landar på är
tre vita serif-fragment ur Calyx egen jätterubrik, ungefär 90 px höga, tvärs
över fotografiet i högra halvan:

```
cal
ure,
olm.
```

De är resterna av `Botanical / architecture, / from Stockholm.`, vars vänsterände
ligger utanför den avslöjade ytan. Delaren är 2 px bred. En 2 px linje kan inte
bära en vy mot tre 90 px glyfgrupper, och `concepts-K4.md` § (1) säger att typen
ska vika under akten — här gör den motsatsen: den enda display-typ som syns mitt
i akten är trasig typ ur en annan sida.

Konsekvensen för argumentet är materiell: mitt i akten ser "efter"-sidan lika
sönderklippt ut som "före"-sidan, och sidans hela tes är att den ena är hel.

Samma fragment finns vid 390 (`review/r2/K4-fold-390.png`: `re,` och `ockholm.`).

Nuvarande kod, kurvan som styr resan:

```js
/* tests/alunix-r8/runs/K4/index.html:582 — current */
return 0.5 * (1 - clamp01((ps - SILENCE) / (1 - SILENCE)));
```

Resan är alltså linjär från `--split` 0,5 till 0 över ps 0,10 → 1,0. Calyx egen
jätterubrik upptar ungefär x 30–600 av dess 1440 breda layout, alltså
`--split` ≈ 0,42 → 0,02. Med en linjär kurva ligger sömmen inne i det intervallet
under **cirka 44 % av hela akten**.

## Target

Sömmen ska passera Calyx egna display-typzon fort, och gå långsamt där det inte
finns något att skära sönder. Resan förblir **monoton**, den vänder aldrig och
den studsar aldrig; bara hastighetsprofilen ändras.

Måltal, mätbara som skärmbilder:

| Mätpunkt | Målvärde |
|---|---|
| Andel av akten där `--split` ligger i intervallet 0,42–0,02 | **≤ 0,12** (idag ≈ 0,44) |
| `--split` vid ps = 0,40 | **≥ 0,44** (idag 0,167) |
| `--split` vid ps = 0,72 | **≤ 0,06** |
| Största legibla objektet i högra halvan vid ps = 0,40, 1440 × 900 | Calyx **fotografi**, inte ett rubrikfragment |
| `staircase` på `--split`, hjul 100:60 och 20:120, 4× CPU | **0**, oförändrat |
| `max_step` på `--split`, hjul 20:120 | **≤ 3 %**, oförändrat |

Kurvan, skriven ut:

```js
/* target — samma monotona resa, annan hastighetsprofil.
   ease: långsam till ps 0.55, sedan snabbt genom Calyx typzon.
   Kontrollpunkterna är valda så att split(0.40) = 0.44 och split(0.72) = 0.05. */
function splitTarget(ps) {
  var t = clamp01((ps - SILENCE) / (1 - SILENCE));
  var e = t * t * t;                    // ren cubic-in, monoton, derivata ≥ 0
  return 0.5 * (1 - e);
}
```

Kontrollräkning med `SILENCE = 0.10`: `ps = 0.40 → t = 0.333 → e = 0.037 →
split = 0.481`. `ps = 0.72 → t = 0.689 → e = 0.327 → split = 0.337` — **det
räcker inte**. Byggaren ska därför **mäta fram exponenten** i stället för att
ärva 3: kör `splitTarget` med exponenter 1,5, 2, 2,5 och 3, skärmbilda vid
ps = 0,40 och ps = 0,72 vid 1440, och välj det lägsta exponentvärde som
uppfyller **båda** raderna i tabellen ovan. Skriv in det mätta värdet och de två
skärmbilderna som en rad i `NOTES.md`.

Om ingen exponent uppfyller båda raderna: fall tillbaka på det andra tillåtna
ingreppet, ett **fönster** i stället för en exponent — sömmen står stilla vid
`--split` ≈ 0,44 över ps 0,10–0,62 och gör hela resan 0,44 → 0 över ps 0,62–1,0.
Det är fortfarande monotont och fortfarande 1:1 mot handen inom sitt fönster.
Välj det som ger den jämnaste `motion_probe`-kurvan och skriv ut varför.

## Repo conventions to follow

- Kurvor och fönster i den här filen skrivs som rena funktioner av `ps` och
  kommenteras med det mätta talet; se `index.html:582` och `:690`.
- `clamp01` finns redan i filen; återanvänd den.
- Allt som ögat ser förflytta sig läser `--sc-ps`, aldrig rå `--sc-p` (F-014).
  Ändringen får inte flytta någon avläsning från `--sc-ps`.
- Fjädern, pekarhandoffen och tangentbordssteget läser `target` och ska fortsätta
  göra det oförändrat: ändringen sitter i hur `target` beräknas, inte i hur den
  konsumeras.

## Steps

1. Byt `index.html:582` mot en `splitTarget(ps)` med en namngiven exponent i en
   konstant överst, `var SPLIT_EASE = <mätt värde>;`.
2. Kör mätserien i § Target och skriv in exponenten, de två `--split`-värdena vid
   ps 0,40 och 0,72, och filnamnen på de två skärmbilderna i `NOTES.md`.
3. Kontrollera att `stepPs` för tangentbordet (`index.html:690`) fortfarande ger
   ett steg på ungefär 2 % av `--split` **efter** kurvbytet; justera talet så att
   ett piltangenttryck flyttar delaren mellan 1,5 % och 3 % av scenens bredd,
   mätt, och skriv ut det mätta steget.
4. Kör om `motion_probe` på `section.split:--split` i båda kadenserna och skriv in
   `staircase` och `max_step`.
5. Skriv in avvikelsen som en rad i `BRIEF.md` § decision ledger (Area: aktform,
   Source: F-007-kontrollen R2, Source rule: `concepts-K4.md` § (3) s2).

## Boundaries

- Rör INTE `sites/calyx.html`. Calyx egen rubrik ändras aldrig, flyttas aldrig
  och skrollas aldrig ur bild av K4.
- Transformera ALDRIG `.layer--after` eller dess ram för att panorera Calyx.
  Ytan som fyller ramen vid ps = 1 ska vara samma ram som stod till höger vid
  ps = 0, i pixlar (F-010, `index.html:186`).
- Gör INTE resan icke-monoton. Ingen studs, ingen återgång, ingen paus som ser ut
  som att sidan hängt sig.
- Lägg INTE till en skrim, en toning eller en vinjett över Calyx för att dölja
  fragmenten. PRODUCT.md § Operating Context förbjuder skrim på en ram.
- Rör INTE fjädern (damping 1,0), pekarhandoffen eller avbrytbarheten. De är
  mätta och gröna.

## Verification

- **Mekaniskt**:
  - `motion_probe` på `section.split:--split`, hjul `100:60` och `20:120`, 4× CPU: `staircase = 0` i båda, `max_step ≤ 3 %` vid 20:120.
  - `--split` avläst per hjulklick nedåt: monoton, inga teckenflippar, samma kontroll som i R2 § Mätningar.
- **Feel check**: scrolla akten långsamt vid 1440 × 900 och kontrollera i pixlar:
  - vid ps = 0,40 är det största legibla objektet i högra halvan Calyx fotografi; inget rubrikfragment står ensamt över fotot;
  - delaren är den enda sak i vyn som byter läge, och ögat följer den;
  - resan känns som en hand som skjuter en gräns, inte som ett hopp: ingen bildruta flyttar sömmen mer än en glyfbredd vid hjul 20:120;
  - dra i sömmen mitt i det snabba partiet: 1:1-följningen är oförändrad och släppet landar på scrollens värde.
- **Done when**: skärmbilder vid ps = 0,12, 0,40 och 0,72 vid 1440 visar, i tur och ordning, två hela sidor, en delare på väg med Calyx foto bakom, och en nästan upplöst scen — och ingen av de tre bilderna har ett avskuret display-ord som vyns tyngsta objekt.
