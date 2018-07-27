clear;

%%
Pr.Mt.YM=115e3;
Pr.Mt.nu=0.33;

Pr.Ge.r=1.15;
Pr.Mt.G=Pr.Mt.YM./(2.*(1+Pr.Mt.nu));
Pr.Ge.kappa=6.*(1+Pr.Mt.nu)./(7+Pr.Mt.nu);

Pr.Ge.Jtor=2.*(Pr.Ge.r.^4)./12;
Pr.Ge.I=(Pr.Ge.r.^4)./12;
Pr.Ge.A=(Pr.Ge.r.^2);


Pr.Mt.YS=1119;
Pr.Mt.rho=(4430./1000).*((1e-3).^3);
Sc(1).Pr=Pr;

%%

Mesh.Node(1).N=[0;0;0];
Mesh.Node(2).N=[1;0;0];
Mesh.Node(3).N=[0;1;0];
Mesh.Node(4).N=[0;0;1];

Mesh.Element(1).Ps=[1 2];
Mesh.Element(2).Ps=[1 3];
Mesh.Element(3).Ps=[1 4];

Mesh.Element(1).Sc=1;
Mesh.Element(2).Sc=1;
Mesh.Element(3).Sc=1;

Mesh.El(1).Pr=Pr;
Mesh.El(2).Pr=Pr;
Mesh.El(3).Pr=Pr;

%%
St.a1=[1;0;0];
St.a2=[0;1;0];
St.a3=[0;0;1];
St.IND=[1];
St.Dependency=[2 1;3 1;4 1];
St.AType=[1 0 0;0 1 0;0 0 1];

[Out]=Vig3DSystemGen(Mesh,Sc,St);

%%
Mesh.Node(1).N=[0;0;0];
Mesh.Node(2).N=[1;0;0];
Mesh.Node(3).N=[0;1;0];
Mesh.Node(4).N=[0;0;1];

Mesh.Element(1).Ps=[1 2];
Mesh.Element(2).Ps=[1 3];
Mesh.Element(3).Ps=[1 4];

Mesh.Element(1).Sc=1;
Mesh.Element(2).Sc=1;
Mesh.Element(3).Sc=1;

Mesh.El(1).Pr=Pr;
Mesh.El(2).Pr=Pr;
Mesh.El(3).Pr=Pr;





