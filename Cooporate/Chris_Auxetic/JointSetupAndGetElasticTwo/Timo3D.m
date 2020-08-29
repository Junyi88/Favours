function [K]=Timo3D(Pr)

%%
% F=[Fx1 Fy1 Fz1 Mx1 My1 Mz1, Fx2 Fy2 Fz2 Mx2 My2 Mz2].';
% u=[ux1 uy1 uz1 ux1 uy1 uz1, thx2 thy2 thz2 thx2 thy2 thz2].';


%%
K=zeros(12,12); 


%% Deal with axial (easiest)
[Kax]=KAxial(Pr);
[KTimZ]=KTimoZ(Pr);
[KTimY]=KTimoY(Pr);
[KTr]=KTor(Pr);

%% Sort into Big matrix

% Axial
XRow=[1 7]; 
XCol=[1 7 13];
[LRow,LCol]=size(Kax);
for nRow=1:LRow
    for nCol=1:LCol
        
        NRow=XRow(nRow);
        NCol=XCol(nCol);
        
        K(NRow,NCol)=Kax(nRow,nCol);
        
    end
end

% Torsion
XRow=[4 10]; 
XCol=[4 10];
[LRow,LCol]=size(KTr);
for nRow=1:LRow
    for nCol=1:LCol
        
        NRow=XRow(nRow);
        NCol=XCol(nCol);
        
        K(NRow,NCol)=KTr(nRow,nCol);        
    end
end

% F=[Fx1 Fy1 Fz1 Mx1 My1 Mz1, Fx2 Fy2 Fz2 Mx2 My2 Mz2].';
% u=[ux1 uy1 uz1 ux1 uy1 uz1, thx2 thy2 thz2 thx2 thy2 thz2 DT].';

% Bending Z
XRow=[2 6 8 12]; 
XCol=[2 6 8 12];
[LRow,LCol]=size(KTimZ);
for nRow=1:LRow
    for nCol=1:LCol
        
        NRow=XRow(nRow);
        NCol=XCol(nCol);
        
        K(NRow,NCol)=KTimZ(nRow,nCol);        
    end
end

% F=[Fx1 Fy1 Fz1 Mx1 My1 Mz1, Fx2 Fy2 Fz2 Mx2 My2 Mz2].';
% u=[ux1 uy1 uz1 ux1 uy1 uz1, thx2 thy2 thz2 thx2 thy2 thz2 DT].';

% Bending Y
XRow=[3 5 9 11]; 
XCol=[3 5 9 11];
[LRow,LCol]=size(KTimZ);
for nRow=1:LRow
    for nCol=1:LCol
        
        NRow=XRow(nRow);
        NCol=XCol(nCol);
        
        K(NRow,NCol)=KTimY(nRow,nCol);        
    end
end
% 
% %% Deal with Full Rotation Matrix
% % Rot.RYZ
% % Rot.RYZI
% R=zeros(12,12); 
% RI=zeros(12,12); 
% for n1=1:4     
%     N1=[3*(n1-1)+1:1:3*n1];
%     R(N1,N1)=Rot.RYZ;
%     RI(N1,N1)=Rot.RYZI;
% end
% 
% if dTFlag==1
%  R(13,13)=Rot.RYZ(1,1);
% %  RI(13,13)=Rot.RYZI(1,1);
%  RI(13,13)=1;
% end
% 
% % Kel=(RI(1:12,1:12))*(K*R);
%  Kel=(R(1:12,1:12))*(K*RI);
% %   Kel=(R.')*(K*R);