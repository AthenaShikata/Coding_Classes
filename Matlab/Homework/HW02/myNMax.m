function [M] = myNMax(A,N) 
    M=[];
    for k=1:N
        M = [M,max(A)];
        A(A == max(A))=[];
    end
end