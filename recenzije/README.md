# Vanjske recenzije — zapisi

Ovdje se, **svaka u svojoj datoteci**, čuvaju vanjske recenzije knjige: što je zatraženo, kako, što je
vraćeno i **što je od toga ušlo u rukopis**. Datoteke se **ne brišu** — i odbijena preporuka je nalaz.

## Pravilo zapisa

Svaki zapis ima šest dijelova, istim redom:

1. **Zadatak** — što je modelu zadano (doslovno) i koji je model odgovorio (`vratio=`).
2. **Kontekst** — što je model dobio kao gradivo (cijela knjiga? sekcija? koje mjerilo registra?).
3. **Način provjere** — koje su mjere pokrenute na vraćenome tekstu
   (`check_stil`, `check_sekcije`, `check_leprsavost`, `check_lit`, `check_fakti --strict`, `check_refs`),
   uz usporedbu citata, brojki i uputa **prije i poslije**.
4. **Rezultat** — vraćeni tekst (ili njegov sažetak, uz putanju do pune verzije).
5. **Odluka** — je li primljeno, djelomično primljeno ili odbijeno, i **zašto**.
6. **Nalazi koje je model prijavio** — i što je od toga provjereno.

## Tvrdi prag provjere (autor, 3. 10. 2026.: „Nemoj uzimati neprovjereno")

- Nalaz vanjskoga modela dobiva oznaku **provjereno** samo uz **navod iz samoga teksta** (rečenica i
  poglavlje) ili zapis iz `data/fakti.csv`. **Bez navoda nema oznake.**
- Nalaz se provjerava **u cijelome rukopisu**, ne samo u poglavlju na koje model upućuje — model poglavlja
  pripisuje pogrešno (dva puta u jednome zapisu).
- Vlastito izvješće modela **nije dokaz**; ni tvrdnja „preneseno doslovno", ni „aparatura netaknuta".
- Prijedlog („ovo bi trebalo razlučiti") nije nalaz. Prijedlozi se vode odvojeno i traže autorovu odluku.

## Zašto tako

Model može napisati bolju rečenicu, ali ne smije nositi nijednu neprovjerenu tvrdnju. Zato se **nijedan
citat, brojka ni uputa ne primaju** bez prolaza kroz mjere; a preporuka koja je odbijena zapisuje se s
razlogom, da se ne vrti u krug.
