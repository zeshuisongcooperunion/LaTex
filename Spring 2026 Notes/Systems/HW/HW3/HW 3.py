# HW 3 - Zeshui Song

import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
import os

# Define the folder where figures will be saved
folder = os.path.dirname(os.path.abspath(__file__))  # same folder as script

# Constants
R = 10          # Resistance (ohms)
L = 1         # Inductance (H)
C = 0.1        # Capacitance (F)

# Define transfer functions
s = ctrl.TransferFunction.s
G_a = (1) / (L*C*s**2 + R*C*s + 1) # Transfer function for part A
G_b = (L*s) / (L*R*C*s**2 + L*s + R) # Transfer function for part B

# Unit Step Input
t = np.linspace(0, 20, 1000)
t_a, y_a = ctrl.step_response(G_a, t)
t_b, y_b = ctrl.step_response(G_b, t)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t_a, y_a, label='Circuit (a)', linewidth=2)
plt.plot(t_b, y_b, label='Circuit (b)', linewidth=2)
plt.axhline(1, color='gray', linestyle='--', alpha=0.5, label='Unit Step Input')
plt.title('Step Response Comparison')
plt.xlabel('Time (s)')
plt.ylabel('Output Voltage $e_o(t)$ (V)')
plt.legend()
plt.grid(True)

# Save the figure
plt.savefig(os.path.join(folder, 'circuit_responses.png'))
plt.show()

# Steady State values
print(f"Steady-state e_o (circuit a): {y_a[-1]:.4f} V")
print(f"Steady-state e_o (circuit b): {y_b[-1]:.4f} V")