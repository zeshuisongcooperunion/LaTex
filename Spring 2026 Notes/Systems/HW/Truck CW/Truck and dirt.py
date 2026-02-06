# Truck and Dirt Problem - Zeshui Song

import numpy as np
import matplotlib.pyplot as plt

# Constants
m = 3000          # Mass of truck (kg)
c = 40000         # Damping coefficient (kg/s)
k = 8.08e6        # Spring constant (N/m)
g = 10            # Gravity (m/s^2)
md = 20000 / g    # Mass of dirt (2000 kg)
F = -20000        # Downward force (N)

def x(t, M, c, k, F):
    a = F / k
    b = c / (2*M)
    w = np.sqrt(k/M - c**2 / (4*M**2))

    # Eqn: x(t) = a - a*exp(-b*t)*[cos(w*t) + (b/w)*sin(w*t)]
    sol = a - a * np.exp(-b * t) * (np.cos(w * t) + (b / w) * np.sin(w * t))
    return sol

def omega(M, c, k):
    return np.sqrt(k/M - c**2 / (4*M**2))

t = np.linspace(0, 1.0, 1000)

x_m = x(t, m, c, k, F)           
x_m_md = x(t, m + md, c, k, F)    

w_m = omega(m, c, k)
w_m_md = omega(m + md, c, k)
T_m = 2 * np.pi / w_m
T_m_md = 2 * np.pi / w_m_md

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 8))

# Static displacement in mm
y_static = (F / k) * 1000

# Plot 1: m
label_m = f'Inertia $m$: $\omega$={w_m:.2f} rad/s, $T$={T_m:.3f}s'
ax1.plot(t, x_m * 1000, color='blue', label=label_m)
ax1.axhline(y=y_static, color='black', linestyle='--', alpha=0.5)
ax1.text(1.01, y_static, f'F/K {y_static:.2f} mm', va='center', ha='left', transform=ax1.get_yaxis_transform(), color='black')
ax1.set_ylabel('Displacement (mm)')
ax1.set_title('Truck Response: $m$ only')
ax1.legend(loc='upper right')
ax1.grid(True, linestyle=':', alpha=0.6)

# Plot 2: m + md
label_m_md = f'Inertia $m+m_d$: $\omega$={w_m_md:.2f} rad/s, $T$={T_m_md:.3f}s'
ax2.plot(t, x_m_md * 1000, color='red', label=label_m_md)
ax2.axhline(y=y_static, color='black', linestyle='--', alpha=0.5)
ax2.text(1.01, y_static, f'F/K {y_static:.2f} mm', va='center', ha='left', transform=ax2.get_yaxis_transform(), color='black')
ax2.set_ylabel('Displacement (mm)')
ax2.set_xlabel('Time (s)')
ax2.set_title('Truck Response: $m + m_d$')
ax2.legend(loc='upper right')
ax2.grid(True, linestyle=':', alpha=0.6)
plt.suptitle('Truck and Dirt Problem - Zeshui Song', fontsize=16)
plt.tight_layout()
plt.show()