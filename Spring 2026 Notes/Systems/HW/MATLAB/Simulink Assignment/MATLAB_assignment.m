% MATLAB/Simulink Assignment- Zeshui Song
clear; clc; close all;

R = 3.3; %omega
L = 0.1; %H
J1 = 9.64 * 10^-6; %kg*m^2
m = 0.033; %kg
r = 0.0242; %m
B = 0.01; %N*m*s
Km = 0.0280; %N*m/A
Kg = 0.0280; %V/(rad/s)
N = 2; % gear ratio
s = tf('s');

%% Find J2
J2 = 1/2 * m * r^2; %kg*m^2

%% Define the transfer function of the system
P_motor = (N*Km)/((J2*L+J1*L*N^2)*s^2+(J2*R+J1*R*N^2+B*L)*s+(B*R+Kg*Km*N^2))

t = 0:0.01:16; %time vector from 0 to 16 secs
u = 10*[0:0.01:16]; %10 V step input from 0 to 16 secs

y = lsim(P_motor,u,t); %simulate the response of the system to the input u over time t

%% Plot the response
plot(t,y);
grid on;
xlabel('Time (s)');
ylabel('Angular Velocity (rad/s)');
title('Response of the Motor to a 10 V Step Input');