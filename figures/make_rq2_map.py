#!/usr/bin/env python3
"""Generate RQ2 MAP results and semantic-vs-raw paired intervals."""

import matplotlib.pyplot as plt
import numpy as np

# Data
workloads = ['AgentProcessBench', 'HINTBench', 'TraceElephant']
methods = ['Direct+AgentProf', 'Direct+AgentProf-Raw', 'Direct only', 'AgentProf only']

data = {
    'Direct+AgentProf': [0.894, 0.517, 0.326],
    'Direct+AgentProf-Raw': [0.893, 0.518, 0.324],
    'Direct only': [0.863, 0.411, 0.209],
    'AgentProf only': [0.791, 0.432, 0.259],
}

raw_deltas = np.array([0.001, -0.001, 0.002])
raw_ci_low = np.array([-0.0003, -0.0116, -0.0247])
raw_ci_high = np.array([0.0029, 0.0103, 0.0280])
raw_ci_labels = ['[-.0003,.0029]', '[-.0116,.0103]', '[-.0247,.0280]']

# Setup
x = np.arange(len(workloads))
width = 0.18
plt.rcParams.update({
    'font.size': 8,
    'axes.labelsize': 8,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 7,
    'font.family': 'serif',
    'pdf.fonttype': 42,
})
fig, (ax, ax_ci) = plt.subplots(
    2, 1, figsize=(3.35, 2.55), sharex=True,
    gridspec_kw={'height_ratios': [1.55, 1], 'hspace': 0.18},
)

# Colors
colors = ['#2563eb', '#60a5fa', '#6b7280', '#d1d5db']

# Bars
for i, (method, values) in enumerate(data.items()):
    offset = (i - 1.5) * width
    ax.bar(x + offset, values, width, label=method, color=colors[i], edgecolor='white', linewidth=0.5)

# Labels and formatting
ax.set_ylabel('MAP', fontsize=9)
ax.set_xticks(x)
ax.set_ylim(0, 1.0)
ax.set_yticks([0, 0.5, 1.0])
ax.tick_params(axis='x', labelbottom=False)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.52), ncol=2, frameon=False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', linestyle='--', alpha=0.3)

# Candidate-minus-raw paired intervals
raw_yerr = np.vstack((raw_deltas - raw_ci_low, raw_ci_high - raw_deltas))
ax_ci.axhline(0, color='#6b7280', linewidth=0.8, linestyle='--')
ax_ci.errorbar(
    x, raw_deltas, yerr=raw_yerr, fmt='o', color='#2563eb',
    ecolor='#2563eb', elinewidth=1.2, capsize=3, markersize=3.5,
)
for i, label in enumerate(raw_ci_labels):
    y = raw_ci_high[i] + 0.004 if i < 2 else raw_ci_low[i] - 0.004
    va = 'bottom' if i < 2 else 'top'
    ax_ci.text(i, y, label, ha='center', va=va, fontsize=7)

ax_ci.set_ylabel(r'$\Delta$ MAP')
ax_ci.set_xticks(x)
ax_ci.set_xticklabels(['AgentProcess\nBench', 'HINTBench', 'TraceElephant'])
ax_ci.set_ylim(-0.04, 0.04)
ax_ci.set_yticks([-0.03, 0, 0.03])
ax_ci.spines['top'].set_visible(False)
ax_ci.spines['right'].set_visible(False)
ax_ci.grid(axis='y', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig('fig-rq2-map.pdf', bbox_inches='tight', dpi=300)
plt.savefig('fig-rq2-map.png', bbox_inches='tight', dpi=300)
print('Saved fig-rq2-map.pdf and fig-rq2-map.png')
