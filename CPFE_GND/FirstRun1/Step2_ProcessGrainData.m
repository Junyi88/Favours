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

%%
V=grains.boundary.V;
F=grains.boundary.F;

Taken=zeros(length(F),1);
RedundantGrain=zeros(length(sGB0),1);

%%
for n1=1:size(sGB0,2)
   
    f=sGB(n1).Chain;
    f=[f f(1)];
    sGB(n1).Cut=zeros(length(f)-1,1);
    
    for n2=1:length(f)-1
        f0=f(n2);
        f1=f(n2+1);
        [row,col]=find(F==f0);
        for n3=1:length(row)
           
            r=row(n3);
            c=col(n3);
            
            if c==1
                f1c=F(r,2);
            elseif c==2
                f1c=F(r,1);
            end
            
            if f1c==f1
                if Taken(r)==1
                    sGB(n1).Cut(n2)=1;
                else 
                    Taken(r)=1;
                end
                
            end
            
        end
        
    end
    
end

%%
VXmin=0-0.1;%min(V(:,1));
VXmax=760+0.1;max(V(:,1));
VYmin=0-0.1;%min(V(:,2));
VYmax=567+0.1;max(V(:,2));

% VXmin=min(V(:,1));
% VXmax=max(V(:,1));
% VYmin=min(V(:,2));
% VYmax=max(V(:,2));

for n1=1:size(sGB0,2)
    f=sGB(n1).Chain;
    f=[f f(1)];
    count=0;
    sGB(n1).ToExt=zeros(length(sGB(n1).Cut),2);
    
    for n2=1:length(sGB(n1).Cut)
        
        if (sGB(n1).Cut(n2)~=1)
            NotEdge=true;
            x=V(f(n2),1);
            y=V(f(n2),2);
            if (x<=VXmin)||(x>=VXmax)||(y<=VYmin)||(y>=VYmax)
                NotEdge=false;
            end
            x=V(f(n2+1),1);
            y=V(f(n2+1),2);
            if (x<=VXmin)||(x>=VXmax)||(y<=VYmin)||(y>=VYmax)
                NotEdge=false;
            end
            
           if NotEdge
               count=count+1;
               sGB(n1).ToExt(count,:)=[f(n2),f(n2+1)];
           end
        end
        sGB(n1).ToExt=sGB(n1).ToExt(1:count,:);
    end
    
    
end

%%
for n1=1:size(sGB0,2)
%     sGB(n1).ToExt=zeros(length(sGB(n1).Cut),2);
    
    SCount=0;
    f0=-1;
    
    PCount=0;
    HIT=0;
    for n2=1:size(sGB(n1).ToExt,1)
       
        if f0==sGB(n1).ToExt(n2,1)
            PCount=PCount+1;
            NewChain.Grain(n1).Set(SCount).Chain(PCount)=f0; %sGB(n1).ToExt(n2,2);
            f0=sGB(n1).ToExt(n2,2);
        else
            
            if SCount>=1
                PCount=PCount+1;
                NewChain.Grain(n1).Set(SCount).Chain(PCount)=f0;
                NewChain.Grain(n1).Set(SCount).Chain=...
                    NewChain.Grain(n1).Set(SCount).Chain(1:PCount);
            end
            HIT=1;
            SCount=SCount+1;
            PCount=1;
            NewChain.Grain(n1).Set(SCount).Chain=zeros(size(sGB(n1).ToExt,1),1);
            f0=sGB(n1).ToExt(n2,2);
            NewChain.Grain(n1).Set(SCount).Chain(PCount)=sGB(n1).ToExt(n2,1);
        end    
        
    end

    
    if HIT==0
         NewChain.Grain(n1).Set(1).Chain=[];
         disp(n1);
    else
            PCount=PCount+1;
    NewChain.Grain(n1).Set(SCount).Chain(PCount)=f0;
    NewChain.Grain(n1).Set(SCount).Chain=...
                    NewChain.Grain(n1).Set(SCount).Chain(1:PCount);
    end
end
disp('STOP_HERE');
%%
% for n1=1:size(sGB0,2)
%    
%         
%      
%     t=logical(sGB(n1).Taken);
%     if sum(Taken(t))>0
%         RedundantGrain(n1)=1;
%     else
%         Taken(t)=1;
%     end
% end

%%
figure(1);
clf;
hold on;

