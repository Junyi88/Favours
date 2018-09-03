clear;

OutputFileName='WTest0.py';
fileID = fopen(OutputFileName,'a+');

%%
load ../Step2_Data.mat;
% W1F_CDatum(fileID,V,LineList,[0 50]);

% W1F_DatumPoints(fileID,V,[0 50]);

[dCount]=W1F_DatumPoints(fileID,VShort,[0 50]);
W1F_DatumPlane(fileID,VShort,ShortList2);

%%
fclose(fileID);