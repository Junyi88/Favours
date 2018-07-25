clear;

H=17.75;
L=11.0;
h=5.5;

%%
x=[-L./2 0 L./2];
y=[-L./2 0 L./2];
z=[-H./2 (-H./2+h) 0 H./2-h H./2];

%%
orderX=1+[2 2 2 1 1 1 0 0 0,...
    2 1 1 0, ...
    2 2 0 0, ...
    2 1 1 0, ...
    2 2 2 1 1 1 0 0 0 ...
    ].';

orderY=1+[0 1 2 0 1 2 0 1 2, ...
    1 0 2 1,...
    0 2 0 2,...
    1 0 2 1,...
    0 1 2 0 1 2 0 1 2].';
orderZ=1+[zeros(1,9),...
    1.*ones(1,4),...
    2.*ones(1,4),...
    3.*ones(1,4),...
    4.*ones(1,9),...
    ].';

%%

Nodes=zeros(30,3);

for n1=1:30
   Nodes(n1,1)=x(orderX(n1)); 
   Nodes(n1,2)=y(orderY(n1)); 
   Nodes(n1,3)=z(orderZ(n1)); 
end

figure(1);
clf;
hold on;
plot3(Nodes(:,1),Nodes(:,2),Nodes(:,3),'bo');
axis equal;

%%
MyCell(1).P=[1 14; 1 10; 2 10; 1 11; 4 11; 5 10; 5 11];
MyCell(2).P=[3 15; 3 10; 2 10; 3 12; 6 12; 5 10; 5 12];
MyCell(3).P=[7 16; 7 13; 8 13; 7 11; 4 11; 5 13; 5 11];
MyCell(4).P=[9 17; 9 13; 8 13; 9 12; 6 12; 5 13; 5 12];
MyCell(5).P=[22 14; 22 18; 23 18; 22 19; 25 19; 26 19; 26 21];
MyCell(6).P=[24 15; 23 18; 24 18; 24 20; 27 20; 26 18; 26 20];
MyCell(7).P=[28 16; 28 21; 29 21; 28 19; 25 19; 26 19; 26 21];
MyCell(8).P=[30 17; 30 21; 29 21; 30 20; 27 20; 26 21; 26 20];

%%
figure(1);
hold on;

lineSp='k-';
n2=1;
for n1=1:7
    XX=[Nodes(MyCell(n2).P(n1,1),1) Nodes(MyCell(n2).P(n1,2),1)];
    YY=[Nodes(MyCell(n2).P(n1,1),2) Nodes(MyCell(n2).P(n1,2),2)];
    ZZ=[Nodes(MyCell(n2).P(n1,1),3) Nodes(MyCell(n2).P(n1,2),3)];
    plot3(XX,YY,ZZ,lineSp);
end

lineSp='k-';
n2=2;
for n1=1:7
    XX=[Nodes(MyCell(n2).P(n1,1),1) Nodes(MyCell(n2).P(n1,2),1)];
    YY=[Nodes(MyCell(n2).P(n1,1),2) Nodes(MyCell(n2).P(n1,2),2)];
    ZZ=[Nodes(MyCell(n2).P(n1,1),3) Nodes(MyCell(n2).P(n1,2),3)];
    plot3(XX,YY,ZZ,lineSp);
end

lineSp='k-';
n2=3;
for n1=1:7
    XX=[Nodes(MyCell(n2).P(n1,1),1) Nodes(MyCell(n2).P(n1,2),1)];
    YY=[Nodes(MyCell(n2).P(n1,1),2) Nodes(MyCell(n2).P(n1,2),2)];
    ZZ=[Nodes(MyCell(n2).P(n1,1),3) Nodes(MyCell(n2).P(n1,2),3)];
    plot3(XX,YY,ZZ,lineSp);
end

lineSp='k-';
n2=4;
for n1=1:7
    XX=[Nodes(MyCell(n2).P(n1,1),1) Nodes(MyCell(n2).P(n1,2),1)];
    YY=[Nodes(MyCell(n2).P(n1,1),2) Nodes(MyCell(n2).P(n1,2),2)];
    ZZ=[Nodes(MyCell(n2).P(n1,1),3) Nodes(MyCell(n2).P(n1,2),3)];
    plot3(XX,YY,ZZ,lineSp);
end

lineSp='k-';
n2=5;
for n1=1:7
    XX=[Nodes(MyCell(n2).P(n1,1),1) Nodes(MyCell(n2).P(n1,2),1)];
    YY=[Nodes(MyCell(n2).P(n1,1),2) Nodes(MyCell(n2).P(n1,2),2)];
    ZZ=[Nodes(MyCell(n2).P(n1,1),3) Nodes(MyCell(n2).P(n1,2),3)];
    plot3(XX,YY,ZZ,lineSp);
end

lineSp='k-';
n2=6;
for n1=1:7
    XX=[Nodes(MyCell(n2).P(n1,1),1) Nodes(MyCell(n2).P(n1,2),1)];
    YY=[Nodes(MyCell(n2).P(n1,1),2) Nodes(MyCell(n2).P(n1,2),2)];
    ZZ=[Nodes(MyCell(n2).P(n1,1),3) Nodes(MyCell(n2).P(n1,2),3)];
    plot3(XX,YY,ZZ,lineSp);
end

lineSp='k-';
n2=7;
for n1=1:7
    XX=[Nodes(MyCell(n2).P(n1,1),1) Nodes(MyCell(n2).P(n1,2),1)];
    YY=[Nodes(MyCell(n2).P(n1,1),2) Nodes(MyCell(n2).P(n1,2),2)];
    ZZ=[Nodes(MyCell(n2).P(n1,1),3) Nodes(MyCell(n2).P(n1,2),3)];
    plot3(XX,YY,ZZ,lineSp);
end

lineSp='k-';
n2=8;
for n1=1:7
    XX=[Nodes(MyCell(n2).P(n1,1),1) Nodes(MyCell(n2).P(n1,2),1)];
    YY=[Nodes(MyCell(n2).P(n1,1),2) Nodes(MyCell(n2).P(n1,2),2)];
    ZZ=[Nodes(MyCell(n2).P(n1,1),3) Nodes(MyCell(n2).P(n1,2),3)];
    plot3(XX,YY,ZZ,lineSp);
end