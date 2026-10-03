#!/usr/bin/env python3
"""Povezanost na razini SEKCIJA (spoj sekcija): naslanjanje, paradigmatski okvir, predaja dalje."""
import glob
import os
import re
import sys

KOR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = os.path.join(KOR, "rukopis") + os.sep
KONEKTOR = re.compile(
    r"^(Ta|Taj|To|Ono|Ova|Ovaj|Ovo|Tim|Time|Toga|Odatle|Iz toga|Zato|Zbog toga|No|Ako|Sada|Pritom|Ovdje|"
    r"Tu|Uz to|Drugo|Prvo|Treće|Naposljetku|Posljedica|Otud|Stoga|Dakle|Ipak|Ali|Osim toga|Sljedeće|"
    r"Za razliku|Nasuprot|Umjesto|Naprotiv|Kad|Kada|Gdje|Što|Kako|Zašto|Pitanje|Odgovor|Problem|Teza|Prvi|"
    r"Drugi|Treći|Najprije|Zatim|Na kraju|Nakon|Prije|Vrijedi|Njegov|Njezin|Njihov|Isti|Ista|Isto|Ponovno|"
    r"Opet|Svaki|Nijedan|Nema|Postoji|Takav|Takva|Takve|Takvi|U tome|U tom|S tim|Od toga|Po tome|Iz svega|"
    r"Sve|Svako|Svi|Nikad|Uvijek|Ova knjiga|Ovaj okvir|Ukratko|Jednom riječju)", re.UNICODE)
PARADIGM = re.compile(
    r"\b(nasuprot|naprotiv|umjesto|suprotno|za razliku|razlika je|razlika prema|a ne\b|nije isto|ne znači|"
    r"tek\b|ipak\b|dok\b|s jedne strane|ni jedno ni drugo)", re.I)
NAPRIJED = re.compile(
    r"\b(zato|otud|stoga|dakle|slijedi|posljedic|iz toga|time se|time je|time postaje|ostaje pitanje|"
    r"otvara se|vodi k|prelazi u|pokazuje se|sljedeće poglavlje|sljedeća sekcija|sljedeći odjeljak|"
    r"na kraju ovoga|vraćamo se|time je otvoreno)", re.I)
STOP = set("koji koja koje kojim kojima nego tako tada sada ovdje ondje zato jer dakle stoga biti jesu jest nije "
           "nisu bio bila bilo može mogu treba valja vrlo više manje samo između prema protiv kroz nakon prije "
           "tijekom pomoću sve svi svaka svaki svako njegov njezin njihov time".split())


def sadrz(t):
    return {w.lower().strip(".,;:()»«„\"'") for w in re.findall(r"\b[\wčćšđžČĆŠĐŽ-]{5,}\b", t)
            if w.lower() not in STOP}


def sekcije(t):
    t = re.sub(r"^!\[.*$", "", t, flags=re.M)
    t = re.sub(r"^\|.*$", "", t, flags=re.M)
    t = re.sub(r"^```.*?^```", "", t, flags=re.M | re.S)
    t = re.sub(r"^\s*[-*]\s.*$", "", t, flags=re.M)
    t = re.sub(r"^\s*\d+\.\s.*$", "", t, flags=re.M)
    dijelovi = re.split(r"^(#{2,4}\s+[^\n]+)$", t, flags=re.M)
    out = []
    for k in range(1, len(dijelovi), 2):
        nas = dijelovi[k].strip("# ").strip()
        pas = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", dijelovi[k + 1])
               if len(p.split()) >= 25]
        if nas.split()[0] in ("Ključni", "Literatura", "Sadržaj", "Vježbe"):
            continue
        if pas:
            out.append((nas, pas))
    return out


def main():
    if "--dir" in sys.argv:
        B2 = sys.argv[sys.argv.index("--dir") + 1]
        datoteke = sorted(glob.glob(B2 + "/poglavlje-*.md")) + [B2 + "/uvod.md", B2 + "/zakljucak.md"]
    elif "--datoteka" in sys.argv:
        datoteke = [sys.argv[sys.argv.index("--datoteka") + 1]]
    else:
        datoteke = (sorted(glob.glob(B + "poglavlje-*.md")) + [B + "uvod.md", B + "zakljucak.md"]
                    + [f for f in sorted(glob.glob(B + "dodaci/dodatak-*.md"))
                       if os.path.basename(f)[8] not in ("B", "E", "G")])
    ispis = "--isoli" in sys.argv
    ukupno = 0
    izvještaj = []
    for f in datoteke:
        S = sekcije(open(f, encoding="utf-8").read())
        man = [0, 0, 0]
        propusti = []
        for i, (nas, pas) in enumerate(S):
            ukupno += 1
            preth = " ".join(S[i - 1][1][-1:]) if i > 0 else " ".join(pas)
            back = bool(KONEKTOR.match(pas[0])) or bool(sadrz(pas[0]) & sadrz(preth))
            par = any(PARADIGM.search(p) for p in pas[:3])
            slj = " ".join(S[i + 1][1][:1]) if i + 1 < len(S) else None   # zadnja sekcija nema kamo predati
            fwd = (slj is None) or bool(NAPRIJED.search(pas[-1])) or bool(sadrz(pas[-1]) & sadrz(slj))
            man[0] += not back
            man[1] += not par
            man[2] += not fwd
            if not back:
                propusti.append(nas)
        u = len(S)
        izvještaj.append((os.path.basename(f), u, man, propusti))
        print(f"{os.path.basename(f):<20} sekcija {u:>3} | bez naslanjanja {man[0]:>2} ({100*man[0]//max(u,1):>3}%)"
              f" | bez paradigmatskog okvira {man[1]:>2} ({100*man[1]//max(u,1):>3}%)"
              f" | bez predaje dalje {man[2]:>2} ({100*man[2]//max(u,1):>3}%)")
    print(f"\nukupno sekcija: {ukupno}")
    z = sum(r[2][0] for r in izvještaj), sum(r[2][1] for r in izvještaj), sum(r[2][2] for r in izvještaj)
    print(f"UKUPNO: bez naslanjanja {z[0]} | bez paradigmatskog okvira {z[1]} | bez predaje dalje {z[2]}")
    if ispis:
        for ime, u, man, propusti in izvještaj:
            if propusti:
                print(f"\n--- {ime}: sekcije koje ne naslanjaju na prethodnu ({len(propusti)}) ---")
                for p in propusti:
                    print("   •", p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
