function [I] = myNumInt(f, a, b, n, option)
x = linspace(a, b, n);
h = (b - a) / (n - 1);
switch option
    case 'left'
        I = sum(f(x(1:end-1))) * h;
    case 'right'
        I = sum(f(x(2:end))) * h;
    case 'middle'
        xm = (x(1:end-1) + x(2:end)) / 2;
        I = sum(f(xm)) * h;
    case 'trap'
        I = (f(a) + f(b) + 2*sum(f(x(2:end-1)))) * h / 2;
end
end
