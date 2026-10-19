# 019 · Processakten i ny form: sju stycken i flödet, arket sticky, fönster ankrade i stegens läge, copy v1, "Hur vi tänker"

- **Status**: TODO (R6, efter 018)
- **Commit**: R5-läget av `runs/V3c/index.html`, md5 `fcbee8f1`
- **Severity**: HIGH (F-007-blockerande vid 390; Antons dom 2026-09-16 om innehållet)
- **Category**: Purpose + Cohesion (H-02, H-06, H-08, H-14, H-25, H-28, H-30, H-31)
- **Estimated scope**: 1 fil: ~60 rader CSS, ~90 rader markup, ~25 rader JS; `plans/010-process.md` får en rättelse (fotnot), `BRIEF.md` fyra ledgerrader
- **Källor**: Antons dom 2026-09-16 (stegen ska vara riktiga beskrivningar, inte fråga och svar); `PROCESS-UNDERLAG.md` § 3 (copy v1), § 4 (antagandena gäller), § 5 (formen); a11y F-03 (fix 3), F-05 (fix 5), F-08 (fix 8); Astra 3, 4, 7, 8; design-critic 1, 2, 4, 5; heuristik 1, 2, 3, 5, 6, 7; leadens F-007 (1440 sex av sju, 07 landar sent, 390 avviker materiellt); perf 3 (banor utanför stilträdet tills deras fönster öppnat)

## Problem

Sju rapporter, samma riktning. (1) Innehållet: varje steg är en rubrik, en fråga och ett
svar på en mening; Anton vill ha ett stycke per steg som täcker frågorna, som referenserna
gör. (2) Formen på 1440: sju absolut positionerade `<li>` korsfadas i en 384 px-spalt.
PageDown (787 px) landar aldrig på steg 02, 04 och 06 (a11y F-03); två texter ligger
ovanpå varandra vid varje fönstergräns (Astra 8); `elementFromPoint` returnerar ett
osynligt steg (a11y F-05); ankomstskärmen är tom i 504 px (critic 5, heuristik 6, 8);
sista steget landar efter att arket släppt sticky vid ps 0,806 (lead, critic 1, Astra 4,
heuristik 3); sektionsrubriken 25,6 px rankar under stegtitlarna (critic 4). (3) 390:
stegen staplas alla synliga före arket, arket är inte sticky och kommer in färdigritat
(lead, Astra 3, critic 2, heuristik "0 synliga px till ps 0,46"). (4) Perf: 7 `<li>` läser
`--sc-ps` per bildruta för korsfadningen; banor som ännu inte ritats ligger i stilträdet.

Sju stycken på fyra till sex meningar ryms inte i korsfadning. Highways form löser alla
fyra: stegen som prosa i flödet under varandra, arket sticky bredvid (1440) eller ovanför
(390), varje stegs fönster ankrat i stegets egen position i flödet.

```css
/* index.html:683-720 - current (utdrag) */
  .process{background:var(--bg);color:var(--ink);min-height:300svh;
    padding-block:0;position:relative;}
  .process-title{font-family:var(--f-display);font-weight:700;
    font-size:clamp(1.3rem,1.8vw,1.6rem);letter-spacing:-.01em;
  .process-stage{position:sticky;top:202px;height:495px;
    display:flex;align-items:center;justify-content:space-between;
    padding-inline:var(--rail-x) 80px;}
  .process-steps{position:relative;width:384px;max-width:384px;
    height:495px;flex:none;list-style:none;margin:0;padding:0;}
  .process-steps li{position:absolute;inset:0;
    display:flex;flex-direction:column;justify-content:center;gap:.6rem;}
/* index.html:712-718 - current */
  .process-steps li{
    opacity:min(
      clamp(0,calc((var(--sc-ps,0) - var(--step-start)) / 0.02),1),
      clamp(0,calc((var(--step-end) + 0.02 - var(--sc-ps,0)) / 0.02),1)
    );}
  .process-steps li[data-step="07"]{
    opacity:clamp(0,calc((var(--sc-ps,0) - var(--step-start)) / 0.02),1);}
/* index.html:835-841 - current */
  @media (max-width:899px){
    .process-stage{position:static;height:auto;flex-direction:column;
      align-items:stretch;padding-inline:var(--rail-x);gap:24px;}
    .process-sheet{width:100%;height:auto;aspect-ratio:320/640;}
    .process-steps{position:static;width:auto;max-width:none;height:auto;
      display:flex;flex-direction:column;gap:clamp(28px,6vh,56px);}
    .process-steps li{position:static;opacity:1 !important;}
```

