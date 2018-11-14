clear;

OutputFileName='WTest0.py';
% fileID = fopen(OutputFileName,'a+');
load Write1_Dat CreateRec;
%%
ZThickness=10.0;
NLayer=5;

MyBounds=[0.0 0.0 10.0 10.0];
% CreateRec=[10,10,740,570];
xMin=CreateRec(1);
xMax=CreateRec(3);
yMin=CreateRec(2);
yMax=CreateRec(4);

%%
load ../Step2_Data.mat;
NGrains=length(ShortList2.Grain);
GrainMid=zeros(NGrains,2);

for n1=1:NGrains
   tt=sGB(n1).Chain;
   xx=V(tt,1);
   yy=V(tt,2);
   GrainMid(n1,:)=[mean(xx) mean(yy)];
    
end

% Correction
% GrainMid(15,1)=735;
% GrainMid(23,2)=250;
% GrainMid(26,2)=230;
%%
T0_Preamble=['\n \n# Make Parts ------------------ \n'];

%% Copy Part
% COPY
%{
    p = mdb.models['Model-1'].Part(name='Part-2-Copy', 
        objectToCopy=mdb.models['Model-1'].parts['Part-2'])
%}
T1_Text=['\n \n# Generating Grain %d ---------------------- \n'];
T1_CopyPart=['p = mdb.models[' char(39) 'Model-1' char(39) ...
    '].Part(name=' char(39) 'Part-Temp' char(39) ...
    ', objectToCopy=mdb.models[' char(39) ...
    'Model-1' char(39) '].parts[' char(39) 'Part-Base' char(39) ']) \n'];


%% Create Bottom Up Mesh

T2_SetupBot={['p = mdb.models[' char(39) 'Model-1' char(39) ...
    '].parts[' char(39) 'Part-Temp' char(39) '] \n']; ...
    ['f = p.faces \n']; };

T2_GetFaces=['faces = f.findAt(((%8.4e, %8.4e, 0.0), ),) \n']; %xC yC
T2_GetSource=['pickedGeomSourceSide=regionToolset.Region(faces=faces) \n'];
T2_SetVector=['vector =((0.0, 0.0, 0.0), (0.0, 0.0, %8.4e)) \n']; % Zcal

T2_GenerateMesh=['p.generateBottomUpExtrudedMesh(' ...
    'geometrySourceSide=pickedGeomSourceSide, ' ...
        'extrudeVector=vector, numberOfLayers=%d) \n']; % NUMLAYER

T2_DeleteMesh=['p.deleteMesh() \n'];    
    
% BottomUP
%{
    p = mdb.models['Model-1'].parts['Part-2']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#2 ]', ), )
    pickedGeomSourceSide=regionToolset.Region(faces=faces)
    vector =((0.0, 0.0, 0.0), (0.0, 0.0, 2.0))
    p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, 
        extrudeVector=vector, numberOfLayers=2)
    p = mdb.models['Model-1'].parts['Part-2']
    e = p.elements
    elements = e.getSequenceFromMask(mask=('[#0:3 #fffe0000 #ffffffff:2 #1f ]', ), 
        )
    p.Set(elements=elements, name='BottomUpElements-1')
%}

% DELETE MESH
% p = mdb.models['Model-1'].parts['Part-2']
%     p.deleteMesh()

%%

T3_SetVal=['p = mdb.models[' char(39) 'Model-1' char(39) ...
    '].parts[' char(39) 'Part-Temp' char(39) '] \n'];

T3_CreatePart=['p.PartFromMesh(name=' char(39) 'Grain-%d' char(39) ...
    ', copySets=True) \n']; % Grain Number

T3_DeleteOld=['del mdb.models[' char(39) 'Model-1' ...
    char(39) '].parts[' char(39) 'Part-Temp' char(39) '] \n'];


% CREATE MESH PART
%{
p = mdb.models['Model-1'].parts['Part-2']
    p.PartFromMesh(name='Part-2-mesh-1', copySets=True)
    p1 = mdb.models['Model-1'].parts['Part-2-mesh-1']

remove surface sets
    mdb.models['Model-1'].parts['Part-3'].deleteSets(setNames=('Surf-2', 'Surf-1', 
        ))

del mdb.models['Model-1'].parts['Part-2-mesh-1'].sets['Surf-2']
%}


%%

% Pick one
T4_ElemType=['elemType1 = mesh.ElemType(elemCode=C3D20R, elemLibrary=STANDARD) \n']; 
T4_ElemType=['elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, ' ... 
        'secondOrderAccuracy=OFF, distortionControl=DEFAULT) \n']; 

%     
T4_Setup=['p = mdb.models[' char(39) 'Model-1' char(39) ...
    '].parts[' char(39) 'Grain-%d' char(39) '] \n']; % Grain Num
% T4_Setup2=['z1 = p.elements \n'];
% T4_PickElements=[elems1 = z1[0:84]]
T4_BuildStuff={['elems1 = p.elements \n'];... % Might have to remove this
    ['pickedRegions =(elems1, ) \n']; ...
    ['p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) \n']; ...
    };

