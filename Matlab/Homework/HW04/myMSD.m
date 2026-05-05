function [dS] = myMSD(t, S, m, c, k)
x = S(1);
v = S(2);
dx = v;
dv = (-c*v - k*x) / m;
dS = [dx; dv];
end