## Target

### Formbeslutet, i tre rader

1. **Texten är alltid synlig och ligger i flödet**; ingen opacitet på stegen, ingen
   korsfadning. Det löser a11y F-03 och F-05, Astra 8, heuristik 1 och 7 utan ett enda
   hållfönster: PageDown kan bara landa på text som finns.
2. **Arket är sticky bredvid texten (≥ 1280) eller ovanför den (≤ 1279)** och ritas i
   takt med att stegen passerar viewportens mitt. Sektionens höjd är textens egen höjd;
   inga `300svh`, ingen manuell svans, inget steg 07 utanför sticky-hållet.
3. **Varje stegs fönster ankras i stegets egen position i flödet**, mätt en gång vid
   mount och resize av sidans befintliga `measureAct`, skrivet som fjorton tal på
   `#process` (`--s1..--s7`, `--e1..--e7`). Rittempot följer läsaren, inte en tabell.

### Målbild skärm för skärm, 1440x900

Layout: `#process` är en grid `minmax(300px,384px) minmax(0,880px)`, kolumngap
`clamp(48px,4vw,80px)`, inline-padding `var(--rail-x)`. Vänster: kicker, h2 (48 px),
ingressrad, sedan `<ol>` med sju `<li>` i flödet, var och en `padding-block:
clamp(40px,6vh,64px)`, index + titel (32 px versal) + stycke (16 px, 34ch) + marginalrad
(13 px, `--hair-ink`). Höger: `.process-stick` (`position:sticky; top:
max(24px, calc((100svh - 495px) / 2)); align-self:start`) som bär arket 880x495
(`width:100%; max-width:880px; height:auto; aspect-ratio:880/495`). Kolumnen slutar med
`padding-bottom: clamp(96px,12vh,140px)` så att steg 07 står i viewportens mitt medan
arket ännu är sticky.

Fönster per steg N (JS, se Steps 5): `--sN` = ps när `<li N>`:s överkant når 85 % av
viewporthöjden (steget kommer in i läszonen), `--eN` = ps när `<li N>`:s mitt står i
viewportens mitt. Arket ritar steg N:s banor mellan `--sN` och `--eN`, så att ritningen är
klar när stycket är mitt på skärmen. Beräknade värden vid 1440x900 (li-höjder ~460 px,
kolumnstart y 260, sektionshöjd ~3 700, liv ~4 600): s1 ≈ 0,09, e1 ≈ 0,16; s2 0,19, e2
0,26; s3 0,29, e3 0,36; s4 0,39, e4 0,46; s5 0,49, e5 0,56; s6 0,59, e6 0,66; s7 0,69, e7
0,76. Talen i CSS är **fallback** för no-JS; JS skriver de uppmätta.

| Skärm | Vad som står i viewportens mitt | Arket vid `--eN` | Sant mått |
|---|---|---|---|
| s-process-01 | 01 Uppstart, stycket | kontur `#p-outline` + A-glyf `#p-glyph` (plan 020) | inget |
| s-process-02 | 02 Planering | hjälplinjer, måttlinje, stationer, **320 · 768 · 1440** i accent | 320 · 768 · 1440 |
| s-process-03 | 03 Design | öppningen, spaltmått med utrop `7 rem` (geometri rättad i plan 020), ledare `16:9` | 16:9 · 7 rem |
| s-process-04 | 04 Utveckling | skraffering, liggarrader, lodrät måttlinje `96 px` | 96 px |
| s-process-05 | 05 Innehåll | Calyx maskad in, halvvägs vid `--s5 + 0,5·(e5 - s5)`, full vid `--e5` | inget nytt |
| s-process-06 | 06 Lansering | kontur tunnas, hjälplinjer och skraffering tonar, siffrorna faller till 12 px och byter till `--hair-ink` | inget nytt |
| s-process-07 | 07 Förvaltning | titelblocket ritas, revisionsfältet skrafferas, `A` | inget nytt |

