#!/usr/bin/env python3
"""Three nested loops: processing < human reward < recursive self-improvement."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

INK='#1C2B4A'; INK2='#334463'; ACC='#C0502E'; ACC2='#0F766E'; SOFT='#EEF2F8'
MUTED='#5A6B80'; LINEC='#D5DDE8'

fig, ax = plt.subplots(figsize=(12.1, 2.75), dpi=200)
ax.set_xlim(0, 100); ax.set_ylim(0, 25); ax.axis('off')

def ring(x, y, w, h, ec, ls='solid', lw=1.6, fc='none'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0,rounding_size=1.2',
                                fc=fc, ec=ec, lw=lw, ls=ls, zorder=2))

import numpy as _np

def arc(cx, cy, r, col, lw=1.8):
    ax.add_patch(plt.Circle((cx, cy), r, fill=False, ec=col, lw=1.3, zorder=3))
    th0, th1 = _np.deg2rad(155), _np.deg2rad(35)
    p0 = (cx + r * _np.cos(th0), cy + r * _np.sin(th0))
    p1 = (cx + r * _np.cos(th1), cy + r * _np.sin(th1))
    ax.add_patch(FancyArrowPatch(p0, p1, connectionstyle='arc3,rad=-0.42', arrowstyle='-|>',
                                 mutation_scale=13, color=col, lw=lw, zorder=4))

# outer: recursive self-improvement
ring(1.0, 1.0, 98.0, 22.5, ACC, ls=(0, (5, 3)), lw=1.8)
ax.text(3.0, 21.4, 'RECURSIVE SELF-IMPROVEMENT  —  agent-written code, data and experiments feed the next model (months)',
        ha='left', va='center', fontsize=9.6, color=ACC, fontweight='bold')
# middle: human reward
ring(4.0, 4.0, 86.0, 15.4, ACC2, lw=1.6)
ax.text(6.0, 16.2, 'HUMAN REWARD  —  humans compare outputs → reward model → policy update (weeks)',
        ha='left', va='center', fontsize=9.4, color=ACC2, fontweight='bold')
# inner: processing
ring(9.0, 7.2, 66.0, 7.6, INK2, lw=1.6, fc='white')
ax.text(12.5, 12.0, 'PROCESSING  —  predict → append → re-read (milliseconds)',
        ha='left', va='center', fontsize=9.6, color=INK2, fontweight='bold')
ax.text(12.5, 9.4, 'the context is continuously improved', ha='left', va='center',
        fontsize=8.6, color=MUTED, style='italic')

arc(68.5, 10.9, 2.2, INK2)
arc(85.0, 11.7, 2.4, ACC2)
arc(95.0, 12.4, 2.6, ACC)

fig.tight_layout()
fig.savefig('/home/agent/iuc-dubrovnik-2026/fig_loops.png', facecolor='white',
            bbox_inches='tight', pad_inches=0.06)
print('saved fig_loops.png')
