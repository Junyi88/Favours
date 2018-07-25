clear;

H=17.75;
L=11.0;
h=5.5;

M.X=L;
M.Y=L;
M.Z=(H-h);



%%
dx=0;
dy=0;
dz=0;
np=1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);
pck(np).p=[1:8];

dx=M.X;
dy=0;
dz=0;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);
pck(np).p=[1:8];
%%
figure(1);
clf;
hold on;

lineSp='ks-';
for n1=1:2
    for n2=pck(n1).p
        for n3=1:7
        plot3(MyLat(n1).Cells(n2).L(n3).X,MyLat(n1).Cells(n2).L(n3).Y,...
            MyLat(n1).Cells(n2).L(n3).Z,lineSp);
    
        end
    end
end

axis equal;
view([0 0])
%%
dx=-M.X./2;
dy=0;
dz=-M.Z;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);
pck(np).p=[5 6];

dx=M.X./2;
dy=0;
dz=-M.Z;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);
pck(np).p=[5:8];

dx=M.X./2.*3;
dy=0;
dz=-M.Z;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);
pck(np).p=[8 7];

lineSp='rs-';
for n1=3:5
    for n2=pck(n1).p
        for n3=1:7
        plot3(MyLat(n1).Cells(n2).L(n3).X,MyLat(n1).Cells(n2).L(n3).Y,...
            MyLat(n1).Cells(n2).L(n3).Z,lineSp);
    
        end
    end
end



%%
dx=-M.X./2;
dy=0;
dz=M.Z;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);
pck(np).p=[1 2];

dx=M.X./2;
dy=0;
dz=M.Z;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);
pck(np).p=[1:4];

dx=M.X./2.*3;
dy=0;
dz=M.Z;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);
pck(np).p=[3 4];

lineSp='rs-';
for n1=6:8
    for n2=pck(n1).p
        for n3=1:7
        plot3(MyLat(n1).Cells(n2).L(n3).X,MyLat(n1).Cells(n2).L(n3).Y,...
            MyLat(n1).Cells(n2).L(n3).Z,lineSp);
    
        end
    end
end

%%---------------------
%%
dx=0;
dy=M.Y;
dz=0;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);
pck(np).p=[1:8];

dx=M.X;
dy=M.Y;
dz=0;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);
pck(np).p=[1:8];

%%


lineSp='bs-';
for n1=1+8:2+8
    for n2=pck(n1).p
        for n3=1:7
        plot3(MyLat(n1).Cells(n2).L(n3).X,MyLat(n1).Cells(n2).L(n3).Y,...
            MyLat(n1).Cells(n2).L(n3).Z,lineSp);
    
        end
    end
end

axis equal;
%%
dx=-M.X./2;
dy=M.Y;
dz=-M.Z;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);
pck(np).p=[5 6];

dx=M.X./2;
dy=M.Y;
dz=-M.Z;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);
pck(np).p=[5:8];

dx=M.X./2.*3;
dy=M.Y;
dz=-M.Z;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);
pck(np).p=[7 8];

lineSp='gs-';
for n1=3+8:5+8
    for n2=pck(n1).p
        for n3=1:7
        plot3(MyLat(n1).Cells(n2).L(n3).X,MyLat(n1).Cells(n2).L(n3).Y,...
            MyLat(n1).Cells(n2).L(n3).Z,lineSp);
    
        end
    end
end

view([0 0])

%%
dx=-M.X./2;
dy=M.Y;
dz=M.Z;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);
pck(np).p=[1 2];

dx=M.X./2;
dy=M.Y;
dz=M.Z;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);
pck(np).p=[1:4];

dx=M.X./2.*3;
dy=M.Y;
dz=M.Z;
np=np+1;
[MyLat(np)]=SingleCellAuxetic(H,L,h,dx,dy,dz);
pck(np).p=[3 4];

lineSp='gs-';
for n1=6+8:8+8
    for n2=pck(n1).p
        for n3=1:7
        plot3(MyLat(n1).Cells(n2).L(n3).X,MyLat(n1).Cells(n2).L(n3).Y,...
            MyLat(n1).Cells(n2).L(n3).Z,lineSp);
    
        end
    end
end

figure(2);
clf;
hold on;
for n1=1
    for n2=[1:8]
        for n3=1:7
        plot3(MyLat(n1).Cells(n2).L(n3).X,MyLat(n1).Cells(n2).L(n3).Y,...
            MyLat(n1).Cells(n2).L(n3).Z,'bs');
    
        end
    end
end
for n1=1
    for n2=1:8
        for n3=1:7
        plot3(MyLat(n1).Cells(n2).L(n3).X,MyLat(n1).Cells(n2).L(n3).Y,...
            MyLat(n1).Cells(n2).L(n3).Z,'r-');
    
        end
    end
end

axis equal;