`?preview=process-0N` scrollar till `top + yc_N - innerHeight/2` (li N:s mitt i
viewportens mitt) med `__scFreezeMotion = true`; ingen `forcePs`-slinga behövs längre,
eftersom det råa värdet där per konstruktion är `--eN`.

### Målbild skärm för skärm, 390x844 (och allt ≤ 1279)

`#process` blir en kolumn: kicker, h2, ingress, sedan `.process-stick` **före** `<ol>` i
DOM-ordning (markupen byts inte; `.process-stick` får `order:-1` i mediablocket och
`grid-template-columns:1fr`). Arket: `position:sticky; top:0; z-index:2;
background:var(--bg); padding-block:12px`, bredd `min(100%, 480px)` centrerad, viewBox
`0 0 320 360` (8:9; vid 358 px bredd 403 px hög = 48 % av 844). Texten passerar under
arket; varje `<li>` `padding-block: clamp(32px,5vh,48px)`. Fönstren ankras på samma sätt
(JS läser li-positionerna vid den aktuella bredden), men mot ett läsfönster som börjar
under arket: `--sN` när li-toppen når 95 % av vh, `--eN` när li-mitten står vid
`0,5·(vh + arkets höjd)` (mitten av den synliga texten). Reducerad plansch (K3:s regel: en
station visas bara på en bredd den beskriver): kontur, öppning 272x153 vid x 24 y 56,
måttkedjan `320 768 1440` som utrop (34 px) med baslinje y 236, måttlinje y 250 utan
stationer, `16:9`-ledare, titelblock x 112..296 y 292..346 (tre celler à 18), A-glyf
uppe till vänster. Hjälplinjer, skraffering, liggarrader, `7 rem` och `96 px` visas inte.
`plansch()` (rad 1503) byter viewBox till `0 0 320 360` vid ≤ 1279 och flyttar
`<text>`-koordinaterna som i dag; `MOBILE_TEXT` (rad 1496-1501) får nya y: `p-m320`
`[48,236]`, `p-m768` `[145,236]`, `p-m1440` `[304,236]`, `p-c-169` `[312,44]`, `p-c-rev`
`[204,306]`.

| Skärm 390 | Överst (sticky) | Under |
|---|---|---|
| s-process-01..07 | arket i tillstånd N | steg N:s index, titel, stycke, marginalrad |

### Copyutkast v1, ordagrant ur `PROCESS-UNDERLAG.md` § 3, med § 4:s antaganden inskrivna

Märks i källan `<!-- copy v1, copy-gate i R7 -->`. Vi-form, noll tankstreck, inga tal
utöver 320 · 768 · 1440, 16:9, 7 rem, 96 px. Rader som var märkta `[A]` är skrivna enligt
antagandet i § 4 (P1 "ett innehållssystem", P2 "sidan är ert att bygga vidare på" i stället
för "koden är er", P3 bara "vi finns kvar" och "samma väg som bygget", P4 utan
innehållshjälp, P5 domän nämns inte, P6 och P7 skrivs, P8 utanför, P9 sju steg, P10 skrivs).
Kopplingarna i 06 namnges med paketradens egna ord (bokning, betalning, kunddatabas).

**Ingress:** kicker `Så går det till` · h2 `Från samtal till lanserad sida.` · rad
`Sju steg, samma ordning i varje projekt, så att ni alltid vet var vi är.`

**01 Uppstart.** Vi börjar med ett samtal om er verksamhet: vad ni gör, vilka ni vill nå
och vad sidan ska göra för er. Ni behöver inte ha texter eller bilder klara, det räcker att
ni kan berätta. Efter samtalet skriver vi ner vad vi hört och vad vi föreslår, så att ni
kan läsa och rätta innan något ritas. Det dokumentet är grunden för allt som följer, och
ni får det.
*Marginal:* Ett tomt ark. Inget ritas innan vi vet vad sidan ska säga.