for n1=1:size(sGB0,2)
    f=sGB(n1).Chain;
    x=V(f,1);
    y=V(f,2);
    
    plot(x,y,'bs-');
    
    x(logical(sGB(n1).Cut))=nan;
    y(logical(sGB(n1).Cut))=nan;
%     x=V(f,1);
%     y=V(f,2);
    
    
    plot(x,y,'rx-');
    
end

figure(2);
clf;
hold on;
for n1=1:size(sGB0,2)
    f=sGB(n1).Chain;
    x=V(f,1);
    y=V(f,2);
    
  
    
    x(logical(sGB(n1).Cut))=nan;
    y(logical(sGB(n1).Cut))=nan;
%     x=V(f,1);
%     y=V(f,2);
    
    
    plot(x,y,'r-');
    
end


figure(3);
% clf;
hold on;
for n1=1:size(sGB0,2)
    EX=sGB(n1).ToExt;
    for n2=1:length(EX)
        f=EX(n2,:);
    x=V(f,1);
    y=V(f,2);
    plot(x,y,'rx-');
    end
    
    
end


figure(4);
clf;
hold on;
for n1=1:size(sGB0,2)
    EX=NewChain.Grain(n1);
    for n2=1:length(EX.Set)
        f=EX.Set(n2).Chain;
    x=V(f,1);
    y=V(f,2);
    plot(x,y,'rx-');
    end
    
    
end

%%
disp('CONTINUE_HERE');
VCaps=false(size(V,1),1);
for n1=1:size(sGB0,2)
%     sGB(n1).ToExt=zeros(length(sGB(n1).Cut),2);
    
        EX=NewChain.Grain(n1);
    for n2=1:length(EX.Set)
        if ~isempty(NewChain.Grain(n1).Set(n2).Chain)
        f=[NewChain.Grain(n1).Set(n2).Chain(1) NewChain.Grain(n1).Set(n2).Chain(end)];
        VCaps(f)=true;
        end
    end
end
%% Deal With Cutting Later
NCut=7;

%%
for n1=1:size(sGB0,2)
%     sGB(n1).ToExt=zeros(length(sGB(n1).Cut),2);
    
%         EX=NewChain.Grain(n1);
    for n2=1:length(NewChain.Grain(n1).Set)
        %%
        ShortChain.Grain(n1).Set(n2).Chain=NewChain.Grain(n1).Set(n2).Chain;
        
        if length(ShortChain.Grain(n1).Set(n2).Chain)>=2
            CutCount=1;
            ItemCount=1;

            for n3=2:length(NewChain.Grain(n1).Set(n2).Chain)-1
                f=NewChain.Grain(n1).Set(n2).Chain(n3);
                if (VCaps(f))
                    ItemCount=ItemCount+1;
                    ShortChain.Grain(n1).Set(n2).Chain(ItemCount)=...
                            NewChain.Grain(n1).Set(n2).Chain(n3);
                else
                    if CutCount==NCut
                        ItemCount=ItemCount+1;
                        ShortChain.Grain(n1).Set(n2).Chain(ItemCount)=...
                            NewChain.Grain(n1).Set(n2).Chain(n3);
                        CutCount=1;
                    else
                        CutCount=CutCount+1;
                    end
                end
                
            end
            ItemCount=ItemCount+1;
            ShortChain.Grain(n1).Set(n2).Chain(ItemCount)=...
                    NewChain.Grain(n1).Set(n2).Chain(end);
             ShortChain.Grain(n1).Set(n2).Chain=...
                 ShortChain.Grain(n1).Set(n2).Chain(1:ItemCount);  
        
        end
        
    end
end

figure(5);
clf;
hold on;
for n1=1:size(sGB0,2)
    EX=ShortChain.Grain(n1);
    for n2=1:length(EX.Set)
        f=EX.Set(n2).Chain;
    x=V(f,1);
    y=V(f,2);
    plot(x,y,'bs-');
    end
    
    
end

disp('STOP2');


%% Now Convert to List
%%
for n1=1:size(sGB0,2)
%     sGB(n1).ToExt=zeros(length(sGB(n1).Cut),2);
    
