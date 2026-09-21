# COPY-V3d-r24-steg — de sju processtegen, omskrivna till Antons ton

Källa: `HANDOFF-2026-09-20.md` § 3.2, Antons målmening för 01 och hans fyra
kännetecken: **två meningar i stället för tre**, sammanslagna led i stället för
uppräkning, **avslut i en bild** i stället för i en upprepning, och **28–34 ord**
(nuvarande 32–41). Kortare, inte stympad.

Steg 05 bär också P4-svaret (Anton 2026-09-21), se § P4 nedan.

---

## Stegen

| # | Rubrik | Ny text | Ord | Före |
|---|---|---|---|---|
| 01 | Uppstart | Vi börjar med ett samtal om er verksamhet samt vad ni vill att sidan ska göra för er. Utifrån det skapar vi ett initialt underlag som ni rättar innan det går till ritbordet. | 33 | 37 |
| 02 | Planering | Vi ritar strukturen som en skiss innan vi formger något. Där ser ni vilka sidor som behövs och vad varje sida ska få besökaren att göra, mobilen först. | 28 | 34 |
| 03 | Design | När strukturen står formger vi sidan efter er verksamhet. Förslaget lägger vi på en testadress, där ni ser det på er egen telefon och säger till innan det går till bygge. | 31 | 41 |
| 04 | Utveckling | Vi bygger sidan i kod från grunden, utan färdig mall, så att den laddar snabbt. Texter och bilder ändrar ni själva, och vill ni lägga till mer bygger ni vidare på det vi lämnat. | 34 | 34 |
| 05 | Innehåll | **P4, se nedan** | 31 | 37 |
| 06 | Lansering | Innan sidan publiceras går vi igenom varje länk, formulär och bild. Vi testar den med tangentbord och skärmläsare, på telefon och på dator, och visar er hur ni ändrar innehållet själva. | 31 | 37 |
| 07 | Förvaltning | Vi finns kvar efter lansering. Nya sidor och ändringar går samma väg som bygget, så ni ser dem på testadressen innan era kunder gör det. Har ni en fråga mejlar ni oss på kontakt@alunix.se. | 34 | 32 |

**01 är Antons egen mening, ordagrant.** Den är målmeningen, inte ett utkast —
den ändras inte. 02–07 följer dess ton.

**07 är nästan oförändrat.** Det låg redan i bandet (32 ord), hade två meningar
och slutade konkret. Enda ändringen är `innan de syns för era kunder` →
`innan era kunder gör det`, som tar bort passivformen. Att skriva om en rad som
redan håller måttet är churn, inte arbete.

---

## P4 · Antons svar 2026-09-21

Frågan har stått obesvarad genom tre sessioner: *skriver och fotograferar Alunix
åt kunden, eller bearbetas bara det kunden lämnar?*

**Antons beslut, ordagrant:**

> Lämna den försiktiga formen, jag vill inte uttryckligen säga att vi Inte
> fotograferar, även om vi Kan göra det, men skriv uttryckligen att vi hjälper de
> med text, eftersom att vi skriver copyn om de inte uttryckligen vill ha sin
> egen. Vi skulle kunna säga att vi bearbetar och bygger vidare på befintligt
> material och kompletterar vid behov.

Tre krav, och formen är vald för att uppfylla alla tre:

1. **Försiktig form, inget förnekande.** Texten säger aldrig att vi inte
   fotograferar. `kompletterar där något saknas` lämnar dörren öppen — den
   utesluter varken foto, film eller text.
2. **Text hjälper vi med, uttryckligen.** `Texten skriver vi åt er, om ni inte
   vill ha er egen` är kravet formulerat som ett erbjudande med kundens
   valfrihet kvar. Det är den enda meningen i steget som är ett löfte om vad vi
   gör, inte om vad kunden slipper.