**02 Planering.** Vi ritar sidans struktur innan vi ritar dess utseende: vilka sidor som
finns, vad varje sida ska få besökaren att göra, och i vilken ordning innehållet kommer.
Vi planerar för tre skärmbredder från början, telefon, surfplatta och dator, så att
mobilen inte blir en efterhandskonstruktion. Ni ser strukturen som en enkel skiss och
godkänner den innan vi går vidare till design.
*Marginal:* 320, 768 och 1440, de tre bredder varje sida verifieras vid.

**03 Design.** Med strukturen på plats formger vi sidan: typografi, färg, bild och rytm
hämtas ur er verksamhet, inte ur en mall. Förslaget lägger vi på en testadress som ni
öppnar i er egen webbläsare, på er egen telefon, så att ni ser det som era kunder kommer
att se det. Ni lämnar synpunkter, vi justerar, och ni godkänner innan vi bygger vidare.
Inget går i produktion som ni inte sett.
*Marginal:* 16:9, öppningen där ert innehåll ska sitta, proportionen bestämd innan bilden finns.

**04 Utveckling.** Vi bygger sidan i kod från grunden, för de tre bredderna vi planerade
för. Sidan ska ladda snabbt, fungera med tangentbord och skärmläsare och gå att bygga
vidare på. Texter och bilder ändrar ni själva i ett innehållssystem; vi visar hur. Sidan är
ert att bygga vidare på. Behöver ni bokningar, betalning eller kunddatabas bygger vi det i
samma steg, på samma tekniska nivå som sajten.
*Marginal:* 96 px, radavståndet i liggaren, en mätt enhet som all rytm räknas ur.
*(Copy-agenten: "bygga vidare på" förekommer två gånger; den andra är P2:s antagande och
den första är underlagets, en av dem stryks i R7.)*

**05 Innehåll.** Ni kan er verksamhet, vi kan sätta den på plats. Ni levererar texter och
bilder i den takt ni har dem; vi bearbetar texten så att den är kort och läsbar och beskär
och optimerar bilderna för webben. Saknas något säger vi till i tid. Sidan fylls på
testadressen så att ni ser hur den växer.
*Marginal:* Strukturen får sitt material. Ritningen blir er sida.

**06 Lansering.** Innan sidan går live går vi igenom den tillsammans på testadressen:
varje länk, varje formulär, varje koppling till bokning, betalning och kunddatabas, på
telefon och på dator. Vi testar med tangentbord och skärmläsare, i tre bredder och i
riktiga webbläsare. Vi flyttar sedan sidan till er adress och kontrollerar att allt
fungerar på plats. Ni får en genomgång av sidan och av hur ni ändrar innehåll själva.
*Marginal:* Bläcket står kvar som ram. Ritningen och sidan är samma sak.

**07 Förvaltning.** Vi finns kvar efter lansering. En sida är ett levande dokument:
ändringar, nya sidor och nya funktioner går samma väg som bygget, testadress först,
godkännande, sedan live. Har ni en fråga mejlar ni oss på kontakt@alunix.se.
*Marginal:* Revisionsfältet fylls. En bokstav, aldrig ett datum.

**Liggarens tre underrader** (rad 1037-1050, rubrikerna `Design`/`Utveckling`/`System`
rörs inte):
- Design: Identitet och formspråk hämtat ur er verksamhet. Ni ser förslaget på en
  testadress och godkänner innan vi bygger.
- Utveckling: Byggt i kod från grunden för telefon, surfplatta och dator. Snabbt,
  tillgängligt och ert att bygga vidare på.
- System: Bokningar, betalning och kunddatabas byggda i samma steg som sajten och skötta
  efter lansering.

### "Hur vi tänker": eget kort avsnitt på papper, efter akten, före avslutet

Beslut: **inte** inne i akten (arket ritar steg, principerna är inte steg) utan som
`<section id="principer" class="principles on-paper" data-sc-act="flow">` direkt efter
`</section><!-- #process -->` och före `</main>`. Anatomin är sidans egen liggare
(`.ledger`, `.ledger-row`, `.ledger-body`, rad 641-650) med modifieraren
`.ledger--plain` (`grid-template-columns:1fr`, ingen numrering: gate 69), tre rader,
`data-sc-in data-sc-stagger="70"` på `.ledger`. Kicker `.kicker-sans`: `Hur vi tänker`.
Ingen ikon, inget kort. Padding `var(--panel-pad-y)` (`.panel-pad`), max-width 64ch.

