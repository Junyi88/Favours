clear;

% theta = arctan(2*h/L)

H=17.5;
h=5.5;
L=11.5;

Thickness = linspace(0.5, 2.5, 201);

%%
YMx_n = zeros(length(Thickness), 1);
YMy_n = zeros(length(Thickness), 1);
YMz_n = zeros(length(Thickness), 1);
nuxy_n = zeros(length(Thickness), 1);
nuxz_n = zeros(length(Thickness), 1);
nuzy_n = zeros(length(Thickness), 1);

YMx_s = zeros(length(Thickness), 1);
YMy_s = zeros(length(Thickness), 1);
YMz_s = zeros(length(Thickness), 1);
nuxy_s = zeros(length(Thickness), 1);
nuxz_s = zeros(length(Thickness), 1);
nuzy_s = zeros(length(Thickness), 1);


%%

for n1=1:length(Thickness)
    thickness = Thickness(n1);
    [ValuesNoStrut, ValuesStrut] = get_single_youngs(H, h, L, thickness);
    
    
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
plot(Thickness, YMx_n, 'b-')



