% Vehicle System Efficiency Calculation for 2026 Honda Accord (ID: EPNA1C)
clear; clc; close all;

%% Import Drive Cycle Data
uddscol = importdata('uddscol.txt');
t = uddscol.data(:,1);           % Time in seconds
v_mph = uddscol.data(:,2);       % Speed in mph
v = v_mph * 0.44704;             % Speed converted to m/s

%% Vehicle Parameters
m = 3625*0.453592;  % Equivalent Test Weight (lbs) to mass (kg)
A = 51.820 * 4.44822;   % Target A (lbf to N)
B = -0.53320 * (4.448 / 0.44704);   % Target B (lbf/mph to N/(m/s))
C = 0.025350 * (4.448 / (0.44704^2));   % Road load C (lbf/mph^2 to to N/(m/s)^2)
q_NHV = 46.7e6; % Net/Lower Heating Value of Tier 2 Cert Gasoline (J/kg)

% Finding weight of fuel consumed by integrating the UDDS data to find total distance traveled, since the EPA dataset gives CO2 emissions in g/mile, I can find the weight of CO2 emitted, and then use the carbon content of gasoline to find the weight of fuel consumed.
total_distance_m = trapz(t, v); % Integrate speed over time (meters)
total_distance_miles = total_distance_m / 1609; % Meters to miles

Weight_CO2_g = total_distance_miles * 240.8100000; % g/mile * miles = total g of CO2 emitted
Weight_C_g = Weight_CO2_g * (12.011 / 44.009); % Find weight of carbon in the CO2 (g) using the molar mass ratio of C to CO2
Weight_gas_g = Weight_C_g / 0.87; % Find weight of gasoline consumed (g). Gas is approx 87% carbon by weight.
Weight_gas = Weight_gas_g / 1000; % Convert to kg

% Finally, the fuel energy input in J will just be the weight of fuel consumed multiplied by the lower heating value of the fuel.
TotalFuelEnergy = Weight_gas * q_NHV; % Total energy input from fuel (J)

%% Calculate Propulsion Energy
F_rl = A + B*v + C.*v.^2; % Road Load Force (N)

% Calculate acceleration (dv/dt)
dv = diff(v); % Forward difference to find change in velocity
dt = diff(t); % Forward difference to find change in time
a_raw = dv./ dt; 
a = [0; a_raw]; % Append 0 for the first element because differentiation shortened the vector by 1
F_t = F_rl + m*a; % Tractive Force (N)

Power_t = F_t .* v; % Calculate Power required for tractive road load (Force * Velocity)
PropulsionPower = Power_t; 
PropulsionPower(PropulsionPower < 0) = 0; % Apply the R+ constraint, keeping only positive power values and setting negatives to zero

PropulsionEnergy = trapz(t, PropulsionPower); % Integrate power over time to get energy (J)
%% Calculate Vehicle System Efficiency
VSE = (PropulsionEnergy / TotalFuelEnergy) * 100; % Vehicle System Efficiency (%)

%% Plotting Results
figure('Name', 'UDDS Power Requirements', 'Units', 'normalized', 'Position', [0.1 0.1 0.8 0.7]);

% Subplot 1: UDDS speed profile
subplot(2,1,1); 
plot(t, v_mph, 'Color', [0 0.4470 0.7410], 'LineWidth', 1.5);
ylabel('Speed (mph)');  
title('UDDS Drive Cycle: Speed vs Time');
grid on;
set(gca, 'FontSize', 10);

% Subplot 2: Power required for tractive road load
% Convert PropulsionPower from Watts to kW for plotting
subplot(2,1,2);
area(t, PropulsionPower / 1000, 'FaceColor', [0.8500 0.3250 0.0980], 'EdgeColor', 'none', 'FaceAlpha', 0.5);
hold on;
plot(t, PropulsionPower / 1000, 'Color', [0.6350 0.0780 0.1840], 'LineWidth', 1);
xlabel('Time (seconds)');
ylabel('Power Required (kW)');
title(['Tractive Power Required (VSE = ', num2str(VSE, '%.2f'), '%)']);
grid on;
set(gca, 'FontSize', 10);

% Link the x-axes so they zoom together
linkaxes(findobj(gcf, 'Type', 'axes'), 'x');