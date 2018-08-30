% Calculate GND density based on Euler anlges determined in Hough domain
% Created by Jun Jiang, 10/12/2015

% load cft file into Matlab

% Bruker_file= 'D:\IC PhD\Year1 PhD\Exp Results\EBSD_Auriga\20171102_cp al rolled edge\CP Al cross section.txt';
% Bruker_file='Myfile.txt';
% clear; 
% 
% load('D:\IC PhD\Year1 PhD\Exp Results\EBSD_Hitachi\Edge surface\GND Cal\GND_Smooth\2_Data4GNDcal.mat');
% % [X, Y, Phi1, Phi, Phi2, GrainID, IQ]= Text_reader_Bruker(Bruker_file);
XX=X;
YY=Y;

[Temp1,Temp2]=size(X);
Y=1:Temp1;
X=1:Temp2;
[X,Y]=meshgrid(X,Y);

X=X-1;
Y=Y-1;

clear Temp1 Temp2;
%% Change the step size here
stepsize = 3e-6;  %m nominal stepsize
% determine the crystal orientation matrix according to Ben's tutorial
% paper
%%
[num_row, num_col] = size(Phi);

for i=1:num_row
    for j=1:num_col
        Rz_phi2{i,j} = [cosd(Phi2(i,j)), sind(Phi2(i,j)), 0; -sind(Phi2(i,j)), cosd(Phi2(i,j)),0; 0, 0, 1];
        Rx_phi{i,j}  = [1, 0, 0; 0, cosd(Phi(i,j)), sind(Phi(i,j)); 0, -sind(Phi(i,j)), cosd(Phi(i,j))];
        Rz_phi1{i,j}= [cosd(Phi1(i,j)), sind(Phi1(i,j)), 0; -sind(Phi1(i,j)), cosd(Phi1(i,j)),0; 0, 0, 1];
        
        O{i,j} = Rz_phi2{i,j}*Rx_phi{i,j}*Rz_phi1{i,j}; % determine the orientation matrix
    end
end

% determine the misorientation within the grains
% select a reference point within each grain

for n=1:max(GrainID(:))
    if isempty(IQ(GrainID==n))~=1
        [~,ref_IQ] = max(IQ(GrainID==n));
        X_ref     =   X(GrainID ==n)+1;
        Y_ref     =   Y(GrainID ==n)+1;
        
        ref_point(n,2) = X_ref(ref_IQ);
        ref_point(n,1) = Y_ref(ref_IQ);
    else
        ref_point(n,1:2) = NaN;
    end
    if isempty(IQ(GrainID==n))~=1
        for k=1:numel(IQ(GrainID==n))
            misorientation{Y_ref(k), X_ref(k)}= O{ref_point(n,1),ref_point(n,2)}*O{Y_ref(k), X_ref(k)}';
        end
    [GND_B{n},GND_Burgers{n},GND_BurgLength{n},GND_Line{n},GND_Sliplabels{n},GND_Weights{n}] = lBurgLine('Aluminium',O{ref_point(n,1),ref_point(n,2)});
%     GND_Weights{ref}([1 4 7 10 13 34 37 40 43 46])=10*GND_Weights{ref}([1 4 7 10 13 34 37 40 43 46]);
    GND_LB{n}=zeros(size(GND_Burgers{n},2),1);
    end
end
% determine Nye's tensor components according to Jun's thesis 
for i=1:num_row
    for j=1:num_col
        if isempty(misorientation{i,j})~=1
        a12(i,j) = misorientation{i,j}(1,3)/stepsize;
        a13(i,j) = misorientation{i,j}(2,1)/stepsize;
        a21(i,j) = misorientation{i,j}(3,2)/stepsize;
        a23(i,j) = misorientation{i,j}(2,1)/stepsize;
        a33(i,j) = misorientation{i,j}(3,1)/stepsize-misorientation{i,j}(3,2)/stepsize;
        a11_a22(i,j) = -misorientation{i,j}(1,3)/stepsize-misorientation{i,j}(2,3)/stepsize;
        else 
        a12(i,j) = NaN;
        a13(i,j) = NaN;
        a21(i,j) = NaN;
        a23(i,j) = NaN;
        a33(i,j) = NaN;
        a11_a22(i,j) = NaN;
        end 
    end
