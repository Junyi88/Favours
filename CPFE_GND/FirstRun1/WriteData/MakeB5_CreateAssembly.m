clear;

OutputFileName='WTest0.py';
% fileID = fopen(OutputFileName,'a+');

%%


%%
load ../Step2_Data.mat;

T0_Preamble=['\n \n# CreateInstances ----------- \n'];

%% 
T1_SelectPart=['p = mdb.models[' char(39) 'Model-1' ...
    char(39) '].parts[' char(39) 'Grain-%d' char(39) '] \n']; % Grain Num
T1_CreateIns=['a.Instance(name=' char(39) 'Grain-%d-1' char(39) ...
    ', part=p, dependent=ON) \n']; % Grain Num

%%
T2_SelectRoot=['a = mdb.models[' char(39) ...
    'Model-1' char(39) '].rootAssembly \n'];

T3_Start=['a.InstanceFromBooleanMerge(name=' char(39) ...
    'Combined-Part' char(39) ', instances=(\n'];
T3_Fill=['\ta.instances[' char(39) 'Grain-%d-1' char(39) '], \n']; % Grain num

T3_Close=['\t), mergeNodes=ALL, nodeMergingTolerance=1e-06, domain=MESH, \n' ... 
        '\toriginalInstances=SUPPRESS) \n \n'];
%{
    p = mdb.models['Model-1'].parts['Part-2-mesh-1']
    a.Instance(name='Part-2-mesh-1-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=88.1207, 
        farPlane=144.747, width=104.949, height=47.9318, viewOffsetX=16.6935, 
        viewOffsetY=-0.568226)
    a = mdb.models['Model-1'].rootAssembly
    a.InstanceFromBooleanMerge(name='Part-3', instances=(
        a.instances['Part-2-Copy-mesh-1-1'], a.instances['Part-2-mesh-1-1'], ), 
        mergeNodes=ALL, nodeMergingTolerance=1e-06, domain=MESH, 
        originalInstances=SUPPRESS)
    %}
        
%%
fileID = fopen(OutputFileName,'a+');

fprintf(fileID,T0_Preamble);

for n1=1:NGrains
    fprintf(fileID,T1_SelectPart,n1);
    fprintf(fileID,T1_CreateIns,n1);

end

fprintf(fileID,T2_SelectRoot);
fprintf(fileID,T3_Start);

for n1=1:NGrains
    fprintf(fileID,T3_Fill,n1);
    fprintf(fileID,T1_CreateIns,n1);

end

fprintf(fileID,T3_Close);
fprintf(fileID,' \n');
fclose(fileID);

