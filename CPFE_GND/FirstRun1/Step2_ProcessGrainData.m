clear;

%% User Input Parameter
GrainSmoothFactor = 2; % This is a factor used to smooth the grains


%% Load Previous Step Data
load Step1_Data.mat;

%% First smooth the grains
if GrainSmoothFactor > 0
    grains =smooth(grains,GrainSmoothFactor);
end

%% Now we get the Chain
%{ 
We create a new object called sGB which stands for sorted grain boundaries
We then find the loop of lines for each chain
%} 

for nG=1:size(grains,1)
    [sGB0(nG).Sets]=GetChainGB(grains(nG).boundary,nG); 
    %sGB0 is because we want to remove the inner boundaries later
end

%% Now we remove the internal boundaries
% DANGER:Assumption: We assume that the inner boundary has a lower size
% compared to the outer boundaries

for nG=1:size(grains,1)
    [sGB0(nG).Sets]=GetChainGB(grains(nG).boundary,nG); 
    %sGB0 is because we want to remove the inner boundaries later
end

for n1=1:size(sGB0,2)

    SetSize=zeros(length(sGB0(n1).Sets),1);
    for n2=1:length(sGB0(n1).Sets)
        SetSize(n2)=length(sGB0(n1).Sets(n2).Chain);
    end
    [~,n2]=max(SetSize);
    sGB(n1).Chain=sGB0(n1).Sets(n2).Chain;
    
end

%%
F=grains(nG).boundary.F;
V=grains(nG).boundary.V;
figure(100);
clf;
hold on;

for n1=1:size(sGB,2)

        x=V(sGB(n1).Chain,1);
        y=V(sGB(n1).Chain,2);
        plot(x,y,'rs-')

    
end

%%
nG=26;
figure(30);
clf;
hold on;

F=grains(nG).boundary.F;
V=grains(nG).boundary.V;
for n1=1:size(F,1)
    x=V(F(n1,:),1);
    y=V(F(n1,:),2);
    plot(x,y,'rs-')
end


%%
figure(100);
clf;
hold on;

for n1=1:size(sGB,2)
    St=sGB(n1).Sets;
    for n2=1:length(St)
        x=V(St(n2).Chain,1);
        y=V(St(n2).Chain,2);
        plot(x,y,'rs-')
    end
    
end

%%
figure(101);
clf;
hold on;

for n1=1:size(sGB,2)
    St=sGB(n1).Sets;
    sz=zeros(length(St),1);
    for n2=1:length(St)
        sz(n2)=length(St(n2).Chain);
    end
    [~,n2]=max(sz);
    x=V(St(n2).Chain,1);
    y=V(St(n2).Chain,2);
    plot(x,y,'bx-');
end

%%

% First 
nG=15;


F1=gB.F(:,1);
F2=gB.F(:,2);
[f,ia,ic]=unique([gB.F(:,1);gB.F(:,2)]);
F=[ic(gB.F(:,1)),ic(gB.F(:,2))];

figure(2);
clf;
hold on;
plot(gB.V(:,1),gB.V(:,2),'bs')

figure(1);
clf;
hold on;

for n1=1:size(grains(nG).boundary.F,1)
    f=grains(nG).boundary.F(n1,:);
   x=grains(nG).boundary.V(f,1);
   y=grains(nG).boundary.V(f,2);
   plot(x,y,'bs-');
   
end


%% Now we get the grain data
% First 
figure(1);
clf;
hold on;

for n1=1:size(grains.boundary.F,1)
    f=grains.boundary.F(n1,:);
   x=grains.boundary.V(f,1);
   y=grains.boundary.V(f,2);
   plot(x,y,'b-');
   
end

plot(grains.boundary);
% hold on;
% for n1=1:length(grains)
%    plot(grains(n1).boundary) ;
% end


%%


gB = grains.boundary;

GrainID=grains.id;

spc=['r-';'g-';'b-';'c-'];

GBLines.V=gB.V;
GBLines.Li=zeros(length(gB),2);

GData.Phi=zeros(length(grains),3);

count=0;
VF=gB.I_VF;
[row,col]=size(VF);
for n1=1:col
    count=count+1;
    nP=find(VF(:,n1)~=0);
    GBLines.Li(n1,:)=nP;
    disp(n1);
end
GBLines.Li=GBLines.Li(1:count,:);

GData.Centroid=grains.centroid;
GData.Phi=[grains.meanOrientation.phi1,grains.meanOrientation.Phi,grains.meanOrientation.phi2];

figure(1);
clf;
hold on;
plot(GData.Centroid(:,1),GData.Centroid(:,2),'rx');
for n1=1:length(GBLines.Li)
    nP=GBLines.Li(n1,:);
    plot(GBLines.V(nP,1),GBLines.V(nP,2),'b-');

    disp(n1);
end

TP.V=grains.triplePoints.V;
TP.GP=grains.triplePoints.grainId;

GP=[TP.GP(:,1:2);TP.GP(:,2:3)];
[C1,ia1,ic1]=unique(GP(:,1));
ic1=sort(ic1);

GP1=GP(ic1,:);

prev=[0 0];

U=zeros(size(GP1,1),2);
Ucount=0;

for n1=1:size(GP1,1)
 if (prev(1)~=GP1(n1,1))&&(prev(2)~=GP1(n1,2))
     Ucount=Ucount+1; 
     prev=GP1(n1,:);
     
     U(Ucount,:)=prev;
 end

end

U=U(1:Ucount,:);

figure(1);
hold on;
[rU,Xu]=size(U);
for n1=1:rU
    X=TP.V(U(n1,:),1);
    Y=TP.V(U(n1,:),2);
    plot(X,Y,'ks'); 
end