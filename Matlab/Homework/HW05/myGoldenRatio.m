function [G] = myGoldenRatio(n)
    % Base case: for n = 1, G(1) = 1
    if n == 1
        G = 1;
    else
        % Recursive case: G(n) = 1 + 1 / G(n-1)
        G = 1 + 1 / myGoldenRatio(n-1);
    end
end
