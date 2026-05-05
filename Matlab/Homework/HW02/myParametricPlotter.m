function [] = myParametricPlotter(x,y,t)
    X = x(t);
    Y = y(t);
    plot3(X,Y,t,'b')
    title('My Parametric Plot');
    xlabel('x');
    ylabel('y');
    zlabel('t');
end