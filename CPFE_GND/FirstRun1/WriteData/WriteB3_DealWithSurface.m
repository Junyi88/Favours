clear;

OutputFileName='WTest0.py';
% fileID = fopen(OutputFileName,'a+');

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


T0_Preamble=['\n \n# Create Surfaces --------- \n'];
T0_BaseText={['p = mdb.models[' char(39) 'Model-1' ...
    char(39) '].parts[' char(39) 'Part-Base' char(39) '] \n'];...
    ['s = p.faces \n'];
    };
T1_FindFace=['side1Faces = s.findAt(((%8.4e, %8.4e, 0.0), ),) \n']; % x y
T2_MakeFaces=['p.Surface(side1Faces=side1Faces, name=' char(39)  ...
    'Surf-%d' char(39) ') \n']; % Surf number

%%

fileID = fopen(OutputFileName,'a+');

fprintf(fileID,T0_Preamble);

for n1=1:NGrains
    for n2=1:length(T0_BaseText)
        %fprintf(fileID,FMT,g);
        fprintf(fileID,T0_BaseText{n2});
    end
    
    fprintf(fileID,T1_FindFace,GrainMid(n1,1),GrainMid(n1,2));
    fprintf(fileID,T2_MakeFaces,n1);
end
% fprintf(fileID,T1_FindFace);

fprintf(fileID,' \n');
fclose(fileID);


%%
%{
p = mdb.models['Model-1'].parts['Part-2']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#2 ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-1')
faces = f.findAt(((-16.438578, -41.835673, -24.19804), ),)
%}