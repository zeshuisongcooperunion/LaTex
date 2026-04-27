import numpy as np
import matplotlib.pyplot as plt

# 1. Circuit Constants (using your specified source values)
V1 = 12          # Volts [cite: 157]
R1 = 4700        # Ohms (4.7 kΩ) [cite: 159]
R2 = 6800        # Ohms (6.8 kΩ) [cite: 159]

# 2. Calculate Thevenin Equivalent using your specified formulas
# Rth = (R1 * R2) / (R1 + R2)
# Vth = V1 * (R2 / (R1 + R2))
Rth = (R1 * R2) / (R1 + R2) #
Vth = V1 * (R2 / (R1 + R2)) #

# 3. Define the range for R3 (Load Resistance) from 500 to 5000 Ohms
r3_range = np.arange(500, 5250, 250) # [cite: 161]

# 4. Calculate Predicted Values using your equations
# I_R3 = Vth / (Rth + R3)
# V_R3 = Vth * (R3 / (Rth + R3))
# P_R3 = I_R3^2 * R3
i_r3 = Vth / (Rth + r3_range) #
v_r3 = Vth * (r3_range / (Rth + r3_range)) #
p_r3 = (i_r3**2) * r3_range #

i_r3_ma = i_r3 * 1000  # Convert to mA for plotting
p_r3_mw = p_r3 * 1000  # Convert to mW for plotting

# PLOT 1: Power vs. Resistance
plt.figure(figsize=(10, 6))
plt.plot(r3_range, p_r3_mw, marker='o', linestyle='-', color='g', label='Power in $R_3$ (mW)')
plt.axvline(x=Rth, color='r', linestyle='--', alpha=0.7, label=f'$R_{{th}}$ ≈ {Rth:.1f} Ω')
plt.text(Rth + 50, max(p_r3_mw)*0.9, f'Max Power at $R_{{th}}$\n({Rth:.1f} Ω)', color='r')

plt.title('Power across $R_3$ vs. Load Resistance (Calculated)', fontsize=14)
plt.xlabel('Resistance of $R_3$ (Ω)', fontsize=12)
plt.ylabel('Power $P_{R_3}$ (mW)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.savefig('power_vs_resistance.png')
plt.show()

# PLOT 2: Load Voltage vs. Load Current
plt.figure(figsize=(10, 6))
plt.plot(i_r3_ma, v_r3, marker='o', linestyle='-', color='b', label='Load Characteristic')

# Add trendline for slope visualization
z = np.polyfit(i_r3_ma, v_r3, 1)
p = np.poly1d(z)
plt.plot(i_r3_ma, p(i_r3_ma), "r--", alpha=0.5)

# Label Intercept (Vth) and Slope (-Rth)
plt.annotate(f'y-intercept = $V_{{th}}$\n({Vth:.3f} V)', 
             xy=(0, Vth), xytext=(0.3, Vth-0.8),
             arrowprops=dict(facecolor='black', shrink=0.05))

slope_text = f'Slope = $-R_{{th}}$\n({-Rth:.1f} Ω)'
plt.text(np.mean(i_r3_ma), np.mean(v_r3) + 0.5, slope_text, 
         color='red', fontweight='bold', bbox=dict(facecolor='white', alpha=0.5))

plt.title('Load Voltage ($V_{R3}$) vs. Load Current ($I_{R3}$) (Calculated)', fontsize=14)
plt.xlabel('Load Current $I_{R3}$ (mA)', fontsize=12)
plt.ylabel('Load Voltage $V_{R3}$ (V)', fontsize=12)
plt.xlim(left=0)
plt.ylim(0, max(v_r3) + 1)
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()

#####
#Plotting Experimental data
r3_range = np.array([500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500, 2750, 3000, 3250, 3500, 3750, 4000, 4250, 4500, 4750, 5000])
v_r3 = np.array([1.3408, 1.8462, 2.2785, 2.6506, 2.9730, 3.2540, 3.5000, 3.7190, 3.9130, 4.0857, 4.2394, 4.3770, 4.5000, 4.6105, 4.7097, 4.7989, 4.8793, 4.9524, 5.0189])
i_r3_ma = np.array([2.6816, 2.4615, 2.2785, 2.1205, 1.9820, 1.8594, 1.7500, 1.6529, 1.5652, 1.4857, 1.4131, 1.3468, 1.2857, 1.2295, 1.1774, 1.1291, 1.0843, 1.0426, 1.0038])
p_r3_w = np.array([0.0035954, 0.00454438, 0.00519149, 0.00562055, 0.00589238, 0.00607049, 0.006125, 0.0061471, 0.00612476, 0.0060702, 0.00599097, 0.00589492, 0.00578571, 0.0056685, 0.00554523, 0.00541859, 0.00529061, 0.00516335, 0.00503781])
p_r3_mw = p_r3_w * 1000  # Convert to mW for plotting

# 2. Derive Experimental Thevenin values using linear regression (V_L vs I_L)
# The slope is -Rth and the intercept is Vth
coeffs = np.polyfit(i_r3_ma, v_r3, 1)
rth_exp = -coeffs[0] * 1000  # Multiplied by 1000 because I_L is in mA
vth_exp = coeffs[1]

# --- PLOT 1: Power vs. Resistance ---
plt.figure(figsize=(10, 6))
plt.plot(r3_range, p_r3_mw, marker='o', linestyle='-', color='g', label='Experimental Power in $R_3$')
plt.axvline(x=rth_exp, color='r', linestyle='--', alpha=0.7, label=f'$R_{{th}}$ ≈ {rth_exp:.1f} Ω')
plt.text(rth_exp + 50, max(p_r3_mw)*0.9, f'Max Power at $R_{{th}}$\n({rth_exp:.1f} Ω)', color='r')

plt.title('Power across $R_3$ vs. Load Resistance (Experimental)', fontsize=14)
plt.xlabel('Resistance of $R_3$ (Ω)', fontsize=12)
plt.ylabel('Power $P_{R_3}$ (mW)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.savefig('power_vs_resistance_exp.png')
plt.show()

# --- PLOT 4: Load Voltage vs. Load Current (Experimental) ---
plt.figure(figsize=(10, 6))
# linestyle='' ensures points are not connected
plt.plot(i_r3_ma_exp, v_r3_exp, marker='o', linestyle='', color='b', label='Experimental Load Characteristic')

# Linear Trendline
z_exp = np.polyfit(i_r3_ma_exp, v_r3_exp, 1)
p_exp = np.poly1d(z_exp)
plt.plot(i_r3_ma_exp, p_exp(i_r3_ma_exp), "r--", alpha=0.5)

# Label Intercept (Vth) and Slope (-Rth)
plt.annotate(f'y-intercept = $V_{{th}}$\n({vth_exp:.3f} V)', 
             xy=(0, vth_exp), xytext=(0.4, vth_exp-0.5),
             arrowprops=dict(facecolor='black', shrink=0.05))

slope_text_exp = f'Slope = $-R_{{th}}$\n({-rth_exp:.1f} $\Omega$)'
plt.text(np.mean(i_r3_ma_exp), np.mean(v_r3_exp) + 0.3, slope_text_exp, 
         color='red', bbox=dict(facecolor='white', alpha=0.5))

plt.title('Load Voltage ($V_{R_3}$) vs. Load Current ($I_{R_3}$) (Experimental)', fontsize=14)
plt.xlabel('Load Current $I_{R_3}$ (mA)', fontsize=12)
plt.ylabel('Load Voltage $V_{R_3}$ (V)', fontsize=12)
plt.xlim(left=0)
plt.ylim(0, max(v_r3_exp) + 1)
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()