function [tip] = myTipCalc(bill, party)
if ( party < 6)
    tip = .15*bill
elseif (party < 8)
    tip = .18*bill
elseif (party < 11)
    tip = .20*bill
else
    tip = .25*bill
end