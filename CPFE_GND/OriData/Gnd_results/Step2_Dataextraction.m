% x=min(ebsd.x):5:max(ebsd.x);
% y=min(ebsd.y):5:max(ebsd.y);

%%
% clear;
% load 1_Smoothing_Fill;
% % close all

x = ebsdOriginal.x;
y = ebsdOriginal.y;
num_row = size(find(y==x(2)),1);
num_col = size(find(x==x(2)),1);
X = reshape(x,num_row, num_col)';
Y = reshape(y,num_row, num_col)';

% [X,Y]=meshgrid(x,y);

[NY,NX]=size(X);
phi1=zeros(NY,NX);
phi2=zeros(NY,NX);
Phi=zeros(NY,NX);
IQ=zeros(NY,NX);
GrainID=zeros(NY,NX);

for ny=1:NY
    for nx=1:NX
        id=ebsd_smoothed.findByLocation([X(ny,nx) Y(ny,nx)]);
        if isempty(id)== 0
            phi1(ny,nx)=ebsd_smoothed(id).orientations.phi1;
            phi2(ny,nx)=ebsd_smoothed(id).orientations.phi2;
            Phi(ny,nx)=ebsd_smoothed(id).orientations.Phi;
            
            GrainID(ny,nx)=ebsd_smoothed(id).grainId;
            IQ(ny,nx)=ebsd_smoothed(id).bc;
            
            %         if isnan(IQ(ny,nx))
            %            IQ(ny,nx)=0;
            %         end
            
        elseif isempty(id) == 1
            phi1(ny,nx)=NaN;
            phi2(ny,nx)=NaN;
            Phi(ny,nx)=NaN;
            GrainID(ny,nx)=NaN;
            IQ(ny,nx)=NaN;
        end
    end
    disp(ny);
end

for ny=1:NY
    for nx=1:NX
        if isnan(IQ(ny,nx))
            IQ(ny,nx)=0;
        end
    end
    disp(ny);
end
Phi1=phi1.*180./pi;
Phi2=phi2.*180./pi;
Phi=Phi.*180./pi;

resultsdir=fullfile([pname1 '\gnd_results']);%resultsdir=fullfile(pname,'results',fname(1:end-3));
if isdir(resultsdir) == 0; mkdir(resultsdir); end

%% Saving
save(fullfile(resultsdir, '2_Data4GNDcal.mat')); %Change the .mat name here

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



%%
% save 2_Data4GNDcal.mat X Y Phi Phi1 Phi2 IQ GrainID grains;
% save 2_Data4GNDcal_all.mat


% Y = NY - Y % Correct the Y-axis of the figure

% %% Plot
% figure(2);
% clf;
% surf(X,Y,Phi2,'EdgeColor','none');
% caxis([0 360])
% colorbar;
% title(['\Phi_2 (^o)']);
% view([0 90]);
% xlim([0 NX]);
% ylim([0 NY]);
% % pbaspect([1 1 1]);  
% 
% figure(1);
% clf;
% surf(X,Y,Phi1,'EdgeColor','none');
% caxis([0 360])
% colorbar;
% title(['\Phi_1 (^o)']);
% view([0 90]);
% xlim([0 NX]);
% ylim([0 NY]);
% % pbaspect([1 1 1]); 
% 
% figure(3);
% clf;
% surf(X,Y,Phi,'EdgeColor','none');
% caxis([0 360])
% colorbar;
% title(['\Phi (^o)']);
% view([0 90]);
% xlim([0 NX]);
% ylim([0 NY]);
% % pbaspect([1 1 1]); 