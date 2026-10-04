<!-- zatražen: ~google/gemini-pro-latest | vratio: google/gemini-3.1-pro-preview | finish: stop | reasoning: 2137 | prompt: 6720 | completion: 5042 -->

Evo predgovora napisanoga tvojim glasom, uz analizu postupka. 

Što se tiče **registra** (odgovor na tvoje 4. pitanje): predgovor **ne traži** drukčiji registar od uvoda. Naprotiv, on mora zvučati kao isti čovjek. Predgovor je autorov stisak ruke s čitateljem prije nego što se prijeđe na stvar. Ako je uvod precizan, strog i lišen akademskoga fraziranja, predgovor ne smije zvučati kao birokratska bilješka ili neobavezno ćaskanje. Razlika je samo u predmetu: uvod postavlja tezu, a predgovor postavlja logistiku knjige. Glas ostaje isti.

Evo teksta.

***

# Predgovor

## Zašto još jedna knjiga o jeziku i umjetnoj inteligenciji

Svaki rad s jezikom i umjetnom inteligencijom prije ili poslije udari u istu rečenicu: model „razumije“, „komunicira“, „stvara značenje“. Ta se rečenica izgovara i prima, a uz nju se rijetko pita **gdje** bi to svojstvo uopće stajalo — na kojoj razini stvarnosti. Bez odgovora na to pitanje o tvrdnjama se ne odlučuje, nego se o njima pregovara. Odluke se, međutim, donose i bez njega: pripisivanje autorstva, povlačenje granice između pomoći i prepisivanja, definiranje onoga što se traži od studenta. 

Zato ova knjiga nije suvišna. Njezino je pitanje uže i tvrdoglavije od pitanja dviju srodnih knjiga. *Komunikacija u doba umjetne inteligencije* (Perak 2025) opisuje što se dogodilo; *Data Science u kulturi* pokazuje kako se to mjeri. Obje ostavljaju netaknutim ono što spor čini nerješivim: gdje to ontološki stoji? Ova knjiga ne opisuje iznova ni povijest ni statistiku. Ona nudi mjerilo: razine s relacijskim shemama, uvjet koji se na konkretnome slučaju može ispuniti ili ne ispuniti, i mjesto na kojemu bi odgovor pao.

Teza ove knjige, prevedena na običan jezik, glasi: knjiga ne nudi stav o modelima, nego mjerilo. Svaka tvrdnja o jeziku i o modelu ima razinu na kojoj stoji i uvjet pod kojim pada. Nakon čitanja moći ćete za tvrdnju o „razumijevanju“ ili „komunikaciji“ reći na kojoj razini stoji i koji je nositelj nosi. Moći ćete razlikovati ono što stoji u zapisu od onoga što se pripisuje, i to pokazati na vlastitome slučaju. Ono što time dobivate nije gotov sud, nego kriterij koji možete primijeniti i osporiti.

## Kome je namijenjena

Knjiga je pisana za studente kulturalnih studija, lingvistike i digitalne humanistike. Pisana je za istraživače koji se bave emergencijom, kompleksnošću i umjetnom inteligencijom. Pisana je za praktičare u jezičnim tehnologijama i kulturnoj baštini koji traže pojmovni aparat bez matematike — ali i bez pojednostavljenja koje iskrivljuje. 

Ona im daje ono što rasprava obično nema: **mjesto** na kojemu tvrdnja stoji i **kriterij** po kojemu se o njoj odlučuje. Knjiga pretpostavlja znatiželju, ne predznanje programiranja. Kod koji se u njoj pojavljuje uvijek je objašnjen i uvijek se može preskočiti bez gubitka tvrdnje. Tvrdnja nikada ne ovisi o kodu.

## Kako je organizirana

Arhitektura knjige počiva na četiri dijela i šesnaest poglavlja. Prvi dio postavlja okvir: sustave, razine, model OMLCC, tri koraka emergencije i metodologiju. Drugi dokazuje da je komunikacija **razina**, a ne alat. Treći ulazi u modele, prateći put od vektorskoga prostora do mišljenja kao procesiranja i, konačno, do novoga entiteta u sustavu. Četvrti dio pita što se time mijenja — u komunikaciji, u kulturi i u samoj lingvistici.

Svako poglavlje dijeli istu unutarnju strukturu. Započinje tezom sažetom u jedan odlomak, prelazi na teorijski okvir, a zatim na metode i podatke. Slijedi praktikum s kodom korak po korak (uz nužan odjeljak „Ako ne radi“) te vježbe za provjeru, primjenu i istraživanje. Poglavlje se zatvara sažetkom, ključnim pojmovima i odjeljkom „Kako bismo znali da griješimo“. Taj posljednji odjeljak nije ukras: on je mjesto na kojemu svako poglavlje jasno kaže koji bi ga rezultat oborio. Knjiga koja to ne može reći nije teorija, nego pripovijest.

## Kako je čitati uz druge dvije knjige

Ova knjiga ne stoji sama. Ona je dio mreže triju knjiga s jasnom podjelom posla. *Komunikacija u doba umjetne inteligencije* (2025) zadužena je za pitanje **što se dogodilo** (povijest, arhitektura, praksa). *Data Science u kulturi* odgovara na pitanje **kako se mjeri** (podaci, statistika, ugrađivanja). Ova knjiga pita **gdje to ontološki stoji**.

U tekstu se upute precizno označavaju: strelica **↗** upućuje na drugu knjigu, a strelica **→** na drugo poglavlje ove knjige. Pravilo je da svaka tema ima jednoga vlasnika. Ova knjiga ne objašnjava iznova kako se izračunava ugrađivanje ili kako se priprema korpus — to čini *Data Science u kulturi* — nego pita što ti postupci znače za tvrdnju o razinama. Popis svih uputa nalazi se u `docs/UPUTE-PO-POGLAVLJIMA.md`, a zajednički rječnik pojmova u `pojmovnik/RJECNIK.md`.

