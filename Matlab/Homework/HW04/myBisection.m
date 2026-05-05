function [R, E] = myBisection(f, a, b, tol) 

R = [];
E = [];
while true
    c = (a + b) / 2;
    R(end+1) = c;
    E(end+1) = abs(f(c));
    if E(end) < tol
        break
    end
end
end