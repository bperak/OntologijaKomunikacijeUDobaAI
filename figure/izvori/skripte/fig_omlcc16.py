#!/usr/bin/env python3
"""OMLCC 16-level diagram, drawn from the 2018 'Emergence of Social Reality in the OMLCC' deck."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import textwrap

INK='#1C2B4A'; INK2='#334463'; ACC='#C0502E'; ACC2='#0F766E'; SOFT='#EEF2F8'
MUTED='#5A6B80'; LINEC='#D5DDE8'; DEEP='#8E3A20'

# (number, name, schema, band colour)
LEVELS = [
    ('01', 'Existence', 'A (Entity) exists', MUTED),
    ('02', 'Emergence', 'A (Form) becomes B (Transformation)', MUTED),
    ('03', 'MaterialStructure', 'A (Part) isPartOf B (Whole) · {stuff–object, member–collection}', INK2),
    ('04', 'Spatial', 'A (Figure) is_in_spatial_relation_to B (Ground) · {place–area}', INK2),
    ('05', 'Force', 'A (Force structure) influences B (Patient) · {portion–mass}', INK2),
    ('06', 'Motion', 'A (Mover) moves on B (Path) with (Vehicle) · {mover–path}', INK2),
    ('07', 'SequenceActivity', 'A (Activity) has sequence (3–6) · {feature–event}', INK2),
    ('08', 'InformationSystem', 'A (Organism) acts / reacts to B (Environment 1–8)', ACC2),
    ('09', 'Perception', 'A (Perceiver 8–11) perceives 9 B (Object of perception 1–8)', ACC2),
    ('10', 'Affect', 'A (Experiencer 8–14) experiences B (Affect state 10)', ACC2),
    ('11', 'Cognition', 'A (Cogitor 8–14) thinks B (Mental representation 11)', ACC2),
    ('12', 'SocIdentity', 'A (Person 8–14) identifies as B (Social identity 12)', ACC),
    ('13', 'SocBehaviourInteraction', 'A (Person.Agent) performs B (Social interaction 13)', ACC),
    ('14', 'SocCommunication', 'A (Communicator) communicates with B about C on D (code)', ACC),
    ('15', 'SocCulturalInstitution', 'conventionalized norms and institutionalized power, mandated by a cultural model', ACC),
    ('16', 'CulturalModel', 'values, beliefs, institutions shared by a community in locality B and span C', DEEP),
]

fig, ax = plt.subplots(figsize=(12.1, 5.6), dpi=200)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

COLW, GAP = 47.6, 4.8
TOP, ROWH, ROWGAP = 79.0, 7.6, 0.9

for idx, (num, name, schema, col) in enumerate(LEVELS):
    c = 0 if idx < 8 else 1
    r = idx % 8
    x = 0.4 + c * (COLW + GAP)
    y = TOP - r * (ROWH + ROWGAP) - ROWH
    ax.add_patch(FancyBboxPatch((x, y), COLW, ROWH, boxstyle='round,pad=0,rounding_size=1.0',
                                fc='white', ec=LINEC, lw=1.0, zorder=2))
    ax.add_patch(FancyBboxPatch((x, y), 2.6, ROWH, boxstyle='round,pad=0,rounding_size=0.9',
                                fc=col, ec='none', zorder=3))
    ax.text(x + 3.6, y + ROWH * 0.70, f'{num}  {name}', ha='left', va='center',
            fontsize=9.6, color=col, fontweight='bold', zorder=4)
    wrapped = textwrap.fill(schema, 64)
    ax.text(x + 3.6, y + ROWH * 0.24, wrapped, ha='left', va='center',
            fontsize=7.2, color=MUTED, style='italic', zorder=4, linespacing=1.2)

# --- the new entity (not a new level) ---
ax.add_patch(FancyBboxPatch((0.4, 82.5), 95.4, 9.6, boxstyle='round,pad=0,rounding_size=1.1',
                            fc='white', ec=ACC, lw=1.7, ls=(0, (5, 3)), zorder=2))
ax.text(2.6, 89.4, 'A NEW ENTITY IN THE SYSTEM — not a new level', ha='left', va='center',
        fontsize=9.8, color=ACC, fontweight='bold', zorder=4)
ax.text(2.6, 86.2, 'the language model, co-present with humans:', ha='left', va='center',
        fontsize=8.4, color=INK2, zorder=4)
for k, (lab, col) in enumerate((('collaborator — co-communicator, co-worker', ACC2),
                                ('potential competitor for resources — compute, energy, data', ACC))):
    bx, bw = (30.0, 28.5) if k == 0 else (60.5, 35.0)
    ax.add_patch(FancyBboxPatch((bx, 84.1), bw, 4.2, boxstyle='round,pad=0,rounding_size=0.8',
                                fc='white' if k else '#F4FAF8', ec=col, lw=1.1, zorder=3))
    ax.text(bx + bw / 2, 86.2, lab, ha='center', va='center', fontsize=7.0, color=col,
            fontweight='bold', zorder=4)

# band legend + the emergence loop
ax.text(50, 98.4, 'OMLCC — 16 levels of ontological complexity (Perak 2018; 2019)',
        ha='center', va='center', fontsize=11.5, color=ACC, fontweight='bold')
band = [('1–7  material', INK2), ('8  informational / computational', ACC2), ('9–11  psychological', ACC2),
        ('12–15  social', ACC), ('16  cultural', DEEP)]
bx = 3.0
for lab, col in band:
    ax.add_patch(FancyBboxPatch((bx, 2.0), 1.5, 3.2, boxstyle='round,pad=0,rounding_size=0.6',
                                fc=col, ec='none'))
    ax.text(bx + 2.4, 3.6, lab, ha='left', va='center', fontsize=8.0, color=INK2)
    bx += 19.0
ax.text(50, 7.4, 'Each level: network x  →  emergent entity {property}  →  network x+1   (Emmeche, Køppe & Stjernfelt 1997)',
        ha='center', va='center', fontsize=8.6, color=INK2)
fig.tight_layout()
fig.savefig('/home/agent/iuc-dubrovnik-2026/fig_omlcc16.png', facecolor='white',
            bbox_inches='tight', pad_inches=0.06)
print('saved fig_omlcc16.png')
