import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Load Excel file
df = pd.read_excel("Data/2EOR.xlsx")

# Create figure and axes
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
(ax0, ax1), (ax2, ax3) = axs

# Function to plot regression and return equation string
def add_trendline(ax, x, y, color='black'):
    slope, intercept, r_value, _, _ = linregress(x, y)
    line = slope * np.array(x) + intercept
    ax.plot(x, line, color=color, linestyle='--', linewidth=2)
    eq_str = f"$y = {slope:.2f}x + {intercept:.2f}$\n$R^2 = {r_value**2:.2f}$"
    return eq_str

# Panel 1: ΔGO* vs. ΔGOH*
x0 = df['ΔGOH* (eV)']
y0 = df['ΔGO* (eV)']
ax0.scatter(x0, y0, c='tab:blue')
ax0.set_xlabel('ΔG$_{\\mathrm{OH}^*}$ (eV)', fontsize=24)
ax0.set_ylabel('ΔG$_{\\mathrm{O}^*}$ (eV)', fontsize=24)
eq0 = add_trendline(ax0, x0, y0, color='tab:blue')
ax0.text(0.05, 0.95, eq0, transform=ax0.transAxes, fontsize=14, verticalalignment='top')

# Panel 2: ΔGOOH* vs. ΔGOH*
x1 = df['ΔGOH* (eV)']
y1 = df['ΔGOOH* (eV)']
ax1.scatter(x1, y1, c='tab:green')
ax1.set_xlabel('ΔG$_{\\mathrm{OH}^*}$ (eV)', fontsize=24)
ax1.set_ylabel('ΔG$_{\\mathrm{OOH}^*}$ (eV)', fontsize=24)
eq1 = add_trendline(ax1, x1, y1, color='tab:green')
ax1.text(0.05, 0.95, eq1, transform=ax1.transAxes, fontsize=14, verticalalignment='top')

# Panel 3: ΔGO* vs. ΔGOOH*
x2 = df['ΔGOOH* (eV)']
y2 = df['ΔGO* (eV)']
ax2.scatter(x2, y2, c='tab:purple')
ax2.set_xlabel('ΔG$_{\\mathrm{OOH}^*}$ (eV)', fontsize=24)
ax2.set_ylabel('ΔG$_{\\mathrm{O}^*}$ (eV)', fontsize=24)
eq2 = add_trendline(ax2, x2, y2, color='tab:purple')
ax2.text(0.05, 0.95, eq2, transform=ax2.transAxes, fontsize=14, verticalalignment='top')

# Panel 4: G1 and G2 vs. ΔGOH*
x3 = df['ΔGOH* (eV)']
y3a = df['G1 (eV)']
y3b = df['G2 (eV)']
ax3.scatter(x3, y3a, label='G$_1$', c='tab:red')
ax3.scatter(x3, y3b, label='G$_2$', c='tab:orange')

# Add trendlines to ax3
eq3a = add_trendline(ax3, x3, y3a, color='tab:red')
eq3b = add_trendline(ax3, x3, y3b, color='tab:orange')

ax3.set_xlabel('ΔG$_{\\mathrm{OH}^*}$ (eV)', fontsize=24)
ax3.set_ylabel('G (eV)', fontsize=24)

# Adjust legend position and frame
legend = ax3.legend(loc='upper center', bbox_to_anchor=(0.83, 0.98), fontsize=16, frameon=True)
legend.get_frame().set_linewidth(2)
legend.get_frame().set_edgecolor('black')

# Make spines thicker and ticks bolder
for ax in [ax0, ax1, ax2, ax3]:
    for spine in ax.spines.values():
        spine.set_linewidth(2)
    ax.tick_params(axis='both', which='major', direction='in', length=8, width=2, labelsize=13, top=True, right=True)
    ax.tick_params(axis='both', which='minor', direction='in', length=5, width=1.5, top=True, right=True)

fig.subplots_adjust(wspace=0.3, hspace=0.3)  # Adjust values as needed

plt.show()