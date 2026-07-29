#!/usr/bin/env python3
"""Generate the RQ2 MAP results."""

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
fig, ax = plt.subplots(figsize=(3.35, 1.85))

# Colors
colors = ['#2563eb', '#60a5fa', '#6b7280', '#d1d5db']

# Bars
for i, (method, values) in enumerate(data.items()):
    offset = (i - 1.5) * width
    ax.bar(x + offset, values, width, label=method, color=colors[i], edgecolor='white', linewidth=0.5)

# Labels and formatting
ax.set_ylabel('MAP', fontsize=9)
ax.set_xticks(x)
ax.set_xticklabels(['AgentProcess\nBench', 'HINTBench', 'TraceElephant'])
ax.set_ylim(0, 1.0)
ax.set_yticks([0, 0.5, 1.0])
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.52), ncol=2, frameon=False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig('fig-rq2-map.pdf', bbox_inches='tight', dpi=300)
plt.savefig('fig-rq2-map.png', bbox_inches='tight', dpi=300)
print('Saved fig-rq2-map.pdf and fig-rq2-map.png')
