% MATLAB/Simulink Assignment- Zeshui Song
clear; clc; close all;

% Save cache to the current folder
Simulink.fileGenControl('set', 'CacheFolder', pwd, 'CodeGenFolder', pwd);

% Parameters
m = 3000; 
b = 40e3; 
k = 80.8e5; 
u = 20000; 
%% Part A
% Run simulation
out = sim('Truckmodel', 'StopTime', '2', 'MaxStep', '0.001'); %Stop time of 2 seconds and max step size of 0.001 seconds

t = out.tout;
force = out.applied; 
pos = out.truckpos; 
vel = out.truckvel;

% Plot Results
sgtitle('2a: Truck Response to Force Input u_1(t)');

% Plot 1: Input Force u(t)
subplot(3,1,1);
plot(t, force, 'b', 'LineWidth', 1.5);
title('Input Force u_1(t)');
ylabel('Force (N)');
grid on;

% Plot 2: Displacement
subplot(3,1,2);
plot(t, pos, 'b', 'LineWidth', 1.5);
title('Truck Displacement');
ylabel('Position (m)');
grid on;

% Plot 3: Velocity
subplot(3,1,3);
plot(t, vel, 'b', 'LineWidth', 1.5);
title('Truck Velocity');
xlabel('Time (s)');
ylabel('Velocity (m/s)');
grid on;

fprintf('Max Displacement: %.4f meters\n', max(pos));

%% Part B
b_B  = 2*sqrt(m*k); % Critical damping coefficient
fprintf('Critical Damping Coefficient: %.2f kg/s\n', b_B);

%% Part C:
b_values = [40e2, 40e3, 40e4, 40e5]; % Different damping coefficients to compare
colors = ['r', 'b', 'g', 'k']; 

for i = 1:length(b_values)
    % Update the damping coefficient for this iteration 
    b = b_values(i);
    
    % Run simulation
    out = sim('Truckmodel', 'StopTime', '5', 'MaxStep', '0.001'); 
    
    % Plot 1: Input Force (u)
    subplot(2,1,1);
    plot(out.tout, out.applied, colors(i), 'LineWidth', 1.5);
    hold on;
    title('Input Force u(t)');
    ylabel('Force (N)');
    grid on;

    % Plot 2: Displacement
    subplot(2,1,2);
    plot(out.tout, out.truckpos, colors(i), 'LineWidth', 1.5);
    hold on;
    title('Truck Displacement comparison ');
    xlabel('Time (s)');
    ylabel('Position (m)');
    grid on;
end

sgtitle('Part 2c: Comparison of Truck Displacement for Different Damping Coefficients');

subplot(2,1,2);
legend('b = 40e2 kg/s', 'b = 40e3 kg/s', 'b = 40e4 kg/s', 'b = 40e5 kg/s');

hold off;

%% Part D
% Parameters
m = 3000; 
b = 40e3; 
k = 80.8e5;         
x_int = 0.01;          % Initial displacement (m) 

% Run simulation
outD = sim('Truckmodel', 'StopTime', '2', 'MaxStep', '0.001');

% Extract data
t_d = outD.tout;
pos_d = outD.truckpos; % Displacement from To Workspace block
vel_d = outD.truckvel; % Velocity from To Workspace block

% Plotting
figure;
subplot(2,1,1);
plot(t_d, pos_d, 'b', 'LineWidth', 1.5);
title('Displacement Free Response (Initial x = 0.01m)');
ylabel('Displacement (m)');
grid on;

subplot(2,1,2);
plot(t_d, vel_d, 'r', 'LineWidth', 1.5);
title('Velocity Free Response (Initial v = 0)');
xlabel('Time (s)');
ylabel('Velocity (m/s)');
grid on;
sgtitle('Part 2d: Free Response of the Truck with Initial Displacement');