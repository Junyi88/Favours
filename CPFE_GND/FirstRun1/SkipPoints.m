function [sRGB]=SkipPoints(sGB,N)

for n1=1:length(sGB)
   sRGB(n1).Chain=[sGB(n1).Chain(1),sGB(n1).Chain(2:N:end-1),sGB(n1).Chain(end)]; 
end


end

