function [dCount]=W1F_DatumPoints(fileID,V,ZVals)

Start1=['\n#- Create Datums [1]------------------------ \n'];
Start2=['\n#- Create Datums [2]------------------------ \n'];
DatumPoText=['vP.DatumPointByCoordinate(coords=( %8.4e, %8.4e, %8.4e)) \n'];

dCount=1;

%%
for n1=1:size(V,1)
    fprintf(fileID,Start1);
    fprintf(fileID,DatumPoText,V(n1,1),V(n1,2),ZVals(1));
    dCount=dCount+1;
end

%%
for n1=1:size(V,1)
    fprintf(fileID,Start2);
    fprintf(fileID,DatumPoText,V(n1,1),V(n1,2),ZVals(2));
    dCount=dCount+1;
end

end