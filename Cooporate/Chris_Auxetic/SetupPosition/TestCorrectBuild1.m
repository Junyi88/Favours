clear;

%%
% This is the one with the extra struts

H=17.5;
h=5.5;
L=11.5;

%% Setup first system

Latt.Prep.H=H;
Latt.Prep.h=h;
Latt.Prep.L=L;

Latt.Prep.x=[-L -L./2 0 L./2 L].';
Latt.Prep.y=[-L -L./2 0 L./2 L].';
Latt.Prep.z=[-(H-h) -H./2 h-H./2 H./2-h H./2 H-h].';

Latt.Prep.XCoord=zeros(5,5,6);
Latt.Prep.YCoord=zeros(5,5,6);
Latt.Prep.ZCoord=zeros(5,5,6);
Latt.Prep.Phit=false(5,5,6);
Latt.Prep.PMap=zeros(5,5,6);
Latt.Prep.XLType=[2 1 2 1 2].';

Latt.Prep.LayerHit(1).Mp=false(5,6);
Latt.Prep.LayerHit(1).Mp([1 3 5],1)=true;
Latt.Prep.LayerHit(1).Mp([2 4],2)=true;
Latt.Prep.LayerHit(1).Mp([1 3 5],3)=true;
Latt.Prep.LayerHit(1).Mp([1 3 5],4)=true;
Latt.Prep.LayerHit(1).Mp([2 4],5)=true;
Latt.Prep.LayerHit(1).Mp([1 3 5],6)=true;

Latt.Prep.LayerHit(2).Mp=false(5,6);
Latt.Prep.LayerHit(2).Mp([2 4],1)=true;
Latt.Prep.LayerHit(2).Mp([1 3 5],2)=true;
Latt.Prep.LayerHit(2).Mp([2 4],3)=true;
Latt.Prep.LayerHit(2).Mp([2 4],4)=true;
Latt.Prep.LayerHit(2).Mp([1 3 5],5)=true;
Latt.Prep.LayerHit(2).Mp([2 4],6)=true;
Latt.Prep.NodePoints=zeros(74,3);
nNodes=0;

for nx=1:5   
    nType=Latt.Prep.XLType(nx);
    for ny=1:5
        for nz=1:6
            Latt.Prep.XCoord(ny,nx,nz)=Latt.Prep.x(nx);
            Latt.Prep.YCoord(ny,nx,nz)=Latt.Prep.y(ny);
            Latt.Prep.ZCoord(ny,nx,nz)=Latt.Prep.z(nz);
            
            Latt.Prep.Phit(ny,nx,nz)=Latt.Prep.LayerHit(nType).Mp(ny,nz);
            
            if (Latt.Prep.Phit(ny,nx,nz))
                nNodes=nNodes+1;
                Latt.Prep.NodePoints(nNodes,:)=[ny,nx,nz];
                Latt.Prep.PMap(ny,nx,nz)=nNodes;
            end
            
        end
    end
end

%%
Latt.Nodes=zeros(size(Latt.Prep.NodePoints,1),3);
for nNodes=1:size(Latt.Prep.NodePoints,1)
    ny=Latt.Prep.NodePoints(nNodes,1);
    nx=Latt.Prep.NodePoints(nNodes,2);
    nz=Latt.Prep.NodePoints(nNodes,3);
    Latt.Nodes(nNodes,:)=[Latt.Prep.XCoord(ny,nx,nz),...
        Latt.Prep.YCoord(ny,nx,nz),Latt.Prep.ZCoord(ny,nx,nz)];
end

%% Now for Beams
Latt.Prep.Layer(1).Struts=zeros(16,2);
Latt.Prep.Layer(1).ExtraStrut=false(16,1);
Latt.Prep.Layer(1).EdgeStrut=false(16,1);

Latt.Prep.Layer(1).ExtraStrut([8,9])=true;
Latt.Prep.Layer(1).EdgeStrut([3,16])=true;

