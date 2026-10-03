#!/usr/bin/env python3
"""vrati_natuknice.py — vraća masno na UVODNE NATUKNICE (run-in) koje su radnici skinuli.

Uvodna natuknica je masni ulomak na početku retka iza kojega slijedi tekst („**Najčešća pogreška:**
mjera se čita kao uzrok…"). Ona je APARAT, a ne tvrdnja, pa masno na njoj ostaje.

NE vraća masno na podebljane TVRDNJE koje su opravdano odboldane. Isključuje:
  - nabrojane tvrdnje („Prvo, …", „Druga je da …", „Treći: …"),
  - citate autora na početku retka („Edward Sapir (1921: 7)"),
  - ulomke dulje od 12 riječi.

    python3 kod/vrati_natuknice.py --dry-run   # popis kandidata
    python3 kod/vrati_natuknice.py             # primijeni
"""
import importlib.util
import os
import re
import sys

B = "/home/agent/knjiga-emergencija/"
STARO = "/tmp/stil-staro"
spec = importlib.util.spec_from_file_location("cs", B + "kod/check_stil.py")
cs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cs)

NABROJANO = re.compile(r"^(?:Prvo|Drugo|Treće|Četvrto|Peto|Prvi|Drugi|Treći|Četvrti|Peti|Prva|Druga|Treća|Četvrta|Peta|Treći korak|Peti korak)\b", re.I)
NAJAVNO = re.compile(r"^(?:Što|Zašto|Kako|Gdje|Koje|Koji|Koja|Kad|Ako|Je li|Dva|Tri|Četiri|Pet|Slučaj [A-F])\b", re.I)
AUTOR_CITAT = re.compile(r"^[A-ZČĆĐŠŽ][\w.\-]+(?: [\w.\-]+){0,3} \(?\d{4}")


def kandidati():
    for put in cs.datoteke():
        rel = os.path.relpath(put, B)
        stari = os.path.join(STARO, rel[len("rukopis/"):])
        if not os.path.exists(stari):
            continue
        a = open(stari, encoding="utf-8").read().splitlines()
        b = open(put, encoding="utf-8").read()
        for linija in a:
            m = re.match(r"^\*\*([^*]{2,80})\*\*([:.]?)\s+(\S.*)$", linija.strip())
            if not m:
                continue
            nat, ost = m.group(1).strip(), m.group(3)
            if len(nat.split()) > 12 or len(ost.split()) < 8:
                continue
            if NABROJANO.match(nat) or AUTOR_CITAT.match(nat):
                continue
            # Vraćamo SAMO nedvojbene natuknice: one koje završavaju dvotočkom ili upitnikom.
            # Ostalo su često podebljane TVRDNJE, a njih standard zabranjuje (ZAPIS-007/009).
            # Nedvojbene natuknice: završavaju dvotočkom/upitnikom ILI najavljuju (Što…, Zašto…,
            # Kako…, Gdje…, Dva…, Slučaj A…). Deklarativne tvrdnje („Kompetitor je ista tablica…")
            # ostaju bez masnoga — njih standard zabranjuje.
            if not (re.search(r"[:?]$", nat) or NAJAVNO.match(nat)):
                continue
            # je li natuknica u novoj verziji ostala bez masnoga?
            if ("**" + nat) in b:
                continue
            if nat not in b:
                continue
            yield rel, nat, ost


def main():
    suho = "--dry-run" in sys.argv
    po_datoteci = {}
    for rel, nat, ost in kandidati():
        po_datoteci.setdefault(rel, []).append(nat)
    for rel, natuknice in sorted(po_datoteci.items()):
        print(f"{rel}: {len(natuknice)} natuknica")
        for n in natuknice:
            print(f"    **{n}**")
        if not suho:
            put = B + rel
            t = open(put, encoding="utf-8").read()
            for n in natuknice:
                t = t.replace(n, "**" + n + "**", 1)
            open(put, "w", encoding="utf-8").write(t)
    uk = sum(len(v) for v in po_datoteci.values())
    print(f"\n{'kandidata' if suho else 'vraćeno'}: {uk} u {len(po_datoteci)} datoteka")
    return 0


if __name__ == "__main__":
    sys.exit(main())
