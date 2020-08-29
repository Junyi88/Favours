function [Pos]=InTimoSingleZ(F,U,Pr,Nu)

    L=Pr.Ge.L;
    
%     F(2:3)=-F(2:3);
    F=KTimoZ(Pr)*U;
    x=linspace(0,L,Nu);
    
    pw=[0 0 0 0];
    pphi=[0 0 0];
    

    k=Pr.Ge.kappa;
    A=Pr.Ge.A;
    G=Pr.Mt.G;

    Y=Pr.Mt.YM;
    I=Pr.Ge.I;
    
%     pw(1)=F(1)./(6.*Pr.Mt.YM.*Pr.Ge.I);
%     pw(2)=F(2)./(2.*Pr.Mt.YM.*Pr.Ge.I);
%     pw(3)=U(2)+F(1)./(Pr.Ge.kappa.*Pr.Ge.A.*Pr.Mt.G);a
%     pw(4)=U(1);
%     
% %     pw(3)=-pw(3);
% %     pw(2)=-pw(2);
% %     pw(1)=-pw(1);s
%     
%     pphi(1)=F(1)./(2.*Pr.Mt.YM.*Pr.Ge.I);
%     pphi(2)=F(2)./(Pr.Mt.YM.*Pr.Ge.I);
%     pphi(3)=U(2);
    
    pw(1)=F(1)./(6.*Y*I);
    pw(2)=-F(2)./(2.*Y*I);
    pw(3)=U(2)-F(1)./(k*A*G);
    pw(4)=U(1);

    pphi(1)=F(1)./(2.*Y*I);
    pphi(2)=-F(2)./(Y*I);
    pphi(3)=U(2);


    
    Pos.w=pw(1).*x.^3+pw(2).*x.^2+pw(3).*x+pw(4);
    Pos.phi=pphi(1).*x.^2+pphi(2).*x+pphi(3);
    
    Pos.pphi=pphi;
    Pos.pw=pw;
    Pos.x=x;

    Pos.dw=3.*pw(1).*x.^2+2.*pw(2).*x+pw(3);
    Pos.dphi=2.*pphi(1).*x+pphi(2);

    Pos.EpBenA=-Pr.Ge.r.*Pos.dphi;
    Pos.EpBenS=0.5.*(Pos.dw-Pos.phi).*Pr.Ge.kappa;
    

end