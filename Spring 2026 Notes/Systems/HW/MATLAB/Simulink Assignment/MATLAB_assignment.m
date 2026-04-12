% MATLAB/Simulink Assignment- Zeshui Song
clear; clc; close all;

%% Part A

R = 3.3; %omega
L = 0.1; %H
J1 = 9.64 * 10^-6; %kg*m^2
m = 0.033; %kg
r = 0.0242; %m
B = 0.01; %N*m*s
Km = 0.0280; %N*m/A
Kg = 0.0280; %V/(rad/s)
N = 2; % gear ratio (r2/r1)
s = tf('s');

% Find J2 
J2 = 1/2 * m * r^2; %kg*m^2

% Define the transfer function of the system
num = N*Km;
den = [J1*N^2*L+J2*L, J1*N^2*R+J2*R+B*L, B*R+Kg*Km*N^2];

sys = tf(num, den);

t = 0:0.001:1;        % Time vector from 0 to 1 second with a step of 0.01 seconds
u_val = 10;          % 10 V Step 
[y_tf, t_tf] = step(u_val * sys, t); % Simulate the response of the system to the input u over time t


%% Part B
steady = (10*N*Km) / (B*R + Kg*Km*N^2); % Steady state value of the system
disp(['Steady State Value: ', num2str(steady), ' rad/s']);

%% Part D
A_ss = [ -B/(J1*N^2+J2),    (N*Km)/(J1*N^2+J2); 
     -(Kg*N)/L,   -R/L ];
B_ss = [0; 1/L];
C_ss = [1, 0];
D_ss = 0;
sys_ss = ss(A_ss, B_ss, C_ss, D_ss);

% Part e: Verify State-Space
[y_ss, t_ss] = step(u_val* sys_ss, t);

% Plotting
figure;
plot(t_tf, y_tf, 'b', 'LineWidth', 2); hold on;
plot(t_ss, y_ss, 'r--', 'LineWidth', 1.5);
grid on;
xlabel('Time (s)'); ylabel('Angular Velocity (rad/s)');
title('1a & 1e: Motor Response to 10V Step');
legend('Transfer Function', 'State-Space');

%% Part F
% New Motor Parameters
J1_new = 4.65 * 10^-6;      % New motor inertia 
m_new = 0.053;              % New disc mass 
r_new = 0.0248;             % New disc radius 
R_new = 8.4;                % New resistance 
Km_new = 0.042;             % New torque constant 
Kg_new = 0.042;             % New back-EMF constant 

% Calculate new Load Inertia J2
J2_new = 0.5 * m_new * r_new^2;

% Define New State-Space Matrices
A_new = [ -B/(J1_new*N^2+J2_new),    (N*Km_new)/(J1_new*N^2+J2_new); 
         -(Kg_new*N)/L,   -R_new/L ];
B_new = [0; 1/L];
C_new = [1, 0];
D_new = 0;

sys_ss_new = ss(A_new, B_new, C_new, D_new);

% Simulate response for the new motor to 10V input
[y_new, t_new] = step(u_val * sys_ss_new, t);

% Plotting Comparison
figure;
plot(t_tf, y_tf, 'b', 'LineWidth', 2); hold on;
plot(t_new, y_new, 'r', 'LineWidth', 2);
grid on;
xlabel('Time (s)'); ylabel('Angular Velocity (rad/s)');
title('Part f: Comparison of Motor Responses (10V Step)');
legend('Original Motor (Part a)', 'New Motor (Part f)');

%% Part G
t_g = 0:0.0000001:0.05; % Time vector from 0 to 5 seconds with a step of 0.01 seconds
u_g = zeros(size(t_g));  % Zero applied voltage for the spin-down

x0 = [100; 0]; % Initial Conditions: x = [omega2; i] = [100 rad/s; 0 Amps]

% Simulate with lsim
[y_g, t_out_g] = lsim(sys_ss_new, u_g, t_g, x0);

% Plot the spin-down
figure;
plot(t_out_g, y_g, 'm', 'LineWidth', 2);
grid on;
xlabel('Time (s)');
ylabel('Angular Velocity (rad/s)');
title('Part g: New Motor Spin-down from \omega_0 = 100 rad/s');
legend('Spin-down Response');

%% Part I
T_mech = (J2_new*R_new+J1_new*R_new*N^2)/(Kg_new*Km_new*N^2); % Mechanical time constant
disp(['Mechanical Time Constant: ', num2str(T_mech), ' seconds']);

%% Part K
L_k = 0.1;
B_k = 0.01;

% Rewriting the transfer function with new parameters:
num_k = N*Km_new;
den_k = [J1_new*N^2*L_k+J2_new*L_k, J1_new*N^2*R_new+J2_new*R_new+B_k*L_k, B_k*R_new+Kg_new*Km_new*N^2];
P = tf(num_k, den_k);

t_k = 0:0.00001:0.1; % Time vector 
Kp_vals = [1, 10, 100]; % Different proportional gains
R_ref = 100; % Reference input (100 rad/s)

figure; hold on;
for Kp = Kp_vals
    % Define Controller (C)
    C = tf(Kp);
    
    % Define CLTF = CP / (1 + CP)
    CLTF = (C * P) / (1 + C * P);
    
    % Simulate the response to R(s) = 100/s
    [y_k, t_out_k] = step(R_ref * CLTF, t_k);
    
    plot(t_out_k, y_k, 'LineWidth', 1.5, 'DisplayName', ['Kp = ', num2str(Kp)]);
end

grid on;
xlabel('Time (s)'); ylabel('Angular Velocity (rad/s)');
title('Part k: Closed-Loop Response');
legend show;

%% Part K (FVT for steady state error)
syms s

P_s = (N*Km_new) / ((J1_new*N^2*L_k+J2_new*L_k)*s^2 + (J1_new*N^2*R_new+J2_new*R_new+B_k*L_k)*s + (B_k*R_new+Kg_new*Km_new*N^2));

R_s = 100/s; % Step input of magnitude 100

fprintf('\n--- Symbolic Steady-State Error Analysis ---\n');

for Kp = [1, 10, 100]
    % Define the Error Transfer Function E(s) = R(s) - Y(s)
    % For unity feedback: E(s) = R(s) * (1 / (1 + Kp*P(s)))
    E_s = R_s * (1 / (1 + Kp * P_s));
    
    % 3. Apply Final Value Theorem: ess = lim(s->0) s * E(s)
    ess_expr = s * E_s;
    ess_val = subs(ess_expr, s, 0); % Substitute s = 0
    
    % Convert from symbolic to double for printing
    fprintf('For Kp = %d, ess = %.4f rad/s\n', Kp, double(ess_val));
end