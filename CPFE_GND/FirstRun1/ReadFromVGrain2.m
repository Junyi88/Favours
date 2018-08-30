function [Coords1,FullText,EndLineForPoints]=ReadFromVGrain2(filename)

fileID = fopen(filename,'r');
[FullText,posX ]= textscan(fileID,'%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s','EndOfLine','\n');
fclose(fileID);


%% Get Lines
text1=['keepIntersections=ON,' , 'originalInstances=DELETE)'];
TextLength1=length(text1);

EndLineForPoints=0;
NLines=length(FullText{1,1});

for n1=1:NLines
    if strncmpi([FullText{1,1}{n1},FullText{1,3}{n1}],text1,TextLength1)
        EndLineForPoints=n1;
        break;
    end
end


%% Get Line Locations For Coordinates

text1=['mdb.models[' char(39) 'Model-1' char(39) '].parts[' char(39) 'Part-total' char(39) ...
    '].SectionAssignment(region=Region(cells='];
TextLength1=length(text1);
CoordLines=zeros(100,1);
CoordLinesNum=0;

for n1=EndLineForPoints:NLines
     if strncmpi(FullText{1,1}{n1},text1,TextLength1)
         CoordLinesNum=CoordLinesNum+1;
         CoordLines(CoordLinesNum)=n1;
     end
end

CoordLines=CoordLines(1:CoordLinesNum);
Coords1=zeros(CoordLinesNum,3);

%%
for n1=1:CoordLinesNum
    nCoord=CoordLines(n1);
    T1=FullText{1,2}{nCoord};
    nTextFirst=find(T1=='(',8,'last');
    nTextFirst=nTextFirst(end);
    T1=T1(nTextFirst+1:end);
    T1=T1(T1~=',');
    T1=T1(T1~='(');
    
    T2=FullText{1,3}{nCoord};
    T2=T2(T2~=',');
    T3=FullText{1,4}{nCoord};
    T3=T3(T3~=',');
    T3=T3(T3~=')');
    
    Coords1(n1,1)=str2num(T1);
    Coords1(n1,2)=str2num(T2);
    Coords1(n1,3)=str2num(T3);
end


%% Get 


end