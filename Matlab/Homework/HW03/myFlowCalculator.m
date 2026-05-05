function [f] = myFlowCalculator(S, d) 
    % Define how the flow of energy in each node
    b = [S,d];
    b = rot90(b,3);

    % Define the flow of energy in the system
    A = zeros(7);
    A(1,1)=1;
    A(2,4)=1; A(2,5)=1;
    A(3,3)=-1; A(3,4)=1; A(3,6)=-1;
    A(4,5)=1; A(4,7)=-1;
    A(5,2)=1;
    A(6,1)=1; A(6,2)=-1; A(6,3)=1;
    A(7,6)=1; A(7,7)=1;
    
    % myNumSols
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
        f = [];
    elseif N == 1 % one solution
        f = A\b;
    elseif N == Inf % inf solutions
        f = pinv(A)*b;
    end
    f = rot90(f);
end