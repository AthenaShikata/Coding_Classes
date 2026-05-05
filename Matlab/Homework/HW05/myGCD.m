function [gcd] = myGCD(a, b)
    % Base case: if b is 0, then the GCD is a
    if b == 0
        gcd = a;
    else
        % Recursive case: GCD(a, b) = GCD(b, rem(a, b))
        gcd = myGCD(b, rem(a, b));
    end
end
