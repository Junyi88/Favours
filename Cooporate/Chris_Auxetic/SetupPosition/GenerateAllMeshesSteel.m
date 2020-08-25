clear;

H=17.5;
h=5.5;
L=11.5;
thickness = 1.15;

%%
Pr.Mt.YM=200e3;
Pr.Mt.nu=0.3;

Pr.Ge.r=thickness;
Pr.Mt.G=Pr.Mt.YM./(2.*(1+Pr.Mt.nu));
Pr.Ge.kappa=6.*(1+Pr.Mt.nu)./(7+Pr.Mt.nu);

Pr.Ge.Jtor=2.*(Pr.Ge.r.^4)./12;
Pr.Ge.I=(Pr.Ge.r.^4)./12;
Pr.Ge.A=(Pr.Ge.r.^2);


Pr.Mt.YS=595;
Pr.Mt.rho=(7850./1000).*((1e-3).^3);
Sc(1).Pr=Pr;

%%
[LattStrut]=GenerateLattice(H,L,h,false,true);
[LattNoStrut]=GenerateLattice(H,L,h,true,true);

[MeshStrut]=ConvertToVigMesh(LattStrut,Pr);
[MeshNoStrut]=ConvertToVigMesh(LattNoStrut,Pr);

save TotalMesh316L;