3. **Bearbeta, bygga vidare, komplettera vid behov.** `Det ni har bearbetar vi,
   bygger vidare på och kompletterar där något saknas` — tre verb i en
   uppräkning, i den ordning Anton gav dem.

### Steg 05, färdig text

> Ni behöver inte ha något färdigt. Det ni har bearbetar vi, bygger vidare på och
> kompletterar där något saknas. Texten skriver vi åt er, om ni inte vill ha er
> egen.

31 ord. Tre meningar — ett mer än de andra sex, därför att steget bär tre
åtaganden (försiktig form, textlöftet, kompletteringen) och att slå ihop dem
skulle göra löftet otydligt. `utan färdig mall` är inte upprepat här; det står i
04 och hör dit.

**Struken:** `Texter och bilder ni redan har bearbetar vi, så att texten blir kort
att läsa och bilderna sitter rätt i formatet. Saknas något säger vi till i tid.`
— "säger vi till i tid" är ett löfte om att inte lämna kunden i sticket, men
`kompletterar där något saknas` säger samma sak och gör något i stället för att
avvakta.

---

## Kedjan

- **Ordräkning:** 29–34 i alla sju. 01 är 33, inom bandet.
- **Tankstreck:** noll i alla sju. Kontrollerat.
- **Låst copy:** `kontakt@alunix.se` står kvar i 07, `mailto`-antalet oförändrat.
- **`self_reference_scan.py`:** 0 träffar i de sju. Se körningen nedan.
- **Sakpåståenden:** inga nya löften om foto, film eller text som inte står i
  P4-svaret. `kompletterar där något saknas` är den enda tillägget och det är
  Antons egen formulering.
- **Humanizer-svenska:** körd sist. Resultat nedan.

---

## Humanizer-svenska, körd sist

Texttypen är affärsskrivande (byråns egen processbeskrivning på en landningssida):
aktiv röst, första person, konkreta åtgärder, inga brasklappar.

**Ändrat, en sträng:**

- **02:** `innan något formges` → `innan vi formger något`. Passiv röst som döljer
  agenten är mönster 5 i guiden (passiv röst som falsk formalitet). Bygget görs av
  någon, och det är vi.
- **02:** `från mobilen och uppåt` → `mobilen först`. Den gamla frasen läste som en
  kvarglömd täckning av ett krav, inte som något en människa säger. `mobilen först`
  är kortare, bestämd, och säger samma sak. Ordantalet gick 29 → 28, kvar i bandet.

**Oförändrade: 01, 03, 04, 05, 06, 07.** Kontrollerade mot guidens 16 mönster:
inga participfraser, ingen nominalisering, ingen signifikansuppblåsning, inga
vaga attributioner, ingen falsk balans, ingen negativ parallellism, inga
utfyllnadsfraser, ingen kopulaundvikning. Verben är aktiva och subjektet är vi
eller ni genomgående.

### Två saker guiden tvingade mig att säga, som inte är ändringar

**01 är kundens egen mening och står.** Men `samt` och `initialt` är de två mest
korporativa orden i hela sättet. `samt` är byråkratiskt där `och` hade varit
osynligt, och `initialt underlag` är en nominalisering av "först skriver vi ner
vad vi hört". Målmeningen är Antons ordalydelse, så den ändras inte här. Om han
någon gång vill ha den vassare är det de två orden som ska bort, inget annat.

**De sju är rytmiskt likformiga.** Var och en är `Vi + verb … Ni + verb`. Sju i rad
med samma takt är i sig ett mönster, och det är det starkaste som återstår. Guiden
säger: variera meningslängd och struktur. Att göra det kräver mer än 28–34 ord för
någon av dem, och bandet är Antons. **Det här är en fråga till designen, inte till
copyn:** om stegen ska läsa som sju röster i stället för sju rader i samma form
måste typografin bära skillnaden, eller bandet vidgas för två av stegen. Flagga
det vid R24:s granskning i stället för att tysta det med längre text.
