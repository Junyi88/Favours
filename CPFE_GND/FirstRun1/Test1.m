clear;

%% User Input Parameter
GrainSmoothFactor = 3; % This is a factor used to smooth the grains


%% Load Previous Step Data
load Step1_Data.mat;

%% First smooth the grains
grainsOri=grains;
if GrainSmoothFactor > 0
    grains =smooth(grains,GrainSmoothFactor);
end

%%
nG=15; nG=1;
gB=grains(nG).boundary; % Grain Boundary Object

%%
F=gB.F; % This is the faces
V=gB.V; % This is all the vertices

[V_loc2glo,F_ia,F_ic] = unique(F);
Vloc=V(V_loc2glo,:);
Floc=zeros(size(F));

for n1=1:size(F,1)
  [p1,~]=find(V_loc2glo==F(n1,1));
  [p2,~]=find(V_loc2glo==F(n1,2));
  Floc(n1,:)=[p1,p2];
end

%% 
Chain=zeros(size(F,1)+1,1);
Ft=F;
count=1;
Chain(count)=Ft(1,1);
count=count+1;
Chain(count)=Ft(1,2);
RemoveItem=zeros(size(Ft,1),1);
RemoveItem(1)=1;
Ft=Ft(~RemoveItem,:);

while (~isempty(Ft))
    currentV=Chain(count);
    count=count+1;
    [row,col]=find(Ft==currentV);
    RemoveItem=zeros(size(Ft,1),1);
    if col==1
        Chain(count)=Ft(row,2);
    else
        Chain(count)=Ft(row,1);
    end
    RemoveItem(row)=1;
    Ft=Ft(~RemoveItem,:);
end
Chain=Chain(1:end-1);

for n1=2:size(F,1)
    count=count+1;
    
    
    
end


figure(2);
clf;
hold on;

for n1=1:size(Floc,1)
    f=Floc(n1,:);
   x=Vloc(f,1);
   y=Vloc(f,2);
   plot(x,y,'bs-');
   
   f=grainsOri(nG).boundary.F(n1,:);
   x=grainsOri(nG).boundary.V(f,1);
   y=grainsOri(nG).boundary.V(f,2);
   plot(x,y,'rx-');
end

%%
F0=grainsOri(nG).boundary.F; 

figure(1);
clf;
hold on;

for n1=1:size(grains(nG).boundary.F,1)
    f=grains(nG).boundary.F(n1,:);
   x=grains(nG).boundary.V(f,1);
   y=grains(nG).boundary.V(f,2);
   plot(x,y,'bs-');
   
   f=grainsOri(nG).boundary.F(n1,:);
   x=grainsOri(nG).boundary.V(f,1);
   y=grainsOri(nG).boundary.V(f,2);
   plot(x,y,'rx-');
end