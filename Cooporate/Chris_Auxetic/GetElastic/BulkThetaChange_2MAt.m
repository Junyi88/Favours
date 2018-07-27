clear;

Pr1.Mt.YM=69.16e3;
Pr1.Mt.nu=0.33;

Pr1.Ge.r=0.75;
Pr1.Mt.G=Pr1.Mt.YM./(2.*(1+Pr1.Mt.nu));
Pr1.Ge.kappa=6.*(1+Pr1.Mt.nu)./(7+Pr1.Mt.nu);

Pr1.Ge.Jtor=pi.*(Pr1.Ge.r.^4)./2;

Pr1.Ge.I=pi.*(Pr1.Ge.r.^4)./4;
Pr1.Ge.A=pi.*(Pr1.Ge.r.^2);
Pr1.Mt.YS=276;
Pr1.Mt.rho=(2700./1000).*((1e-3).^3);

Sc(1).Pr=Pr1;

%%
Pr2.Mt.YM=115e3;
Pr2.Mt.nu=0.33;

Pr2.Ge.r=0.75;
Pr2.Mt.G=Pr2.Mt.YM./(2.*(1+Pr2.Mt.nu));
Pr2.Ge.kappa=6.*(1+Pr2.Mt.nu)./(7+Pr2.Mt.nu);

Pr2.Ge.Jtor=pi.*(Pr2.Ge.r.^4)./2;

Pr2.Ge.I=pi.*(Pr2.Ge.r.^4)./4;
Pr2.Ge.A=pi.*(Pr2.Ge.r.^2);
Pr2.Mt.YS=1119;
Pr2.Mt.rho=(4430./1000).*((1e-3).^3);
Sc(2).Pr=Pr2;
l=26; 

Theta=linspace(0,60,121);
LTheta=length(Theta);
%%
BC=zeros(60,2);

BC(:,2)=1;

for n1=37:60
    BC(n1,:)=[0 2];
end

BC(57,:)=[-1.0 2];

%%
Mass=zeros(1,LTheta);
Volume=zeros(1,LTheta);
Density=zeros(1,LTheta);

Elastic=zeros(9,LTheta);

Epp=zeros(6,LTheta);
YieldF=zeros(24,LTheta);
BuckF=zeros(24,LTheta);

YieldS=zeros(1,LTheta);
BuckS=zeros(1,LTheta);
BuckSF=zeros(1,LTheta);

YieldEp=zeros(1,LTheta);
BuckEp=zeros(1,LTheta);
BuckFEp=zeros(1,LTheta);

YieldLoc=zeros(1,LTheta);
BuckLoc=zeros(1,LTheta);
BuckLocF=zeros(1,LTheta);

count=0;
for nTheta=1:LTheta
    
    theta=Theta(nTheta)./180.*pi;
    [Mesh]=GenerateLowCTEMesh(l,theta);
    [Kg,Mesh]=GlobalTimoLattice3D(Mesh,Sc);
    [Vig]=Vig3DSystemLowCTE(Mesh,Kg,Sc);
    [UniSt]=CalculateUniAxStrengthVig(Vig,100);
    
    Mass(nTheta)=(pi.*(Pr1.Ge.r.^2)).*(12.*(Pr1.Mt.rho.*Mesh.Misc.l1+Pr2.Mt.rho.*Mesh.Misc.l2));
    Volume(nTheta)=Vig.Eff.Volume;
    Density(nTheta)=Mass(nTheta)./Volume(nTheta);

    Elastic(1,nTheta)=Vig.Eff.KEp(1,1);
    Elastic(2,nTheta)=Vig.Eff.KEp(2,2);
    Elastic(3,nTheta)=Vig.Eff.KEp(3,3);
    Elastic(4,nTheta)=Vig.Eff.KEp(4,4);
    Elastic(5,nTheta)=Vig.Eff.KEp(5,5);
    Elastic(6,nTheta)=Vig.Eff.KEp(6,6);
    Elastic(7,nTheta)=Vig.Eff.KEp(1,2);
    Elastic(8,nTheta)=Vig.Eff.KEp(1,3);
    Elastic(9,nTheta)=Vig.Eff.KEp(2,3);
 
    Epp(:,nTheta)=UniSt.Misc.Ep;

    YieldS(nTheta)=UniSt.Fail.Yield.Stress;
    BuckS(nTheta)=UniSt.Fail.Buck.Stress;
    BuckSF(nTheta)=UniSt.Fail.BuckF.Stress;
    
    YieldLoc(nTheta)=UniSt.Fail.Yield.Loc;
    BuckLoc(nTheta)=UniSt.Fail.Buck.Loc;
    BuckLocF(nTheta)=UniSt.Fail.BuckF.Loc;
    
    disp(nTheta);
    
    count=count+1;
    if count==10
       save temp1;
       count=0;
    end
    
end

save BulkThetaChange1_2Mat.mat;