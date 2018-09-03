clear;
load ../Step2_Data.mat;

%%
SheetSize=200.0;
% CreateRec=[2.0,2.0,740,480];

%---
GridSize=SheetSize./100;

%%
T0_Prep=['t = p.MakeSketchTransform(sketchPlane=f[0], origin=(0.0, 0.0, 0.0)) \n'];
T0_Sketch=['s = mdb.models[' char(39) 'Model-1' char(39) ...
    '].ConstrainedSketch(name=' char(39) '__profile__' char(39) ...
    ', sheetSize=%8.4e, gridSpacing=%8.4e, transform=t) \n \n'];

T1_Line=['s.Line(point1=(%8.4e, %8.4e), point2=(%8.4e, %8.4e)) \n'];

T2_Partition={['\n \n# Partition--------------------'];...
    ['p = mdb.models[' char(39) 'Model-1' ...
    char(39) '].parts[' char(39) 'Part-Base' char(39) '] \n'];...
    ['f = p.faces \n']; ...
    ['pickedFaces = f.getSequenceFromMask(mask=(' char(39) ...
    '[#1 ]' char(39) ', ), ) \n']; ...
    ['e1, d2 = p.edges, p.datums \n']; ...
    ['p.PartitionFaceBySketch(faces=pickedFaces, sketch=s) \n\n'];...
    };

%%
OutputFileName='WTest0.py';
fileID = fopen(OutputFileName,'a+');

fprintf(fileID,T0_Prep);
fprintf(fileID,T0_Sketch,SheetSize,GridSize);

%---
for n1=1:length(ShortList2.Grain)
    for n2=1:length(ShortList2.Grain(n1).Set)
        for n3=1:size(ShortList2.Grain(n1).Set(n2).List,1)
           x1=VShort(ShortList2.Grain(n1).Set(n2).List(n3,1),1);
           y1=VShort(ShortList2.Grain(n1).Set(n2).List(n3,1),2);
           x2=VShort(ShortList2.Grain(n1).Set(n2).List(n3,2),1);
           y2=VShort(ShortList2.Grain(n1).Set(n2).List(n3,2),2);
           
           fprintf(fileID,T1_Line,x1,y1,x2,y2);
        end

    end
end

for n1=1:length(T2_Partition)
    fprintf(fileID,T2_Partition{n1});
end

%%

fclose(fileID);

%%
%{
t = p.MakeSketchTransform(sketchPlane=f[0], origin=(0.0, 0.0, 0.0))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=1819.45, gridSpacing=45.48, transform=t)
s1.Line(point1=(0, 100), point2=(1000, 100))
p = mdb.models['Model-1'].parts['Part-Base']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
e1, d2 = p.edges, p.datums
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s1)
%}

% getByBoundingBox(xMin=, yMin=, zMin=, xMax= ,yMax=, zMax=)
% faces = f.findAt(((-16.438578, -41.835673, -24.19804), ),
%                 ((25.210364, -35.689868, 1.860314), ),
%                 ((26.727683, -38.207055, 4.164759), ))