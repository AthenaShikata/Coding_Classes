function [boundedA] = myBoundingArray(A, top, bottom) 
    boundedA = []
    for k = 1:length(A)
        if A(k) < bottom
            boundedA = [boundedA,bottom];
        elseif A(k) > top
            boundedA = [boundedA,top];
        elseif (A(k) >= bottom) && (A(k) <= top)
            boundedA = [boundedA,A(k)];
        end
    end
end