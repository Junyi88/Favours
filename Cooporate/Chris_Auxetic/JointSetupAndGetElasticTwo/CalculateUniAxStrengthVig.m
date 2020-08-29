function [UniSt]=CalculateUniAxStrengthVig(Vig,Nu)

%% Find the Uniaxial strains

UniSt.Misc.Ep=Vig.Eff.KEp\[-1;0;0;0;0;0];
UniSt.Misc.d0u=Vig.Eff.D0*(Vig.Eff.BEp*UniSt.Misc.Ep);
UniSt.Misc.du=Vig.Eff.Da*(Vig.Eff.BEp*UniSt.Misc.Ep);

%%
BC=zeros(60,2);
BC(:,2)=2;
BC(:,1)=UniSt.Misc.du;

[UniSt.unit.F,UniSt.unit.U]=Solve3DLattice(Vig.Eff.Kuc,BC);
[UniSt.unit.Dis]=GetDisplacements(Vig.Mesh,UniSt.unit.F,UniSt.unit.U,Nu);

%%
RYield=1./UniSt.unit.Dis.Stress.RVMMax;
RBuck=1./UniSt.unit.Dis.Buck.RPPmax;
RBuckF=1./UniSt.unit.Dis.Buck.RFFmax;

UniSt.Fail.Yield.Loc=UniSt.unit.Dis.Stress.RVMMaxLoc;
UniSt.Fail.Buck.Loc=UniSt.unit.Dis.Buck.RPPmaxLoc;
UniSt.Fail.BuckF.Loc=UniSt.unit.Dis.Buck.RFFmaxLoc;

UniSt.Fail.Yield.Stress=RYield;
UniSt.Fail.Buck.Stress=RBuck;
UniSt.Fail.BuckF.Stress=RBuckF;

UniSt.Fail.Yield.Ep=RYield.*UniSt.Misc.Ep;
UniSt.Fail.Buck.Ep=RBuck.*UniSt.Misc.Ep;
UniSt.Fail.BuckF.Ep=RBuckF.*UniSt.Misc.Ep;

UniSt.Fail.Yield.F=RYield.*UniSt.unit.F;
UniSt.Fail.Buck.F=RBuck.*UniSt.unit.F;
UniSt.Fail.BuckF.F=RBuckF.*UniSt.unit.F;

UniSt.Fail.Yield.U=RYield.*UniSt.unit.U;
UniSt.Fail.Buck.U=RBuck.*UniSt.unit.U;
UniSt.Fail.BuckF.U=RBuckF.*UniSt.unit.U;

end