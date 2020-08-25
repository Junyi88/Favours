function [Mesh]=ConvertToVigMesh(Latt,Pr)
%% ------------------------------
% Convert to mesh
% Nodes
for n1=1:length(Latt.Nodes)
   Mesh.Node(n1).N=Latt.Nodes(n1,:).';
end

%%
for n1=1:length(Latt.Struts)
   Mesh.Element(n1).Ps=Latt.Struts(n1,:);
   Mesh.Element(n1).Sc=1;
   Mesh.El(n1).Pr=Pr;
end

Mesh.Prep=Latt.Prep;

end