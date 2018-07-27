function [K]=KTimoZ(Pr)


%     a1=(12*Pr.Ge.kappa*Pr.Ge.A*...
%         Pr.Mt.G.*Pr.Mt.YM*Pr.Ge.I)/...
%         (Pr.Ge.L*(Pr.Ge.A*Pr.Mt.G.*Pr.Ge.L*Pr.Ge.L*Pr.Ge.kappa-...
%         12*Pr.Ge.I*Pr.Mt.YM));
%     
%     a2=(6.*Pr.Ge.kappa*...
%         Pr.Ge.A*...
%         Pr.Mt.G*...
%         Pr.Mt.YM*...
%         Pr.Ge.I)/...
%         (Pr.Ge.A*Pr.Mt.G*Pr.Ge.L*Pr.Ge.L*Pr.Ge.kappa-...
%         12*Pr.Ge.I*Pr.Mt.YM);
%     
%     a3=a2;
%     
%     a4=4.*(Pr.Ge.A*Pr.Mt.G*Pr.Ge.L*Pr.Ge.L*Pr.Ge.kappa-...
%         3*Pr.Ge.I*Pr.Mt.YM)*Pr.Mt.YM*Pr.Ge.I/...
%         Pr.Ge.L*(Pr.Ge.A*Pr.Mt.G*Pr.Ge.L*Pr.Ge.L*Pr.Ge.kappa-...
%         12*Pr.Ge.I*Pr.Mt.YM);
%     
%     a5=2.*(Pr.Ge.A*Pr.Mt.G*Pr.Ge.L*Pr.Ge.L*Pr.Ge.kappa+...
%         6*Pr.Ge.I*Pr.Mt.YM)*Pr.Mt.YM*Pr.Ge.I/...
%         Pr.Ge.L*(Pr.Ge.A*Pr.Mt.G*Pr.Ge.L*Pr.Ge.L*Pr.Ge.kappa-...
%         12*Pr.Ge.I*Pr.Mt.YM);
%     
%     
%     K=[a1,a2,-a1,a3;...
%        a2,a4,-a2,a5;...
%        -a1,-a2,a1,-a2;...
%        a3,a5,-a2,a4];


L=Pr.Ge.L;
ka=Pr.Ge.kappa;
A=Pr.Ge.A;
G=Pr.Mt.G;

YM=Pr.Mt.YM;
S=Pr.Ge.I;


% t1 = (L ^ 2 * k * A * G);
% t2 = 12 * Y * S;
% t3 = t1 - t2;
% t4 = 1 / L;
% t3 = 1 / t3;
% t2 = t2 * t4 * t3 * k * A * G;
% t5 = 6 * t3 * k * A * G * Y * S;
% t6 = 2 * Y * S * (6 * Y * S + t1) * t4 * t3;
% t1 = 4 * t4 * (-3 * Y * S + t1) * t3 * Y * S;
% K = [t2 t5 -t2 t5; t5 t1 -t5 t6; -t2 -t5 t2 -t5; t5 t6 -t5 t1;];
% % K(3,4)=-K(3,4);
% K(4,3)=-K(4,3);

% K(3,4)=-K(3,4);
% K(4,3)=-K(4,3);

t1 = (L ^ 2 * ka * A * G);
t2 = 12 * YM * S;
t3 = t2 + t1;
t3 = 1 / t3;
t4 = 1 / L;
t2 = t2 * t4 * t3 * ka * A * G;
t5 = 6 * t3 * YM * S * ka * A * G;
t6 = 6 * L * ka * A * G;
t7 = 2 * t4 * (-6 * YM * S + t1);
t8 = YM * S;
t3 = t8 * t3;
t1 = (12 * t8 + 4 * t1) * t4;
K = [t2 t5 -t2 t5; t5 t3 * (-t7 + t6) -t5 t3 * t7; -t2 -t5 t2 -t5; t5 t3 * (-t1 + t6) -t5 t1 * t3;];


end