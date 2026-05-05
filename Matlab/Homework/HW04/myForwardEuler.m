function [T, S] = myForwardEuler(dS, tSpan, S0)
T = tSpan(:);
S = zeros(length(T),1);
S(1) = S0;
for i = 2:length(T)
    h = T(i) - T(i-1);
    S(i) = S(i-1) + h * dS(T(i-1), S(i-1));
end
end
