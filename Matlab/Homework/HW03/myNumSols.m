function [N, x] = myNumSols(A,b) 
    augM = [A b];
    [rowesc,jb] = rref(augM)
    [m, n] = size(A);
    
    if any(jb == n+1) % if pivot in augmented collumn
        N = 0;
    elseif length(jb) ~= n % if no free variables
        N = Inf;
    else % else
        N = 1;
    end

    if N == 0 % no solutions
        x = [];
    elseif N == 1 % one solution
        x = A\b;
    elseif N == Inf % inf solutions
        x = pinv(A)*b;
    end
end