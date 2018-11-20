clear;

run SetPathForMTex.m; % Start MTex

%% Load the data that has already been processed previously

% GND_total = GND values
% grains = Grains used to get the grain data
% X, Y = are the X and Y data

% load 4_GNDinMTEX2.mat GND_total grains X Y;
load 4_GNDinMTEXinit.mat GND_total grains X Y;

save Step1_Data;