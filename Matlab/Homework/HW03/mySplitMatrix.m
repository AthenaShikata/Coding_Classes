function [M1,M2] = mySplitMatrix(M) 

    [rows collumns] = size(M)
    M1 = M(:,1:ceil(collumns/2))
    M2 = M(:,ceil(collumns/2)+1:end)

end