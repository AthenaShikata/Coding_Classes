function y = myFilterMatrix(x, b) 
    
    indices = x>b;
    y = x(indices);

end