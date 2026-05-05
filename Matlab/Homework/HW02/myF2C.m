function [TemC] = myF2C(TemF)
    TemC=[]
    for k=1:length(TemF)
        TemC = [TemC,(TemF-32)*(5/9)];
    end
end