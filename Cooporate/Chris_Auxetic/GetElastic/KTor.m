function [K]=KTor(Pr)

X=Pr.Mt.G.*Pr.Ge.Jtor./Pr.Ge.L;
K=[X -X;-X X];

end