function [out] = myIsPrime(n)
    if n > 1
        for i = 2:((n/2)+1)
            if (rem(n,i) == 0) & (n/i ~= 1)
                out = 0;
                break
            else
                out = 1;
            end
        end
    else
        out = 0;
    end
end