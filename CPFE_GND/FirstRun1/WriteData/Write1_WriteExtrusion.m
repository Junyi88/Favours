clear;

OutputFileName='WTest0.py';
fileID = fopen(OutputFileName,'a+');

%%
load ../Step2_Data.mat;
% W1F_CDatum(fileID,V,LineList,[0 50]);

W1F_DatumPoints(fileID,V,[0 50]);




%%
fclose(fileID);