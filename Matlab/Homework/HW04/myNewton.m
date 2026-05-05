function [R, E] = myNewton(f, df, x0, tol)
R = x0;
E = abs(f(x0));
while E(end) >= tol
    x0 = x0 - f(x0)/df(x0);
    R(end+1) = x0;
    E(end+1) = abs(f(x0));
end
end