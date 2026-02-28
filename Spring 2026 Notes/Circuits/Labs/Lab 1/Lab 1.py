import matplotlib.pyplot as plt
import numpy as np
import os
folder = os.path.dirname(os.path.abspath(__file__))
# --- Data Entry ---
# Circuit A (R2 = 1k Ohm) - Measured Values
v_a = np.array([1, 1.96, 2.96, 4, -1, -1.97, -2.74, -4])
i_a = np.array([1, 1.96, 2.94, 3.98, -1, -2.03, -2.8, -4.09])

# Circuit B (R2 = 3.3k Ohm) - Measured Values
v_b = np.array([1.53, 3.11, 4.59, 5.92, -1.52, -3.05, -4.62, -6.17])
i_b = np.array([0.46, 0.97, 1.42, 1.9, -0.47, -0.95, -1.44, -1.92])

def plot_with_best_fit(x, y, label, color, marker):
    # Scatter plot of measured data
    plt.scatter(x, y, color=color, marker=marker, label=f'{label} Measured')
    
    # Calculate best fit line (y = mx + b)
    m, b = np.polyfit(x, y, 1)
    x_range = np.linspace(min(x), max(x), 100)
    plt.plot(x_range, m * x_range + b, color=color, linestyle='--', 
             alpha=0.7, label=f'{label} Fit (slope={m:.3f})')

# --- Plotting ---
plt.figure(figsize=(10, 6))

plot_with_best_fit(v_a, i_a, 'Circuit A (1kΩ)', 'blue', 'o')
plot_with_best_fit(v_b, i_b, 'Circuit B (3.3kΩ)', 'red', 's')

# Formatting
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.title('Measured Load Current vs. Voltage')
plt.xlabel('Measured Voltage (V)')
plt.ylabel('Measured Current (mA)')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.savefig(os.path.join(folder, "Plot.png"), dpi=300, bbox_inches='tight')

plt.show()