%         EX=NewChain.Grain(n1);
    for n2=1:length(NewChain.Grain(n1).Set)
        %%
        if ~isempty(length(NewChain.Grain(n1).Set(n2).Chain))
        LineList.Grain(n1).Set(n2).List=zeros(length(NewChain.Grain(n1).Set(n2).Chain)-1,2);
        end
        
        for n3=1:(length(NewChain.Grain(n1).Set(n2).Chain)-1)
            LineList.Grain(n1).Set(n2).List(n3,1)=...
                NewChain.Grain(n1).Set(n2).Chain(n3);
            LineList.Grain(n1).Set(n2).List(n3,2)=...
                NewChain.Grain(n1).Set(n2).Chain(n3+1);
        end
        
       
        
    end
end



for n1=1:size(sGB0,2)
%     sGB(n1).ToExt=zeros(length(sGB(n1).Cut),2);
    
%         EX=NewChain.Grain(n1);
    for n2=1:length(ShortChain.Grain(n1).Set)
        %%
        if ~isempty(length(ShortChain.Grain(n1).Set(n2).Chain))
        ShortList.Grain(n1).Set(n2).List=zeros(length(ShortChain.Grain(n1).Set(n2).Chain)-1,2);
        end
        
        for n3=1:(length(ShortChain.Grain(n1).Set(n2).Chain)-1)
            ShortList.Grain(n1).Set(n2).List(n3,1)=...
                ShortChain.Grain(n1).Set(n2).Chain(n3);
            ShortList.Grain(n1).Set(n2).List(n3,2)=...
                ShortChain.Grain(n1).Set(n2).Chain(n3+1);
        end
        
       
        
    end
end


%%
vTake=false(size(V,1),1);
vMap=zeros(size(V,1),1);

for n1=1:size(sGB0,2)
%     sGB(n1).ToExt=zeros(length(sGB(n1).Cut),2);
    
%         EX=NewChain.Grain(n1);
    for n2=1:length(ShortChain.Grain(n1).Set)
        %%
        
        for n3=1:(length(ShortChain.Grain(n1).Set(n2).Chain)-1)
            f1=ShortList.Grain(n1).Set(n2).List(n3,1);
            f2=ShortList.Grain(n1).Set(n2).List(n3,2);
            
            vTake([f1 f2],1)=true;
        end
                
    end
end

Count=0;
%%
for n1=1:length(vMap)
   
    if vTake(n1)
       Count=Count+1;
       vMap(n1)=Count;
    end
    
end

for n1=1:size(sGB0,2)
%     sGB(n1).ToExt=zeros(length(sGB(n1).Cut),2);
    
%         EX=NewChain.Grain(n1);
    for n2=1:length(ShortChain.Grain(n1).Set)
        %%
        if ~isempty(length(ShortChain.Grain(n1).Set(n2).Chain))
        ShortList2.Grain(n1).Set(n2).List=zeros(length(ShortChain.Grain(n1).Set(n2).Chain)-1,2);
        end
        
        for n3=1:(length(ShortChain.Grain(n1).Set(n2).Chain)-1)
            ShortList2.Grain(n1).Set(n2).List(n3,1)=...
                vMap(ShortChain.Grain(n1).Set(n2).Chain(n3));
            ShortList2.Grain(n1).Set(n2).List(n3,2)=...
                vMap(ShortChain.Grain(n1).Set(n2).Chain(n3+1));
        end
        
       
        
    end
end

VShort=V(vTake,:);
save Step2_Data.mat V F LineList ShortList ShortList2 ShortChain vMap VShort sGB sGB0;
disp('Complete');
%%
NGrains=length(ShortList2.Grain);
GrainMid=zeros(NGrains,2);

for n1=1:NGrains
   tt=sGB(n1).Chain;
   xx=V(tt,1);
   yy=V(tt,2);
   GrainMid(n1,:)=[mean(xx) mean(yy)];
    
end

figure(6);
clf;
hold on;
for n1=1:size(sGB0,2)
    EX=ShortChain.Grain(n1);
    for n2=1:length(EX.Set)
        f=EX.Set(n2).Chain;
    x=V(f,1);
    y=V(f,2);
    plot(x,y,'b-');
    end
    
    text(GrainMid(n1,1).*1.04,GrainMid(n1,2).*1.04,num2str(n1));
end

plot(GrainMid(:,1),GrainMid(:,2),'rx');
plot(GrainMid(24,1),GrainMid(24,2),'rs');
plot([10 10],[10 480],'k-');
plot([10 740],[480 480],'k-');
plot([740 740],[480 10],'k-');
plot([10 740],[10 10],'k-');

figure(7);
% clf;
% plot(ebsd);

