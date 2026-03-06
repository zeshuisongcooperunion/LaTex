import numpy as np
import matplotlib.pyplot as plt

# Refractive indices
n_air = 1
n_water = 1.33

# Fresnel coefficients
def get_coeffs(n1, n2):
    theta_i = np.linspace(0, np.pi/2, 1000)

    term = (n2/n1)**2 - np.sin(theta_i)**2
    sqrt_term = np.sqrt(term + 0j)  # allow complex values for TIR

    # s-polarization (perpendicular)
    r_s = -(np.cos(theta_i) - sqrt_term) / (np.cos(theta_i) + sqrt_term)
    t_s = (2*np.cos(theta_i)) / (np.cos(theta_i) + sqrt_term)

    # p-polarization (parallel)
    r_p = ((n2/n1)**2*np.cos(theta_i) - sqrt_term) / \
          ((n2/n1)**2*np.cos(theta_i) + sqrt_term)

    t_p = (2*(n2/n1)*np.cos(theta_i)) / \
          ((n2/n1)**2*np.cos(theta_i) + sqrt_term)

    return theta_i, r_s, t_s, r_p, t_p


# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# (a) Air → Water
theta, r_s, t_s, r_p, t_p = get_coeffs(n_air, n_water)

ax1.plot(np.degrees(theta), r_s.real, label=r'$r_{\perp}$')
ax1.plot(np.degrees(theta), t_s.real, label=r'$t_{\perp}$')
ax1.plot(np.degrees(theta), r_p.real, label=r'$r_{\parallel}$')
ax1.plot(np.degrees(theta), t_p.real, label=r'$t_{\parallel}$')

ax1.set_title("Air → Water")
ax1.set_xlabel("Incident Angle (deg)")
ax1.set_ylabel("Coefficient")
ax1.set_xlim(0, 90)
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.7)


# (b) Water → Air
theta, r_s, t_s, r_p, t_p = get_coeffs(n_water, n_air)

ax2.plot(np.degrees(theta), r_s.real, label=r'$r_{\perp}$')
ax2.plot(np.degrees(theta), t_s.real, label=r'$t_{\perp}$')
ax2.plot(np.degrees(theta), r_p.real, label=r'$r_{\parallel}$')
ax2.plot(np.degrees(theta), t_p.real, label=r'$t_{\parallel}$')

# Critical angle
theta_c = np.arcsin(n_air/n_water)

ax2.axvline(np.degrees(theta_c), linestyle='--', color='black',
            label='Critical Angle')

# Shade total internal reflection region
ax2.axvspan(np.degrees(theta_c), 90, alpha=0.15)
ax2.text(np.degrees(theta_c)+20, 2, "TIR Region")

ax2.set_title("Water → Air")
ax2.set_xlabel("Incident Angle (deg)")
ax2.set_xlim(0, 90)
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.7)


plt.tight_layout()
plt.show()


### Problem 4
# Fresnel coefficients
def get_coeffs(theta_i, n1, n2):
    term = (n2/n1)**2 - np.sin(theta_i)**2
    sqrt_term = np.sqrt(term + 0j)  # allow complex values for TIR

    # s-polarization (perpendicular)
    r_s = -(np.cos(theta_i) - sqrt_term) / (np.cos(theta_i) + sqrt_term)
    t_s = (2*np.cos(theta_i)) / (np.cos(theta_i) + sqrt_term)

    # p-polarization (parallel)
    r_p = ((n2/n1)**2*np.cos(theta_i) - sqrt_term) / \
          ((n2/n1)**2*np.cos(theta_i) + sqrt_term)

    t_p = (2*(n2/n1)*np.cos(theta_i)) / \
          ((n2/n1)**2*np.cos(theta_i) + sqrt_term)

    return r_s, t_s, r_p, t_p

print("S-Polarization (perpendicular):")
print(f"r_s = {get_coeffs(np.deg2rad(0), 1, 1.51)[0]}")
print(f"t_s = {get_coeffs(np.deg2rad(0), 1, 1.51)[1]}")

print("P-Polarization (parallel):")
print(f"r_p = {get_coeffs(np.deg2rad(0), 1, 1.51)[2]}")
print(f"t_p = {get_coeffs(np.deg2rad(0), 1, 1.51)[3]}")