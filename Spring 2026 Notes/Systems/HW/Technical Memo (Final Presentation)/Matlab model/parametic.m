%% SC251: Parametric Analysis - Impact of Resistance (R)
clear; clc; close all;

% Parameters
C = 2e-6;              
Vm = 5.76;              
R_values = [500, 1000, 2000, 5000]; % Resistances to compare (Ohms)
t = linspace(0, 0.04, 1000);        % Time vector (40 ms)
T_pulse = 0.02;                     % Discharge start time (20 ms)

figure('Color', 'w'); hold on; grid on;

% 2. Simulation and Plotting Loop
for R = R_values
    tau = R * C; % Calculate time constant for each R [cite: 23]
    Vc = zeros(size(t));
    
    for j = 1:length(t)
        if t(j) < T_pulse
            % Charging Response [cite: 25]
            Vc(j) = Vm * (1 - exp(-t(j)/tau));
        else
            % Discharging Response [cite: 25]
            t_d = t(j) - T_pulse;
            V_initial = Vm * (1 - exp(-T_pulse/tau)); 
            Vc(j) = V_initial * exp(-t_d/tau);
        end
    end
    
    % Legend includes R and the calculated time constant
    plot(t*1000, Vc, 'LineWidth', 2, ...
        'DisplayName', sprintf('R = %d \\Omega, \\tau = %.1f ms', R, tau*1000));
end

% 3. Labeling
xlabel('Time (ms)');
ylabel('Capacitor Voltage (V)');
title('Parametric Analysis: Varying Resistance (R)');
legend('show', 'Location', 'northeast');
hold off;