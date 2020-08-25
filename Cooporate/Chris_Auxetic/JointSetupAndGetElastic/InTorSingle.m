function [Pos]=InTorSingle(F,U,Pr,Nu)
    L=Pr.Ge.L;
    x=linspace(0,L,Nu);
    F(1)=-F(1);
    F=KTor(Pr)*U;
    ptheta=[F(2)./(Pr.Mt.G.*Pr.Ge.Jtor) U(1)];
    
    Pos.theta=ptheta(1).*x+ptheta(2);
    
    Pos.ptheta=ptheta;
    Pos.x=x;
    
    Pos.EpTor=ptheta(1).*Pr.Ge.r;
end