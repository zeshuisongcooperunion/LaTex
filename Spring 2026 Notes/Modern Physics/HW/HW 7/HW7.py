import numpy as np
import matplotlib.pyplot as plt

# 1. Constants
h = 6.626e-34  # Planck's constant (J*s)
k = 1.3806e-23   # Boltzmann constant (J/K)
c = 3.0e8      # Speed of light (m/s)
T = 2289       # Temperature from part (a) in Kelvin

# 2. Setup frequency range (Hz)
# The peak frequency is around 2.4e14 Hz, so we'll go from 1e12 to 1e15 Hz
v = np.linspace(1e12, 1e15, 1000)

# 3. Calculate Planck Model (Correct)
# u(v) = (8 * pi * h * v^3 / c^3) * (1 / (exp(hv / kT) - 1))
planck_u = (8 * np.pi * h * v**3 / c**3) * (1 / (np.exp(h * v / (k * T)) - 1))

# 4. Calculate Rayleigh-Jeans Model (Classical)
# u(v) = (8 * pi * v^2 * k * T / c^3)
rj_u = (8 * np.pi * v**2 * k * T / c**3)

# 5. Create the Plot
plt.figure(figsize=(10, 6))
# Using 'v' to match your array definition
plt.plot(v, planck_u, label='Planck Model (Quantized)', color='blue', linewidth=2)
plt.plot(v, rj_u, label='Rayleigh-Jeans (Classical)', color='red', linestyle='--')

# Formatting
plt.title('Problem 3 (c)')
plt.xlabel(r'Frequency $\nu$ (Hz)')
plt.ylabel(r'Energy Density ($J \cdot s / m^3$)')

# Limit y-axis to see the Planck "hump" clearly
plt.ylim(0, max(planck_u) * 1.5)
plt.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
plt.legend()
plt.grid(True, alpha=0.3)

plt.show()