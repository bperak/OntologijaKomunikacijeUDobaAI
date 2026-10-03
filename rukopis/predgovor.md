# Predgovor

## Zašto još jedna knjiga o jeziku i umjetnoj inteligenciji

Tko radi s jezikom i umjetnom inteligencijom, prije ili poslije nađe se pred istom rečenicom: model „razumije", „komunicira", „stvara značenje". Ta se rečenica izgovara i prima, a uz nju se rijetko pita **gdje** bi to svojstvo uopće stajalo — na kojoj razini stvarnosti. Bez odgovora se o takvim tvrdnjama ne odlučuje, nego pregovara; odluke se, pritom, donose i bez njega — pripisivanje, granica između pomoći i prepisivanja, ono što se traži od studenta.

Zato ova knjiga nije suvišna, i zato je njezino pitanje uže i tvrdoglavije od pitanja dviju srodnih knjiga. *Komunikacija u doba umjetne inteligencije* (Perak 2025) opisuje **što se dogodilo**; *Data Science u kulturi* pokazuje **kako se to mjeri**. Obje ostavljaju netaknutim ono što spor čini nerješivim: **gdje to ontološki stoji?** Ova knjiga ne opisuje iznova ni jedno ni drugo — ona nudi mjerilo: razine s relacijskim shemama, uvjet koji se na konkretnome slučaju može ispuniti ili ne ispuniti, i mjesto na kojem bi odgovor pao.

## Kome je namijenjena

Studentima kulturalnih studija, lingvistike i digitalne humanistike; istraživačima koji se bave emergencijom, kompleksnošću i umjetnom inteligencijom; praktičarima u jezičnim tehnologijama i kulturnoj baštini koji traže pojmovni aparat bez matematike — ali i bez pojednostavljenja koje iskrivljuje. Ona im daje ono što rasprava obično nema: **mjesto** na kojem tvrdnja stoji i **kriterij** po kojem se o njoj odlučuje. Knjiga pretpostavlja znatiželju, ne predznanje programiranja; kod koji se pojavljuje uvijek je objašnjen i uvijek se može preskočiti bez gubitka tvrdnje. Tvrdnja ne ovisi o kodu.

## Kako je organizirana

Četiri dijela, šesnaest poglavlja. **I.** postavlja okvir (sustavi, razine, OMLCC, tri koraka emergencije, metodologija). **II.** dokazuje da je komunikacija *razina*, a ne alat. **III.** ulazi u modele: od vektorskog prostora do mišljenja kao procesiranja i do novog entiteta u sustavu. **IV.** pita što se time mijenja — u komunikaciji, u kulturi i u samoj lingvistici.

Svako poglavlje ima isti oblik:

**teza** (jedan odlomak) → **teorijski okvir** → **metode i podaci** → **praktikum** (kod korak po korak, uz odjeljak „Ako ne radi") → **vježbe** (🟢 provjeri, 🟡 primijeni, 🏆 istraži) → **sažetak i ključni pojmovi** → **„Kako bismo znali da griješimo"**.

Taj posljednji odjeljak nije ukras: on je mjesto na kojem svako poglavlje kaže koji bi ga rezultat oborio. Otud falsifikacijski odjeljak u svakom poglavlju. Knjiga koja to ne može reći nije teorija, nego pripovijest.

## Kako je čitati uz druge dvije knjige

Tri knjige tvore mrežu s podjelom posla:

| knjiga | pitanje |
|---|---|
| *Komunikacija u doba umjetne inteligencije* (2025) | **što se dogodilo** (povijest, arhitektura, praksa) |
| *Data Science u kulturi* | **kako se mjeri** (podaci, statistika, ugrađivanja) |
| **ova knjiga** | **gdje to ontološki stoji** |

U tekstu se upute označavaju: **↗** upućuje na drugu knjigu, **→** na drugo poglavlje ove. Pravilo je, naime, da tema ima jednog vlasnika: ova knjiga ne objašnjava iznova kako se izračunava ugrađivanje ili kako se priprema korpus — to čini *Data Science u kulturi* — nego pita što ti postupci znače za tvrdnju o razinama. Popis svih uputa je u `docs/UPUTE-PO-POGLAVLJIMA.md`, a zajednički rječnik pojmova u `pojmovnik/RJECNIK.md`.

## Četiri pravila čitanja

1. **Ova knjiga radi isključivo sa slabom emergencijom** (Bedau 1997): ono što nastaje izvedivo je iz nižega, ali samo simulacijom. Jakom se emergencijom (Chalmers 2006) pak ne služimo nigdje — ni za jezik, ni za komunikaciju, ni za modele.
2. **Entitet imenuje *gdje*, agent imenuje *što*.** Model je novi *entitet* u sustavu (pozicija), a *agent* je njegova sistemska uloga (djeluje, pamti, dohvaća, orkestrira). Riječ „razina" u ovoj knjizi nikad ne označava model.
3. **Mjera je dio tvrdnje.** Ako se pojava ne može razlučiti od artefakta mjere, prijavljuje se kao nerazlučiva (pouka Schaeffer et al. 2023). Usto, nalaz bez mjere nije nalaz.
4. **Svaka brojka ima izvor, datum i vrstu** (*mjereno* ili *procjena*). Procjena se nikad ne prikazuje kao mjerenje; evidencija je u `data/fakti.csv`.

## Što ova knjiga ne tvrdi

- da su razine „u prirodi" kao takve; tvrdi da su **operativan okvir** koji se može mjeriti (→ pogl. 4);
- da model ima svijest, iskustvo ili namjeru; tvrdi da je **kandidat** za novi entitet u sustavu (→ pogl. 12);
- da slabu emergenciju treba zamijeniti jakom; ostaje na prvoj (→ pogl. 1.3);
- da je ontološki okvir dokazan time što je koristan; korisnost nije dokaz (→ pogl. 16);
- da je mreža triju knjiga dokaz njezine teorije — to je organizacijska odluka, ne argument (`docs/MREZA-KNJIGA.md`).

## Kako je knjiga napravljena

Rukopis se razvija iz izlaganja *Elements of Cognition in Complex Language* (Inter-University Centre Dubrovnik, 11. rujna 2026.). Sve reference prolaze kroz zajedničku **bazu referenci** (`referencije/REFERENCE_BASE.md`): nijedan citat ne ulazi u tekst ako nije u toj bazi, a svaka tvrdnja nosi izvor u istoj rečenici. Provjere se pokreću automatski:

```bash
python kod/pojmovnik_build.py        # registar pojmova → rječnik
python kod/check_links.py --http     # upute, sidra, mrežne provjere
python kod/check_fakti.py            # brojke u tekstu ↔ evidencija
```

## Zahvale

Zahvaljujem Inter-University Centru u Dubrovniku na stipendiji koja mi je omogućila izlaganje iz kojeg je knjiga nastala, te projektima **STUDIA**, **DEMOKRACIJA** i **FORMALS** i projektu **Erasmus+ AI4LANG (AI Language Tutor)** uz koje se razvijao istraživački i metodološki aparat knjige. Zahvaljujem Laboratoriju za istraživanje kulturne složenosti (Odsjek za kulturalne studije, Filozofski fakultet u Rijeci) na prostoru za spore provjere i brze pogreške.

*Benedikt Perak*
*Rijeka, rujna 2026.*
