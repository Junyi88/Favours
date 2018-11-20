clear;

load Read0_Data ElSystems NodeCoords;

LEl=size(ElSystems,1);

xNodes=zeros(LEl,8);
yNodes=zeros(LEl,8);
zNodes=zeros(LEl,8);

for n1=1:LEl
    for n2=1:8
        N=ElSystems(n1,n2+1);
        if N==0
        else
        xNodes(n1,n2)=NodeCoords(N,2);
        yNodes(n1,n2)=NodeCoords(N,3);
        zNodes(n1,n2)=NodeCoords(N,4);
        end
    end
   
end

%%
figure(1);
clf;
hold on;
plot3(xNodes(1,:),yNodes(1,:),zNodes(1,:),'rx');
for n1=1:8
text(xNodes(1,n1).*1.001,yNodes(1,n1).*1.001,zNodes(1,n1).*1.001,num2str(n1));
end
xlabel('x');
ylabel('y');
zlabel('z');
axis equal;

%% 
xNodeI=xNodes(:,[1 2 4 3 5 6 8 7]);
yNodeI=yNodes(:,[1 2 4 3 5 6 8 7]);
zNodeI=zNodes(:,[1 2 4 3 5 6 8 7]);

%%

PNat=[-1 1 1;...
    -1 -1 1;...
    -1 1 -1;...
    -1 -1 -1;...
    1 1 1;...
    1 -1 1;...
    1 1 -1;...
    1 -1 -1];
PI=PNat./sqrt(3);

%%
NEnat=zeros(8,8);
NEI=zeros(8,8);

for n1=1:8
   for n2=1:8
       NEnat(n1,n2)=(1+PNat(n1,1)*PNat(n2,1))*...
           (1+PNat(n1,2)*PNat(n2,2))*...
           (1+PNat(n1,3)*PNat(n2,3));
       NEI(n1,n2)=(1+PI(n1,1)*PI(n2,1))*...
           (1+PI(n1,2)*PI(n2,2))*...
           (1+PI(n1,3)*PI(n2,3));
   end
end

NEnat=NEnat./8;
NEI=NEI./8;

%%
xI=zeros(LEl,8);
yI=zeros(LEl,8);
zI=zeros(LEl,8);

for n1=1:LEl
   xI(n1,:)=(NEI*(xNodeI(n1,:).')).'; 
   yI(n1,:)=(NEI*(yNodeI(n1,:).')).'; 
   zI(n1,:)=(NEI*(zNodeI(n1,:).')).'; 
end

figure(1);
plot3(xI(1,:),yI(1,:),zI(1,:),'bs');
for n1=1:8
text(xI(1,n1).*1.001,yI(1,n1).*1.001,zI(1,n1).*1.001,num2str(n1));
end

%%
load ../Step1_Data;
% load ../4_GNDinMTEX2 X Y;
% load ./EBSD10min_GND;

load ../4_GNDinMTEXinit X Y;
load ./EBSDinitial_GND;

XX=X.*(max(grains.x)-min(grains.x))./max(X(:));
YY=Y.*(max(grains.y)-min(grains.y))./max(Y(:));

XXX=XX(:);
YYY=YY(:);
% PP=XXX;
% XXX=XXX(XXX~=0);
% YYY=YYY(YYY~=0);

% GGG=GND_total(:);
gndDensity_Gridified=gndDensity_Gridified(2:end,2:end);
GGG=gndDensity_Gridified(:);
% GGG=GGG(PP~=0);
NotNan=~isnan(GGG);
SF=fit([XXX(NotNan),YYY(NotNan)],GGG(NotNan),'linearinterp');

GND=zeros(LEl,8);

for n1=1:LEl
    for n2=1:8
      GND(n1,n2)=feval(SF,[xI(n1,n2),yI(n1,n2)]);
      
      if isnan(GND(n1,n2))
          GND(n1,n2) = 0.0;
      end
    end
end

figure(290);
clf;
% plot3(xI,yI,GND,'bo');
surf(xI,yI,GND,'EdgeColor','none');

GNDI=zeros(LEl,8);
for n1=1:LEl
   GNDI(n1,:)=(NEI*(GND(n1,:).')).'; 

end

OutputFileName='GNDSPLIT.f';
fileID = fopen(OutputFileName,'w+');

FMT='     +  %12.8e %12.8e %12.8e %12.8e %12.8e %12.8e %12.8e %12.8e \n';
FMT4='     +  %12.8e, %12.8e, %12.8e, %12.8e, \n';
FMT4L='     +  %12.8e, %12.8e, %12.8e, %12.8e \n';

STARTTEXT='      REAL*8:: GND(8,%d) \n \n';

NEWHEADER='      GND(1:8,%d) = (/ \n';
NEWEND='     +  /) \n \n'; 
%%
fprintf(fileID,STARTTEXT,LEl);   



for n1=1:LEl-1
fprintf(fileID,NEWHEADER,n1);
fprintf(fileID,FMT4,GNDI(n1,1:4));    
fprintf(fileID,FMT4L,GNDI(n1,5:8));   
fprintf(fileID,NEWEND);  
end
% for n1=LEl:LEl
% fprintf(fileID,FMT4,GNDI(n1,1:4));    
% fprintf(fileID,FMT4L,GNDI(n1,5:8));    
% end

% fprintf(fileID,ENDTEXT,LEl);   
fclose(fileID);

OutputFileName='GND.txt';
fileID = fopen(OutputFileName,'w+');

FMT='%12.8e %12.8e %12.8e %12.8e %12.8e %12.8e %12.8e %12.8e \n';


for n1=1:LEl
fprintf(fileID,FMT,GNDI(n1,:));    
end

fclose(fileID);