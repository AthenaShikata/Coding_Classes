function [p1, f1, p2, f2] = myCurveFitting(x, y)
p1 = polyfit(x, y, 1);
f1 = polyval(p1, x);
p2 = polyfit(x, y, 2);
f2 = polyval(p2, x);
plot(x, y, 'ro-', x, f1, 'g--', x, f2, 'k-.')
title('Curve Fitting Results')
xlabel('x values')
ylabel('y values')
legend('Data points','Linear fit','Quadratic fit')
end
