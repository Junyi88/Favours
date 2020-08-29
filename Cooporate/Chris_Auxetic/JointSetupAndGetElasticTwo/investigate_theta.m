clear;

% theta = arctan(2*h/L)

Hp=17.5;
hp=5.5;
HH = Hp-hp;
L=11.5;
thickness = 1.15;

Theta = linspace(15, 60, 601);

%%
YMx_n = zeros(length(Theta), 1);
YMy_n = zeros(length(Theta), 1);
YMz_n = zeros(length(Theta), 1);
nuxy_n = zeros(length(Theta), 1);
nuxz_n = zeros(length(Theta), 1);
nuzy_n = zeros(length(Theta), 1);

YMx_s = zeros(length(Theta), 1);
YMy_s = zeros(length(Theta), 1);
YMz_s = zeros(length(Theta), 1);
nuxy_s = zeros(length(Theta), 1);
nuxz_s = zeros(length(Theta), 1);
nuzy_s = zeros(length(Theta), 1);


%%

for n1=1:length(Theta)
    theta = Theta(n1);
    h = tand(theta) * L./2;
    H = HH + h;
    [ValuesNoStrut, ValuesStrut] = get_single_youngs(H, h, L, thickness, theta);
    
    
    YMx_n(n1) = ValuesNoStrut.YMx;
    YMy_n(n1) = ValuesNoStrut.YMy;
    YMz_n(n1) = ValuesNoStrut.YMz;
    nuxy_n(n1) = ValuesNoStrut.nuxy;
    nuxz_n(n1) = ValuesNoStrut.nuxz;
    nuzy_n(n1) = ValuesNoStrut.nuzy;

    YMx_s(n1) = ValuesStrut.YMx;
    YMy_s(n1) = ValuesStrut.YMy;
    YMz_s(n1) = ValuesStrut.YMz;
    nuxy_s(n1) = ValuesStrut.nuxy;
    nuxz_s(n1) = ValuesStrut.nuxz;
    nuzy_s(n1) = ValuesStrut.nuzy;
    
end

%%
figure(1);
clf;
plot(Theta, YMx_n, 'b-')

figure(2);
clf;
plot(Theta, nuzy_n, 'b-')
