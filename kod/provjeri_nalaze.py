#!/usr/bin/env python3
"""provjeri_nalaze.py — provjerava na izvoru nalaze čitatelja (prije nego uđu u preporuke)."""
import glob
import os
import re

B = "/home/agent/knjiga-emergencija/"
R = B + "rukopis/"


def prikaz(oznaka, tocno, detalj=""):
    print(f"{'✔' if tocno else '✗'} {oznaka}{(' — ' + detalj) if detalj else ''}")


print("1) MRTVA UPUTA: razine 4-6 u karti 2.3 → 5.2 obrađuje li prostor/silu/gibanje?")
t2 = open(R + "poglavlje-02.md", encoding="utf-8").read()
t5 = open(R + "poglavlje-05.md", encoding="utf-8").read()
for razina, pojam in [("4", "Spatial"), ("5", "Force"), ("6", "Motion")]:
    m = re.search(r"\|[^|]*\|\s*" + razina + r"\s*[^|]*\|([^|]*)\|([^|]*)\|", t2)
    print("   karta 2.3:", (m.group(0).strip()[:120] if m else "nije nađen redak"))
    break
i = t5.find("## 5.2")
print("   5.2 naslov:", t5[i:i + 90].split("\n")[0], "| spominje prostor/silu/gibanje:",
      bool(re.search(r"\b(prostor|sila|gibanje|Spatial|Force|Motion)\b", t5[i:i + 2000])))

print("\n2) MAPE I PUTANJE u pogl. 4 (slike/ vs figure/, kod/negativni/, data/negativni*)")
t4 = open(R + "poglavlje-04.md", encoding="utf-8").read()
for putanja in ["slike/README.md", "figure/", "kod/negativni/", "data/negativni"]:
    print(f"   tekst spominje {putanja}: {putanja in t4} | postoji na disku: {os.path.exists(B + putanja.rstrip('/'))}")
print("   PNG u figure/:", len(glob.glob(B + "figure/*.png")), "| mapa slike/ postoji:", os.path.isdir(B + "slike"))

print("\n3) UVOD: uputa na 4.3 (pet stupnjeva) — postoji li tablica 4.3 i gdje?")
tu = open(R + "uvod.md", encoding="utf-8").read()
print("   u uvod.md spominje '4.3':", "4.3" in tu, "| u pogl. 4 postoji naslov '4.3':", bool(re.search(r"^#+ *4\.3", t4, re.M)),
      "| '4.4':", bool(re.search(r"^#+ *4\.4", t4, re.M)))

print("\n4) POGL. 6: koliko puta 'primjer'?")
t6 = open(R + "poglavlje-06.md", encoding="utf-8").read()
print("   'primjer*':", len(re.findall(r"\bprimjer\w*", t6, re.I)), "| 'npr.':", len(re.findall(r"\bnpr\.", t6)))

print("\n5) POGL. 9: 'Napomena o izvorima' — upućuje li se i postoji li?")
t9 = open(R + "poglavlje-09.md", encoding="utf-8").read()
print("   spominje 'Napomenu o izvorima':", t9.count("Napomen"), "| postoji naslov:", bool(re.search(r"^#+.*Napomen", t9, re.M)))

print("\n6) RAZINA 14: četiri ili pet uvjeta? (karta 2.3 vs 7.5 vs 13)")
t7 = open(R + "poglavlje-07.md", encoding="utf-8").read()
t13 = open(R + "poglavlje-13.md", encoding="utf-8").read()
for ime, t in [("2", t2), ("7", t7), ("13", t13)]:
    cetiri = len(re.findall(r"četiri uvjeta", t))
    pet = len(re.findall(r"pet uvjeta|petog uvjeta|peti uvjet", t))
    print(f"   pogl. {ime}: 'četiri uvjeta' {cetiri} | 'pet uvjeta/peti' {pet}")

print("\n7) KLJUČNI POJMOVI bez pojave u tekstu (deontologija, performativ, prokletstvo dimenzionalnosti)")
for pojam in ["deontologija", "deontološ", "performativ", "prokletstvo dimenzionalnosti"]:
    gdje = []
    for p in sorted(glob.glob(R + "**/*.md", recursive=True)):
        t = open(p, encoding="utf-8").read()
        # pojavljuje li se IZVAN popisa ključnih pojmova
        bez = re.sub(r"^### Ključni pojmovi[\s\S]*?(?=^#{2,3} |\Z)", "", t, flags=re.M)
        if pojam.lower() in bez.lower():
            gdje.append(os.path.basename(p))
    print(f"   '{pojam}' u tijelu teksta: {len(gdje)} puta → {gdje[:6]}")

print("\n8) SADRŽAJ: 'fantomski' naslovi — postoje li svi navedeni u datotekama?")
sad = open(R + "sadrzaj.md", encoding="utf-8").read()
naslovi = re.findall(r"^\s*[-*]\s*(?:\*\*)?([0-9]+\.[0-9]+[^\n*]*)", sad, re.M)[:40]
sve = "\n".join(open(p, encoding="utf-8").read() for p in glob.glob(R + "**/*.md", recursive=True))
fal = [n.strip() for n in naslovi if not re.search(r"^#+ *" + re.escape(n.strip()[:18]), sve, re.M)]
print(f"   broj provjerenih naslova iz sadržaja: {len(naslovi)} | ne nađeni u tijelu: {len(fal)}")
for n in fal[:8]:
    print("     –", n[:70])
