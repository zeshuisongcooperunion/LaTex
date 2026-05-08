close all;
clc;
clear;

% --- Common Parameters ---
r1 = 1000; 
c1 = 2e-6;
tau = r1 * c1; % Time constant
vC0 = 0;
vm = 5;
t = linspace(0, 0.02, 1000); 

% System Definition (Transfer Function)
num = 1;
den = [tau 1];
sys = tf(num, den);

%% Plot 1: Standard 4-Tau Pulse
figure(1);
T4 = 4 * tau; 
vs4 = vm * (t <= T4); 
[vC4, t_out4] = lsim(sys, vs4, t, vC0);

plot(t_out4, vC4, 'b', 'LineWidth', 2);
hold on;
plot(t, vs4, '--r', 'LineWidth', 1.5);

xline(tau, '--', 'Color', [0 0.5 0], 'Label', '\tau', ...
    'LineWidth', 2, 'LabelVerticalAlignment', 'bottom');

grid on;
xlabel('Time (s)');
ylabel('Voltage (V)');
legend('Capacitor Voltage (v_C)', 'Input Voltage (v_m)', 'Time Constant (\tau)');
title('RC Circuit Response (Period = 8\tau, Pulse = 4\tau)');
ylim([0 6]);

%% Plot 2: Shared Plot (Comparison of 1\tau through 5\tau)
figure(2);
hold on;
grid on;

% Define colors
colors = lines(5); 

for n = 1:5
    T_pulse = n * tau;
    vs_loop = vm * (t <= T_pulse);
    [vC_loop, t_out_loop] = lsim(sys, vs_loop, t, vC0);
    
    % Solid for 1 and 4, Dotted for others
    if n == 1 || n == 4
        style = '-';
        width = 2.5; 
    else
        style = ':';
        width = 1.5;
    end
    
    plot(t_out_loop, vC_loop, style, 'Color', colors(n,:), 'LineWidth', width, ...
        'DisplayName', [num2str(n), '\tau Pulse']);
end

xline(tau, '--', 'Color', [0 0.5 0], 'LineWidth', 2, ...
    'Label', '\tau', 'LabelVerticalAlignment', 'bottom', ...
    'HandleVisibility', 'off');

% Horizontal line for Max Input Voltage
yline(vm, '--k', 'Max Input (5V)', 'LineWidth', 1, ...
    'LabelHorizontalAlignment', 'right', 'HandleVisibility', 'off');

% Formatting
xlabel('Time (s)');
ylabel('Voltage (V)');
title('Comparison of RC Circuit Responses for Different Pulse Durations');
legend('Location', 'northeastoutside');
ylim([0 6]);
hold off;

%% Plot 3: Parametric Analysis (Varying Resistance R)
figure(3);
hold on; 
grid on;

R_values = [500, 1000, 2000, 5000]; % Parametric variation of Resistance
T_sim = 0.02; 
t_param = linspace(0, T_sim, 1000);
T_pulse_param = T4; % 4*tau pulse duration

vs_param = vm * (t_param <= T_pulse_param);
plot(t_param, vs_param, '--r', 'LineWidth', 1.5, 'DisplayName', 'Input Voltage (v_m)');

for R = R_values
    current_tau = R * c1; % Recalculate tau for each R 
    
    % Define specific Transfer Function for this R
    sys_param = tf(1, [current_tau 1]);
    
    % Simulate Response
    [vC_param, t_out_param] = lsim(sys_param, vs_param, t_param, vC0);
    
    % Plot with R and Tau in the legend
    plot(t_out_param , vC_param, 'LineWidth', 2, ...
        'DisplayName', sprintf('R = %d \\Omega, \\tau = %.1f ms', R, current_tau*1000));
end

% Formatting
xlabel('Time (s)');
ylabel('Capacitor Voltage (V)');
title('Varying Resistance R (Period = 8\tau, Pulse = 4\tau)');
legend('show', 'Location', 'northeast');
ylim([0 6]);
hold off;