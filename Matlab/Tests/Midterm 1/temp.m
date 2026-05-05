fxn = @(x) x*2
x=linspace(-3, 3, 100)
y=feval(fxn,x)
minx = min(x) 
maxx=max(x)
miny=min(y)
maxy=max(y)
for j = 1:length(x)
    plot(x(j),y(j),'o')
    xlim([-3,3])
    pause(.05)
end