Latt.Prep.Layer(1).Struts(1,:)=sort([1 6]);
Latt.Prep.Layer(1).Struts(2,:)=sort([2 7]);
Latt.Prep.Layer(1).Struts(3,:)=sort([3 8]);
Latt.Prep.Layer(1).Struts(4,:)=sort([6 4]);
Latt.Prep.Layer(1).Struts(5,:)=sort([4 7]);
Latt.Prep.Layer(1).Struts(6,:)=sort([7 5]);
Latt.Prep.Layer(1).Struts(7,:)=sort([5 8]);
Latt.Prep.Layer(1).Struts(8,:)=sort([4 12]);
Latt.Prep.Layer(1).Struts(9,:)=sort([5 13]);
Latt.Prep.Layer(1).Struts(10,:)=sort([9 12]);
Latt.Prep.Layer(1).Struts(11,:)=sort([10 12]);
Latt.Prep.Layer(1).Struts(12,:)=sort([10 13]);
Latt.Prep.Layer(1).Struts(13,:)=sort([13 11]);
Latt.Prep.Layer(1).Struts(14,:)=sort([9 14]);
Latt.Prep.Layer(1).Struts(15,:)=sort([10 15]);
Latt.Prep.Layer(1).Struts(16,:)=sort([11 16]);

Latt.Prep.Layer(1).ConnectStruts=[4 5 6 7 10 11 12 13];

Latt.Prep.Layer(1).NMap=zeros(16,2);
Latt.Prep.Layer(1).NMap(1,:)=[1,1];
Latt.Prep.Layer(1).NMap(2,:)=[3,1];
Latt.Prep.Layer(1).NMap(3,:)=[5,1];
Latt.Prep.Layer(1).NMap(4,:)=[2,2];
Latt.Prep.Layer(1).NMap(5,:)=[4,2];
Latt.Prep.Layer(1).NMap(6,:)=[1,3];
Latt.Prep.Layer(1).NMap(7,:)=[3,3];
Latt.Prep.Layer(1).NMap(8,:)=[5,3];
Latt.Prep.Layer(1).NMap(9,:)=[1,4];
Latt.Prep.Layer(1).NMap(10,:)=[3,4];
Latt.Prep.Layer(1).NMap(11,:)=[5,4];
Latt.Prep.Layer(1).NMap(12,:)=[2,5];
Latt.Prep.Layer(1).NMap(13,:)=[4,5];
Latt.Prep.Layer(1).NMap(14,:)=[1,6];
Latt.Prep.Layer(1).NMap(15,:)=[3,6];
Latt.Prep.Layer(1).NMap(16,:)=[5,6];



% --
Latt.Prep.Layer(2).Struts=zeros(15,2);
Latt.Prep.Layer(2).ExtraStrut=false(15,1);
Latt.Prep.Layer(2).EdgeStrut=false(15,1);

Latt.Prep.Layer(2).EdgeStrut(9)=true;

Latt.Prep.Layer(2).Struts(1,:)=sort([1 6]);
Latt.Prep.Layer(2).Struts(2,:)=sort([2 7]);
Latt.Prep.Layer(2).Struts(3,:)=sort([3 6]);
Latt.Prep.Layer(2).Struts(4,:)=sort([4 6]);
Latt.Prep.Layer(2).Struts(5,:)=sort([4 7]);
Latt.Prep.Layer(2).Struts(6,:)=sort([5 7]);
Latt.Prep.Layer(2).Struts(7,:)=sort([3 10]);
Latt.Prep.Layer(2).Struts(8,:)=sort([4 11]);
Latt.Prep.Layer(2).Struts(9,:)=sort([5 12]);
Latt.Prep.Layer(2).Struts(10,:)=sort([10 8]);
Latt.Prep.Layer(2).Struts(11,:)=sort([8 11]);
Latt.Prep.Layer(2).Struts(12,:)=sort([11 9]);
Latt.Prep.Layer(2).Struts(13,:)=sort([9 12]);
Latt.Prep.Layer(2).Struts(14,:)=sort([8 13]);
Latt.Prep.Layer(2).Struts(15,:)=sort([9 14]);