- **Vi visar innan vi påstår.** De tre exempelsajterna på den här sidan är riktiga och går
  att använda. Det är hela vårt bevis, och det räcker.
- **Sidan ska fungera för alla.** Tre skärmbredder, tangentbord, skärmläsare, kontrast som
  går att läsa i solljus. Det är inte ett tillägg, det är hur vi bygger.
- **Ni ska kunna ändra själva.** En sida ni inte kan uppdatera åldras från dag ett.

(H-06: en femte anatomi, hairline-liggare utan nummer, mellan det ritade arket och den
typsatta adressen. Bär `data-sc-in`, alltså rörelse en gång, H-25.)

### Device-tabell för akten efter 019

| # | Vad | Device | Läser | Uttryck |
|---|---|---|---|---|
| 1 | arkets banor, steg N | `stroke-dashoffset` via `--p-l`, `pathLength="1"` | `--kN` (härledd ur `--sc-ps`, se nedan) | `--p-l:clamp(0,calc((var(--kN) - a) / (b - a)),1)` med `[a,b]` som andel av stegets fönster |
| 2 | skraffering, revisionsfält, stationer, liggarrader | `clip-path` wipe | `--kN` | samma |
| 3 | utrop, siffror | `opacity:var(--p-t)` | `--kN` | `--p-t:clamp(0,calc((var(--kN) - a) / 0.15),1)` |
| 4 | siffrornas fall och tonbyte | `transform:scale`, `fill:color-mix` | `--k6` | plan 020 |
| 5 | Calyx | `clip-path inset` | `--k5` | `inset(0 0 calc((1 - var(--k5)) * 100%) 0)` |
| 6 | arket | `position:sticky` | ingen | ren CSS |
| 7 | stegtexterna | inga; i flödet, `data-sc-in data-sc-stagger="70"` på `<ol>` för en engångs premium-fade | motorns egen | stagger 70 ms |
| 8 | ogated banor utanför stilträdet | `display:none` på `<g data-step="N">` tills `ps ≥ --sN`, togglas av `readState` vid gräns | `scrollY` en gång per bildruta (befintlig läsare) | `.process-sheet g[data-step]:not([data-on]){display:none}` |
| 9 | `will-change` | `.process.is-drawing .draw` bort (perf 7: inte kompositerbar) | | raden 825 tas bort |
| 10 | principerna | `flow` + `in` | motorns egen | stagger 70 |

`--k1..--k7` deklareras **på `#process`** som vanliga (oregistrerade) custom properties:
`--k1:clamp(0,calc((var(--sc-ps,0) - var(--s1)) / (var(--e1) - var(--s1))),1);` … `--k7`.
De ärvs av arkets alla barn (vanliga custom properties ärver; `--p-*` gör det inte, R5:s
verktygsfynd 6). `--s1..--e7` får CSS-fallback i samma regel (talen i målbildstabellen) och
skrivs om av JS.

### Fingerprint-delta

Cellens registerrad, cellen "Act-sequence shape": "… a sticky drawn process act **read as
prose in flow, windows anchored to the reader's position**, plus a hairline principles
ledger, 8 flow acts, ~9,4 vh". Signaturen oförändrad (kortet vänds). Arket blir aldrig sidan
(Calyx som bild), K3:s rad står isär.

### Vad i HELHET.md § 3 akten måste uppfylla

H-02, H-05, H-06, H-08, H-14 (vid 390 följer akten efter priset, plan 012 äger ordningen
före den), H-15, H-21, H-22, H-23, H-24, H-25, H-26, H-28 (uppdaterad: ett flow-ark, ingen
pin), H-29, H-30, H-31 (uppdaterad: ett stycke per steg som täcker frågorna, i stället för
fråga och svar), H-32, H-33, H-34, H-35 (inklusive 1024, 1280, 1366 för klippningen, plan 020).

## Repo conventions to follow

