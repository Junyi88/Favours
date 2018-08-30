from part import * 
from material import * 
from section import * 
from assembly import * 
from step import * 
from interaction import * 
from load import * 
from mesh import * 
from job import * 
from sketch import * 
from visualization import * 
from connectorBehavior import * 
 
# OpenSketch 
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=( 2.0000e+01 )) 
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0000e+00,0.0000e+00), point2=(5.0000e+00,5.0000e+00)) 
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-1', type= DEFORMABLE_BODY) 
vP=mdb.models['Model-1'].parts['Part-1'] 
vP.BaseSolidExtrude(depth=1.0000e+00, sketch= mdb.models['Model-1'].sketches['__profile__']) 
del mdb.models['Model-1'].sketches['__profile__'] 
 
vP.DatumPointByCoordinate(coords=( 1, 1, 0 ))
vP.DatumPointByCoordinate(coords=( 1, 2, 0 ))
vP.DatumPointByCoordinate(coords=( 1, 2, 1 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[3], point2=vP.datums[4])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[5], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[6],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[5], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[6])
del mdb.models['Model-1'].sketches['__profile__']