end

% determine the GND density from Curl(F), it should be very small ~noise
% for single clip sum(kron(b*rho')) = curl(F) = 0

% dislocation line vector is euqal to cross product of slip plane and slip direction

 %preset items for the linprog command % got from TBB's XEBSD 
options = optimset('Display', 'off','LargeScale', 'on','UseParallel','always'); %suppress 'optimization terminated' messages

%generate the b and l vectors for all the references
%populate the B matrix
%populate the weighting vector


GND_rho=zeros(num_row,num_col,size(GND_Burgers{1},2)/2);
GND_exittest=zeros(num_row,num_col);
GND_total=zeros(num_row,num_col);

GND_rho = zeros(num_row,num_col,18);

for x=1:num_row
    for y=1:num_col
        grain_id=GrainID(x,y);
        if isempty(IQ(GrainID==grain_id)) ~=1 & GrainID(x,y)>0
            %at each point solve:
            %GND_B . GND_rho = GND_Lambda
            
            %GND_Lambda = curvature vector;
            %order of terms:
            %dw23/dx1, dw31/dx1, dw12/dx1
            %dw23/dx2, dw31/dx2, dw12/dx2
            % a12, a13, a21, a23,a33,a11_a22;
            %this is equivelent to:
            %GND_Lambda = [squeeze(Grad_X(y,x,:));squeeze(Grad_Y(y,x,:))];
            GND_Lambda = [a12(x,y), a13(x,y), a21(x,y), a23(x,y), a33(x,y), a11_a22(x,y)];
            
            %GND_B is set above for each grain
            [GND_full,~,GND_exittest(x,y)] = linprog(GND_Weights{grain_id},[],[],GND_B{grain_id},GND_Lambda,GND_LB{grain_id},[],[],options);
            GND_fold=reshape(GND_full,size(GND_full,1)/2,2);
            GND_fold(:,2)=-GND_fold(:,2);
            GND_rho(x,y,:)=sum(GND_fold,2)./(GND_BurgLength{grain_id}*1e-9);
            GND_total(x,y)=sum(abs(GND_rho(x,y,:)));   
        end
    end
      disp(x);
end

%Be careful here!!! Turn data upside down- care with axes!
% GND_Total=flipud(GND_total) %


[NY, NX]= size(GND_total)

%% Saving
resultsdir=fullfile([pname1 '\gnd_results']);%resultsdir=fullfile(pname,'results',fname(1:end-3));
if isdir(resultsdir) == 0; mkdir(resultsdir); end

save(fullfile(resultsdir, '3_GND_Smoothing.mat')); %Change the .mat name here
csvwrite([resultsdir '\rho.csv'],GND_total);
csvwrite([resultsdir '\theta.csv'],Phi2);


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




%% figures to verify the results
% figure(1);
% clf;
% surf(X,Y,GND_total,'EdgeColor','none');
% caxis([0 15*10^14])
% colorbar;
% title(['\rho_{GND} (/m^2)']);
% view([0 90]);
% xlim([0 NX]);
% ylim([0 NY]);
% % pbaspect([1 1 1]);        
% 
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


%% Saves 
% pname = 'D:\IC PhD\Year1 PhD\Exp Results\EBSD_Auriga\20171102_cp al rolled edge\GND_Smooth'
% csvwrite([pname '\rho.csv'],GND_total);
% csvwrite([pname '\theta.csv'],Phi2);
% saveas(figure(1),[pname '\\','CalGND_total'],'png')
% saveas(figure(2),[pname '\\','Theta_Phi2'],'png')
% 

%% Save workspace
% close all
% save(fullfile(resultsdir,'3_GND_Smoothing.mat'));
