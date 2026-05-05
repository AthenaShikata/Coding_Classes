function [] = myPolyPlotter(n,x)
    y=[];
    for k = 1:n
        y = x.^k; 
        plot(x, y,"b");
        hold on;
    end
    hold off;
    title(sprintf("Polynomials Up To Degree %d",n));
    xlabel('x');
    ylabel('y');
    grid on;
    xlim([min(x) max(x)]);
    ylim([min(y) max(y)]);
    xticks(min(x):.2:max(x));
    yticks(min(y):.2:max(y));
end