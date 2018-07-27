function [Out]=Vig3DSystemLowCTE(Mesh,Kg,Sc)

Out=[];
%% Rearrange Nodes
ReN.Nref=Mesh.Node(8).N;
ReN.a1=Mesh.Node(9).N-Mesh.Node(8).N;
ReN.a2=Mesh.Node(7).N-Mesh.Node(8).N;
ReN.a3=Mesh.Node(10).N-Mesh.Node(8).N;

for n1=1:length(Mesh.Node)
    Mesh.Node(n1).N=Mesh.Node(n1).N-ReN.Nref;
end
ReN.a1b=Mesh.Node(9).N-Mesh.Node(8).N;
ReN.a2b=Mesh.Node(7).N-Mesh.Node(8).N;
ReN.a3b=Mesh.Node(10).N-Mesh.Node(8).N;

%% Get GlobalStiffnessMatrix
[Kuc,Mesh]=GlobalTimoLattice3D(Mesh,Sc);

%% Obtaining Independence Relationship

Rel.In=[1:6,8].';
Rel.De.d=[7;9;10];
Rel.De.R=[8;8;8];
Rel.De.a=[0 1 0;1 0 0;0 0 1];
Rel.a{1}=ReN.a1;
Rel.a{2}=ReN.a2;
Rel.a{3}=ReN.a3;

Ls.Nodes=length(Mesh.Node);
Ls.IdNodes=length(Rel.In);
Ls.DeNodes=length(Rel.De.d);
Ls.DoF=6;
Ls.DoFxy=3;
Ls.a=length(Rel.a);
Ls.Ntheta=3;

%% Calculate B0,Ba
Is=eye(Ls.DoF); Ia=eye(Ls.DoFxy);
% Os=zeros(Ls.DoF); Oa=zeros(Ls.DoFxy);

B0=zeros(Ls.DoF.*Ls.Nodes,Ls.DoF.*Ls.IdNodes);
Ba=zeros(Ls.DoF.*Ls.Nodes,Ls.DoFxy.*Ls.a);
for n1=1:Ls.Nodes
    N1start=Ls.DoF.*(n1-1)+1;
    N1end=Ls.DoF.*n1;
    
    if isempty(find(Rel.In==n1,1))~=1
        n2=find(Rel.In==n1,1);
        N2start=Ls.DoF.*(n2-1)+1;
        N2end=Ls.DoF.*n2;
        
        B0(N1start:N1end,N2start:N2end)=Is;
    else
        n2R=find(Rel.De.d==n1,1);
        n2=find(Rel.In==Rel.De.R(n2R),1);
        
        N2start=Ls.DoF.*(n2-1)+1;
        N2end=Ls.DoF.*n2;
        
        B0(N1start:N1end,N2start:N2end)=Is;
        
        %%
        for n3=1:Ls.a
            
            if Rel.De.a(n2R,n3)==1
            N2start=Ls.DoFxy.*(n3-1)+1;
            N2end=Ls.DoFxy.*n3;
            Ba(N1start:N1end-Ls.Ntheta,N2start:N2end)=Ia;
            end
            
        end
        
    end
    
end

%% Get Volume
Volume=dot(Rel.a{1},cross(Rel.a{2},Rel.a{3}));

%% Get BEp
BEp=zeros(Ls.DoFxy.*Ls.a,Ls.DoF);
for n1=1:Ls.a
%     B=[...
%         Rel.a{n1}(1),0,0,0,Rel.a{n1}(3)./2,Rel.a{n1}(2)./2;...
%         0,Rel.a{n1}(2),0,Rel.a{n1}(3)./2,0,Rel.a{n1}(1)./2;...
%         0,0,Rel.a{n1}(3),Rel.a{n1}(2)./2,Rel.a{n1}(1)./2,0 ...
%         ];
%     B=[...
%         Rel.a{n1}(1),0,0,   0,0,0;...
%         0,Rel.a{n1}(2),0,   0,0,0;...
%         0,0,Rel.a{n1}(3),   0,0,0 ...
%         ];
    B=[...
        Rel.a{n1}(1),0,0,   Rel.a{n1}(2)./2,0, Rel.a{n1}(3)./2;...
        0,Rel.a{n1}(2),0,   Rel.a{n1}(1)./2, Rel.a{n1}(3)./2,0;...
        0,0,Rel.a{n1}(3),   0, Rel.a{n1}(2)./2, Rel.a{n1}(1)./2 ...
        ];
    N1start=Ls.DoFxy.*(n1-1)+1;
    N1end=Ls.DoFxy.*n1;
    N2start=1;
    N2end=Ls.DoF;
    
    BEp(N1start:N1end,N2start:N2end)=B;
end


%% Find Ds

D0back=(B0.')*(Kuc*Ba);
D0front=pinv((B0.')*(Kuc*B0));
D0=-D0front*D0back;
Da=B0*D0+Ba;

Kda=Da.'*(Kuc*Da);
KEp=(BEp.')*(Kda*BEp)./Volume;

%% Outputs
% Out.Eff.Kuc6=Kuc6;
Out.Eff.Kuc=Kuc;
Out.Eff.B0=B0;
Out.Eff.Ba=Ba;
Out.Eff.BEp=BEp;

Out.Eff.D0=D0;
Out.Eff.Da=Da;

Out.Eff.Kda=Kda;
Out.Eff.KEp=KEp;
Out.Eff.Volume=Volume;

Out.Mesh=Mesh;

Out.Rel=Rel;
Out.Ls=Ls;

%% Check 
% Ye=[37:60];
% Na=[1:36];
% KSim=Kuc(Ye,Ye)-Kuc(Ye,Na)*(Kuc(Na,Na)\Kuc(Na,Ye));

end