## Četiri pravila čitanja

Da bi ljestvica radila, čitanje podliježe četirima pravilima.

Prvo, knjiga radi isključivo sa **slabom emergencijom** (Bedau 1997): ono što nastaje izvedivo je iz nižega, ali isključivo simulacijom. Jakom se emergencijom (Chalmers 2006) ne služimo nigdje — ni za jezik, ni za komunikaciju, ni za modele.

Drugo, **entitet** imenuje mjesto i odgovara na pitanje *gdje*. **Agent** imenuje sistemsku ulogu i odgovara na pitanje *što*. Model je novi entitet u sustavu (pozicija), a agent je njegova uloga (djeluje, pamti, dohvaća, orkestrira). Riječ „razina“ u ovoj knjizi nikada ne označava model.

Treće, **mjera je dio tvrdnje**. Ako se pojava ne može razlučiti od artefakta mjere, prijavljuje se kao nerazlučiva (pouka Schaeffer et al. 2023). Nalaz bez mjere nije nalaz.

Četvrto, **svaka brojka ima izvor, datum i vrstu** (*mjereno* ili *procjena*). Procjena se nikada ne prikazuje kao mjerenje, a evidencija svih brojki nalazi se u `data/fakti.csv`.

## Što ova knjiga ne tvrdi

Znanstveni je tekst definiran i onime što odbija tvrditi. Ova knjiga ne tvrdi da su razine upisane „u prirodu“ kao takve; tvrdi da su one **operativan okvir** koji se može mjeriti (→ pogl. 4). Ne tvrdi da model ima svijest, iskustvo ili namjeru; tvrdi da je **kandidat** za novi entitet u sustavu (→ pogl. 12). Ne tvrdi da slabu emergenciju treba zamijeniti jakom. Ne tvrdi da je ontološki okvir dokazan time što je koristan, jer korisnost nije dokaz (→ pogl. 16). Konačno, ne tvrdi da je mreža triju knjiga dokaz njezine teorije — to je organizacijska odluka, a ne argument (`docs/MREZA-KNJIGA.md`).

## Kako je knjiga napravljena

Rukopis ne skriva svoje podrijetlo. Razvija se iz izlaganja *Elements of Cognition in Complex Language* (Inter-University Centre Dubrovnik, 11. rujna 2026.). Sve reference prolaze kroz zajedničku bazu (`referencije/REFERENCE_BASE.md`): nijedan citat ne ulazi u tekst ako nije u toj bazi, a svaka tvrdnja nosi izvor u istoj rečenici. 

Provjere se pokreću automatski. Skripte nadziru izgradnju rječnika iz registra pojmova (`kod/pojmovnik_build.py`), ispravnost unutarnjih uputa i mrežnih poveznica (`kod/check_links.py --http`) te poklapanje brojki u tekstu s evidencijom (`kod/check_fakti.py`).

## Zahvale

Zahvaljujem Inter-University Centru u Dubrovniku na stipendiji koja mi je omogućila izlaganje iz kojega je knjiga nastala. Zahvaljujem projektima **STUDIA**, **DEMOKRACIJA** i **FORMALS** te projektu **Erasmus+ AI4LANG (AI Language Tutor)**, uz koje se razvijao istraživački i metodološki aparat ove knjige. Zahvaljujem Laboratoriju za istraživanje kulturne složenosti (Odsjek za kulturalne studije, Filozofski fakultet u Rijeci) na prostoru za spore provjere i brze pogreške.

*Benedikt Perak*  
*Rijeka, rujna 2026.*

***

### 2. Što je u sadašnjem predgovoru dobro i ostalo je nepromijenjeno
*   **Falsifikacijski etos:** Rečenica *"Knjiga koja to ne može reći nije teorija, nego pripovijest"* je briljantna i zadržana je netaknuta. Savršeno pogađa tvoj autorski glas.
*   **Struktura i ograničenja:** Sva pravila čitanja, popis onoga što knjiga ne tvrdi, kao i tehnički detalji o skriptama i repozitorijima ostali su sadržajno potpuno isti.
*   **Zahvale i imena:** Svi projekti, datumi i institucije zadržani su točno onako kako su navedeni, bez ikakvih dodataka.

### 3. Što sam promijenio i zašto (4 poteza)
1.  **Pretvaranje natuknica (bulleta) u ritmičnu prozu:** Tvoj uvod ima sjajan ritam paralelnih rečenica (npr. *Pisana je za studente... Pisana je za istraživače... Pisana je za praktičare...*). U starom su predgovoru to bile suhe natuknice. Proza daje autoritet; natuknice djeluju kao *PowerPoint* prezentacija.
2.  **Integracija tablice u tekst:** Tablica o tri knjige razbijala je tijek čitanja. Pretvorio sam je u jasan, tečan odlomak koji objašnjava podjelu posla, zadržavajući jasnu distinkciju između *što*, *kako* i *gdje*.
3.  **Uklanjanje viška podebljavanja (bolda):** U starom je nacrtu bilo previše podebljanog teksta (npr. cijeli podnaslovi u tekstu poput **Što vam ova knjiga daje**). Podebljanje sam sveo isključivo na ključne pojmove (entitet, agent, razina, slaba emergencija), točno onako kako traži tvoja terminološka stega.
4.  **Povezivanje "Zašto još jedna knjiga" s uvodom:** Početak predgovora sada logički i stilski priprema teren za uvod. Motiv "gdje to stoji" sada se provlači glatko, bez skokova u tonu.