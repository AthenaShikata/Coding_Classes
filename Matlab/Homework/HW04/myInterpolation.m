function [vq1, vq2] = myInterpolation(x, y)
    xq= -3:0.1:9;
    vq1 = interp1(x,y,xq);
    vq2 = spline(x,y,xq);
    plot(x, y, 'ro-', xq, vq1, 'g--', xq, vq2, 'k-.')
    title('Linear and Cubic Spline Interpolation')
    xlabel('x values')
    ylabel('y values')
    legend('Data points','Linear interpolation','Cubic spline interpolation')
end