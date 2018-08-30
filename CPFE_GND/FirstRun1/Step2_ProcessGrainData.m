clear;

%% User Input Parameter
GrainSmoothFactor = 2; % This is a factor used to smooth the grains


%% Load Previous Step Data
load Step1_Data.mat;

%% First smooth the grains
if GrainSmoothFactor > 0
    grains =smooth(grains,GrainSmoothFactor);
end

%% Now we get the Chain
%{ 
We create a new object called sGB which stands for sorted grain boundaries
We then find the loop of lines for each chain
%} 

for nG=1:size(grains,1)
    [sGB0(nG).Sets]=GetChainGB(grains(nG).boundary,nG); 
    %sGB0 is because we want to remove the inner boundaries later
end

%% Now we remove the internal boundaries
% DANGER:Assumption: We assume that the inner boundary has a lower size
% compared to the outer boundaries

for nG=1:size(grains,1)
    [sGB0(nG).Sets]=GetChainGB(grains(nG).boundary,nG); 
    %sGB0 is because we want to remove the inner boundaries later
end

for n1=1:size(sGB0,2)

    SetSize=zeros(length(sGB0(n1).Sets),1);
    for n2=1:length(sGB0(n1).Sets)
        SetSize(n2)=length(sGB0(n1).Sets(n2).Chain);
    end
    [~,n2]=max(SetSize);
    sGB(n1).Chain=sGB0(n1).Sets(n2).Chain;
    
end


