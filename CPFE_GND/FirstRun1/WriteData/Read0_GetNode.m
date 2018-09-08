clear;

filename='ExtractForPoints-1.inp';
fileID = fopen(filename,'r');
[FullText,posX ]= textscan(fileID,'%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s','EndOfLine','\n');

% [FullText,posX ]= textscan(fileID,'%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s','EndOfLine','\n');
fclose(fileID);

%%
FlagNode=false;
FlagEl=false;
for n1=1:length(FullText{1})
    s1=FullText{1}(n1);
    if ~FlagNode
        tf = strncmpi(s1{1},'*Node',5);
        if tf
            NodeStart=n1+1;
            FlagNode=true;
        end
    elseif ~FlagEl
        tf = strncmpi(s1{1},'*Element',8);
        if tf
            NodeEnd=n1-1;
            ElStart=n1+1;
            FlagEl=true;
        end
    elseif FlagEl
        tf = strncmpi(s1{1},'*',1);
        if tf
            
            ElEnd=n1-1;
            break;
            
        end
    end
        
end


%%
LNode=NodeEnd-NodeStart;
LEl=ElEnd-ElStart;

%%
NodeCoords=zeros(LNode,4);

for n1=NodeStart:NodeEnd
    s1=FullText{1}(n1);
    N= str2double(s1{1});
    
    s1=FullText{2}(n1);
    x=str2double(s1{1});
    
    s1=FullText{3}(n1);
    y=str2double(s1{1});
    
    s1=FullText{4}(n1);
    z=str2double(s1{1});
    NodeCoords(N,:)=[N,x,y,z];
end

%%
ElSystems=zeros(LEl,8);

for n1=ElStart:ElEnd
    s1=FullText{1}(n1);
    N=str2double(s1{1});
    ElSystems(N,1)=N;
    
    for n2=1:8
        s1=FullText{n2+1}(n1);
        ElSystems(N,n2+1)=str2double(s1{1});
    end
    
end
save Read0_Data ElSystems NodeCoords;
