x = linspace(-3,3,20)
y = cos(x)

% red doted line
subplot(3,2,1);xlim([-4,4]);ylim([-1,1]);plot(x,y,":r")
% green line
subplot(3,2,2);xlim([-4,4]);ylim([-1,1]);plot(x,y,"g")
% black circle
subplot(3,2,3);xlim([-4,4]);ylim([-1,1]);plot(x,y,"ko")
% blue stars
subplot(3,2,4);xlim([-4,4]);ylim([-1,1]);plot(x,y,"b pentagram")
% magenta triangles
subplot(3,2,5);xlim([-4,4]);ylim([-1,1]);plot(x,y,"m<")
% cyan dashed line
subplot(3,2,6);xlim([-4,4]);ylim([-1,1]);plot(x,y,"--c")