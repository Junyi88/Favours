clear;
load ../Step2_Data.mat;



p = mdb.models['Model-1'].parts['Part-Base']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#10000 ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-1')