- `readState`/`measureAct` (rad 1293-1344) är sidans enda scroll-läsare; ankarmätningen
  läggs i `measureAct`, som redan körs vid mount, `load`, `resize` och `fonts.ready`
  (rad 1262-1264). Ingen `getComputedStyle` per bildruta.
- Liggaren (rad 641-650) och `.kicker-sans` (rad 499) återanvänds för principerna; inga
  nya tokens.
- `?preview=` (rad 1440-1490): `PROCESS_MID` och `forcePs` ersätts av en scroll till li N:s
  mitt.
- Kommentaren i källan: `<!-- PROCESS: sju stycken i flödet med ett ritat ark sticky
  bredvid, INTE sju kort, INTE en tidslinje med punkter, INTE korsfadade rubriker -->`.
- Ledgerrader i `BRIEF.md` § Byggarens rader, R6: (a) formen (prosa i flödet, ankrade
  fönster; källor a11y F-03/F-05, Astra 8, lead F-007 390); (b) copy v1 ur
  PROCESS-UNDERLAG § 3 med § 4-antagandena; (c) "Hur vi tänker" som egen liggare;
  (d) 390-planschen 320x360.

## Steps

1. **Markup.** Byt `#process` (rad 1079-1230) mot: kicker, `<h2 id="process-title">`,
   `<p class="process-lead">`, sedan `<div class="process-grid">` med `<ol class="process-steps"
   data-sc-in data-sc-stagger="70">` (sju `<li data-step="0N">` med `<span class="ledger-num">`,
   `<h3 class="process-step-title">`, `<p class="process-p">` (stycket), `<p class="process-note">`
   (marginalraden)) och `<div class="process-stick">` med `<svg class="process-sheet">`
   (arkets innehåll oförändrat utom plan 020:s rader; varje stegs element grupperas i
   `<g data-step="01">` … `<g data-step="07">`; `.p-live` och `#p-open`-clipPath ligger i
   `<g data-step="05">`). Copy v1 ordagrant, `<!-- copy v1, copy-gate i R7 -->` per steg.
2. **CSS 1440.** Ersätt rad 683-720 med: `.process{background:var(--bg);color:var(--ink);
   padding-block:clamp(48px,8vh,88px) clamp(96px,12vh,140px);}` `.process-title{font-size:
   clamp(2.2rem,3.4vw,3rem)}` (critic 4) `.process-lead{max-width:40ch;font-size:var(--body-r5);
   color:rgba(22,20,15,.78);margin-top:.8rem}` `.process-grid{display:grid;grid-template-columns:
   minmax(300px,384px) minmax(0,880px);column-gap:clamp(48px,4vw,80px);align-items:start;
   padding-inline:var(--rail-x);margin-top:clamp(40px,6vh,64px)}` `.process-steps{list-style:none;
   margin:0;padding:0}` `.process-steps li{padding-block:clamp(40px,6vh,64px);display:flex;
   flex-direction:column;gap:.6rem}` `.process-p{font-family:var(--font);font-weight:300;
   font-size:16px;color:rgba(22,20,15,.78);max-width:34ch}` `.process-note{font-family:var(--font);
   font-weight:600;font-size:13px;color:var(--hair-ink);max-width:34ch;margin-top:.4rem}`
   `.process-stick{position:sticky;top:max(24px,calc((100svh - 495px) / 2));align-self:start}`
   `.process-sheet{display:block;width:100%;max-width:880px;height:auto;aspect-ratio:880/495}`.
   Ta bort rad 712-718 (korsfadningen) och rad 825 (`will-change`).
3. **Fönstren.** På `#process`: `--s1:.09;--e1:.16;--s2:.19;--e2:.26;--s3:.29;--e3:.36;
   --s4:.39;--e4:.46;--s5:.49;--e5:.56;--s6:.59;--e6:.66;--s7:.69;--e7:.76;` och
   `--k1..--k7` enligt device-tabellen. Skriv om rad 788-821 så att varje bana läser sitt
   stegs `--kN` med en andel `[a,b]`; ordningen inom steget som i dag; två banor i samma
   steg får överlappa med högst halva sitt fönster (perf 4: fönster ≥ 0,06 av `--sc-ps`).
   Exempel steg 02 (tre banor + siffror): guides `[0,0.45]`, dim-width `[0.3,0.75]`,
   stationer `[0.6,0.9]`, siffrorna `--p-t` från 0,75. Steg 05: `.p-live` `inset(0 0
   calc((1 - var(--k5)) * 100%) 0)`. Steg 06 (rad 782-783, 753-760): fönster `--k6` i
   stället för `(ps - 0.64)/0.06` och `/0.09`.
