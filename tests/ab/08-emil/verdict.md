# AB08 — emilkowalski-uppdatering (gamla emil-design-eng mot nya emil + animate)

Brief: settings-yta "Tidvatten Konto" (Operate). Två blinda Sonnet-byggen, samma tokens, samma
produktreferenser; enda skillnaden är motion-referensen (A: gamla lokala emil-design-eng;
B: uppströms emil-design-eng + animate/RECIPES.md).

| Mått | A baseline | B med | Not |
|---|---|---|---|
| detect.mjs findings | 1 (layout-transition: `transition: width`) | 0 | A animerar tab-strecket via width (icke-GPU) |
| `@media (hover: hover)`-gating | 0 | 7 | ogatad hover = falsk hover på touch (escalation trigger) |
| `transition: all` / `ease-in` | 0 / 0 | 0 / 0 | båda rena |
| easing-kurvor | de tre emil-kurvorna | de tre emil-kurvorna | lika |
| `@starting-style` | 5 | 0 | A:s toast-enter är mer modern; B använder klass-toggle |
| reduced motion | innehåll kvar, drawer syns | innehåll kvar, drawer syns | båda "gentler, not zero" |
| konsolfel | 0 | 0 | |
| drawer-rader | kort i kort (boxade nyckelrader) | hairline-ledger, maskerade nycklar | B följer house-physics "ledgers over cards" |

Visuellt (compare/*.png, lästa): fold, drawer, hold-to-delete mitt i, toast-stack och mobil är
alla presentabla i båda. B:s drawer är lugnare och mer produktlik (ledger, sekundärtext per rad,
"3 aktiva nycklar"); A:s toastar och håll-fyllning är lika bra som B:s. Ingen av dem har en
visuell defekt vid 1440 eller 390. Skillnaden ligger i det som syns i rörelse och i kod: B
klarar review-animations-baren utan trigger, A faller på två (layout-property, ogatad hover).

**Beslut: IN.** Uppströms emil-design-eng + animate ersätter den gamla kopian; review-animations
blir Step 5-passet för rörelse. Modifiering: RECIPES-vägen ska nämna `@starting-style` för
toast-enter (A gjorde rätt där) — kontrolleras i uppströms RECIPES.md innan SKILL.md-texten skrivs.
