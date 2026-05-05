function [S] = myInsideTriangle(x,y)
if (x + y == 1)
    S = 'border'
elseif (x + y < 1)
    S = 'inside'
elseif (x + y > 1)
    S = 'outside'
end
end