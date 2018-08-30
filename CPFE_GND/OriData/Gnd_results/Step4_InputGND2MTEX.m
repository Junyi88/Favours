%% plotting convention
setMTEXpref('xAxisDirection','east');
setMTEXpref('zAxisDirection','intoPlane');

%%
ebsd_smoothed = ebsd_smoothed.gridify;

% Linear interpolate 2 matix: GND and ebsd_smoothed
[y1,x1]=size(GND_total);
[y2,x2]=size(ebsd_smoothed.grainId);

%Interpolate
x_new=linspace(1,x1,x2)
y_new=linspace(1,y1,y2)
[X_NEW,Y_NEW]=meshgrid(x_new,y_new);
GND_total_interpolated = interp2(GND_total,X_NEW,Y_NEW)

%% Input GND data to EBSD map
ebsd_smoothed.prop.GND=log10(GND_total_interpolated); %this is not ideal, but we will cope - care with axes!
ebsd_smoothed.GND(ebsd_smoothed.GND == -inf) = nan;

%% plot the GND data
FigH.GNDg=figure;
plot(ebsd_smoothed,ebsd_smoothed.GND);
mtexColorbar;
colormap('Parula'); 
caxis([12 16])
% CAxis range is 10^13 to 10^15 dislocations per m^2, unit is 'log10(m^{-2})'
% Jet is not a great colour scale, but I'm being lazy here
% You can find out about good use of colours in a few articles linked here
% http://www2.expmicromech.com/resources#TOC-Representing-Data
%title('GND (log10(m^{-2}))','FontSize',24);

% overlay the grain boundaries
hold on; 
plot(grains.boundary,'linewidth',2.0); 
hold off;

%% Saving
resultsdir=fullfile([pname1 '\gnd_results']);%resultsdir=fullfile(pname,'results',fname(1:end-3));
if isdir(resultsdir) == 0; mkdir(resultsdir); end

%GND with grain boundaries
print(FigH.GNDg,fullfile(resultsdir,['Map_GNDg_' fname(end-11:end-3) '.png']),'-dpng','-r600');
savefig(FigH.GNDg,fullfile(resultsdir,['Map_GNDg_' fname(end-11:end-3)]));

%Save workspace
close all
save(fullfile(resultsdir,'4_GNDinMTEX.mat'));

%% copy this m file over, for archival purposes
mf_long=mfilename('fullpath');
[f1,f2,f3]=fileparts(mf_long);
mf_start=[mf_long '.m'];
mf_end=fullfile(resultsdir,[f2 '.m']);
try
copyfile(mf_start,mf_end)
catch
    warning('m file not saved, likely due to spaces in the file name');
end