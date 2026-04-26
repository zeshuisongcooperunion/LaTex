close all;
clc;
clear;

% --- Parameters ---
r1 = 1000; 
c1 = 2e-6;      % Updated to 2uF
tau = r1 * c1;  % Time constant (0.002s)
vC0 = 0;
vm = 5;         % Updated to 5V

% System Definition (Transfer Function)
num = 1;
den = [tau 1];
sys = tf(num, den);

% Time vector
t = linspace(0, 0.02, 5000); 

figure;

%% Subplot 1: Square Wave with Pulse Width = 1*tau
k1 = 1;
half_period1 = k1 * tau;
period1 = 2 * half_period1;
vs1 = vm * (mod(t, period1) < half_period1);

[vC1, t_out1] = lsim(sys, vs1, t, vC0);

subplot(2, 1, 1);
plot(t_out1, vC1, 'b', 'LineWidth', 2);
hold on;
plot(t, vs1, '--r', 'LineWidth', 1.5);

% Darker green Time Constant line
xline(tau, '--', 'Color', [0 0.5 0], 'Label', '\tau', ...
    'LineWidth', 2, 'LabelVerticalAlignment', 'bottom');

grid on;
ylim([0 6]);
ylabel('Voltage (V)');
legend('v_C', 'v_m', '\tau');
title(['Square Wave Response: Period = 2\tau, Pulse Width = \tau']);

%% Subplot 2: Square Wave with Pulse Width = 4*tau
k2 = 4;
half_period2 = k2 * tau;
period2 = 2 * half_period2;
vs2 = vm * (mod(t, period2) < half_period2);

[vC2, t_out2] = lsim(sys, vs2, t, vC0);

subplot(2, 1, 2);
plot(t_out2, vC2, 'b', 'LineWidth', 2);
hold on;
plot(t, vs2, '--r', 'LineWidth', 1.5);

% Darker green Time Constant line
xline(tau, '--', 'Color', [0 0.5 0], 'Label', '\tau', ...
    'LineWidth', 2, 'LabelVerticalAlignment', 'bottom');

grid on;
ylim([0 6]);
xlabel('Time (s)');
ylabel('Voltage (V)');
title(['Square Wave Response: Period = 8\tau, Pulse Width = 4\tau']);