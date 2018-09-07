clear;

DepVar=89;
% NConst=10;
OutputFileName='WTest0.py';
%%
load Write1_Dat CreateRec;
load WriteB4_Data HasGrain NGrains;

%%
load ../Step2_Data.mat sGB;
load ../Step1_Data.mat grains;


%%
RMat=2.0.*ones(NGrains,10);

for n1=1:NGrains
      
        a1=grains.meanOrientation.phi1(n1);
        a2=grains.meanOrientation.Phi(n1);
        a3=grains.meanOrientation.phi2(n1);
        
%         R1=[cos(a1) -sin(a1) 0; sin(a1) cos(a1) 0; 0 0 1];
%         R2=[cos(a2) 0 sin(a2); 0 1 0; -sin(a2) 0 cos(a2)];
%         R3=[cos(a3) -sin(a3) 0; sin(a3) cos(a3) 0; 0 0 1];
        
%         NoX=R3*(R2*(R1*nox));
%         NoY=R3*(R2*(R1*noy));
   
        R1=[cos(a1) sin(a1) 0; -sin(a1) cos(a1) 0; 0 0 1];
        R2=[1 0 0; 0 cos(a2) sin(a2); 0 -sin(a2) cos(a2)];
        R3=[cos(a3) sin(a3) 0; -sin(a3) cos(a3) 0; 0 0 1];
        g = R3*R2*R1;
        RMat(n1,2:10)=g(:);
end

%%
T0_Preamble=['\n \n# Add Materials------------------ \n'];

T1_Text=['\n \n# Generating Grain %d ---------------------- \n'];
T1_Generate=['mdb.models[' char(39) 'Model-1' char(39) ...
    '].Material(name=' char(39) 'Material-%d' char(39) ') \n']; %NGrains
T1_DepVar=['mdb.models[' char(39) 'Model-1' char(39) ...
    '].materials[' char(39) 'Material-%d' char(39) '].Depvar(n=%d)\n']; % NGrain Depvar
T1_Constants=['mdb.models[' char(39) 'Model-1' char(39) '].materials[' ...
    char(39) 'Material-%d' char(39) '].UserMaterial(\n\t' ...
        'mechanicalConstants=(%8.4e,\n\t' ...
        '%12.8e, %12.8e, %12.8e,\n\t' ...
        '%12.8e, %12.8e, %12.8e,\n\t' ...
        '%12.8e, %12.8e, %12.8e))'];
    % Ngrain val RMat
%%
fileID = fopen(OutputFileName,'a+');

fprintf(fileID,T0_Preamble);

for n1=1:NGrains
fprintf(fileID,T1_Text,n1);    
fprintf(fileID,T1_Generate,n1);    
fprintf(fileID,T1_DepVar,n1,DepVar);   
fprintf(fileID,T1_Constants,n1,RMat(n1,:));

end
fprintf(fileID,' \n');
fclose(fileID);

%%
%{
    mdb.models['Model-1'].Material(name='Material-1')
    mdb.models['Model-1'].materials['Material-1'].Depvar(n=5)
    mdb.models['Model-1'].materials['Material-1'].UserMaterial(
        mechanicalConstants=(1.0, 2.0, 3.0, 4.0, 5.0))
%}

%{
*USER MATERIAL, CONSTANTS=10
2.00000000, 0.36810619, -0.50358516, -0.78160081, 0.64868606, -0.46314095, 0.60390964, -0.66611128, 
-0.72931642, 0.15618362
 %}