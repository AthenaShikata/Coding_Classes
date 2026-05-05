function [out] = myIsOrthogonal(v1,v2, tol)
    format long
    A = norm(v1)
    B = norm(v2)
    dotAB = dot(v1,v2)

    theta = acos(dotAB/(A*B))

    if abs(pi/2 - theta) < tol
        out = 1;
    else
        out = 0;
    end
end