clear;

OutputFileName='WTest0.py';

PreambleText=[{'from part import * \n'}; ...
    {'from material import * \n'};...
    {'from section import * \n'};...
    {'from assembly import * \n'};...
    {'from step import * \n'};...
    {'from interaction import * \n'};...
    {'from load import * \n'};...
    {'from mesh import * \n'};...
    {'from job import * \n'};...
    {'from sketch import * \n'};...
    {'from visualization import * \n'};...
    {'from connectorBehavior import * \n'};...  % ___
    {'from regionToolset import * \n'};...
    {' \n'}; ...
    {'# Completed Preamble \n'};...
    ];


fileID = fopen(OutputFileName,'w+');

for n1=1:length(PreambleText)
    fprintf(fileID,PreambleText{n1});
end

fclose(fileID);