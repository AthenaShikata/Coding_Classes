function [response] = mySpeedAlarm(S1, S2,S3) 
    
    if abs(S1-S2) > 10
        response ="alarm!";
    elseif abs(S1-S3) > 10
        response ="alarm!";
    elseif abs(S2-S3) > 10
        response ="alarm!";
    else
        response = "normal";
    end
end