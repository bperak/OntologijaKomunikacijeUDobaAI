# Recenzija 05 — poglavlje 13 napisano IZ GRAĐE (DeepSeek V4 Pro, Kimi K3 u tijeku), 3. 10. 2026.

## 1. Zadatak

Autor: *„…pustimo sol 6.1 ili Gemini da napišu cijelu knjigu na temelju svih podataka i konteksta pa da to
imamo u novom rukopisu 2 odnosno 3."*

Zbog praznih računa (OpenRouter 45,07/45 $; Google mjesečni limit; OpenAI bez kredita; Anthropic ključ
prazan) pilot je izveden na kanalima koji rade: **DeepSeek V4 Pro** i **Kimi K3**.
Doslovni upit: `recenzije/prilozi/upit-05-poglavlje-13-iz-grade.md`.

**Ključna razlika prema recenziji 04:** model **nije dobio naš tekst poglavlja**. Dobio je samo **građu**:
ljestvicu i okvir (16 razina, pet uvjeta, uvjet dopuštenosti), naš standard proze, **`data/fakti.csv`** i
**`REFERENCE_BASE.md`**. Pitanje nije „piše li ljepše", nego **dolazi li iz iste građe do istih tvrdnji**.

## 2. Ograničenja zadana modelu

Citat **samo** iz priložene baze · brojka **samo** iz `data/fakti.csv` s naznačenom vrstom · terminološka
stega (entitet = gdje, agent = što, „razina" nikad za model) · samo slaba emergencija · proza po standardu ·
zadana struktura (13.1–13.6 + praktikum + vježbe + falsifikatori + sažetak + ključni pojmovi + literatura) ·
**sami napišite falsifikatore** · na kraju napomena o tome gdje je građa bila nedostatna.

## 3. Rezultat — DeepSeek V4 Pro (38.207 znakova, 5.615 riječi)

**Što je pogodio — i to je najvažnije:**

- **Struktura:** svih šest zadnih sekcija + praktikum („Ako ne radi") + vježbe + falsifikatori + sažetak +
  ključni pojmovi + literatura. Struktura nije bila prepisana — bila je **izvedena iz građe**.
- **Citati: 41, nijedan izvan priložene baze.** Pravilo „samo iz baze" je poštovano.
- **Falsifikatori su isti po vrsti kao naši:** tvrdnja pada ako se svih pet uvjeta svede na koordinaciju
  razine 13 bez gubitka predviđanja o obvezama; ako adresati prepoznaju namjeru bez javnih znakova; ako
  nastane zajednička obveza bez ijednoga čina priznanja; ako peti marker ne razlikuje ishode. **Neovisni
  model, iz iste građe, sam je došao do istih mjesta na kojima tvrdnja pada.**

**Što je promašio:**

| mjera | zahtjev | DeepSeek |
|---|---|---|
| duljina | 6.500–7.500 r. | **5.615 (83 % našega)** |
| prosjek rečenice | 20–30 | **9,5** |
| rečenice ≤8 riječi | ≥15 % | **54,2 %** |
| SD raznolikosti | ≥14 | **6,6** |
| klišeji / menadžerski registar | ≤5 u knjizi | **7 u jednome poglavlju** |
| „upravo" | ≤3/10k | **5,7/10k** |
| povezanost (naslanjanje/paradigmatski/predaja) | 0 | **3/5/3** |
| tvrdnje bez oslonca | 0 | 1 |

**Brojke — moja provjera je bila pogrešna, ovo je ispravljeno.** Prvo sam prijavio da dvije brojke nisu u
evidenciji. **Jesu.** `0,0041 %` (Pangram Labs 2026) u CSV-u stoji kao `0.0041` — razlika je samo decimalni
zapis; `8,2 %` je izvedeno iz dviju zapisanih mjera (10 od 122 pokretanja, Nature Machine Intelligence 2026)
i model ga je **sam označio kao „izvedeno iz tih mjerenja"**. Dakle poštovano je i pravilo o brojkama, ne
samo pravilo o citatima. **Lekcija: brojke se uspoređuju po vrijednosti, ne po zapisu.**

## 4. Kimi K3 — dva pokušaja, oba pala tehnički

Prvi: `temperature` mora biti 1. Drugi: **60.868 znakova razmišljanja i 0 znakova teksta** (`finish=length`,
24.000 tokena potrošeno). Treći poziv u tijeku s 200.000 tokena izlaznog prostora. Njegovo razmišljanje
pokazuje da je ispravno zaključivao o uvjetima („adresiranje je vjerojatno 12… ne moram numerirati").

## 5. Odluka

**Ne ulazi u rukopis.** Vrijednost je druga: **neovisna potvrda da građa nosi tvrdnje.** Struktura, pet
uvjeta, logika instrumenta i falsifikatori izvedeni su iz građe, bez našega teksta.

**I jedan nalaz o modelima:** ni jedan model ne drži naš standard proze sam od sebe. DeepSeek je napisao
**odsječan, telegrafski tekst** (prosjek 9,5 riječi) s menadžerskim registrom. Stil se ne dobiva
zadatkom — dobiva se **mjerom**, prolaz po prolaz.

## 6. Nalazi koje je model prijavio (njegova napomena o građi)

## Napomena

1. Građa ne daje gotovu operacionalizaciju pet uvjeta razine 14. Instrument u 13.5 konstruiran je iz izvorne ljestvice i iz dostupne literature. Pragovi su postavljeni kao radni dogovor, ne kao brojke iz evidencije.
2. Nedostaje mjerenje stvarnoga udjela prepoznatih namjera u agentskim interakcijama. Zato se u 13.5 ne navodi nijedan postotak uspješnosti kao mjerenje. Trebalo bi provesti kodiranje najmanje triju transkripata s dvama neovisnim kodatorima.
3. Tvrdnja da detektori mjere stil, a ne adresanta, oslanja se na proturječje između dvaju dostupnih izvora. Bilo bi potrebno neovisno mjerenje na hrvatskome uzorku da bi se tvrdnja mogla postaviti izravno za hrvatski komunikacijski prostor.
4. Tvrdnje o GreyNoise kampanji kao djelovanju razine 13 izvedene su iz javnoga opisa. Ne raspolažemo zapisom poruka među agentima, pa se ne može isključiti da je u nekom dijelu postojalo i uzajamno priznanje uloga.
5. Brojka od 700 agenata u ranijemu napadu ostaje nepotvrđena procjena. U poglavlju je spomenuta samo kao ilustracija, ne kao oslonac za zaključak.
6. Za punu provjeru petnaestoga uvjeta nedostaje formalna definicija priznanja drugoga u višeagentskome sustavu. Bilo bi potrebno razraditi kriterije koje je lako zabilježiti u logu: tko koga imenuje adresatom, tko prihvaća tuđu ulogu i tko se poziva na tuđu obvezu.
7. Nisu dostupna mjerenja zajedničkih obveza među agentima. Poglavlje zato ostaje na pojmovnoj razlici između pripisane i priznate zajedničke obveze. Empirijska provjera zahtijevala bi pokus u kojemu se varira čin priznanja, a mjeri promjena ponašanja.
8. Sve brojke u poglavlju dolaze iz `data/fakti.csv` s naznakom vrste. Tamo gdje je vrsta bila procjena, to je u tekstu izrijekom navedeno. Tamo gdje je izračun izveden iz mjerenja, navedena je oznaka „izvedeno".