4. **Grupperna.** `.process-sheet g[data-step]:not([data-on]){display:none;}` (perf 3, i
   `display`-form eftersom `content-visibility` inte gäller SVG-barn). `<g data-step="05">`
   får inte gömma `#p-open`-clipPath från senare steg: `<defs>` ligger utanför grupperna.
5. **JS, ankarna.** I `measureAct` (rad 1296-1304), efter `processH`:
   ```js
   var lis = process.querySelectorAll('.process-steps li');
   var vh = window.innerHeight, life = processH + vh;
   var top = processTop, stick = document.querySelector('.process-stick');
   var mobile = window.matchMedia('(max-width:1279px)').matches;
   var sheetH = mobile && stick ? stick.getBoundingClientRect().height : 0;
   stepAnchors = [];
   for (var i = 0; i < lis.length; i++){
     var r = lis[i].getBoundingClientRect(), y0 = r.top + window.scrollY - top, yc = y0 + r.height / 2;
     var s = (y0 + vh * (mobile ? 0.05 : 0.15)) / life;
     var e = (yc + (mobile ? 0.5 * (vh + sheetH) : 0.5 * vh)) / life;
     process.style.setProperty('--s' + (i + 1), s.toFixed(4));
     process.style.setProperty('--e' + (i + 1), e.toFixed(4));
     stepAnchors.push({ s: s, yc: yc });
   }
   ```
   (`stepAnchors` deklareras bredvid `processTop`.) Kontroll i konsolen efter load:
   `getComputedStyle(process).getPropertyValue('--e4')` ≈ 0,46 vid 1440x900.
6. **JS, grupperna.** I `readState` (rad 1337-1344), efter `pdrawing`: för varje
   `stepAnchors[i]`, `sheetGroups[i].toggleAttribute('data-on', pps >= stepAnchors[i].s)`
   bara när värdet ändras (cacha senaste). `sheetGroups` =
   `process.querySelectorAll('.process-sheet g[data-step]')`. Sju skrivningar per genomläsning.
7. **JS, preview.** Ersätt rad 1471-1490 (`PROCESS_MID` … `forcePs`) med:
   `var i = parseInt(mode.slice(-2), 10) - 1; measureAct(); window.scrollTo(0, processTop +
   stepAnchors[i].yc - window.innerHeight / 2);` (mobil: `- (window.innerHeight + sheetH) / 2`).
   `__scFreezeMotion` sätts redan (rad 1443-1446).
8. **CSS ≤ 1279.** Ersätt rad 835-855 med `@media (max-width:1279px){ .process-grid{
   grid-template-columns:1fr;row-gap:0} .process-stick{order:-1;position:sticky;top:0;
   z-index:2;background:var(--bg);padding-block:12px;justify-self:center;width:min(100%,480px)}
   .process-sheet{aspect-ratio:320/360} .process-steps li{padding-block:clamp(32px,5vh,48px)}
   … }` plus dagens `display:none`-lista och `d:path()`-overrides omräknade till viewBox
   320x360 (outline `M0.5 0.5 H319.5 V359.5 H0.5 Z`, opening `M24 56 H296 V209 H24 Z`,
   `#p-open-rect,#p-live-img{x:24px;y:56px;width:272px;height:153px}`, dim-width `M0 250
   H320`, lead-169 `M296 56 L306 40 H312`, title `M112 292 H296 V346 H112 Z M112 310 H296
   M112 328 H296`, `#p-rev{x:112px;y:292px;width:184px;height:18px}`, measures 34 px).
   `plansch()` (rad 1503): brytpunkt `(max-width:1279px)`, viewBox `0 0 320 360`,
   `MOBILE_TEXT` y-värden enligt målbilden 390.
