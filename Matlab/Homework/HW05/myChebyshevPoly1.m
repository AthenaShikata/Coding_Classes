function [y] = myChebyshevPoly1(n, x)
    % Initialize the first two Chebyshev polynomials
    T0 = 1;  % T0(x) = 1
    T1 = x;  % T1(x) = x
    
    % For n = 0 or n = 1, return the corresponding Chebyshev polynomial
    if n == 0
        y = T0 * ones(size(x));  % T0(x) = 1 for all x
    elseif n == 1
        y = T1;  % T1(x) = x
    else
        % For n > 1, use the recurrence relation to calculate the nth Chebyshev polynomial
        Tn_2 = T0;  % T(n-2)
        Tn_1 = T1;  % T(n-1)
        
        for k = 2:n
            % Recurrence relation: Tn(x) = 2*x*T(n-1)(x) - T(n-2)(x)
            Tn = 2 * x .* Tn_1 - Tn_2;
            % Update for the next iteration
            Tn_2 = Tn_1;
            Tn_1 = Tn;
        end
        
        % Return the nth Chebyshev polynomial
        y = Tn;
    end
end
