function []=W1F_DatumPlane(fileID,V,LineList)



Start1=['\n#- Create Datum Plane ------------------------ \n'];
DatumPlText=['vP.DatumPlaneByThreePoints( point1=' ...
    'vP.datums[%d], point2=vP.datums[%d], point3=vP.datums[%d]) \n'];



%%
L=size(V,1);
for n1=1:length(LineList.Grain)
    for n2=1:length(LineList.Grain(n1).Set)
       for n3=1:size(LineList.Grain(n1).Set(n2).List,1)
     
           fprintf(fileID,Start1);
           
           v=LineList.Grain(n1).Set(n2).List(n3,:);
           P1=1+v(1);
           P2=1+v(2);
           P3=1+L+v(1);
           
           fprintf(fileID,DatumPlText,P1,P2,P3);
       end        
    end
end


end