9. **Principerna.** Lägg `<section id="principer" …>` efter rad 1230 enligt målbilden;
   CSS: `.principles{background:var(--bg);color:var(--ink);padding:var(--panel-pad-y)
   var(--rail-x);}` `.ledger--plain .ledger-row{grid-template-columns:1fr}`
   `.ledger--plain .ledger-body p{max-width:60ch}` `.ledger--plain h3{font-size:1.15rem}`.
   `.principles .ledger{max-width:64ch}`. Kicker `Hur vi tänker` i `.kicker-sans` ovanför.
10. **Liggarens underrader** (rad 1037-1050): byt till v1-strängarna.
11. **Plan 010:** lägg rättelsen i `plans/010-process.md` (finns redan, skriven av
    arkitekten 2026-09-16; kontrollera att den står överst).
12. **BRIEF.md:** de fyra ledgerraderna.

## Boundaries

- Rör inte `section.hero`, `.stagger`, ramarna (plan 018), `.close` (015, fas C).
- Ingen tredje iframe; `<image>` behålls; ingen `transition` på något som läser `--kN`.
- Låst copy 18/18 ordagrann; noll tankstreck (U+2010 till U+2015) i nya strängar;
  `·` högst en per rad i synlig text (marginalraden i 02 skrivs med kommatecken).
- Motorn och `.sc-*` rörs inte; `data-sc-in` på `<ol>` är motorns egen device.
- Matchar inte raderna 683-720, 712-718, 788-825, 835-855, 1079-1230, 1293-1344 eller
  1440-1503: STOPPA och rapportera.

## Verification

- **Mekaniskt (med 018 gjord först, kontrollen ren):** `motion_probe.py --cpu 4 --wheel
  100:60 --ticks 75 --track "#process:--sc-ps,#p-outline:stroke-dashoffset,#p-opening:
  stroke-dashoffset"` och `--wheel 20:120`: staircase 0 på `--sc-ps`, dashoffset-spårens
  max_step ≤ 12 % (perf 4), rutor > 33 ms ≤ 60 (perf 3:s mål efter 018); `scroll_verify.py`
  1440 och 390: inga `unrevealed`, inga nya `deadScroll`-band utanför sticky-arkets
  hållfönster; `a11y_scan.py` 0; `tab_walk.py` oförändrat; `reflow.py` 320 och 200 %: 0
  overflow, 0 unrevealed (stegen är alltid synliga); PageDown-vandring vid 1440x900: alla sju
  stegtitlar passerar viewporten (a11y fix 3, målet 7 av 7); `elementFromPoint` över ett
  stycke returnerar det stycket (a11y fix 5); `perf_probe.py` CLS ≤ 0,05 vid 390 (arket har
  `aspect-ratio`, sticky-elementet fast höjd); `detect.mjs`; `preflight_taste.py`;
  `contrast_over_media.py --url` på processen: `.process-note` (`--hair-ink`) ≥ 4,5:1 mot
  papperet (mätt 4,89 av Astra).
- **Skärmbilder (F-007):** `?preview=process-01..07` vid 1440 och 390 lästa som bilder mot
  målbildstabellerna: rätt tillstånd på arket, rätt stycke i mitten (1440) eller direkt
  under arket (390), ett displayelement per skärm, inga två stycken i samma box; tolvstegs
  ramsekvens genom aktens liv vid båda bredderna utan hopp; en bild vid 1024 och 1280 som
  visar arket helt (plan 020 klipper inte).
- **Feel check:** läs akten kallt uppifrån: konturen börjar dras när stycke 01 kommer in,
  och varje stegs ritning är färdig när stycket står mitt på skärmen; ingen tom skärm vid
  ankomsten; arket står stilla medan texten passerar; vid 390 sitter arket överst hela
  akten och stycket passerar under. Uppåt suddas i omvänd ordning.
- **Copy:** 18 låsta strängar ordagranna; noll tankstreck; copy v1 ordagrann mot
  underlaget med § 4-antagandena; markörerna `<!-- copy v1, copy-gate i R7 -->` finns.
- **Done when:** F-007 sju av sju vid 1440 och 390 (leadens läsning), H-30/H-31 bockade i
  den uppdaterade lydelsen, probens tal före/efter i NOTES.md, ledgerraderna skrivna.
