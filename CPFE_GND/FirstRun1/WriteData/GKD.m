clear;
F=dlmread('name.txt');

for n1=1:size(F,1)
figure(1);
clf;
hold on;
plot(F(n1,2:end),'r-')
title(F(n1,1));
pause(0.01);
end