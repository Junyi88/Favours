function [Sets]=GetChainGB(gB,nG)

%% Description
%{ 
This is a function extracts the vertices in a function and put them 
in a closed loop. This is so that we can remove

Input:
gB = grains(nG).boundary  % where nG is the grain id
nG = grainID % Mainly for debugging

% Notes
gB.F is an [N by 2] matrix that stores the two vertice ids for each line
gB.V is an [N by 2] matrix that stores the coordinates of the vertices

%}


%%
F=gB.F; % This is the lines

%% Now to get the chain
% The algorithm is simple 
%{
1) We take a current point in our chain 
2) We then find that point in F and the the vertice at the other column
3) We then put that value into our chain
4) We then remove that row
5) Repeat until no rows are left
%}

%% We initialise the chain with the first two points
nSets=1;

count=1;
Sets(nSets).Chain(count)=F(1,1);
count=count+1;
Sets(nSets).Chain(count)=F(1,2);
RemoveItem=zeros(size(F,1),1);
RemoveItem(1)=1;
F=F(~RemoveItem,:);

%% Now we loop until we get the chains
while (~isempty(F))
    currentV=Sets(nSets).Chain(count);
    count=count+1;
    [row,col]=find(F==currentV);
    RemoveItem=zeros(size(F,1),1);
    if col==1
        Sets(nSets).Chain(count)=F(row,2);
        RemoveItem(row)=1;
        F=F(~RemoveItem,:);
    elseif col==2
        Sets(nSets).Chain(count)=F(row,1);
        RemoveItem(row)=1;
        F=F(~RemoveItem,:);
    else
        % This means that there is an inner grain so we have to put it into
        % a diffferent set
        nSets=nSets+1;
        count=1;
        Sets(nSets).Chain(count)=F(1,1);
        count=count+1;
        Sets(nSets).Chain(count)=F(1,2);
        RemoveItem=zeros(size(F,1),1);
        RemoveItem(1)=1;
        F=F(~RemoveItem,:);
        
        %disp(['Error:GetChainGB: Cannot link chain at grain ' num2str(nG)]);
        %break;
    end
    
end

%% The last point should be the same in a loop
for nS=1:nSets
    if Sets(nS).Chain(1)==Sets(nS).Chain(end)
%         Sets(nS).Chain=Sets(nS).Chain(1:end-1);
    else
        disp(['Warning:GetChainGB: This is an open loop at grain' num2str(nG)]);
    end
end
end