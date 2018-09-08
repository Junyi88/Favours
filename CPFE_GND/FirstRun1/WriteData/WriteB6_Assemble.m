clear;

%%
OutputFileName='WTest0.py';
%%
% load Write1_Dat CreateRec;
load WriteB4_Data HasGrain NGrains;

%%
% load ../Step2_Data.mat sGB;
% load ../Step1_Data.mat grains;

%%
T0_Preamble=['\n \n# Assembly------------------ \n'];

T1_Text=['\n \n# Adding Grain %d ---------------------- \n'];
T1_Root=['a = mdb.models[' char(39) 'Model-1' char(39) '].rootAssembly \n'];
T1_SetPart=['p = mdb.models[' char(39) 'Model-1' char(39) ...
    '].parts[' char(39) 'Grain-%d' char(39) '] \n']; %NGrain
T1_AddPart=['a.Instance(name=' char(39) 'Grain-%d-1' char(39) ...
    ', part=p, dependent=ON) \n']; %NGrain

%%
T2_Text=['\n \n# Combine Stuff ---------------------- \n'];
T2_Init=['a.InstanceFromBooleanMerge(name=' char(39) 'Poly-Grain' char(39) ', instances=(\n\t'];
T2_AddPart=['a.instances[' char(39) 'Grain-%d-1' char(39) '],\n\t']; %NGrain
T2_Close=['),mergeNodes=ALL, nodeMergingTolerance=1e-06, domain=MESH,\n\t'];
T2_Finish=['originalInstances=SUPPRESS)\n'];


%%
T3_Text=['\n \n# Write Output ---------------------- \n'];
T3_OffParts=['mdb.models[' char(39) 'Model-1' char(39) ...
    '].setValues(noPartsInputFile=ON)\n'];
% T1_Root=['a = mdb.models[' char(39) 'Model-1' char(39) '].rootAssembly \n'];

T3_Step=['mdb.models[' char(39) 'Model-1' char(39) ...
    '].StaticStep(name=' char(39) 'Step-1' char(39) ...
    ', previous=' char(39) 'Initial' char(39) ')\n'];

T3_Job={['mdb.Job(name=' char(39) 'ExtractForPoints-1' char(39) ', model=' char(39) ...
    'Model-1' char(39) ', description=' char(39) char(39) ', type=ANALYSIS,\n\t'];...
    ['atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, \n\t'];...
    ['memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, \n\t'];...
    ['explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, \n\t'];...
    ['modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine=' ...
    char(39) char(39) ',\n\t'];...
    ['scratch=' char(39) char(39) ...
    ', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1,\n\t'];...
    ['numGPUs=0) \n\n']; ...
    };
T3_Write=['mdb.jobs[' char(39) 'ExtractForPoints-1' char(39) ...
    '].writeInput(consistencyChecking=OFF) \n\n'];
%%
fileID = fopen(OutputFileName,'a+');

fprintf(fileID,T0_Preamble);

for n1=1:NGrains
if HasGrain(n1)
fprintf(fileID,T1_Text,n1);    
fprintf(fileID,T1_Root);    
fprintf(fileID,T1_SetPart,n1);   
fprintf(fileID,T1_AddPart,n1);
end
end

% ---
fprintf(fileID,T2_Text);  
fprintf(fileID,T2_Init); 
for n1=1:NGrains
if HasGrain(n1)
fprintf(fileID,T2_AddPart,n1);    
end
end
fprintf(fileID,T2_Close); 
fprintf(fileID,T2_Finish); 

%%
fprintf(fileID,T3_Text);  
fprintf(fileID,T3_OffParts); 
fprintf(fileID,T1_Root); 
fprintf(fileID,T3_Step); 
for n1=1:length(T3_Job)
    fprintf(fileID,T3_Job{n1}); 
end

fprintf(fileID,T3_Write); 

%%

fprintf(fileID,' \n');
fclose(fileID);

%{
p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Part-2-Copy-mesh-1']
    a.Instance(name='Part-2-Copy-mesh-1-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['Part-2-mesh-1']
    a.Instance(name='Part-2-mesh-1-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=88.1207, 
        farPlane=144.747, width=104.949, height=47.9318, viewOffsetX=16.6935, 
        viewOffsetY=-0.568226)
    a = mdb.models['Model-1'].rootAssembly
%}

%{
a.InstanceFromBooleanMerge(name='Part-3', instances=(
        a.instances['Part-2-Copy-mesh-1-1'], a.instances['Part-2-mesh-1-1'], ), 
        mergeNodes=ALL, nodeMergingTolerance=1e-06, domain=MESH, 
        originalInstances=SUPPRESS)
%}


%{
    mdb.models['Model-1'].setValues(noPartsInputFile=ON)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=OFF)
    mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
        numGPUs=0)
    mdb.jobs['Job-1'].writeInput(consistencyChecking=OFF)
%}