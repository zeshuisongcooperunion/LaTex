import matplotlib.pyplot as plt
import numpy as np

# Data 
load = [49.4, 99.4, 149.4, 199.4, 249.4, 299.4, 349.4, 399.4] #grams
# Micrometer readings for loading and unloading
micro_load = [0.873, 0.847, 0.820, 0.793, 0.766, 0.738, 0.713, 0.685] #inches
micro_unload = [0.873, 0.845, 0.816, 0.791, 0.761, 0.738, 0.710, 0.685] #inches
# Strain readings for loading and unloading
strain_load = [0, 36, 78, 120, 163, 208, 249, 292] #microstrain
strain_unload = [-7, 37, 83, 123, 172, 208, 249, 292] #microstrain

#Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 12))

# Plot 1: Deflection vs Load
ax1.plot(load, micro_load, 'bo', mfc='none', markersize=10, label='Loading (Dots)')
ax1.plot(load, micro_unload, 'rx', markersize=10, label='Unloading (X)')
ax1.set_title('Cantilever Beam: Micrometer Reading vs. Load')
ax1.set_xlabel('Cumulative Load (g)')
ax1.set_ylabel('Micrometer Reading (in)')
ax1.grid(True)
ax1.legend()

# Plot 2: Strain vs Load
ax2.plot(load, strain_load, 'bs', mfc='none', markersize=10, label='Loading (Box)')
ax2.plot(load, strain_unload, 'r+', markersize=10, label='Unloading (+)')
ax2.set_title('Cantilever Beam: Strain vs. Load')
ax2.set_xlabel('Cumulative Load (g)')
ax2.set_ylabel('Strain Gage Reading ($\mu\epsilon$)')
ax2.grid(True)
ax2.legend()
plt.subplots_adjust(hspace=0.4)

plt.show()

##################################################################################################
#  Analysis:

# Converting to force and strain for linear regression:
F = (np.array(load) / 1000) * 9.81  # Newtons
e = np.array(strain_load) * 1e-6  # Convert microstrain to strain

# Find slope
slope, intercept = np.polyfit(F, e, 1)
print(f"Calculated Slope (de/dF): {slope:.6e} strain/Newton")

# Plot best fit line
plt.figure(figsize=(8, 5))
plt.scatter(F, e, color='blue', label='Experimental Data')
slope_label = f'Best Fit Line (Slope: {slope:.3e})'
plt.plot(F, slope * F + intercept, color='red', linestyle='--', label=slope_label)

plt.xlabel('Force (Newtons)')
plt.ylabel('Strain ($\epsilon$)')
plt.title('Strain vs. Force Plot (loading)')
plt.legend()
plt.grid(True)
plt.show()