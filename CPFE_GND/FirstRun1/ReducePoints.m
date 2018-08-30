function [sRGB,PivotPoints,RemovedPoints]=ReducePoints(sGB,V,MaxDiff)

%% This function is used to reduce the number of points

PivotPoints=zeros(length(V),1); %These are points that we will not remove
RemovedPoints=zeros(length(V),1);

for n1=1:length(sGB)
    x=V(sGB(n1).Chain,1);
    y=V(sGB(n1).Chain,2);
    dx=[(x(1)-x(end)); diff(x)];
    dy=[(y(1)-y(end)); diff(y)];
    dydx=dy./dx;
    
    d2ydx2=zeros(size(dydx));
    d2ydx2(1)=(dydx(1)-dydx(end))./(dx(1)+dx(end));
    for n2=2:length(d2ydx2)
        d2ydx2(n2)=(dydx(n2)-dydx(n2-1))./(dx(n2)+dx(n2-1));
    end

    sRGB(n1).Chain=zeros(size(sGB));
    
    for n2=1:length(sGB(n1).Chain)
        f = sGB(n1).Chain(n2);
        
        if (abs(d2ydx2(n2))>MaxDiff)
            PivotPoints(f)=1;
            RemovedPoints(f)=0;
        else            
            if (PivotPoints(f)==1)
                RemovedPoints(f)=0;
            else 
                RemovedPoints(f)=1;
            end             
        end           
    end

end

%%
for n1=1:length(sGB)
    

    sRGB(n1).Chain=zeros(size(sGB));
    count = 0;
    for n2=1:length(sGB(n1).Chain)
        f = sGB(n1).Chain(n2);
        
        if (PivotPoints(f)==1) 
            count=count+1;
            sRGB(n1).Chain(count)=f;            
        end
                       
    end

    sRGB(n1).Chain=sRGB(n1).Chain(1:count);
    
end

end