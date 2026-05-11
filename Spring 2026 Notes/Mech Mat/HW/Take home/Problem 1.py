import numpy as np

# --- Input Parameters (Table 1) ---
F_T = 80.0          # [N]
E = 40.0*1e9        # [Pa] [N/m^2]
sigma_u = 800.0*1e6 # [Pa] [N/m^2]

# Dimensions [m]
t_p = 4.0*1e-3     
w_p = 44.0*1e-3     
t_w = 2.0*1e-3      
d_o = 25.0*1e-3    
L_b = 76.0*1e-3    
L_s = 400.0*1e-3    
L_T = L_b + L_s     

# --- Moment of Inertia Calculations ---

# Spar only (Hollow Box)
I_s = (1/12)*(d_o**4 -(d_o - 2*t_w)**4)  # [m^4]

# Combined section (Spar + 2 Plates)
I_sp = I_s + 2 * ((1/12)*w_p*t_p**3+w_p*t_p*(d_o/2 + t_p/2)**2)  # [m^4]

# --- Slope and Deflection Calculations  ---
## Slope at x=L_b
theta_Lb = ((F_T*L_b)/(E*I_sp))*(2*L_T-L_b)  # [radians]
## Deflection at x=L_b
y_Lb = ((F_T*L_b**2)/(6*E*I_sp))*(3*L_T-L_b)  # [m]
## Slope at x=L_T
theta_LT = (
((F_T*L_T**2)/(2*E*I_s))+
(((F_T*L_b)/(2*E*I_sp))-((F_T*L_b)/(2*E*I_s)))*(2*L_T-L_b)  # [radians]
)
## Deflection at x=L_T
y_LT = (
((F_T*L_T**3)/(3*E*I_s))+
(((F_T*L_b)/(2*E*I_sp))-((F_T*L_b)/(2*E*I_s)))*(2*L_T-L_b)*(L_T-L_b)+
(((F_T*L_b**2)/(6*E*I_sp))-((F_T*L_b**2)/(6*E*I_s)))*(3*L_T-L_b)
)

# --- Output Results ---
print(f"--- Geometry ---")
print(f"I_spar: {I_s:.4e} m^4")
print(f"I_composite: {I_sp:.4e} m^4")
print(f"\n--- Results at x = Lb ({L_b*1000} mm) ---")
print(f"Slope: {theta_Lb:.6f} rad")
print(f"Deflection: {y_Lb*1000:.4f} mm")
print(f"\n--- Results at Tip (x = {L_T*1000} mm) ---")
print(f"Slope: {theta_LT:.6f} rad")
print(f"Deflection: {y_LT*1000:.4f} mm")

###################################################################################
# Bounding cases:
# Minimum deflection: maximum stiffness (I_sp)
y_min = ((F_T*L_T**3)/(2*E*I_sp))  # [m]
# Maximum deflection: minimum stiffness (I_s)
y_max = ((F_T*L_T**3)/(2*E*I_s))  # [m]

print(f"\n--- Bounding Cases ---")
print(f"Minimum Deflection: {y_min*1000:.4f} mm")
print(f"Maximum Deflection: {y_max*1000:.4f} mm")

###################################################################################
# Part d: factor of safety
# Max stress:
sigma_max = ((F_T*L_T)*(d_o/2 + t_p))/I_sp  # [Pa]
# Factor of safety:
FOS = sigma_u/sigma_max
print(f"\n--- Factor of Safety ---")
print(f"Maximum Stress: {sigma_max/1e6:.2f} MPa")
print(f"Factor of Safety: {FOS:.2f}")