Latt.Prep.Layer(2).ConnectStruts=[3 4 5 6 10 11 12 13];

Latt.Prep.Layer(2).NMap=zeros(14,2);
Latt.Prep.Layer(2).NMap(1,:)=[2,1];
Latt.Prep.Layer(2).NMap(2,:)=[4,1];
Latt.Prep.Layer(2).NMap(3,:)=[1,2];
Latt.Prep.Layer(2).NMap(4,:)=[3,2];
Latt.Prep.Layer(2).NMap(5,:)=[5,2];
Latt.Prep.Layer(2).NMap(6,:)=[2,3];
Latt.Prep.Layer(2).NMap(7,:)=[4,3];
Latt.Prep.Layer(2).NMap(8,:)=[2,4];
Latt.Prep.Layer(2).NMap(9,:)=[4,4];
Latt.Prep.Layer(2).NMap(10,:)=[1,5];
Latt.Prep.Layer(2).NMap(11,:)=[3,5];
Latt.Prep.Layer(2).NMap(12,:)=[5,5];
Latt.Prep.Layer(2).NMap(13,:)=[2,6];
Latt.Prep.Layer(2).NMap(14,:)=[4,6];

%%
Latt.Struts=zeros(117,2);
Latt.ExtraStrut=false(117,1);
Latt.EdgeStrut=false(117,1);
nStrut=0;
for nLayer=1:5
   LayerType=Latt.Prep.XLType(nLayer);
   for nS=1:size(Latt.Prep.Layer(LayerType).Struts,1)
       nStrut=nStrut+1;
       p1=Latt.Prep.Layer(LayerType).Struts(nS,1);
       ny=Latt.Prep.Layer(LayerType).NMap(p1,1);
       nz=Latt.Prep.Layer(LayerType).NMap(p1,2);
       P1=Latt.Prep.PMap(ny,nLayer,nz);
       
       p2=Latt.Prep.Layer(LayerType).Struts(nS,2);
       ny=Latt.Prep.Layer(LayerType).NMap(p2,1);
       nz=Latt.Prep.Layer(LayerType).NMap(p2,2);
       P2=Latt.Prep.PMap(ny,nLayer,nz);
       
       Latt.Struts(nStrut,:)=[P1 P2];
       Latt.ExtraStrut(nStrut)=Latt.Prep.Layer(LayerType).ExtraStrut(nS);
       Latt.EdgeStrut(nStrut)=Latt.Prep.Layer(LayerType).EdgeStrut(nS);
       if nLayer==5
           Latt.EdgeStrut(nStrut)=true;
       end
       
   end
end

%%
for nLayer=1:5
   LayerType=Latt.Prep.XLType(nLayer);
   for nS=Latt.Prep.Layer(LayerType).ConnectStruts
       nStrut=nStrut+1;
       p1=Latt.Prep.Layer(LayerType).Struts(nS,1);
       ny=Latt.Prep.Layer(LayerType).NMap(p1,1);
       nz=Latt.Prep.Layer(LayerType).NMap(p1,2);
       P1=Latt.Prep.PMap(nLayer,ny,nz);
       
       p2=Latt.Prep.Layer(LayerType).Struts(nS,2);
       ny=Latt.Prep.Layer(LayerType).NMap(p2,1);
       nz=Latt.Prep.Layer(LayerType).NMap(p2,2);
       P2=Latt.Prep.PMap(nLayer,ny,nz);
       
       Latt.Struts(nStrut,:)=[P1 P2];
       Latt.ExtraStrut(nStrut)=Latt.Prep.Layer(LayerType).ExtraStrut(nS);
%        Latt.EdgeStrut(nStrut)=Latt.Prep.Layer(LayerType).EdgeStrut(nS);
       if nLayer==5
           Latt.EdgeStrut(nStrut)=true;
       end
       
   end
end

removeExtra=true;
removeEdge=true;

