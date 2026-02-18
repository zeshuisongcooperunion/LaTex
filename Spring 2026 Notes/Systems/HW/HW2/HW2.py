# HW2 Problem 2 - Zeshui Song

import numpy as np
import matplotlib.pyplot as plt

# Constants
m = 2          # Mass of camera (kg)
b_val = 80     # Damping coefficient (kg/s)
k = 2600       # Spring constant (N/m)
F_hat = 0.2    # Impulsive force (N-s) from 20g bird at 10 m/s

def x_func(t, m, b, k, F):
    alpha = b / (2 * m) #
    w_d = np.sqrt(k/m - alpha**2) #
    amp = F / (m * w_d) #
    return amp * np.exp(-alpha * t) * np.sin(w_d * t) #
#Time array
t = np.linspace(0, 0.5, 10000)
dt = t[1] - t[0]

# Calculate displacement
x_val = x_func(t, m, b_val, k, F_hat)

# Numeric dervative to find velocity
v_vals = np.gradient(x_val, dt)

# Find max when velocity crosses zero from positive to negative
zero_crossings = np.where(np.diff(np.sign(v_vals)) < 0)[0]
idx_peak = zero_crossings[0]

t_peak_num = t[idx_peak]
x_peak_num = x_val[idx_peak]

# Plotting
fig, ax1 = plt.subplots(figsize=(8, 6))

# Plot the displacement in mm
ax1.plot(t, x_val * 1000, color='blue', label='Camera Displacement')

# Plot the numerical max point
ax1.plot(t_peak_num, x_peak_num * 1000, 'ro', label=f'Max deflection: {x_peak_num*1000:.3f} mm')
ax1.annotate(f'Max: {x_peak_num*1000:.3f} mm\nat {t_peak_num:.4f} s', 
             xy=(t_peak_num, x_peak_num * 1000), 
             xytext=(t_peak_num + 0.05, x_peak_num * 1000 + 0.2),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))

ax1.axhline(y=0, color='black', linestyle='--', alpha=0.5)
ax1.set_ylabel('x(t) Displacement (mm)')
ax1.set_xlabel('Time (s)')
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend()

plt.suptitle('HW2 Problem 2 - Zeshui Song', fontsize=16)
plt.tight_layout()
plt.show()

print(f"The numerical derivative first crosses zero at t = {t_peak_num:.4f} seconds.")
print(f"The numerical maximum displacement is {x_peak_num*1000:.3f} mm.")