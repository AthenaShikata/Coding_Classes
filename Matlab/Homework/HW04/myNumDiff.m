function [dy, X] = myNumDiff(f, a, b, n, option) 
    x = linspace(a, b, n);
    h = x(2) - x(1);
    switch option
        case 'forward'
            dy = (f(x(2:end)) - f(x(1:end-1))) / h;
            X = x(1:end-1);
        case 'backward'
            dy = (f(x(2:end)) - f(x(1:end-1))) / h;
            X = x(2:end);
        case 'central'
            dy = (f(x(3:end)) - f(x(1:end-2))) / (2*h);
            X = x(2:end-1);
    end
end