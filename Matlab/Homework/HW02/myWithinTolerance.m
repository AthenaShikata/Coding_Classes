function [indices] = myWithinTolerance(A, a, tol) 
    indices = []
    for k = 1:length(A)
        if abs(A(k)-a) < tol
            indices = [indices,k];
        end
    end
end