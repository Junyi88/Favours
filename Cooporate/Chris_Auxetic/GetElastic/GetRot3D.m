function [Pr,Rot,L]=GetRot3D(Ps,Pr)

P1=Ps{1};
P2=Ps{2};

N=(P2-P1);

%%
L=sqrt(dot(N.',N));
Pr.Ge.L=L;
N=N./Pr.Ge.L;
Pr.Ge.N=N;

%%

thetaZ=asin(N(2));

cZ=cos(thetaZ);
sZ=sin(thetaZ);

thetaY=atan2(-N(3)./cZ,N(1)./cZ);

Rot.thetaZ=thetaZ;
Rot.thetaY=thetaY;

cY=cos(thetaY);
sY=sin(thetaY);

Rot.RZ=[cZ,-sZ,0;sZ,cZ,0;0,0,1];
Rot.RY=[cY,0,sY;0,1,0;-sY,0,cY];
Rot.RYZ=Rot.RY*Rot.RZ;
Rot.RYZI=inv(Rot.RYZ);

Pr.Ge.Rot=Rot;

end