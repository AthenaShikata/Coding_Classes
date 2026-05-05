function [M] = myCheckerBoard(n) 

    M = zeros(n);
    for i = 1:n
        for j = 1:n
            if (mod(j, 2) == 0) && (mod(i,2) == 0)
                 M(i,j) = 1;
            elseif (mod(j, 2) == 1) && (mod(i,2) == 1)
                M(i,j) = 1;
            end
        end
    end

end