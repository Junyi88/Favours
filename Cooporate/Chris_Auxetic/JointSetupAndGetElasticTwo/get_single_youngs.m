function [ValuesNoStrut, ValuesStrut] =  get_single_youngs(H, h, L, thickness, theta)



% H=17.5;
% h=5.5;
% L=11.5;
% thickness = 1.15;


%%
Pr.Mt.YM=200e3;
Pr.Mt.nu=0.3;
Pr.Mt.YS=595;
Pr.Mt.rho=(7850./1000).*((1e-3).^3);

% Pr.Mt.YM=110e3;
% Pr.Mt.nu=0.33;
% Pr.Mt.YS=595;
% Pr.Mt.rho=(4430./1000).*((1e-3).^3);

%%

Pr.Ge.r=thickness;
Pr.Mt.G=Pr.Mt.YM./(2.*(1+Pr.Mt.nu));
Pr.Ge.kappa=6.*(1+Pr.Mt.nu)./(7+Pr.Mt.nu);

Pr.Ge.Jtor=2.*(Pr.Ge.r.^4)./12;
Pr.Ge.I=(Pr.Ge.r.^4)./12;
Pr.Ge.A=(Pr.Ge.r.^2);


% Pr.Mt.YS=595;
% Pr.Mt.rho=(7850./1000).*((1e-3).^3);
Sc(1).Pr=Pr;

Pr2 = Pr;
rx = thickness .* cosd(theta);
Pr2.Ge.r = rx;
Pr2.Mt.G=Pr2.Mt.YM./(2.*(1+Pr2.Mt.nu));
Pr2.Ge.kappa=6.*(1+Pr2.Mt.nu)./(7+Pr2.Mt.nu);

Pr2.Ge.Jtor=2.*(Pr2.Ge.r.^4)./12;
Pr2.Ge.I=(Pr2.Ge.r.^4)./12;
Pr2.Ge.A=(Pr2.Ge.r.^2);
Pr2.Ge.I=Pr2.Ge.r.*(Pr.Ge.r.^3)./12;
Pr2.Ge.A=(Pr2.Ge.r.*Pr.Ge.r);

Sc(2).Pr=Pr2;

%%
[LattStrut]=GenerateLattice(H,L,h,false,true);
[LattNoStrut]=GenerateLattice(H,L,h,true,true);

[MeshStrut]=ConvertToVigMesh(LattStrut,Pr,Pr2);
[MeshNoStrut]=ConvertToVigMesh(LattNoStrut,Pr,Pr2);

[OutNoStrut]=Vig3DSystemAuxectic(MeshNoStrut,Sc);
[OutStrut]=Vig3DSystemAuxectic(MeshStrut,Sc);

[ValuesNoStrut]=GetYoungsPoisson(OutNoStrut.Eff.KEp);
[ValuesStrut]=GetYoungsPoisson(OutStrut.Eff.KEp);

end

