function [h] = mySplitFunction(f, g, a, b, x)
    % If x <= a, return f(x)
    if x <= a
        h = f(x);
    % If x >= b, return g(x)
    elseif x >= b
        h = g(x);
    % Otherwise, return 0
    else
        h = 0;
    end
end