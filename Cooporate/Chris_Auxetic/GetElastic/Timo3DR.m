function [K]=Timo3DR(K,Pr)


%% Deal with Full Rotation Matrix
% Rot.RYZ
% Rot.RYZI
R=zeros(12,12); 
RI=zeros(12,12); 
for n1=1:4     
    N1=[3*(n1-1)+1:1:3*n1];
    R(N1,N1)=Pr.Ge.Rot.RYZ;
    RI(N1,N1)=Pr.Ge.Rot.RYZI;
end



 K=(R(1:12,1:12))*(K*RI);

end