% ELEMENT TYPE
%{  

elemType1 = mesh.ElemType(elemCode=C3D20R, elemLibrary=STANDARD)
    elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, 
        secondOrderAccuracy=OFF, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts['Part-2-mesh-1']
    z1 = p.elements
    elems1 = z1[0:84]
    pickedRegions =(elems1, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))

%}

%% Create Material
%{
    mdb.models['Model-1'].Material(name='Material-1')
    mdb.models['Model-1'].materials['Material-1'].Depvar(n=5)
    mdb.models['Model-1'].materials['Material-1'].UserMaterial(
        mechanicalConstants=(1.0, 2.0, 3.0, 4.0, 5.0))
        %}

%%
T5_CreateSection=['mdb.models[' char(39) 'Model-1' char(39) ...
    '].HomogeneousSolidSection(name=' char(39) 'Section-%d' char(39) ', ' ...
        'material=' char(39) 'Material-%d' ...
        char(39) ', thickness=None) \n']; % Grain number , grain number
T5_PickPart=['p = mdb.models[' char(39) ...
    'Model-1' char(39) '].parts[' char(39) 'Grain-%d' char(39) '] \n']; % grain number

T5_Element=['e = p.elements \n'];
T5_PickElement=['elements = e.getByBoundingBox(xMin=%8.4e , yMin=%8.4e , '... 
    'xMax=%8.4e , yMax=%8.4e ) \n']; % Xmin yMin xmax ymax
T5_Set=['region = p.Set(elements=elements, name=' char(39) ...
    'Set-El-%d' char(39) ') \n']; % Grain Number
T5_Assign=['p.SectionAssignment(region=region, ' ...
    'sectionName=' char(39) 'Section-%d' char(39) ', offset=0.0, ' ...
        'offsetType=MIDDLE_SURFACE, offsetField=' char(39) char(39) ', ' ...
        'thicknessAssignment=FROM_SECTION) \n']; % Grain Number
    
    
    
% SECTION
%{
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', 
        material='Material-1', thickness=None)
    p = mdb.models['Model-1'].parts['Part-2-mesh-1']
    e = p.elements
    elements = e.getSequenceFromMask(mask=('[#ffffffff:2 #fffff ]', ), )
    region = p.Set(elements=elements, name='Set-3')
    p = mdb.models['Model-1'].parts['Part-2-mesh-1']
    p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)

%}

% DELETE
% del mdb.models['Model-1'].parts['Part-2-Copy-Copy']


%% Start Stuff
fileID = fopen(OutputFileName,'a+');

fprintf(fileID,T0_Preamble);

HasGrain=false(NGrains,1);

for n1=1:NGrains
%     if true
   hasGrain=(GrainMid(n1,1)>=xMin)&&(GrainMid(n1,1)<=xMax)...
       &&(GrainMid(n1,2)>=yMin)&&(GrainMid(n1,2)<=yMax);
   if hasGrain
       HasGrain(n1)=true;
%    end
%    
%    if HasGrain(n1)
%% T1
fprintf(fileID,T1_Text,n1);  
fprintf(fileID,T1_CopyPart);    
    
%% T2
for n2=1:length(T2_SetupBot)
    fprintf(fileID,T2_SetupBot{n2});  
end

fprintf(fileID,T2_GetFaces,GrainMid(n1,1),GrainMid(n1,2));  
fprintf(fileID,T2_GetSource);  
fprintf(fileID,T2_SetVector,ZThickness); %ZThickness
fprintf(fileID,T2_GenerateMesh,NLayer); %NLayer
fprintf(fileID,T2_DeleteMesh);

%% T3
fprintf(fileID,T3_SetVal); 
fprintf(fileID,T3_CreatePart,n1); 
fprintf(fileID,T3_DeleteOld); 

%% T4
fprintf(fileID,T4_ElemType); 
fprintf(fileID,T4_Setup,n1); 
for n2=1:length(T4_BuildStuff)
    fprintf(fileID,T4_BuildStuff{n2});  
end

%% T5
fprintf(fileID,T5_CreateSection,n1,n1); 
fprintf(fileID,T5_PickPart,n1); 
fprintf(fileID,T5_Element); 

fprintf(fileID,T5_PickElement,xMin-10, yMin-10, xMax+10, yMax+10); 

fprintf(fileID,T5_Set,n1); 
fprintf(fileID,T5_Assign,n1); 
    end
end

fprintf(fileID,' \n');
fclose(fileID);

%%
figure(6);
clf;
hold on;
for n1=1:size(sGB0,2)
    EX=ShortChain.Grain(n1);
    for n2=1:length(EX.Set)
        f=EX.Set(n2).Chain;
    x=V(f,1);
    y=V(f,2);
    plot(x,y,'b-');
    end
    
    text(GrainMid(n1,1).*1.04,GrainMid(n1,2).*1.04,num2str(n1));
end

plot(GrainMid(:,1),GrainMid(:,2),'rx');
plot(GrainMid(53,1),GrainMid(53,2),'gs');
plot([xMin xMin],[yMin yMax],'k-');
plot([xMin xMax],[yMax yMax],'k-');
plot([xMax xMax],[yMax yMin],'k-');
plot([xMin xMax],[yMin yMin],'k-');

save WriteB4_Data HasGrain NGrains;