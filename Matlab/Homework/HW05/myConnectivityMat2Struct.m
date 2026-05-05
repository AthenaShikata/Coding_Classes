function [node] = myConnectivityMat2Struct(C, names)
    % Initialize the output struct array
    n = length(names); % Number of points (nodes)
    node = struct('name', cell(1, n), 'neighbors', cell(1, n));
    
    % Populate the struct array
    for i = 1:n
        node(i).name = names{i}; % Set the name
        node(i).neighbors = find(C(i, :) == 1); % Find indices where C(i, j) = 1
    end
end