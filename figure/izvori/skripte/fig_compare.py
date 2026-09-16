#!/usr/bin/env python3
"""Comparison figure: same Croatian emotion lexicon, fastText vs Qwen3-Embedding.
PCA + convex hulls per group; controls/neighbours grey."""
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import Polygon

d = np.load('/tmp/pool_cache.npz', allow_pickle=True)
pool = [str(w) for w in d['pool_words']]
ft = d['ft'].astype(np.float32)
qwen = d['qwen'].astype(np.float32)
meta = json.load(open('/tmp/pool_meta.json', encoding='utf-8'))
GROUPS = meta['groups']
TARGETS = meta['targets']           # [[w, g], ...]
CONTROLS = set(meta['controls'])

COLORS = {'fear': '#C0502E', 'anger': '#5B3A8E', 'sadness': '#2F6DB5', 'joy': '#3F9142'}
PROTO = {'fear': 'strah', 'anger': 'ljutnja', 'sadness': 'tuga', 'joy': 'sreća'}

def convex_hull(points):
    pts = sorted(points)
    if len(pts) <= 2:
        return pts
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def pca2d(W):
    from sklearn.manifold import TSNE
    tsne = TSNE(n_components=2, perplexity=8, metric='cosine', init='pca',
                random_state=5, max_iter=1200)
    return tsne.fit_transform(W)

def draw_panel(ax, W, title):
    proj = pca2d(W)
    members = {g: [] for g in COLORS}
    grey = []
    targ_idx = {w for w, _ in TARGETS}
    for w, (x, y) in zip(pool, proj):
        if w in targ_idx:
            g = next(gg for ww, gg in TARGETS if ww == w)
            members.setdefault(g, []).append((w, float(x), float(y)))
        else:
            grey.append((float(x), float(y)))
    for g, items in members.items():
        col = COLORS[g]
        if len(items) >= 3:
            hull = convex_hull([(x, y) for _, x, y in items])
            ax.add_patch(Polygon(hull, closed=True, facecolor=col, alpha=0.10,
                                 edgecolor=col, linewidth=1.4, zorder=1))
        for w, x, y in items:
            if w == PROTO.get(g):
                ax.scatter(x, y, s=150, c=col, edgecolors='white', linewidths=1.4, zorder=5)
            else:
                ax.scatter(x, y, s=38, c=col, edgecolors='white', linewidths=0.5, zorder=4)
    gx = [p[0] for p in grey]; gy = [p[1] for p in grey]
    if grey:
        ax.scatter(gx, gy, s=9, c='#AEB8C6', alpha=0.85, zorder=2)
    # prototype labels: pull each label from its dot towards the group centroid
    allp = [p for it in members.values() for p in it]
    if allp:
        for g, items in members.items():
            w0 = PROTO[g]
            cgx = np.mean([p[1] for p in items]); cgy = np.mean([p[2] for p in items])
            for w, x, y in items:
                if w == w0:
                    dx, dy = cgx - x, cgy - y
                    n = np.hypot(dx, dy) or 1.0
                    ax.annotate(w, (x, y), xytext=(x + dx / n * 0.34, y + dy / n * 0.30),
                                fontsize=9.5, fontweight='bold', color=COLORS[g], zorder=6,
                                path_effects=[pe.withStroke(linewidth=2.4, foreground='white')])
    ax.set_xticks([]); ax.set_yticks([])
    ax.margins(0.28)
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_title(title, fontsize=10.5, color='#1C2B4A', pad=5)

fig, axes = plt.subplots(1, 2, figsize=(8.7, 4.6), dpi=200)
draw_panel(axes[0], ft,
           'Static word vectors\nfastText cc.hr.300 (t-SNE)')
draw_panel(axes[1], qwen,
           'LLM embeddings\nQwen3-Embedding-8B · Syntagent Spark (t-SNE)')
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=c, markersize=10,
                      label=f'{g.capitalize()} ({PROTO[g]})') for g, c in COLORS.items()]
fig.legend(handles=handles, loc='lower center', fontsize=9, frameon=False, ncol=4,
           bbox_to_anchor=(0.5, -0.005), handletextpad=0.35, columnspacing=1.1)
fig.suptitle('Croatian emotion concepts — do the districts survive the embedding technology?',
             fontsize=12, color='#1C2B4A', y=1.0)
fig.tight_layout(rect=[0, 0.03, 1, 0.97])
fig.savefig('/home/agent/iuc-dubrovnik-2026/fig_strah_usporedba.png',
            facecolor='white', bbox_inches='tight', pad_inches=0.1)
print('saved comparison figure')
