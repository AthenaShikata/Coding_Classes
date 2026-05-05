function [years] = mySavingPlan(P0, i, goal) 
    P = P0;
    years = 0;
    while P < goal
        years = years + 1;
        P = P*(1+i);
    end
end