function [Mesh]=GenerateLowCTEMesh(L,theta)

%%
l1=(L./2).*sqrt((3./2).*(tan(theta).^2)+1);
l2=(L./2).*(sqrt(3).*tan(theta)+1);
Mesh.Misc.l1=l1;
Mesh.Misc.l2=l2;

%%
Mesh.Node(10).N=[0;0;0];
Mesh.Node(7).N=[0;0;0];
Mesh.Node(8).N=[0;0;0];
Mesh.Node(9).N=[0;0;0];

Mesh.Node(1).N=[(-l2./2);l2.*sqrt(3)./2;0];
Mesh.Node(2).N=[0;0;0];
Mesh.Node(3).N=[(l2./2);l2.*sqrt(3)./2;0];
Mesh.Node(4).N=[0;2.*sqrt(3).*l2./3 ;sqrt(6).*l2./3];
Mesh.Node(5).N=[(-l2./2);sqrt(3).*l2./6;sqrt(6).*l2./3];
Mesh.Node(6).N=[(l2./2);sqrt(3).*l2./6;sqrt(6).*l2./3];

%
zC=(1./9).*(sqrt(6).*l2-sqrt(9.*l1.*l1-3.*l2.*l2));
Mesh.Node(7).N(3)=zC;
Mesh.Node(8).N(3)=zC;
Mesh.Node(9).N(3)=zC;

Mesh.Node(7).N(2)=(sqrt(3)./27).*(15.*l2+2.*sqrt(6).*sqrt(9.*l1.*l1-3.*l2.*l2));
    
Mesh.Node(8).N(1)=(-sqrt(12.*l1.*l1-3.*l2.*l2-12.*zC.*zC)-l2)./4;
Mesh.Node(9).N(1)=-Mesh.Node(8).N(1);

Mesh.Node(8).N(2)=(3.*l2-sqrt(12.*l1.*l1-3.*l2.*l2-12.*zC.*zC)).*...
    sqrt(3)./12;
Mesh.Node(9).N(2)=Mesh.Node(8).N(2);

Mesh.Node(10).N(2)=sqrt(3).*l2./3;
Mesh.Node(10).N(3)=l2.*sqrt(6)./3+sqrt(9.*l1.*l1-3.*l2.*l2)./3;

%%
Mesh.Element(24).Ps=[6 10];

Mesh.Element(1).Ps=[1 3];
Mesh.Element(2).Ps=[1 2];
Mesh.Element(3).Ps=[2 3];
Mesh.Element(4).Ps=[4 5];
Mesh.Element(5).Ps=[5 6];

Mesh.Element(6).Ps=[4 6];
Mesh.Element(7).Ps=[1 5];
Mesh.Element(8).Ps=[1 4];
Mesh.Element(9).Ps=[2 5];
Mesh.Element(10).Ps=[2 6];

Mesh.Element(11).Ps=[3 4];
Mesh.Element(12).Ps=[3 6];

%
Mesh.Element(13).Ps=[1 7];
Mesh.Element(14).Ps=[3 7];
Mesh.Element(15).Ps=[4 7];

Mesh.Element(16).Ps=[1 8];
Mesh.Element(17).Ps=[5 8];
Mesh.Element(18).Ps=[2 8];

Mesh.Element(19).Ps=[2 9];
Mesh.Element(20).Ps=[3 9];
Mesh.Element(21).Ps=[6 9];

Mesh.Element(22).Ps=[4 10];
Mesh.Element(23).Ps=[5 10];

%%
Mesh.Element(24).Sc=0;
for n1=1:12
   Mesh.Element(n1).Sc=1; 
end
for n1=13:24
   Mesh.Element(n1).Sc=2; 
end

%%
Mesh.Misc.L=L;
Mesh.Misc.theta=theta;



end