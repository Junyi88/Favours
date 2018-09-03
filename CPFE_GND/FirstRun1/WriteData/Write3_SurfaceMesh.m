clear;
load ../Step2_Data.mat;

CreateRec=[-10.0,-10.0,800,700];
MeshSize=5.0;
MeshDevFac=0.1;
MeshMinFac=0.1;


%%
T0_Ini=['\n# SurfMesh---------------- \n'];

T0_Base=['p = mdb.models[' char(39) 'Model-1' char(39) ...
    '].parts[' char(39) 'Part-Base' char(39) '] \n'];
T1_MeshProp=['p.seedPart(size=%8.4e, deviationFactor=%8.4e, minSizeFactor=%8.4e) \n'];
T1_Face=['f = p.faces \n'];


% T1_Base={['p = mdb.models[' char(39) 'Model-1' char(39) ...
%     '].parts[' char(39) 'Part-Base' char(39) '] \n'];...
%     ['f = p.faces \n'];...
%     };

T2_PickRegion=['pickedRegions = f.getByBoundingBox(' ...
    'xMin=%8.4e, yMin=%8.4e, xMax=%8.4e,yMax=%8.4e) \n'];

T3_GenerateMesh={['p.setMeshControls(regions=pickedRegions, ' ...
    'elemShape=QUAD) \n'];...
    ['p = mdb.models[' char(39) 'Model-1' char(39) ...
    '].parts[' char(39) 'Part-Base' char(39) '] \n'];...
    ['p.generateMesh() \n\n'];...
    };


%%

%%
OutputFileName='WTest0.py';
fileID = fopen(OutputFileName,'a+');

fprintf(fileID,T0_Ini);
fprintf(fileID,T1_MeshProp,MeshSize,MeshDevFac,MeshMinFac);
fprintf(fileID,T1_Face);

% for n1=1:length(T1_Base)
%     fprintf(fileID,T1_Base{n1});
% end

fprintf(fileID,T2_PickRegion,...
    CreateRec(1),CreateRec(2),CreateRec(3),CreateRec(4));

for n1=1:length(T3_GenerateMesh)
    fprintf(fileID,T3_GenerateMesh{n1});
end
%%

fclose(fileID);


%{
p = mdb.models['Model-1'].parts['Part-Base']
    p.seedPart(size=5.0, deviationFactor=0.1, minSizeFactor=0.1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1632.06, 
        farPlane=1879.52, width=1374.27, height=717.921, viewOffsetX=185.351, 
        viewOffsetY=-86.7868)
    p = mdb.models['Model-1'].parts['Part-Base']
    f = p.faces
    pickedRegions = f.getSequenceFromMask(mask=('[#ffffffff #3ff ]', ), )
    p.setMeshControls(regions=pickedRegions, elemShape=QUAD)
    p = mdb.models['Model-1'].parts['Part-Base']
    p.generateMesh()
%}