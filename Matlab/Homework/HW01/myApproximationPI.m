function [mypi] = myApproximationPI(N)
format long
totalSum = 0;
for k = 0:N
    totalSum = totalSum + ((factorial(4*k))*(1103+26390*k))/(((factorial(k))^4)*(396^(4*k)));
end
mypi = ((2*sqrt(2)/9801)*totalSum)^(-1);
end 