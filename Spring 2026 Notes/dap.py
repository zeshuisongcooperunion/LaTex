import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# 1. Configuration & Original 24V Data
v_original = 24
v_new = 9
scale_factor = v_new / v_original  # 0.375

rpm_data_24v = np.array([93.75, 206.25, 300, 393.75, 506.25, 600, 693.75, 806.25, 900, 993.75, 1106.25, 1200])
torque_ncm_data = np.array([41.2, 40.6, 40.6, 42.2, 40.2, 36.2, 32.4, 28.6, 25.4, 23.2, 20.0, 17.2])

# 2. Extrapolate to 9V
# We scale the RPM (X-axis) by the voltage ratio
rpm_data_9v = rpm_data_24v * scale_factor

# 3. Interpolate for smooth curves
rpm_smooth_9v = np.linspace(rpm_data_9v.min(), rpm_data_9v.max(), 1000)
interp_func_9v = interp1d(rpm_data_9v, torque_ncm_data, kind='cubic')
torque_smooth_9v = interp_func_9v(rpm_smooth_9v)

# 4. Calculate Power for 9V (Watts)
# P = (Torque_ncm / 100) * (RPM * 2 * pi / 60)
power_watts_9v = (torque_smooth_9v / 100) * (rpm_smooth_9v * 2 * np.pi / 60)
raw_power_watts_9v = (torque_ncm_data / 100) * (rpm_data_9v * 2 * np.pi / 60)

# 5. Find the maximum power point
max_power_idx = np.argmax(power_watts_9v)
optimal_rpm_9v = rpm_smooth_9v[max_power_idx]
max_power_9v = power_watts_9v[max_power_idx]
torque_at_max_9v = torque_smooth_9v[max_power_idx]

print(f"--- 9V Analysis Results ---")
print(f"Optimal Speed: {optimal_rpm_9v:.2f} RPM")
print(f"Max Power Output: {max_power_9v:.2f} Watts")
print(f"Torque at Max Power: {torque_at_max_9v:.2f} N·cm")

# 6. Dual-Axis Visualization
fig, ax1 = plt.subplots(figsize=(12, 7))

# --- Primary Y-Axis: Power ---
color_p = 'crimson'
ax1.set_xlabel('Speed (RPM)', fontsize=12)
ax1.set_ylabel('Power (Watts)', color=color_p, fontsize=12)
ax1.plot(rpm_smooth_9v, power_watts_9v, color=color_p, linewidth=2.5, label='Power (9V Interpolated)')
ax1.scatter(rpm_data_9v, raw_power_watts_9v, color=color_p, s=40, alpha=0.6, label='Power (9V Extrapolated Points)')
ax1.tick_params(axis='y', labelcolor=color_p)

# Mark the peak power point
ax1.scatter(optimal_rpm_9v, max_power_9v, color='gold', edgecolor='black', s=150, marker='*', zorder=10, label='Peak Power Point')
ax1.axvline(optimal_rpm_9v, color='gray', linestyle=':', alpha=0.5)

# --- Secondary Y-Axis: Torque ---
ax2 = ax1.twinx() 
color_t = 'darkblue'
ax2.set_ylabel('Torque (N·cm)', color=color_t, fontsize=12)
ax2.plot(rpm_smooth_9v, torque_smooth_9v, color=color_t, linewidth=2, linestyle='--', alpha=0.7, label='Torque (9V Interpolated)')
ax2.scatter(rpm_data_9v, torque_ncm_data, color=color_t, s=40, alpha=0.6, label='Torque (9V Extrapolated Points)')
ax2.tick_params(axis='y', labelcolor=color_t)

# Layout and Legend
plt.title('Extrapolated 9V Motor Performance: Power & Torque vs. Speed', fontsize=14, pad=20)
ax1.grid(True, linestyle=':', alpha=0.6)

# Combine legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper right', frameon=True)

fig.tight_layout()
plt.show()
    