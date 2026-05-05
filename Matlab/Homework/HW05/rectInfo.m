function [area, perimeter] = rectInfo(w, l)
    % Check if the user has provided both width and length
    if nargin < 2
        % If not, set area and perimeter to -1
        area = -1;
        perimeter = -1;
    else
        % Otherwise, calculate area and perimeter
        area = w * l;
        perimeter = 2 * (w + l);
    end
end
