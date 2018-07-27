function [Kgl,Mesh]=GlobalTimoLattice3D(Mesh,Sc)

    LNode=length(Mesh.Node);
    LElement=length(Mesh.Element);
    Kgl=zeros(6*LNode,6*LNode);
%     Mesh.El(LElement).Pr=[];
    
    for n1=1:LElement
        Pr=Sc(Mesh.Element(n1).Sc).Pr;
        Ps{1}=Mesh.Node(Mesh.Element(n1).Ps(1)).N;
        Ps{2}=Mesh.Node(Mesh.Element(n1).Ps(2)).N;

        [Pr,~]=GetRot3D(Ps,Pr);
        Mesh.El(n1).Pr=Pr;
        [K]=Timo3D(Pr);
        [K]=Timo3DR(K,Pr);
        
        D1=[1:6]+6*(Mesh.Element(n1).Ps(1)-1);
        D2=[1:6]+6*(Mesh.Element(n1).Ps(2)-1);
        Kgl([D1 D2],[D1 D2])=Kgl([D1 D2],[D1 D2])+K;
    end

end