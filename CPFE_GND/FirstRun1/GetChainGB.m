function [Chain]=GetChainGB(gB,nG)

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
V=gB.V; % This is the vertices

%% Now to get the chain

% This is the output that stores all the vertice ids in a chain
Chain=zeros(size(F,1)+1,1); 

%% The algorithm is simple 
%{
1) We take a current point in our chain 
2) We then find that point in F and the the vertice at the other column
3) We then put that value into our chain
4) We then remove that row
5) Repeat until no rows are left
%}

%% We initialise the chain with the first two points
count=1;
Chain(count)=F(1,1);
count=count+1;
Chain(count)=F(1,2);
RemoveItem=zeros(size(F,1),1);
RemoveItem(1)=1;
F=F(~RemoveItem,:);

%% Now we loop until we get the chains
while (~isempty(F))
    currentV=Chain(count);
    count=count+1;
    [row,col]=find(F==currentV);
    RemoveItem=zeros(size(F,1),1);
    if col==1
        Chain(count)=F(row,2);
    elseif col==2
        Chain(count)=F(row,1);        
    else
        disp(['Error:GetChainGB: Cannot link chain at grain ' num2str(nG)]);
        break;
    end
    RemoveItem(row)=1;
    F=F(~RemoveItem,:);
end

%% The last point should be the same in a loop
if Chain(1)==Chain(end)
    Chain=Chain(1:end-1);
else
    disp(['Warning:GetChainGB: This is an open loop at grain' num2str(nG)]);
end

end