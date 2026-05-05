function [nRoots, r] = myNRoots(a, b, c)
    % Calculate the discriminant
    discriminant = b^2 - 4*a*c;

    % Check the number of roots based on the discriminant
    if discriminant > 0
        % Two real roots
        nRoots = 2;
        r = [(-b + sqrt(discriminant)) / (2*a), (-b - sqrt(discriminant)) / (2*a)];
    elseif discriminant == 0
        % One real root
        nRoots = 1;
        r = -b / (2*a);
    else
        % Two imaginary roots
        nRoots = -2;
        realPart = -b / (2*a);
        imaginaryPart = sqrt(-discriminant) / (2*a);
        r = [realPart + imaginaryPart*1i, realPart - imaginaryPart*1i];
    end
end