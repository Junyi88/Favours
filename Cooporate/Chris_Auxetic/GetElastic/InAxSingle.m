function [Pos]=InAxSingle(F,U,Pr,Nu)
    L=Pr.Ge.L;
    x=linspace(0,L,Nu);
    F(1)=-F(1);
    F=KAxial(Pr)*U;
    pu=[F(2)./(Pr.Mt.YM.*Pr.Ge.A) U(1)];
    
    Pos.u=pu(1).*x+pu(2);
    
    Pos.pu=pu;
    Pos.x=x;

    Pos.EpAx=pu(1);
    Pos.F=F;
end