function [K]=KAxial(Pr)

    k=Pr.Mt.YM*Pr.Ge.A/Pr.Ge.L;
    K=[k,-k;-k,k];

end


