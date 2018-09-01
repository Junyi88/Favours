function []=W1F_CDatum(fileID,V,LineList,ZVals)



Start1=['\n#- Create Datums ------------------------ \n'];
DatumPoText=['vP.DatumPointByCoordinate(coords=( %8.4e, %8.4e, %8.4e)) \n'];
DatumPlText=['vP.DatumPlaneByThreePoints( point1=' ...
    'vP.datums[%d], point2=vP.datums[%d], point3=vP.datums[%d]) \n'];

% Cut1=['mdb.models[' char(39) 'Model-1' char(39) ...
%     '].ConstrainedSketch(gridSpacing=0.12, name=' char(39) ...
%     '__profile__' char(39) ',sheetSize=5.02,' ...
%     'transform=vP.MakeSketchTransform(' ...
%     'sketchPlane=vP.datums[%d], sketchPlaneSide=SIDE1,'
%     'sketchUpEdge=vP.datums[%d],sketchOrientation=RIGHT, origin=(0,0,0))) \n'];
% Cut2=['mdb.models[' char(39) 'Model-1' char(39) ...
%     '].sketches[' char(39) '__profile__' char(39) ...
%     '].sketchOptions.setValues(sheetSize=6000) \n'];
% Cut3=['vP.projectReferencesOntoSketch(filter' ...
%     '=COPLANAR_EDGES, sketch=mdb.models[' char(39) ...
%     'Model-1' char(39) '].sketches[' ...
%     char(39) '__profile__' char(39) ']) \n'];

%%
dCount=1;
dPlaneCount=0;

DPlanes=zeros(size(V,1),1);

for n1=1:length(LineList.Grain)
    for n2=1:length(LineList.Grain(n1).Set)
       for n3=1:size(LineList.Grain(n1).Set(n2).List,1)
     
           fprintf(fileID,Start1);
           
           v=LineList.Grain(n1).Set(n2).List(n3,:);
           x0=V(v(1),1);
           y0=V(v(1),2);
           x1=V(v(2),1);
           y1=V(v(2),2);
           
           % ---
           fprintf(fileID,DatumPoText,x0,y0,ZVals(1));
           fprintf(fileID,DatumPoText,x1,y1,ZVals(1));
           fprintf(fileID,DatumPoText,x1,y1,ZVals(2));
           
           A.P1=dCount+1;
           A.P2=dCount+2;
           A.P3=dCount+3;
           dCount=A.P3;
%            A.PP=dCount+4;
%            
%            fprintf(fileID,DatumPlText,A.P1,A.P2,A.P3);
%            
%            
%            dPlaneCount=dPlaneCount+1;
%            DPlanes(dPlaneCount)=A.PP;
%            dCount=A.PP;
           
           %----
           
       end        
    end
end


end