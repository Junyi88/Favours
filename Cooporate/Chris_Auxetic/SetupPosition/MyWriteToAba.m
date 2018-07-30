clear;

load TotalMesh.mat;


%% write To File
csvwrite('ToAbaNodeLoc.csv',LattStrut.Prep.NodePointsKeep);
csvwrite('ToAbaNoStrutBeam.csv',LattNoStrut.Struts);
csvwrite('ToAbaStrutBeam.csv',LattStrut.Struts);