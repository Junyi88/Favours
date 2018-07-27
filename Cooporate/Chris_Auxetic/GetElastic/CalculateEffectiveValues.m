clear;

load ../SetupPosition/TotalMesh.mat;

[OutNoStrut]=Vig3DSystemAuxectic(MeshNoStrut,Sc);
[OutStrut]=Vig3DSystemAuxectic(MeshStrut,Sc);

figure(2);
clf;
hold on;

for n1=1:length(MeshNoStrut.Node)
   x=MeshNoStrut.Node(n1).N(1);
   y=MeshNoStrut.Node(n1).N(2);
   z=MeshNoStrut.Node(n1).N(3);
   plot3(x,y,z,'ro','MarkerFaceColor','r');
   text(x.*1.1,y.*1.1,z.*1.1,num2str(n1));
end

for n1=1:length(MeshNoStrut.Element)
    Ps=MeshNoStrut.Element(n1).Ps;
    x=[MeshNoStrut.Node(Ps(1)).N(1) MeshNoStrut.Node(Ps(2)).N(1)];
    y=[MeshNoStrut.Node(Ps(1)).N(2) MeshNoStrut.Node(Ps(2)).N(2)];
    z=[MeshNoStrut.Node(Ps(1)).N(3) MeshNoStrut.Node(Ps(2)).N(3)];
    
   plot3(x,y,z,'b-','MarkerFaceColor','b');

end

axis equal;
xlabel('x');
ylabel('y');
zlabel('z');

%%
figure(3);
clf;
hold on;

for n1=1:length(MeshStrut.Node)
   x=MeshStrut.Node(n1).N(1);
   y=MeshStrut.Node(n1).N(2);
   z=MeshStrut.Node(n1).N(3);
   plot3(x,y,z,'ro','MarkerFaceColor','r');
   text(x.*1.1,y.*1.1,z.*1.1,num2str(n1));
end

for n1=1:length(MeshStrut.Element)
    Ps=MeshStrut.Element(n1).Ps;
    x=[MeshStrut.Node(Ps(1)).N(1) MeshStrut.Node(Ps(2)).N(1)];
    y=[MeshStrut.Node(Ps(1)).N(2) MeshStrut.Node(Ps(2)).N(2)];
    z=[MeshStrut.Node(Ps(1)).N(3) MeshStrut.Node(Ps(2)).N(3)];
    
   plot3(x,y,z,'b-','MarkerFaceColor','b');

end

axis equal;
xlabel('x');
ylabel('y');
zlabel('z');