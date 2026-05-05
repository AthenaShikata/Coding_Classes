function [a, b, c] = myVariableTracker3(x, y, z)
a = x - y;
b = a + z;
c = a + b;
c = c + 2;
end