% Parameters
wn = 12;
T = 0.5;

% Transfer Function: T(s) = (144*0.5s + 144) / (s^2 + 72s + 144)
num = [wn^2*T, wn^2];    
den = [1, wn^2*T, wn^2]; 
sys = tf(num, den);

% Define time vector
t = 0:0.005:1.5; 

% Generate responses
[y_step, t] = step(sys, t);
[y_impulse, t] = impulse(sys, t);
u_ramp = t;
[y_ramp, t] = lsim(sys, u_ramp, t);

figure('Name', 'Satellite Altitude Control Responses');

% Unit-Step Response
subplot(3,1,1);
plot(t, y_step, 'b', 'LineWidth', 2);
title('Unit-Step Response');
ylabel('Amplitude');
grid on;

% Unit-Impulse Response
subplot(3,1,2);
plot(t, y_impulse, 'r', 'LineWidth', 2);
title('Unit-Impulse Response');
ylabel('Amplitude');
grid on;

% Unit-Ramp Response
subplot(3,1,3);
plot(t, y_ramp, 'g', 'LineWidth', 2);
title('Unit-Ramp Response');
xlabel('Time (sec)');
ylabel('Amplitude');
grid on;