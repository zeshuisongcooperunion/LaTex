% HW 4 Problem 2B- Zeshui Song
clear; clc; close all;

% Define system parameters
m1 = 1000; % Mass of car (kg)
m2 = 100;  % Mass of tire (kg)
b = 4000;  % Damping coefficient (kg/s)
k1 = 20000; % Suspension stiffness (N/m)

% Define the time vector
t = 0:0.01:16; % (start:step:end) t=0s to 16s with a step of 0.01s makes 1601 points

% Define the triangle bump input u(t)
u1 = [0:0.0001:0.01]; % Step = 0.01m / 100 steps = 0.0001; Increasing from 0m to 0.1m over t=0 to 1s (101 points)        

u2 = [0.0099:-0.0001:-0.01]; % Step = -0.02m / 200 steps = -0.0001; Decreasing from 0.99m down to -0.1m over t=1.01 to 3s (200 points)

u3 = [-0.0099:0.0001:0]; % Step = 0.01m / 100 steps = 0.0001; Increasing from -0.99m back to 0m over t=3.01 to 4s (100 points)   

u4 = 0*[4.01:0.01:16]; % Step = 0.01m / 1200 steps = 0.01; Multiply a time range by 0 to create a flat road over t=4.01s to 16s (1200 points)

u = [u1 u2 u3 u4]; % Combine the piecewise segments into one input vector u

% Loop to run the simulation for each value of k2 (tire stiffness) and plot the results on the same graph
for k2 = [5000, 10000]
    A = [0 0 1 0; 0 0 0 1; -k1/m1 k1/m1 -b/m1 b/m1; k1/m2 -(k1+k2)/m2 b/m2 -b/m2];
    B = [0; 0; 0; k2/m2];
    C = [1 0 0 0]; 
    D = 0;
    
    sys = ss(A,B,C,D); % ss(): 'State-Space' function. 
    
    % lsim(): 'Linear Simulation'. Drives the car model (sys) over the road (u) for the time vector (t) to compute the resulting displacement 'y' of the car's body.
    y = lsim(sys,u,t); 
    
    % plot the displacement of the car's body. hold on allows multiple plots to be shown
    plot(t,y); hold on;
end
plot(t,u,'k--'); % Plot the road input as a dashed black line for reference

grid on; 
xlabel('t (sec)'); 
ylabel('Displacement x_1 (m)'); 
title('Response of Car Body (x_1) to Triangular Road Input');
legend('k_2 = 5000 N/m', 'k_2 = 10000 N/m', 'u'); % Adds labels to the plots in the order they were drawn.