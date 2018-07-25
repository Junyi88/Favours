clear;

H=17.75;
L=11.0;
h=5.5;

M.X=L./2;
M.Y=L./2;
M.Z=(H-h);



%%
dx=-M.X;
dy=-M.Y;
dz=-M.Z;
np=1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);

dx=-M.X;
dy=M.Y;
dz=-M.Z;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);

dx=M.X;
dy=-M.Y;
dz=-M.Z;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);

dx=M.X;
dy=M.Y;
dz=-M.Z;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);

%%
figure(1);
clf;
hold on;

lineSp='ks-';
for n1=1:4
    for n2=5:8
        for n3=1:7
        plot3(MyLat(n1).Cells(n2).L(n3).X,MyLat(n1).Cells(n2).L(n3).Y,...
            MyLat(n1).Cells(n2).L(n3).Z,lineSp);
    
        end
    end
end

axis equal;

%%
dx=-M.X;
dy=0;
dz=0;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);

dx=M.X;
dy=0;
dz=0;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);


% figure(2);
% clf;
% hold on;
lineSp='bs-';
for n1=5:6
    for n2=[1:4]
        for n3=1:7
        plot3(MyLat(n1).Cells(n2).L(n3).X,MyLat(n1).Cells(n2).L(n3).Y,...
            MyLat(n1).Cells(n2).L(n3).Z,lineSp);
    
        end
    end
end

%%
dx=-M.X;
dy=M.Y.*2;
dz=0;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);

dx=M.X;
dy=M.Y.*2;
dz=0;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);

lineSp='rs-';
for n1=7:8
    for n2=[1 3 5 7]
        for n3=1:7
        plot3(MyLat(n1).Cells(n2).L(n3).X,MyLat(n1).Cells(n2).L(n3).Y,...
            MyLat(n1).Cells(n2).L(n3).Z,lineSp);
    
        end
    end
end

%%
dx=-M.X;
dy=-M.Y.*2;
dz=0;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);

dx=M.X;
dy=-M.Y.*2;
dz=0;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);

lineSp='rs-';
for n1=9:10
    for n2=[2 4 6 8]
        for n3=1:7
        plot3(MyLat(n1).Cells(n2).L(n3).X,MyLat(n1).Cells(n2).L(n3).Y,...
            MyLat(n1).Cells(n2).L(n3).Z,lineSp);
    
        end
    end
end

%%