Latt.StrutsFull=Latt.Struts;
Latt.NodesFull=Latt.Nodes;

if (removeExtra) && (removeEdge)
    MyKeep=(~Latt.ExtraStrut)&(~Latt.EdgeStrut);
elseif removeExtra
    MyKeep=(~Latt.ExtraStrut);
elseif removeEdge
    MyKeep=(~Latt.EdgeStrut);
else
    MyKeep=true(117,1);
end

Latt.Struts=Latt.Struts(MyKeep,:);


%% Cleanup 
if removeEdge
MyUniqueNode=unique([Latt.Struts(:,1);Latt.Struts(:,2)]);
NodeKeep=false(length(Latt.Nodes),1);
NewNodeNum=zeros(length(Latt.Nodes),1);
NodeKeep(MyUniqueNode)=true;
nNode=0;
    for n1=1:length(NodeKeep)
       if NodeKeep(n1)
           nNode=nNode+1;
           NewNodeNum(n1)=nNode;
       end
    end
Latt.Nodes=Latt.Nodes(NodeKeep,:);

    for n1=1:length(Latt.Struts)
       Latt.Struts(n1,1)=NewNodeNum(Latt.Struts(n1,1));
       Latt.Struts(n1,2)=NewNodeNum(Latt.Struts(n1,2));
    end
end

%%
figure(1);
clf;
hold on;
plot3(Latt.Nodes(:,1),Latt.Nodes(:,2),Latt.Nodes(:,3),'ro','MarkerFaceColor','r');

for n1=1:length(Latt.Nodes)
%    if ~Latt.ExtraStrut(n1)
   XX=Latt.Nodes(n1,1);
   YY=Latt.Nodes(n1,2);
   ZZ=Latt.Nodes(n1,3);
   text(XX.*1.05,YY.*1.05,ZZ.*1.05,num2str(n1));
%    end
end

axis equal;

for n1=1:length(Latt.Struts)
%    if ~Latt.ExtraStrut(n1)
   XX=Latt.Nodes(Latt.Struts(n1,:),1);
   YY=Latt.Nodes(Latt.Struts(n1,:),2);
   ZZ=Latt.Nodes(Latt.Struts(n1,:),3);
   plot3(XX,YY,ZZ,'b-');
%    end
end

xlabel('x');
ylabel('y');
zlabel('z');

%% ------------------------------
% Convert to mesh
% Nodes
for n1=1:length(Latt.Nodes)
   Mesh.Node(n1).N=Latt.Nodes(n1,:).';
end

%%
Pr2.Mt.YM=115e3;
Pr2.Mt.nu=0.33;

Pr2.Ge.r=1.15;
Pr2.Mt.G=Pr2.Mt.YM./(2.*(1+Pr2.Mt.nu));
Pr2.Ge.kappa=6.*(1+Pr2.Mt.nu)./(7+Pr2.Mt.nu);

Pr2.Ge.Jtor=2.*(Pr2.Ge.r.^4)./12;
Pr2.Ge.I=(Pr2.Ge.r.^4)./12;
Pr2.Ge.A=(Pr2.Ge.r.^2);


Pr2.Mt.YS=1119;
Pr2.Mt.rho=(4430./1000).*((1e-3).^3);
Sc(1).Pr=Pr2;
l=26; 

%%
for n1=1:length(Latt.Struts)
   Mesh.Element(n1).Ps=Latt.Struts(n1,:);
   Mesh.Element(n1).Sc=1;
   Mesh.El(n1).Pr=Pr2;
end

Mesh.Prep=Latt.Prep;

save MyMesh Mesh Sc;

figure(10);
clf;
hold on;

for n1=1:length(Mesh.Node)
   x=Mesh.Node(n1).N(1);
   y=Mesh.Node(n1).N(2);
   z=Mesh.Node(n1).N(3);
   plot3(x,y,z,'ro','MarkerFaceColor','r');
end

axis equal;
xlabel('x');
ylabel('y');
zlabel('z');