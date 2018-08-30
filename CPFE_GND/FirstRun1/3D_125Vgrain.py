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
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-1', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-1']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 417.45664354525684, 25.27312259739948, 55.22718146493581 ))
vP.DatumPointByCoordinate(coords=( 488.65113801855256, 30.34793826668001, 101.02028944742439 ))
vP.DatumPointByCoordinate(coords=( 498.44664721887602, -0.00000000000000, 109.84859549549830 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 399.93720748429536, -0.00000000000000, 5.10027746520772 ))
vP.DatumPointByCoordinate(coords=( 400.21577538583813, -0.00000000000000, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 449.05456164409293, 60.93161762793518, 0.00000000000001 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 407.69305428867733, 0.00000000000000, 50.94815815573405 ))
vP.DatumPointByCoordinate(coords=( 399.93720748429536, -0.00000000000000, 5.10027746520772 ))
vP.DatumPointByCoordinate(coords=( 409.71554568342788, 15.32809717679227, 51.01279931900921 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 114.62089941940560, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 449.05456164409293, 60.93161762793518, 0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 400.21577538583813, -0.00000000000000, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, -0.00000000000000, 89.67306280956568 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 88.93109406791272, 58.10001940676285 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 114.62089941940560, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 400.21577538583813, -0.00000000000000, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 399.93720748429536, -0.00000000000000, 5.10027746520772 ))
vP.DatumPointByCoordinate(coords=( 407.69305428867733, 0.00000000000000, 50.94815815573405 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 88.93109406791272, 58.10001940676285 ))
vP.DatumPointByCoordinate(coords=( 488.65113801855256, 30.34793826668001, 101.02028944742439 ))
vP.DatumPointByCoordinate(coords=( 417.45664354525684, 25.27312259739948, 55.22718146493581 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, -0.00000000000000, 89.67306280956568 ))
vP.DatumPointByCoordinate(coords=( 498.44664721887602, -0.00000000000000, 109.84859549549830 ))
vP.DatumPointByCoordinate(coords=( 488.65113801855256, 30.34793826668001, 101.02028944742439 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-2', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-2']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 99.82392006356918, 215.60609332407853, -0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 99.12569698499642, 214.96983544267653, 3.96638257603154 ))
vP.DatumPointByCoordinate(coords=( 40.04878181090301, 128.72435963964057, 30.88756208597047 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 145.95788942496861, 32.28260515529090, -0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 193.85756043270985, 37.78659735517852, -0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 251.38980576443907, 107.62163849303580, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 40.04878181090301, 128.72435963964057, 30.88756208597047 ))
vP.DatumPointByCoordinate(coords=( 88.01741522207379, 93.73536088691495, 99.59168676123312 ))
vP.DatumPointByCoordinate(coords=( 100.97455266117538, 81.93319796544539, 95.78162423956135 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 197.44443520954425, 184.83397929872177, 108.92918786397236 ))
vP.DatumPointByCoordinate(coords=( 191.04664134247091, 160.57232800005823, 124.71248107077699 ))
vP.DatumPointByCoordinate(coords=( 88.01741522207379, 93.73536088691495, 99.59168676123312 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 99.82392006356918, 215.60609332407853, -0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 193.07527401378826, 204.98840162366400, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 198.44642197988122, 184.84006703104578, 108.26323705343300 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 197.44443520954425, 184.83397929872177, 108.92918786397236 ))
vP.DatumPointByCoordinate(coords=( 198.44642197988122, 184.84006703104578, 108.26323705343300 ))
vP.DatumPointByCoordinate(coords=( 230.74582213651126, 130.44338744813595, 112.78474356679108 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 228.97596426435044, 129.06984482197961, 114.60979350699631 ))
vP.DatumPointByCoordinate(coords=( 207.80968013059712, 98.75890009340093, 103.73082727954660 ))
vP.DatumPointByCoordinate(coords=( 100.97455266117538, 81.93319796544539, 95.78162423956135 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 251.38980576443907, 107.62163849303580, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 193.85756043270985, 37.78659735517852, -0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 207.80968013059712, 98.75890009340093, 103.73082727954660 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 198.44642197988122, 184.84006703104578, 108.26323705343300 ))
vP.DatumPointByCoordinate(coords=( 193.07527401378826, 204.98840162366400, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 251.38980576443907, 107.62163849303580, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 145.95788942496861, 32.28260515529090, -0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 100.97455266117538, 81.93319796544539, 95.78162423956135 ))
vP.DatumPointByCoordinate(coords=( 207.80968013059712, 98.75890009340093, 103.73082727954660 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-3', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-3']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 275.85145011811005, 109.13474224245776, -0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 298.39686795337121, 125.39276822627602, 69.56268282490547 ))
vP.DatumPointByCoordinate(coords=( 399.85695589929867, 32.87033139690689, 67.48083233258004 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 400.21577538583807, -0.00000000000006, -0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 449.05456164409293, 60.93161762793523, -0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 456.41860430618846, 142.98948587190486, -0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 399.93720748429530, -0.00000000000006, 5.10027746520762 ))
vP.DatumPointByCoordinate(coords=( 400.21577538583807, -0.00000000000006, -0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 396.96137261175460, -0.00000000000006, -0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 417.45664354525684, 25.27312259739952, 55.22718146493580 ))
vP.DatumPointByCoordinate(coords=( 409.71554568342788, 15.32809717679227, 51.01279931900920 ))
vP.DatumPointByCoordinate(coords=( 399.85695589929867, 32.87033139690689, 67.48083233258004 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 408.16313202242588, 157.22026779081759, 96.32927290483654 ))
vP.DatumPointByCoordinate(coords=( 425.33289132129948, 184.22186892311987, 67.65062262490515 ))
vP.DatumPointByCoordinate(coords=( 456.41860430618846, 142.98948587190486, -0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 399.85695589929867, 32.87033139690689, 67.48083233258004 ))
vP.DatumPointByCoordinate(coords=( 298.39686795337121, 125.39276822627602, 69.56268282490547 ))
vP.DatumPointByCoordinate(coords=( 345.77081296778090, 191.47027812035185, 92.62811451065157 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 375.99872733114330, 253.62748252725856, 30.21939208751948 ))
vP.DatumPointByCoordinate(coords=( 345.77081296778090, 191.47027812035185, 92.62811451065157 ))
vP.DatumPointByCoordinate(coords=( 298.39686795337121, 125.39276822627602, 69.56268282490547 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 456.41860430618846, 142.98948587190486, -0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 425.33289132129948, 184.22186892311987, 67.65062262490515 ))
vP.DatumPointByCoordinate(coords=( 375.99872733114330, 253.62748252725856, 30.21939208751948 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 375.99872733114330, 253.62748252725856, 30.21939208751948 ))
vP.DatumPointByCoordinate(coords=( 425.33289132129948, 184.22186892311987, 67.65062262490515 ))
vP.DatumPointByCoordinate(coords=( 408.16313202242588, 157.22026779081759, 96.32927290483654 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 409.71554568342788, 15.32809717679227, 51.01279931900920 ))
vP.DatumPointByCoordinate(coords=( 417.45664354525684, 25.27312259739952, 55.22718146493580 ))
vP.DatumPointByCoordinate(coords=( 449.05456164409293, 60.93161762793523, -0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-4', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-4']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 40.04878181090296, 128.72435963964062, 30.88756208597048 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 124.84787939168041, 69.25292341987395 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 217.86831069596244, 103.52888860376889 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 99.82392006356918, 215.60609332407856, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 40.04742449157139, 125.47907047083720, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 40.04878181090296, 128.72435963964062, 30.88756208597048 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 68.83263500799600, 311.03922417744565, 69.46598208289248 ))
vP.DatumPointByCoordinate(coords=( 82.15785382329851, 315.95265203070039, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 99.82392006356918, 215.60609332407856, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 82.15785382329851, 315.95265203070039, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 68.83263500799600, 311.03922417744565, 69.46598208289248 ))
vP.DatumPointByCoordinate(coords=( 56.76604562883994, 313.99665292665821, 82.54548045069346 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 0.00000000000000, 117.57222575138474, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 40.04742449157139, 125.47907047083720, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 99.82392006356918, 215.60609332407856, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 0.00000000000000, 337.22905436907689, 81.38475309015155 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 217.86831069596244, 103.52888860376889 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 124.84787939168041, 69.25292341987395 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 56.76604562883994, 313.99665292665821, 82.54548045069346 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 217.86831069596244, 103.52888860376889 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 337.22905436907689, 81.38475309015155 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 0.00000000000000, 117.57222575138474, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 124.84787939168041, 69.25292341987395 ))
vP.DatumPointByCoordinate(coords=( 40.04878181090296, 128.72435963964062, 30.88756208597048 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-5', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-5']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 198.44642197988119, 184.84006703104575, 108.26323705343300 ))
vP.DatumPointByCoordinate(coords=( 230.74582213651121, 130.44338744813598, 112.78474356679109 ))
vP.DatumPointByCoordinate(coords=( 251.38980576443907, 107.62163849303579, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 250.05717219969901, 290.32377172795907, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 268.20219634913673, 290.78260454581829, 102.59060420064334 ))
vP.DatumPointByCoordinate(coords=( 198.44642197988119, 184.84006703104575, 108.26323705343300 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 251.38980576443907, 107.62163849303579, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 275.85145011811005, 109.13474224245776, -0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 373.58867169314885, 257.79615107152949, -0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 330.64500374835717, 200.68979068726719, 110.29055547578790 ))
vP.DatumPointByCoordinate(coords=( 240.12952162828370, 131.06205098312034, 112.96363528589650 ))
vP.DatumPointByCoordinate(coords=( 230.74582213651121, 130.44338744813598, 112.78474356679109 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 344.14295318630280, 290.02499670502954, 61.70433310639238 ))
vP.DatumPointByCoordinate(coords=( 374.05914073908855, 272.77318527011772, 26.44048724466229 ))
vP.DatumPointByCoordinate(coords=( 375.99872733114330, 253.62748252725856, 30.21939208751950 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 268.20219634913673, 290.78260454581829, 102.59060420064334 ))
vP.DatumPointByCoordinate(coords=( 250.05717219969901, 290.32377172795907, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 348.49690744664809, 289.64352325667949, -0.00000000000001 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 348.49690744664809, 289.64352325667949, -0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 372.07538068840552, 275.00037584965503, -0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 374.05914073908855, 272.77318527011772, 26.44048724466229 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 372.07538068840552, 275.00037584965503, -0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 373.58867169314885, 257.79615107152949, -0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 375.99872733114330, 253.62748252725856, 30.21939208751950 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 230.74582213651121, 130.44338744813598, 112.78474356679109 ))
vP.DatumPointByCoordinate(coords=( 240.12952162828370, 131.06205098312034, 112.96363528589650 ))
vP.DatumPointByCoordinate(coords=( 298.39686795337121, 125.39276822627600, 69.56268282490547 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 298.39686795337121, 125.39276822627600, 69.56268282490547 ))
vP.DatumPointByCoordinate(coords=( 345.77081296778084, 191.47027812035182, 92.62811451065156 ))
vP.DatumPointByCoordinate(coords=( 375.99872733114330, 253.62748252725856, 30.21939208751950 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 298.39686795337121, 125.39276822627600, 69.56268282490547 ))
vP.DatumPointByCoordinate(coords=( 240.12952162828370, 131.06205098312034, 112.96363528589650 ))
vP.DatumPointByCoordinate(coords=( 330.64500374835717, 200.68979068726719, 110.29055547578790 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[62], point2=vP.datums[63], point3=vP.datums[64])
vP.DatumAxisByTwoPoint(point1=vP.datums[62], point2=vP.datums[63])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[66],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[66])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-6', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-6']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 456.41860430618840, 142.98948587190489, -0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 425.33289132129948, 184.22186892311987, 67.65062262490514 ))
vP.DatumPointByCoordinate(coords=( 511.71229281689136, 216.61593336038925, 111.55730423221009 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 198.40539671936745, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 464.59342765772072, 327.82730635988094, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 372.07538068840557, 275.00037584965497, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 179.84869739046383, 46.18027897541781 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 206.70544145069476, 50.21116370506771 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 198.40539671936745, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 520.37129982586202, 292.00693482344150, 105.81942982063870 ))
vP.DatumPointByCoordinate(coords=( 533.75565801220728, 279.24597321791100, 106.01203622506115 ))
vP.DatumPointByCoordinate(coords=( 526.09371961841737, 277.92610056537808, 111.00870043584023 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 511.71229281689136, 216.61593336038925, 111.55730423221009 ))
vP.DatumPointByCoordinate(coords=( 425.33289132129948, 184.22186892311987, 67.65062262490514 ))
vP.DatumPointByCoordinate(coords=( 375.99872733114330, 253.62748252725854, 30.21939208751947 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 533.75565801220728, 279.24597321791100, 106.01203622506115 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 206.70544145069476, 50.21116370506771 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 179.84869739046383, 46.18027897541781 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 456.41860430618840, 142.98948587190489, -0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 373.58867169314885, 257.79615107152944, -0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 375.99872733114330, 253.62748252725854, 30.21939208751947 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 372.07538068840557, 275.00037584965497, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 464.59342765772072, 327.82730635988094, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 479.54472231556065, 326.44295878293951, 78.07572370688980 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 375.99872733114330, 253.62748252725854, 30.21939208751947 ))
vP.DatumPointByCoordinate(coords=( 373.58867169314885, 257.79615107152944, -0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 372.07538068840557, 275.00037584965497, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 206.70544145069476, 50.21116370506771 ))
vP.DatumPointByCoordinate(coords=( 533.75565801220728, 279.24597321791100, 106.01203622506115 ))
vP.DatumPointByCoordinate(coords=( 520.37129982586202, 292.00693482344150, 105.81942982063870 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-7', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-7']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 164.35180339595809, 367.01937270046147, 0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 168.10234969658802, 371.75986728081529, 49.75047633893020 ))
vP.DatumPointByCoordinate(coords=( 205.68230887979115, 344.70473635569005, 90.14580941715013 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 348.49690744664804, 289.64352325667943, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 320.90641785250153, 453.00403040718351, -0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 281.92472609041312, 480.52713239302165, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 268.20219634913673, 290.78260454581823, 102.59060420064331 ))
vP.DatumPointByCoordinate(coords=( 313.45468160836162, 290.47610345675946, 103.68062710931741 ))
vP.DatumPointByCoordinate(coords=( 344.14295318630275, 290.02499670502948, 61.70433310639236 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 344.14295318630275, 290.02499670502948, 61.70433310639236 ))
vP.DatumPointByCoordinate(coords=( 334.69548266367144, 323.59120602254671, 116.05565785355678 ))
vP.DatumPointByCoordinate(coords=( 319.92169978010162, 400.11885451946625, 142.65012036099051 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 237.49323532127300, 482.72186535451812, 42.23891517725127 ))
vP.DatumPointByCoordinate(coords=( 319.87917071103766, 400.10349855540863, 142.68761249733876 ))
vP.DatumPointByCoordinate(coords=( 298.31748454863856, 347.50408870414822, 154.26671940759974 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 225.38805842123895, 476.61025013369056, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 281.92472609041312, 480.52713239302165, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 279.87849361042140, 483.74063444338810, 26.87725390407689 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 182.94824783570914, 445.06332456050620, 22.85601682569857 ))
vP.DatumPointByCoordinate(coords=( 181.64113009307863, 444.75559218473927, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 225.38805842123895, 476.61025013369056, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 316.14812444845842, 459.78405997064181, 51.97534850673907 ))
vP.DatumPointByCoordinate(coords=( 279.87849361042140, 483.74063444338810, 26.87725390407689 ))
vP.DatumPointByCoordinate(coords=( 281.92472609041312, 480.52713239302165, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 182.94824783570914, 445.06332456050620, 22.85601682569857 ))
vP.DatumPointByCoordinate(coords=( 168.10234969658802, 371.75986728081529, 49.75047633893020 ))
vP.DatumPointByCoordinate(coords=( 164.35180339595809, 367.01937270046147, 0.00000000000001 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 319.92169978010162, 400.11885451946625, 142.65012036099051 ))
vP.DatumPointByCoordinate(coords=( 334.69548266367144, 323.59120602254671, 116.05565785355678 ))
vP.DatumPointByCoordinate(coords=( 317.32781038342210, 316.98788047801827, 131.31128916216301 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 237.49323532127300, 482.72186535451812, 42.23891517725127 ))
vP.DatumPointByCoordinate(coords=( 279.87849361042140, 483.74063444338810, 26.87725390407689 ))
vP.DatumPointByCoordinate(coords=( 316.14812444845842, 459.78405997064181, 51.97534850673907 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[62], point2=vP.datums[63], point3=vP.datums[64])
vP.DatumAxisByTwoPoint(point1=vP.datums[62], point2=vP.datums[63])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[66],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[66])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 261.46326718860234, 297.99738250861378, 109.86738632031442 ))
vP.DatumPointByCoordinate(coords=( 299.84224536276128, 336.49197155942568, 151.00578042773998 ))
vP.DatumPointByCoordinate(coords=( 317.32781038342210, 316.98788047801827, 131.31128916216301 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[68], point2=vP.datums[69], point3=vP.datums[70])
vP.DatumAxisByTwoPoint(point1=vP.datums[68], point2=vP.datums[69])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[71], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[72],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[71], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[72])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 298.31748454863856, 347.50408870414822, 154.26671940759974 ))
vP.DatumPointByCoordinate(coords=( 299.84224536276128, 336.49197155942568, 151.00578042773998 ))
vP.DatumPointByCoordinate(coords=( 261.46326718860234, 297.99738250861378, 109.86738632031442 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[74], point2=vP.datums[75], point3=vP.datums[76])
vP.DatumAxisByTwoPoint(point1=vP.datums[74], point2=vP.datums[75])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[77], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[78],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[77], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[78])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 317.32781038342210, 316.98788047801827, 131.31128916216301 ))
vP.DatumPointByCoordinate(coords=( 334.69548266367144, 323.59120602254671, 116.05565785355678 ))
vP.DatumPointByCoordinate(coords=( 344.14295318630275, 290.02499670502948, 61.70433310639236 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[80], point2=vP.datums[81], point3=vP.datums[82])
vP.DatumAxisByTwoPoint(point1=vP.datums[80], point2=vP.datums[81])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[83], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[84],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[83], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[84])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-8', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-8']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 483.58126917449755, 331.82857003053607, 85.17239863321889 ))
vP.DatumPointByCoordinate(coords=( 495.38352751213722, 354.38576920391250, 89.38797911930028 ))
vP.DatumPointByCoordinate(coords=( 507.83347514948252, 341.23686958219150, 101.76181632996754 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 520.37129982586202, 292.00693482344155, 105.81942982063870 ))
vP.DatumPointByCoordinate(coords=( 479.54472231556065, 326.44295878293957, 78.07572370688979 ))
vP.DatumPointByCoordinate(coords=( 483.58126917449755, 331.82857003053607, 85.17239863321889 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 507.83347514948252, 341.23686958219150, 101.76181632996754 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 324.15321298008968, 95.72505701317276 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 282.50893142641547, 100.05659511269566 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 533.75565801220728, 279.24597321791100, 106.01203622506117 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 282.50893142641547, 100.05659511269566 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 206.70544145069476, 50.21116370506772 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 198.40539671936747, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 464.59342765772067, 327.82730635988099, -0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 479.54472231556065, 326.44295878293957, 78.07572370688979 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 282.50893142641547, 100.05659511269566 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 324.15321298008968, 95.72505701317276 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 402.83649969025208, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 324.15321298008968, 95.72505701317276 ))
vP.DatumPointByCoordinate(coords=( 507.83347514948252, 341.23686958219150, 101.76181632996754 ))
vP.DatumPointByCoordinate(coords=( 495.38352751213722, 354.38576920391250, 89.38797911930028 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 593.27799271583206, 404.44436511266304, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 502.05611570194606, 404.94004723904902, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 464.59342765772067, 327.82730635988099, -0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 502.05611570194606, 404.94004723904902, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 593.27799271583206, 404.44436511266304, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 506.61034244868262, 403.40528184839650, 26.48447179046014 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 495.38352751213722, 354.38576920391250, 89.38797911930028 ))
vP.DatumPointByCoordinate(coords=( 483.58126917449755, 331.82857003053607, 85.17239863321889 ))
vP.DatumPointByCoordinate(coords=( 479.54472231556065, 326.44295878293957, 78.07572370688979 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-9', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-9']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 549.38841701614717, 96.95073331518763 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 514.68032124523006, 96.42782182332543 ))
vP.DatumPointByCoordinate(coords=( 479.66231459694319, 469.16090031549140, 93.79563957373409 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 477.60317437700144, 472.64793661557462, 92.86169796608739 ))
vP.DatumPointByCoordinate(coords=( 471.83578655125382, 478.66089243381919, 75.40775321478179 ))
vP.DatumPointByCoordinate(coords=( 475.56195630737619, 523.13191334783642, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 478.08911604837607, 472.00995697903181, 93.81311789334109 ))
vP.DatumPointByCoordinate(coords=( 477.60317437700144, 472.64793661557462, 92.86169796608739 ))
vP.DatumPointByCoordinate(coords=( 478.39556165170541, 472.62087754760279, 93.82727857854805 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 467.35658094043526, 467.68324596676996, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 471.83578655125382, 478.66089243381919, 75.40775321478179 ))
vP.DatumPointByCoordinate(coords=( 477.60317437700144, 472.64793661557462, 92.86169796608739 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 593.27799271583194, 404.44436511266304, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 406.82259813587132, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 600.00000000000000, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 506.61034244868267, 403.40528184839650, 26.48447179046010 ))
vP.DatumPointByCoordinate(coords=( 593.27799271583194, 404.44436511266304, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 502.05611570194611, 404.94004723904902, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 475.56195630737619, 523.13191334783642, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 471.83578655125382, 478.66089243381919, 75.40775321478179 ))
vP.DatumPointByCoordinate(coords=( 467.35658094043526, 467.68324596676996, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 600.00000000000000, 6.22269862082797 ))
vP.DatumPointByCoordinate(coords=( 594.62334633264777, 600.00000000000000, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 600.00000000000000, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 406.82259813587132, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 514.68032124523006, 96.42782182332543 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 549.38841701614717, 96.95073331518763 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 506.61034244868267, 403.40528184839650, 26.48447179046010 ))
vP.DatumPointByCoordinate(coords=( 479.66231459694319, 469.16090031549140, 93.79563957373409 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 514.68032124523006, 96.42782182332543 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-10', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-10']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 209.14217266824204, 600.00000000000000, 89.30089397152958 ))
vP.DatumPointByCoordinate(coords=( 220.29249018794016, 569.51253041112466, 92.78888848831859 ))
vP.DatumPointByCoordinate(coords=( 234.82287918016468, 485.85390847022808, 44.83100928128977 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 337.54094421390397, 600.00000000000000, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 328.61896290639953, 600.00000000000000, 67.69832852173609 ))
vP.DatumPointByCoordinate(coords=( 244.35615162205750, 600.00000000000000, 99.26689102516154 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 225.38805842123895, 476.61025013369056, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 281.92472609041306, 480.52713239302165, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 337.54094421390397, 600.00000000000000, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 234.80255984882297, 482.32316712330140, 40.53839515129875 ))
vP.DatumPointByCoordinate(coords=( 234.82287918016468, 485.85390847022808, 44.83100928128977 ))
vP.DatumPointByCoordinate(coords=( 237.49323532127298, 482.72186535451812, 42.23891517725126 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 279.87849361042134, 483.74063444338810, 26.87725390407690 ))
vP.DatumPointByCoordinate(coords=( 281.92472609041306, 480.52713239302165, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 225.38805842123895, 476.61025013369056, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 234.82287918016468, 485.85390847022808, 44.83100928128977 ))
vP.DatumPointByCoordinate(coords=( 220.29249018794016, 569.51253041112466, 92.78888848831859 ))
vP.DatumPointByCoordinate(coords=( 244.35615162205750, 600.00000000000000, 99.26689102516154 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 209.14217266824204, 600.00000000000000, 89.30089397152958 ))
vP.DatumPointByCoordinate(coords=( 244.35615162205750, 600.00000000000000, 99.26689102516154 ))
vP.DatumPointByCoordinate(coords=( 220.29249018794016, 569.51253041112466, 92.78888848831859 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 281.92472609041306, 480.52713239302165, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 279.87849361042134, 483.74063444338810, 26.87725390407690 ))
vP.DatumPointByCoordinate(coords=( 328.61896290639953, 600.00000000000000, 67.69832852173609 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-11', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-11']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 320.90641785250148, 453.00403040718351, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 316.14812444845842, 459.78405997064181, 51.97534850673903 ))
vP.DatumPointByCoordinate(coords=( 394.70277909194283, 475.69995751417991, 109.57381131286623 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 475.56195630737619, 523.13191334783642, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 439.66581634069490, 600.00000000000000, -0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 337.54094421390403, 600.00000000000000, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 471.83578655125382, 478.66089243381919, 75.40775321478188 ))
vP.DatumPointByCoordinate(coords=( 475.56195630737619, 523.13191334783642, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 467.35658094043526, 467.68324596676990, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 468.78514684299154, 479.49834886596813, 83.59573280875669 ))
vP.DatumPointByCoordinate(coords=( 422.21916707574098, 600.00000000000000, 53.71292295107669 ))
vP.DatumPointByCoordinate(coords=( 439.66581634069490, 600.00000000000000, -0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 328.61896290639959, 600.00000000000000, 67.69832852173607 ))
vP.DatumPointByCoordinate(coords=( 279.87849361042140, 483.74063444338810, 26.87725390407691 ))
vP.DatumPointByCoordinate(coords=( 281.92472609041312, 480.52713239302165, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 439.66581634069490, 600.00000000000000, -0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 422.21916707574098, 600.00000000000000, 53.71292295107669 ))
vP.DatumPointByCoordinate(coords=( 344.76429173368979, 600.00000000000000, 79.38023087890366 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 422.21916707574098, 600.00000000000000, 53.71292295107669 ))
vP.DatumPointByCoordinate(coords=( 468.78514684299154, 479.49834886596813, 83.59573280875669 ))
vP.DatumPointByCoordinate(coords=( 394.70277909194283, 475.69995751417991, 109.57381131286623 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 394.70277909194283, 475.69995751417991, 109.57381131286623 ))
vP.DatumPointByCoordinate(coords=( 316.14812444845842, 459.78405997064181, 51.97534850673903 ))
vP.DatumPointByCoordinate(coords=( 279.87849361042140, 483.74063444338810, 26.87725390407691 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 281.92472609041312, 480.52713239302165, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 279.87849361042140, 483.74063444338810, 26.87725390407691 ))
vP.DatumPointByCoordinate(coords=( 316.14812444845842, 459.78405997064181, 51.97534850673903 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-12', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-12']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 143.55158127150585, 0.00000000000000, -0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 145.95788942496858, 32.28260515529091, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 40.04742449157141, 125.47907047083717, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( -0.00000000000001, 0.00000000000000, 110.26037440554110 ))
vP.DatumPointByCoordinate(coords=( 80.76983778879479, 0.00000000000000, 123.51713860349913 ))
vP.DatumPointByCoordinate(coords=( 143.55158127150585, 0.00000000000000, -0.00000000000001 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 0.00000000000000, 117.57222575138468, 0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 124.84787939168037, 69.25292341987401 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 114.11397978152813, 100.30632410737412 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 100.97455266117537, 81.93319796544537, 95.78162423956135 ))
vP.DatumPointByCoordinate(coords=( 86.25658236822727, 50.00570229504683, 120.05573045710752 ))
vP.DatumPointByCoordinate(coords=( 68.35294395645052, 93.60002839641287, 113.31451368932731 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 40.04878181090298, 128.72435963964057, 30.88756208597044 ))
vP.DatumPointByCoordinate(coords=( 40.04742449157141, 125.47907047083717, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 145.95788942496858, 32.28260515529091, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 68.35294395645052, 93.60002839641287, 113.31451368932731 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 114.11397978152813, 100.30632410737412 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 124.84787939168037, 69.25292341987401 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( -0.00000000000001, 0.00000000000000, 110.26037440554110 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 114.11397978152813, 100.30632410737412 ))
vP.DatumPointByCoordinate(coords=( 68.35294395645052, 93.60002839641287, 113.31451368932731 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 86.25658236822727, 50.00570229504683, 120.05573045710752 ))
vP.DatumPointByCoordinate(coords=( 100.97455266117537, 81.93319796544537, 95.78162423956135 ))
vP.DatumPointByCoordinate(coords=( 145.95788942496858, 32.28260515529091, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 0.00000000000000, 124.84787939168037, 69.25292341987401 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 117.57222575138468, 0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 40.04742449157141, 125.47907047083717, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-13', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-13']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 193.85756043270982, 37.78659735517851, 0.00000000000003 ))
vP.DatumPointByCoordinate(coords=( 207.80968013059714, 98.75890009340091, 103.73082727954662 ))
vP.DatumPointByCoordinate(coords=( 267.78943536544028, 1.05406175289031, 200.00000000000003 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 396.96137261175454, 0.00000000000000, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 275.85145011810999, 109.13474224245778, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 251.38980576443910, 107.62163849303579, 0.00000000000001 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 268.11073582732791, 0.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 275.61525290158721, 0.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 331.54035293848949, 0.00000000000000, 153.50529511580868 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 399.85695589929867, 32.87033139690691, 67.48083233258005 ))
vP.DatumPointByCoordinate(coords=( 331.54035293848949, 0.00000000000000, 153.50529511580868 ))
vP.DatumPointByCoordinate(coords=( 275.61525290158721, 0.00000000000000, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 275.85145011810999, 109.13474224245778, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 396.96137261175454, 0.00000000000000, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 399.93720748429536, 0.00000000000000, 5.10027746520784 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 240.12952162828370, 131.06205098312034, 112.96363528589652 ))
vP.DatumPointByCoordinate(coords=( 230.74582213651126, 130.44338744813595, 112.78474356679109 ))
vP.DatumPointByCoordinate(coords=( 251.38980576443910, 107.62163849303579, 0.00000000000001 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 268.11073582732791, 0.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 267.78943536544028, 1.05406175289031, 200.00000000000003 ))
vP.DatumPointByCoordinate(coords=( 269.43368493013753, 5.77967824002194, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 251.38980576443910, 107.62163849303579, 0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 230.74582213651126, 130.44338744813595, 112.78474356679109 ))
vP.DatumPointByCoordinate(coords=( 228.97596426435044, 129.06984482197964, 114.60979350699634 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 399.85695589929867, 32.87033139690691, 67.48083233258005 ))
vP.DatumPointByCoordinate(coords=( 409.71554568342788, 15.32809717679227, 51.01279931900922 ))
vP.DatumPointByCoordinate(coords=( 407.69305428867733, 0.00000000000001, 50.94815815573406 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 409.71554568342788, 15.32809717679227, 51.01279931900922 ))
vP.DatumPointByCoordinate(coords=( 399.93720748429536, 0.00000000000000, 5.10027746520784 ))
vP.DatumPointByCoordinate(coords=( 407.69305428867733, 0.00000000000001, 50.94815815573406 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 240.12952162828370, 131.06205098312034, 112.96363528589652 ))
vP.DatumPointByCoordinate(coords=( 235.57152538264552, 123.73551643376175, 123.26767577027169 ))
vP.DatumPointByCoordinate(coords=( 228.97596426435044, 129.06984482197964, 114.60979350699634 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[62], point2=vP.datums[63], point3=vP.datums[64])
vP.DatumAxisByTwoPoint(point1=vP.datums[62], point2=vP.datums[63])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[66],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[66])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 228.97596426435044, 129.06984482197964, 114.60979350699634 ))
vP.DatumPointByCoordinate(coords=( 235.57152538264552, 123.73551643376175, 123.26767577027169 ))
vP.DatumPointByCoordinate(coords=( 269.43368493013753, 5.77967824002194, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[68], point2=vP.datums[69], point3=vP.datums[70])
vP.DatumAxisByTwoPoint(point1=vP.datums[68], point2=vP.datums[69])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[71], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[72],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[71], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[72])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-14', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-14']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 82.08525698919254, 320.70846345997990, 99.09475161355839 ))
vP.DatumPointByCoordinate(coords=( 181.25681599582643, 230.22747341866688, 137.23012227410368 ))
vP.DatumPointByCoordinate(coords=( 197.44443520954422, 184.83397929872177, 108.92918786397236 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 82.15785382329850, 315.95265203070039, -0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 164.35180339595806, 367.01937270046147, 0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 168.10234969658796, 371.75986728081529, 49.75047633893018 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 99.12569698499641, 214.96983544267653, 3.96638257603151 ))
vP.DatumPointByCoordinate(coords=( 99.82392006356918, 215.60609332407850, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 82.15785382329850, 315.95265203070039, -0.00000000000001 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 181.25681599582643, 230.22747341866688, 137.23012227410368 ))
vP.DatumPointByCoordinate(coords=( 261.46326718860229, 297.99738250861373, 109.86738632031444 ))
vP.DatumPointByCoordinate(coords=( 268.20219634913673, 290.78260454581823, 102.59060420064333 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 198.44642197988122, 184.84006703104578, 108.26323705343299 ))
vP.DatumPointByCoordinate(coords=( 193.07527401378826, 204.98840162366398, -0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 99.82392006356918, 215.60609332407850, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 99.82392006356918, 215.60609332407850, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 193.07527401378826, 204.98840162366398, -0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 250.05717219969904, 290.32377172795907, -0.00000000000001 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 268.20219634913673, 290.78260454581823, 102.59060420064333 ))
vP.DatumPointByCoordinate(coords=( 261.46326718860229, 297.99738250861373, 109.86738632031444 ))
vP.DatumPointByCoordinate(coords=( 205.68230887979109, 344.70473635569005, 90.14580941715011 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 193.07527401378826, 204.98840162366398, -0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 198.44642197988122, 184.84006703104578, 108.26323705343299 ))
vP.DatumPointByCoordinate(coords=( 268.20219634913673, 290.78260454581823, 102.59060420064333 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 205.68230887979109, 344.70473635569005, 90.14580941715011 ))
vP.DatumPointByCoordinate(coords=( 143.00718007398808, 357.83904465728625, 84.23486340183220 ))
vP.DatumPointByCoordinate(coords=( 168.10234969658796, 371.75986728081529, 49.75047633893018 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 205.68230887979109, 344.70473635569005, 90.14580941715011 ))
vP.DatumPointByCoordinate(coords=( 261.46326718860229, 297.99738250861373, 109.86738632031444 ))
vP.DatumPointByCoordinate(coords=( 181.25681599582643, 230.22747341866688, 137.23012227410368 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-15', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-15']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 334.69548266367144, 323.59120602254677, 116.05565785355675 ))
vP.DatumPointByCoordinate(coords=( 483.58126917449761, 331.82857003053607, 85.17239863321890 ))
vP.DatumPointByCoordinate(coords=( 479.54472231556065, 326.44295878293957, 78.07572370688979 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 348.49690744664804, 289.64352325667949, 0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 320.90641785250153, 453.00403040718351, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 316.14812444845842, 459.78405997064181, 51.97534850673904 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 374.05914073908855, 272.77318527011772, 26.44048724466230 ))
vP.DatumPointByCoordinate(coords=( 372.07538068840552, 275.00037584965503, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 348.49690744664804, 289.64352325667949, 0.00000000000001 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 471.83578655125382, 478.66089243381919, 75.40775321478185 ))
vP.DatumPointByCoordinate(coords=( 468.78514684299154, 479.49834886596807, 83.59573280875668 ))
vP.DatumPointByCoordinate(coords=( 394.70277909194283, 475.69995751417997, 109.57381131286621 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 502.05611570194611, 404.94004723904902, 0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 506.61034244868262, 403.40528184839650, 26.48447179046012 ))
vP.DatumPointByCoordinate(coords=( 479.66231459694319, 469.16090031549135, 93.79563957373412 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 320.90641785250153, 453.00403040718351, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 348.49690744664804, 289.64352325667949, 0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 372.07538068840552, 275.00037584965503, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 398.33623628203298, 455.94407138770987, 142.04799756705839 ))
vP.DatumPointByCoordinate(coords=( 460.89235511111929, 454.70220526533359, 127.64131573007880 ))
vP.DatumPointByCoordinate(coords=( 476.53135793754427, 438.34798119041784, 119.15881057346276 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 316.14812444845842, 459.78405997064181, 51.97534850673904 ))
vP.DatumPointByCoordinate(coords=( 394.70277909194283, 475.69995751417997, 109.57381131286621 ))
vP.DatumPointByCoordinate(coords=( 398.33623628203298, 455.94407138770987, 142.04799756705839 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 495.38352751213722, 354.38576920391245, 89.38797911930028 ))
vP.DatumPointByCoordinate(coords=( 476.53135793754427, 438.34798119041784, 119.15881057346276 ))
vP.DatumPointByCoordinate(coords=( 479.66231459694319, 469.16090031549135, 93.79563957373412 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 502.05611570194611, 404.94004723904902, 0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 464.59342765772072, 327.82730635988099, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 479.54472231556065, 326.44295878293957, 78.07572370688979 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 477.60317437700144, 472.64793661557462, 92.86169796608735 ))
vP.DatumPointByCoordinate(coords=( 478.08911604837607, 472.00995697903181, 93.81311789334112 ))
vP.DatumPointByCoordinate(coords=( 460.89235511111929, 454.70220526533359, 127.64131573007880 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[62], point2=vP.datums[63], point3=vP.datums[64])
vP.DatumAxisByTwoPoint(point1=vP.datums[62], point2=vP.datums[63])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[66],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[66])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 471.83578655125382, 478.66089243381919, 75.40775321478185 ))
vP.DatumPointByCoordinate(coords=( 477.60317437700144, 472.64793661557462, 92.86169796608735 ))
vP.DatumPointByCoordinate(coords=( 468.78514684299154, 479.49834886596807, 83.59573280875668 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[68], point2=vP.datums[69], point3=vP.datums[70])
vP.DatumAxisByTwoPoint(point1=vP.datums[68], point2=vP.datums[69])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[71], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[72],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[71], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[72])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 372.07538068840552, 275.00037584965503, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 374.05914073908855, 272.77318527011772, 26.44048724466230 ))
vP.DatumPointByCoordinate(coords=( 479.54472231556065, 326.44295878293957, 78.07572370688979 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[74], point2=vP.datums[75], point3=vP.datums[76])
vP.DatumAxisByTwoPoint(point1=vP.datums[74], point2=vP.datums[75])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[77], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[78],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[77], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[78])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 460.89235511111929, 454.70220526533359, 127.64131573007880 ))
vP.DatumPointByCoordinate(coords=( 478.08911604837607, 472.00995697903181, 93.81311789334112 ))
vP.DatumPointByCoordinate(coords=( 479.66231459694319, 469.16090031549135, 93.79563957373412 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[80], point2=vP.datums[81], point3=vP.datums[82])
vP.DatumAxisByTwoPoint(point1=vP.datums[80], point2=vP.datums[81])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[83], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[84],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[83], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[84])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-16', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-16']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( -0.00000000000001, 337.22905436907695, 81.38475309015155 ))
vP.DatumPointByCoordinate(coords=( 56.76604562883993, 313.99665292665821, 82.54548045069346 ))
vP.DatumPointByCoordinate(coords=( 68.83263500799600, 311.03922417744570, 69.46598208289247 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 0.00000000000001, 529.11005682998439, 0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 443.72459772869473, 103.48305722416042 ))
vP.DatumPointByCoordinate(coords=( -0.00000000000001, 362.69025149527943, 108.61523448528696 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 82.15785382329851, 315.95265203070039, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 164.35180339595806, 367.01937270046142, 0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 181.64113009307863, 444.75559218473927, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 143.00718007398811, 357.83904465728625, 84.23486340183223 ))
vP.DatumPointByCoordinate(coords=( 82.08525698919257, 320.70846345997984, 99.09475161355836 ))
vP.DatumPointByCoordinate(coords=( 80.05240228059734, 321.04705284937302, 100.75452335445766 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 112.69217116366040, 486.83193422543394, 111.33973178910405 ))
vP.DatumPointByCoordinate(coords=( 182.94824783570914, 445.06332456050620, 22.85601682569859 ))
vP.DatumPointByCoordinate(coords=( 168.10234969658796, 371.75986728081523, 49.75047633893020 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 75.00417322925176, 338.57601143049982, 117.18869801691318 ))
vP.DatumPointByCoordinate(coords=( -0.00000000000001, 362.69025149527943, 108.61523448528696 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 443.72459772869473, 103.48305722416042 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 12.45504127128845, 535.90586262821546, 0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 100.46861047126251, 493.34835366821915, 109.77868906264555 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 443.72459772869473, 103.48305722416042 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 181.64113009307863, 444.75559218473927, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 164.35180339595806, 367.01937270046142, 0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 168.10234969658796, 371.75986728081523, 49.75047633893020 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 112.69217116366040, 486.83193422543394, 111.33973178910405 ))
vP.DatumPointByCoordinate(coords=( 100.46861047126251, 493.34835366821915, 109.77868906264555 ))
vP.DatumPointByCoordinate(coords=( 12.45504127128845, 535.90586262821546, 0.00000000000001 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 68.83263500799600, 311.03922417744570, 69.46598208289247 ))
vP.DatumPointByCoordinate(coords=( 82.08525698919257, 320.70846345997984, 99.09475161355836 ))
vP.DatumPointByCoordinate(coords=( 143.00718007398811, 357.83904465728625, 84.23486340183223 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( -0.00000000000001, 337.22905436907695, 81.38475309015155 ))
vP.DatumPointByCoordinate(coords=( -0.00000000000001, 362.69025149527943, 108.61523448528696 ))
vP.DatumPointByCoordinate(coords=( 75.00417322925176, 338.57601143049982, 117.18869801691318 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[62], point2=vP.datums[63], point3=vP.datums[64])
vP.DatumAxisByTwoPoint(point1=vP.datums[62], point2=vP.datums[63])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[66],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[66])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 80.05240228059734, 321.04705284937302, 100.75452335445766 ))
vP.DatumPointByCoordinate(coords=( 82.08525698919257, 320.70846345997984, 99.09475161355836 ))
vP.DatumPointByCoordinate(coords=( 68.83263500799600, 311.03922417744570, 69.46598208289247 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[68], point2=vP.datums[69], point3=vP.datums[70])
vP.DatumAxisByTwoPoint(point1=vP.datums[68], point2=vP.datums[69])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[71], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[72],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[71], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[72])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-17', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-17']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 112.69217116366038, 486.83193422543394, 111.33973178910404 ))
vP.DatumPointByCoordinate(coords=( 100.46861047126251, 493.34835366821915, 109.77868906264557 ))
vP.DatumPointByCoordinate(coords=( 124.02726812509619, 517.61896722936149, 142.00664784938184 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 203.19156900689680, 525.65034741242766, 110.25403670784542 ))
vP.DatumPointByCoordinate(coords=( 234.82287918016470, 485.85390847022808, 44.83100928128977 ))
vP.DatumPointByCoordinate(coords=( 234.80255984882297, 482.32316712330146, 40.53839515129877 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 124.02726812509619, 517.61896722936149, 142.00664784938184 ))
vP.DatumPointByCoordinate(coords=( 107.59007792746938, 600.00000000000000, 127.43938346154451 ))
vP.DatumPointByCoordinate(coords=( 209.14217266824204, 600.00000000000000, 89.30089397152960 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 225.38805842123895, 476.61025013369056, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 181.64113009307866, 444.75559218473927, 0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 182.94824783570917, 445.06332456050620, 22.85601682569854 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 234.82287918016470, 485.85390847022808, 44.83100928128977 ))
vP.DatumPointByCoordinate(coords=( 220.29249018794016, 569.51253041112466, 92.78888848831858 ))
vP.DatumPointByCoordinate(coords=( 209.14217266824204, 600.00000000000000, 89.30089397152960 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 8.48071268742987, 600.00000000000000, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 107.59007792746938, 600.00000000000000, 127.43938346154451 ))
vP.DatumPointByCoordinate(coords=( 124.02726812509619, 517.61896722936149, 142.00664784938184 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 181.64113009307866, 444.75559218473927, 0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 225.38805842123895, 476.61025013369056, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 184.20262791214384, 600.00000000000000, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 100.46861047126251, 493.34835366821915, 109.77868906264557 ))
vP.DatumPointByCoordinate(coords=( 112.69217116366038, 486.83193422543394, 111.33973178910404 ))
vP.DatumPointByCoordinate(coords=( 182.94824783570917, 445.06332456050620, 22.85601682569854 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 209.14217266824204, 600.00000000000000, 89.30089397152960 ))
vP.DatumPointByCoordinate(coords=( 107.59007792746938, 600.00000000000000, 127.43938346154451 ))
vP.DatumPointByCoordinate(coords=( 8.48071268742987, 600.00000000000000, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 203.19156900689680, 525.65034741242766, 110.25403670784542 ))
vP.DatumPointByCoordinate(coords=( 220.29249018794016, 569.51253041112466, 92.78888848831858 ))
vP.DatumPointByCoordinate(coords=( 234.82287918016470, 485.85390847022808, 44.83100928128977 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-18', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-18']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 475.56195630737619, 523.13191334783642, -0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 471.83578655125376, 478.66089243381919, 75.40775321478174 ))
vP.DatumPointByCoordinate(coords=( 477.60317437700144, 472.64793661557462, 92.86169796608741 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 439.66581634069490, 600.00000000000000, 0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 475.56195630737619, 523.13191334783642, -0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 594.62334633264777, 600.00000000000000, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 600.00000000000000, 6.22269862082797 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 600.00000000000000, 138.44778631671718 ))
vP.DatumPointByCoordinate(coords=( 522.43331995855806, 600.00000000000000, 176.60408781943829 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 549.38841701614717, 96.95073331518765 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 600.00000000000000, 138.44778631671718 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 600.00000000000000, 6.22269862082797 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 422.21916707574098, 600.00000000000000, 53.71292295107671 ))
vP.DatumPointByCoordinate(coords=( 468.78514684299148, 479.49834886596818, 83.59573280875665 ))
vP.DatumPointByCoordinate(coords=( 471.83578655125376, 478.66089243381919, 75.40775321478174 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 468.78514684299148, 479.49834886596818, 83.59573280875665 ))
vP.DatumPointByCoordinate(coords=( 477.60317437700144, 472.64793661557462, 92.86169796608741 ))
vP.DatumPointByCoordinate(coords=( 471.83578655125376, 478.66089243381919, 75.40775321478174 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 549.38841701614717, 96.95073331518765 ))
vP.DatumPointByCoordinate(coords=( 478.39556165170541, 472.62087754760284, 93.82727857854808 ))
vP.DatumPointByCoordinate(coords=( 522.43331995855806, 600.00000000000000, 176.60408781943829 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 477.60317437700144, 472.64793661557462, 92.86169796608741 ))
vP.DatumPointByCoordinate(coords=( 468.78514684299148, 479.49834886596818, 83.59573280875665 ))
vP.DatumPointByCoordinate(coords=( 422.21916707574098, 600.00000000000000, 53.71292295107671 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-19', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-19']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 145.95788942496861, 32.28260515529088, 0.00000000000003 ))
vP.DatumPointByCoordinate(coords=( 100.97455266117538, 81.93319796544539, 95.78162423956137 ))
vP.DatumPointByCoordinate(coords=( 86.25658236822729, 50.00570229504683, 120.05573045710753 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 205.37571973418332, 0.00000000000000, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 193.85756043270982, 37.78659735517851, 0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 145.95788942496861, 32.28260515529088, 0.00000000000003 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 80.76983778879480, 0.00000000000000, 123.51713860349913 ))
vP.DatumPointByCoordinate(coords=( 108.03927642266686, 0.00000000000000, 167.46031305307622 ))
vP.DatumPointByCoordinate(coords=( 263.47543414705092, 0.00000000000000, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 268.11073582732791, 0.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 267.78943536544028, 1.05406175289031, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 207.80968013059709, 98.75890009340091, 103.73082727954663 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 145.95788942496861, 32.28260515529088, 0.00000000000003 ))
vP.DatumPointByCoordinate(coords=( 193.85756043270982, 37.78659735517851, 0.00000000000001 ))
vP.DatumPointByCoordinate(coords=( 207.80968013059709, 98.75890009340091, 103.73082727954663 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 207.80968013059709, 98.75890009340091, 103.73082727954663 ))
vP.DatumPointByCoordinate(coords=( 267.78943536544028, 1.05406175289031, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 263.47543414705092, 0.00000000000000, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 268.11073582732791, 0.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 263.47543414705092, 0.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 267.78943536544028, 1.05406175289031, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 80.76983778879480, 0.00000000000000, 123.51713860349913 ))
vP.DatumPointByCoordinate(coords=( 86.25658236822729, 50.00570229504683, 120.05573045710753 ))
vP.DatumPointByCoordinate(coords=( 108.03927642266686, 0.00000000000000, 167.46031305307622 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-20', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-20']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 456.41860430618840, 142.98948587190489, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 425.33289132129948, 184.22186892311987, 67.65062262490514 ))
vP.DatumPointByCoordinate(coords=( 408.16313202242583, 157.22026779081762, 96.32927290483653 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 114.62089941940562, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 150.58040730481378, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 456.41860430618840, 142.98948587190489, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 417.45664354525684, 25.27312259739949, 55.22718146493580 ))
vP.DatumPointByCoordinate(coords=( 488.65113801855250, 30.34793826668003, 101.02028944742440 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 88.93109406791275, 58.10001940676285 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 511.71229281689136, 216.61593336038925, 111.55730423221009 ))
vP.DatumPointByCoordinate(coords=( 482.04225176219848, 148.58058097965895, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 464.35638396524712, 137.00624197912191, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 456.41860430618840, 142.98948587190489, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 150.58040730481378, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 179.84869739046383, 46.18027897541782 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 114.62089941940562, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 88.93109406791275, 58.10001940676285 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 125.05484864351183, 91.48686227423767 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 482.04225176219848, 148.58058097965895, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 511.71229281689136, 216.61593336038925, 111.55730423221009 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 179.84869739046383, 46.18027897541782 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 479.54259616785180, 128.85060507293707, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 464.35638396524712, 137.00624197912191, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 482.04225176219848, 148.58058097965895, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 125.05484864351183, 91.48686227423767 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 88.93109406791275, 58.10001940676285 ))
vP.DatumPointByCoordinate(coords=( 488.65113801855250, 30.34793826668003, 101.02028944742440 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 417.45664354525684, 25.27312259739949, 55.22718146493580 ))
vP.DatumPointByCoordinate(coords=( 410.56533356585709, 44.88650450844317, 72.05223967898770 ))
vP.DatumPointByCoordinate(coords=( 456.56561672258630, 135.31978053492006, 193.79289062439952 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 410.56533356585709, 44.88650450844317, 72.05223967898770 ))
vP.DatumPointByCoordinate(coords=( 408.16313202242583, 157.22026779081762, 96.32927290483653 ))
vP.DatumPointByCoordinate(coords=( 456.56561672258630, 135.31978053492006, 193.79289062439952 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[62], point2=vP.datums[63], point3=vP.datums[64])
vP.DatumAxisByTwoPoint(point1=vP.datums[62], point2=vP.datums[63])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[66],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[66])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-21', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-21']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 593.27799271583194, 404.44436511266309, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 506.61034244868262, 403.40528184839650, 26.48447179046009 ))
vP.DatumPointByCoordinate(coords=( 495.38352751213722, 354.38576920391245, 89.38797911930030 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 406.82259813587132, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 593.27799271583194, 404.44436511266309, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 402.83649969025208, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 324.15321298008973, 95.72505701317274 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 414.78495000213144, 182.17286023220123 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 514.68032124523006, 96.42782182332542 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 476.53135793754433, 438.34798119041778, 119.15881057346274 ))
vP.DatumPointByCoordinate(coords=( 515.13737771530646, 403.76823930080224, 162.21941396201993 ))
vP.DatumPointByCoordinate(coords=( 507.83347514948252, 341.23686958219150, 101.76181632996754 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 506.61034244868262, 403.40528184839650, 26.48447179046009 ))
vP.DatumPointByCoordinate(coords=( 479.66231459694325, 469.16090031549140, 93.79563957373411 ))
vP.DatumPointByCoordinate(coords=( 476.53135793754433, 438.34798119041778, 119.15881057346274 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 515.13737771530646, 403.76823930080224, 162.21941396201993 ))
vP.DatumPointByCoordinate(coords=( 476.53135793754433, 438.34798119041778, 119.15881057346274 ))
vP.DatumPointByCoordinate(coords=( 479.66231459694325, 469.16090031549140, 93.79563957373411 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 324.15321298008973, 95.72505701317274 ))
vP.DatumPointByCoordinate(coords=( 507.83347514948252, 341.23686958219150, 101.76181632996754 ))
vP.DatumPointByCoordinate(coords=( 515.13737771530646, 403.76823930080224, 162.21941396201993 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 514.68032124523006, 96.42782182332542 ))
vP.DatumPointByCoordinate(coords=( 479.66231459694325, 469.16090031549140, 93.79563957373411 ))
vP.DatumPointByCoordinate(coords=( 506.61034244868262, 403.40528184839650, 26.48447179046009 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-22', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-22']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 0.00000000000001, 114.11397978152810, 100.30632410737410 ))
vP.DatumPointByCoordinate(coords=( -0.00000000000001, 145.70280161442895, 163.29005256275008 ))
vP.DatumPointByCoordinate(coords=( 38.19612060832482, 149.00521675999653, 199.99999999999997 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 88.01741522207377, 93.73536088691495, 99.59168676123312 ))
vP.DatumPointByCoordinate(coords=( 40.04878181090296, 128.72435963964051, 30.88756208597046 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 124.84787939168034, 69.25292341987392 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 50.57807381612290, 144.10734241071250, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 152.65015166265388, 193.36029220931468, 199.99999999999997 ))
vP.DatumPointByCoordinate(coords=( 191.04664134247091, 160.57232800005823, 124.71248107077699 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 197.44443520954425, 184.83397929872177, 108.92918786397236 ))
vP.DatumPointByCoordinate(coords=( 191.04664134247091, 160.57232800005823, 124.71248107077699 ))
vP.DatumPointByCoordinate(coords=( 152.65015166265388, 193.36029220931468, 199.99999999999997 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 82.08525698919260, 320.70846345997984, 99.09475161355837 ))
vP.DatumPointByCoordinate(coords=( 68.83263500799599, 311.03922417744570, 69.46598208289245 ))
vP.DatumPointByCoordinate(coords=( 99.12569698499641, 214.96983544267653, 3.96638257603153 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 151.70629670214404, 211.15288734500174, 199.99999999999997 ))
vP.DatumPointByCoordinate(coords=( 110.36328486810778, 239.00052766720063, 199.99999999999997 ))
vP.DatumPointByCoordinate(coords=( 80.05240228059735, 321.04705284937302, 100.75452335445769 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 152.65015166265388, 193.36029220931468, 199.99999999999997 ))
vP.DatumPointByCoordinate(coords=( 50.57807381612290, 144.10734241071250, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 38.19612060832482, 149.00521675999653, 199.99999999999997 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 0.00000000000001, 217.86831069596249, 103.52888860376888 ))
vP.DatumPointByCoordinate(coords=( 56.76604562883993, 313.99665292665821, 82.54548045069343 ))
vP.DatumPointByCoordinate(coords=( 80.05240228059735, 321.04705284937302, 100.75452335445769 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 0.00000000000001, 114.11397978152810, 100.30632410737410 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 124.84787939168034, 69.25292341987392 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000001, 217.86831069596249, 103.52888860376888 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 40.04878181090296, 128.72435963964051, 30.88756208597046 ))
vP.DatumPointByCoordinate(coords=( 99.12569698499641, 214.96983544267653, 3.96638257603153 ))
vP.DatumPointByCoordinate(coords=( 68.83263500799599, 311.03922417744570, 69.46598208289245 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 88.01741522207377, 93.73536088691495, 99.59168676123312 ))
vP.DatumPointByCoordinate(coords=( 191.04664134247091, 160.57232800005823, 124.71248107077699 ))
vP.DatumPointByCoordinate(coords=( 197.44443520954425, 184.83397929872177, 108.92918786397236 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[62], point2=vP.datums[63], point3=vP.datums[64])
vP.DatumAxisByTwoPoint(point1=vP.datums[62], point2=vP.datums[63])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[66],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[66])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 82.08525698919260, 320.70846345997984, 99.09475161355837 ))
vP.DatumPointByCoordinate(coords=( 80.05240228059735, 321.04705284937302, 100.75452335445769 ))
vP.DatumPointByCoordinate(coords=( 56.76604562883993, 313.99665292665821, 82.54548045069343 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[68], point2=vP.datums[69], point3=vP.datums[70])
vP.DatumAxisByTwoPoint(point1=vP.datums[68], point2=vP.datums[69])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[71], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[72],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[71], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[72])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-23', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-23']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 115.49202185219657, 378.37667619719787, 118.47159797898863 ))
vP.DatumPointByCoordinate(coords=( 112.69217116366038, 486.83193422543394, 111.33973178910404 ))
vP.DatumPointByCoordinate(coords=( 124.57156958297779, 517.13659708255614, 141.92367431021484 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 292.67010469526809, 367.24268555303217, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 298.31748454863856, 347.50408870414822, 154.26671940759974 ))
vP.DatumPointByCoordinate(coords=( 205.68230887979115, 344.70473635569005, 90.14580941715012 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 147.14990159986743, 495.48831914605364, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 240.08941089378885, 492.12437914915563, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 309.63965132805612, 415.79238184552349, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 205.68230887979115, 344.70473635569005, 90.14580941715012 ))
vP.DatumPointByCoordinate(coords=( 168.10234969658799, 371.75986728081529, 49.75047633893018 ))
vP.DatumPointByCoordinate(coords=( 143.00718007398811, 357.83904465728625, 84.23486340183223 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 168.10234969658799, 371.75986728081529, 49.75047633893018 ))
vP.DatumPointByCoordinate(coords=( 182.94824783570917, 445.06332456050620, 22.85601682569858 ))
vP.DatumPointByCoordinate(coords=( 112.69217116366038, 486.83193422543394, 111.33973178910404 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 124.57156958297779, 517.13659708255614, 141.92367431021484 ))
vP.DatumPointByCoordinate(coords=( 112.69217116366038, 486.83193422543394, 111.33973178910404 ))
vP.DatumPointByCoordinate(coords=( 182.94824783570917, 445.06332456050620, 22.85601682569858 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 240.08941089378885, 492.12437914915563, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 147.14990159986743, 495.48831914605364, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 124.57156958297779, 517.13659708255614, 141.92367431021484 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 234.82287918016462, 485.85390847022813, 44.83100928128989 ))
vP.DatumPointByCoordinate(coords=( 237.49323532127300, 482.72186535451812, 42.23891517725129 ))
vP.DatumPointByCoordinate(coords=( 319.87917071103760, 400.10349855540863, 142.68761249733879 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 168.10234969658799, 371.75986728081529, 49.75047633893018 ))
vP.DatumPointByCoordinate(coords=( 205.68230887979115, 344.70473635569005, 90.14580941715012 ))
vP.DatumPointByCoordinate(coords=( 298.31748454863856, 347.50408870414822, 154.26671940759974 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 309.63965132805612, 415.79238184552349, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 319.87917071103760, 400.10349855540863, 142.68761249733879 ))
vP.DatumPointByCoordinate(coords=( 298.31748454863856, 347.50408870414822, 154.26671940759974 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 234.80255984882291, 482.32316712330140, 40.53839515129872 ))
vP.DatumPointByCoordinate(coords=( 237.49323532127300, 482.72186535451812, 42.23891517725129 ))
vP.DatumPointByCoordinate(coords=( 234.82287918016462, 485.85390847022813, 44.83100928128989 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[62], point2=vP.datums[63], point3=vP.datums[64])
vP.DatumAxisByTwoPoint(point1=vP.datums[62], point2=vP.datums[63])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[66],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[66])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-24', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-24']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 240.08941089378885, 492.12437914915563, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 203.19156900689677, 525.65034741242766, 110.25403670784543 ))
vP.DatumPointByCoordinate(coords=( 220.29249018794016, 569.51253041112466, 92.78888848831858 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 326.00743770537048, 600.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 383.69817113619706, 468.74476006346526, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 309.63965132805612, 415.79238184552349, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 244.35615162205744, 600.00000000000000, 99.26689102516153 ))
vP.DatumPointByCoordinate(coords=( 328.61896290639959, 600.00000000000000, 67.69832852173605 ))
vP.DatumPointByCoordinate(coords=( 344.76429173368984, 600.00000000000000, 79.38023087890363 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 328.61896290639959, 600.00000000000000, 67.69832852173605 ))
vP.DatumPointByCoordinate(coords=( 279.87849361042140, 483.74063444338810, 26.87725390407688 ))
vP.DatumPointByCoordinate(coords=( 316.14812444845842, 459.78405997064181, 51.97534850673905 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 394.70277909194283, 475.69995751417991, 109.57381131286623 ))
vP.DatumPointByCoordinate(coords=( 398.33623628203298, 455.94407138770987, 142.04799756705839 ))
vP.DatumPointByCoordinate(coords=( 383.69817113619706, 468.74476006346526, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 319.92169978010168, 400.11885451946625, 142.65012036099048 ))
vP.DatumPointByCoordinate(coords=( 319.87917071103766, 400.10349855540863, 142.68761249733882 ))
vP.DatumPointByCoordinate(coords=( 309.63965132805612, 415.79238184552349, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 394.70277909194283, 475.69995751417991, 109.57381131286623 ))
vP.DatumPointByCoordinate(coords=( 316.14812444845842, 459.78405997064181, 51.97534850673905 ))
vP.DatumPointByCoordinate(coords=( 319.92169978010168, 400.11885451946625, 142.65012036099048 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 319.92169978010168, 400.11885451946625, 142.65012036099048 ))
vP.DatumPointByCoordinate(coords=( 316.14812444845842, 459.78405997064181, 51.97534850673905 ))
vP.DatumPointByCoordinate(coords=( 279.87849361042140, 483.74063444338810, 26.87725390407688 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 237.49323532127300, 482.72186535451812, 42.23891517725127 ))
vP.DatumPointByCoordinate(coords=( 234.82287918016465, 485.85390847022808, 44.83100928128984 ))
vP.DatumPointByCoordinate(coords=( 203.19156900689677, 525.65034741242766, 110.25403670784543 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 234.82287918016465, 485.85390847022808, 44.83100928128984 ))
vP.DatumPointByCoordinate(coords=( 237.49323532127300, 482.72186535451812, 42.23891517725127 ))
vP.DatumPointByCoordinate(coords=( 279.87849361042140, 483.74063444338810, 26.87725390407688 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 203.19156900689677, 525.65034741242766, 110.25403670784543 ))
vP.DatumPointByCoordinate(coords=( 234.82287918016465, 485.85390847022808, 44.83100928128984 ))
vP.DatumPointByCoordinate(coords=( 220.29249018794016, 569.51253041112466, 92.78888848831858 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[62], point2=vP.datums[63], point3=vP.datums[64])
vP.DatumAxisByTwoPoint(point1=vP.datums[62], point2=vP.datums[63])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[66],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[66])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-25', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-25']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 488.65113801855250, 30.34793826668000, 101.02028944742439 ))
vP.DatumPointByCoordinate(coords=( 498.44664721887602, 0.00000000000001, 109.84859549549830 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 0.00000000000000, 89.67306280956568 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 125.05484864351183, 91.48686227423764 ))
vP.DatumPointByCoordinate(coords=( 489.74553649436160, 138.47379855252163, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 479.54259616785180, 128.85060507293707, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 0.00000000000000, 89.67306280956568 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 0.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 118.96225391083983, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 498.44664721887602, 0.00000000000001, 109.84859549549830 ))
vP.DatumPointByCoordinate(coords=( 514.46998938463923, 0.00000000000001, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 0.00000000000000, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 488.65113801855250, 30.34793826668000, 101.02028944742439 ))
vP.DatumPointByCoordinate(coords=( 479.54259616785180, 128.85060507293707, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 514.46998938463923, 0.00000000000001, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 118.96225391083983, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 489.74553649436160, 138.47379855252163, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 125.05484864351183, 91.48686227423764 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 479.54259616785180, 128.85060507293707, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 489.74553649436160, 138.47379855252163, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 118.96225391083983, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-26', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-26']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 275.61525290158721, -0.00000000000001, 200.00000000000003 ))
vP.DatumPointByCoordinate(coords=( 331.54035293848949, 0.00000000000000, 153.50529511580868 ))
vP.DatumPointByCoordinate(coords=( 399.85695589929867, 32.87033139690689, 67.48083233258004 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 254.42585829480373, 109.20366409577126, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 359.75154253002955, 189.05543390950379, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 455.20740236856375, 136.37577864407794, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 235.57152538264552, 123.73551643376177, 123.26767577027167 ))
vP.DatumPointByCoordinate(coords=( 254.42585829480373, 109.20366409577126, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 269.43368493013753, 5.77967824002197, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 359.75154253002955, 189.05543390950379, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 330.64500374835717, 200.68979068726719, 110.29055547578790 ))
vP.DatumPointByCoordinate(coords=( 345.77081296778084, 191.47027812035185, 92.62811451065159 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 456.56561672258624, 135.31978053492008, 193.79289062439952 ))
vP.DatumPointByCoordinate(coords=( 410.56533356585709, 44.88650450844319, 72.05223967898773 ))
vP.DatumPointByCoordinate(coords=( 399.85695589929867, 32.87033139690689, 67.48083233258004 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 345.77081296778084, 191.47027812035185, 92.62811451065159 ))
vP.DatumPointByCoordinate(coords=( 298.39686795337121, 125.39276822627602, 69.56268282490547 ))
vP.DatumPointByCoordinate(coords=( 399.85695589929867, 32.87033139690689, 67.48083233258004 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 410.56533356585709, 44.88650450844319, 72.05223967898773 ))
vP.DatumPointByCoordinate(coords=( 456.56561672258624, 135.31978053492008, 193.79289062439952 ))
vP.DatumPointByCoordinate(coords=( 408.16313202242583, 157.22026779081762, 96.32927290483654 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 235.57152538264552, 123.73551643376177, 123.26767577027167 ))
vP.DatumPointByCoordinate(coords=( 240.12952162828370, 131.06205098312032, 112.96363528589650 ))
vP.DatumPointByCoordinate(coords=( 330.64500374835717, 200.68979068726719, 110.29055547578790 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 331.54035293848949, 0.00000000000000, 153.50529511580868 ))
vP.DatumPointByCoordinate(coords=( 275.61525290158721, -0.00000000000001, 200.00000000000003 ))
vP.DatumPointByCoordinate(coords=( 313.12559895148968, 0.00000000000000, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 345.77081296778084, 191.47027812035185, 92.62811451065159 ))
vP.DatumPointByCoordinate(coords=( 330.64500374835717, 200.68979068726719, 110.29055547578790 ))
vP.DatumPointByCoordinate(coords=( 240.12952162828370, 131.06205098312032, 112.96363528589650 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-27', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-27']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 330.64500374835717, 200.68979068726722, 110.29055547578788 ))
vP.DatumPointByCoordinate(coords=( 313.45468160836162, 290.47610345675946, 103.68062710931746 ))
vP.DatumPointByCoordinate(coords=( 317.32781038342210, 316.98788047801827, 131.31128916216301 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 455.20740236856381, 136.37577864407791, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 456.56561672258630, 135.31978053492008, 193.79289062439952 ))
vP.DatumPointByCoordinate(coords=( 408.16313202242588, 157.22026779081762, 96.32927290483657 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 343.93706948781102, 282.52836735576079, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 498.22794334466323, 275.56819545167383, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 507.53415868941624, 257.90740074291693, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 375.99872733114330, 253.62748252725859, 30.21939208751945 ))
vP.DatumPointByCoordinate(coords=( 374.05914073908855, 272.77318527011772, 26.44048724466231 ))
vP.DatumPointByCoordinate(coords=( 344.14295318630275, 290.02499670502954, 61.70433310639240 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 408.16313202242588, 157.22026779081762, 96.32927290483657 ))
vP.DatumPointByCoordinate(coords=( 425.33289132129954, 184.22186892311987, 67.65062262490517 ))
vP.DatumPointByCoordinate(coords=( 375.99872733114330, 253.62748252725859, 30.21939208751945 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 505.30245217312768, 321.72976141638594, 104.00537980423266 ))
vP.DatumPointByCoordinate(coords=( 520.37129982586202, 292.00693482344155, 105.81942982063870 ))
vP.DatumPointByCoordinate(coords=( 526.09371961841737, 277.92610056537808, 111.00870043584024 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 343.93706948781102, 282.52836735576079, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 317.32781038342210, 316.98788047801827, 131.31128916216301 ))
vP.DatumPointByCoordinate(coords=( 334.69548266367144, 323.59120602254677, 116.05565785355675 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 456.56561672258630, 135.31978053492008, 193.79289062439952 ))
vP.DatumPointByCoordinate(coords=( 464.35638396524706, 137.00624197912191, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 482.04225176219853, 148.58058097965895, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 511.71229281689136, 216.61593336038925, 111.55730423221010 ))
vP.DatumPointByCoordinate(coords=( 526.09371961841737, 277.92610056537808, 111.00870043584024 ))
vP.DatumPointByCoordinate(coords=( 520.37129982586202, 292.00693482344155, 105.81942982063870 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 526.09371961841737, 277.92610056537808, 111.00870043584024 ))
vP.DatumPointByCoordinate(coords=( 511.71229281689136, 216.61593336038925, 111.55730423221010 ))
vP.DatumPointByCoordinate(coords=( 482.04225176219853, 148.58058097965895, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 455.20740236856381, 136.37577864407791, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 464.35638396524706, 137.00624197912191, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 456.56561672258630, 135.31978053492008, 193.79289062439952 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[62], point2=vP.datums[63], point3=vP.datums[64])
vP.DatumAxisByTwoPoint(point1=vP.datums[62], point2=vP.datums[63])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[66],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[66])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 317.32781038342210, 316.98788047801827, 131.31128916216301 ))
vP.DatumPointByCoordinate(coords=( 313.45468160836162, 290.47610345675946, 103.68062710931746 ))
vP.DatumPointByCoordinate(coords=( 344.14295318630275, 290.02499670502954, 61.70433310639240 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[68], point2=vP.datums[69], point3=vP.datums[70])
vP.DatumAxisByTwoPoint(point1=vP.datums[68], point2=vP.datums[69])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[71], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[72],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[71], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[72])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 344.14295318630275, 290.02499670502954, 61.70433310639240 ))
vP.DatumPointByCoordinate(coords=( 374.05914073908855, 272.77318527011772, 26.44048724466231 ))
vP.DatumPointByCoordinate(coords=( 479.54472231556065, 326.44295878293951, 78.07572370688982 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[74], point2=vP.datums[75], point3=vP.datums[76])
vP.DatumAxisByTwoPoint(point1=vP.datums[74], point2=vP.datums[75])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[77], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[78],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[77], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[78])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 483.58126917449755, 331.82857003053601, 85.17239863321890 ))
vP.DatumPointByCoordinate(coords=( 479.54472231556065, 326.44295878293951, 78.07572370688982 ))
vP.DatumPointByCoordinate(coords=( 520.37129982586202, 292.00693482344155, 105.81942982063870 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[80], point2=vP.datums[81], point3=vP.datums[82])
vP.DatumAxisByTwoPoint(point1=vP.datums[80], point2=vP.datums[81])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[83], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[84],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[83], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[84])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-28', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-28']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 88.84892104569019, 600.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 105.35034717345594, 532.70162533977168, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 483.37893169906704, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 0.00000000000000, 600.00000000000000, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 8.48071268742985, 600.00000000000000, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 107.59007792746941, 600.00000000000000, 127.43938346154452 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 0.00000000000000, 483.37893169906704, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 443.72459772869473, 103.48305722416040 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 529.11005682998439, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 107.59007792746941, 600.00000000000000, 127.43938346154452 ))
vP.DatumPointByCoordinate(coords=( 124.02726812509621, 517.61896722936149, 142.00664784938184 ))
vP.DatumPointByCoordinate(coords=( 105.35034717345594, 532.70162533977168, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 0.00000000000000, 529.11005682998439, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 12.45504127128845, 535.90586262821557, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 8.48071268742985, 600.00000000000000, 0.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 12.45504127128845, 535.90586262821557, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 100.46861047126254, 493.34835366821915, 109.77868906264557 ))
vP.DatumPointByCoordinate(coords=( 124.02726812509621, 517.61896722936149, 142.00664784938184 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 105.35034717345594, 532.70162533977168, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 124.02726812509621, 517.61896722936149, 142.00664784938184 ))
vP.DatumPointByCoordinate(coords=( 100.46861047126254, 493.34835366821915, 109.77868906264557 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 12.45504127128845, 535.90586262821557, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 529.11005682998439, 0.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 443.72459772869473, 103.48305722416040 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-29', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-29']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 460.89235511111923, 454.70220526533359, 127.64131573007879 ))
vP.DatumPointByCoordinate(coords=( 478.08911604837607, 472.00995697903187, 93.81311789334107 ))
vP.DatumPointByCoordinate(coords=( 477.60317437700149, 472.64793661557462, 92.86169796608746 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 383.69817113619706, 468.74476006346526, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 451.14416190111052, 470.96598834454858, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 460.89235511111923, 454.70220526533359, 127.64131573007879 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 394.70277909194283, 475.69995751417991, 109.57381131286621 ))
vP.DatumPointByCoordinate(coords=( 344.76429173368979, 600.00000000000000, 79.38023087890363 ))
vP.DatumPointByCoordinate(coords=( 326.00743770537042, 600.00000000000000, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 516.61330489427098, 600.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 451.14416190111052, 470.96598834454858, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 383.69817113619706, 468.74476006346526, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 344.76429173368979, 600.00000000000000, 79.38023087890363 ))
vP.DatumPointByCoordinate(coords=( 422.21916707574098, 600.00000000000000, 53.71292295107669 ))
vP.DatumPointByCoordinate(coords=( 522.43331995855806, 600.00000000000000, 176.60408781943829 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 422.21916707574098, 600.00000000000000, 53.71292295107669 ))
vP.DatumPointByCoordinate(coords=( 344.76429173368979, 600.00000000000000, 79.38023087890363 ))
vP.DatumPointByCoordinate(coords=( 394.70277909194283, 475.69995751417991, 109.57381131286621 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 477.60317437700149, 472.64793661557462, 92.86169796608746 ))
vP.DatumPointByCoordinate(coords=( 478.39556165170535, 472.62087754760279, 93.82727857854802 ))
vP.DatumPointByCoordinate(coords=( 522.43331995855806, 600.00000000000000, 176.60408781943829 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 478.39556165170535, 472.62087754760279, 93.82727857854802 ))
vP.DatumPointByCoordinate(coords=( 478.08911604837607, 472.00995697903187, 93.81311789334107 ))
vP.DatumPointByCoordinate(coords=( 460.89235511111923, 454.70220526533359, 127.64131573007879 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 477.60317437700149, 472.64793661557462, 92.86169796608746 ))
vP.DatumPointByCoordinate(coords=( 478.08911604837607, 472.00995697903187, 93.81311789334107 ))
vP.DatumPointByCoordinate(coords=( 478.39556165170535, 472.62087754760279, 93.82727857854802 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-30', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-30']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 80.76983778879480, 0.00000000000000, 123.51713860349913 ))
vP.DatumPointByCoordinate(coords=( 86.25658236822729, 50.00570229504680, 120.05573045710753 ))
vP.DatumPointByCoordinate(coords=( 68.35294395645050, 93.60002839641287, 113.31451368932736 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 0.00000000000000, 0.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 109.06125681420117, 0.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 108.03927642266684, 0.00000000000000, 167.46031305307622 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 0.00000000000000, 114.11397978152813, 100.30632410737415 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 145.70280161442895, 163.29005256275008 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 147.49769555782228, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 0.00000000000000, 145.70280161442895, 163.29005256275008 ))
vP.DatumPointByCoordinate(coords=( 38.19612060832481, 149.00521675999650, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 147.49769555782228, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 38.19612060832481, 149.00521675999650, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 50.57807381612290, 144.10734241071250, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 109.06125681420117, 0.00000000000000, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 108.03927642266684, 0.00000000000000, 167.46031305307622 ))
vP.DatumPointByCoordinate(coords=( 109.06125681420117, 0.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 50.57807381612290, 144.10734241071250, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 80.76983778879480, 0.00000000000000, 123.51713860349913 ))
vP.DatumPointByCoordinate(coords=( 108.03927642266684, 0.00000000000000, 167.46031305307622 ))
vP.DatumPointByCoordinate(coords=( 86.25658236822729, 50.00570229504680, 120.05573045710753 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 38.19612060832481, 149.00521675999650, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 145.70280161442895, 163.29005256275008 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 114.11397978152813, 100.30632410737415 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-31', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-31']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 68.35294395645052, 93.60002839641287, 113.31451368932730 ))
vP.DatumPointByCoordinate(coords=( 88.01741522207378, 93.73536088691492, 99.59168676123311 ))
vP.DatumPointByCoordinate(coords=( 191.04664134247093, 160.57232800005821, 124.71248107077699 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 109.06125681420119, 0.00000000000001, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 108.03927642266686, 0.00000000000000, 167.46031305307622 ))
vP.DatumPointByCoordinate(coords=( 86.25658236822727, 50.00570229504683, 120.05573045710750 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 152.65015166265385, 193.36029220931465, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 254.42585829480373, 109.20366409577122, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 269.43368493013753, 5.77967824002195, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 269.43368493013753, 5.77967824002195, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 235.57152538264552, 123.73551643376175, 123.26767577027167 ))
vP.DatumPointByCoordinate(coords=( 228.97596426435044, 129.06984482197961, 114.60979350699633 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 207.80968013059709, 98.75890009340091, 103.73082727954662 ))
vP.DatumPointByCoordinate(coords=( 100.97455266117538, 81.93319796544537, 95.78162423956135 ))
vP.DatumPointByCoordinate(coords=( 86.25658236822727, 50.00570229504683, 120.05573045710750 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 109.06125681420119, 0.00000000000001, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 263.47543414705103, 0.00000000000001, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 108.03927642266686, 0.00000000000000, 167.46031305307622 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 254.42585829480373, 109.20366409577122, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 235.57152538264552, 123.73551643376175, 123.26767577027167 ))
vP.DatumPointByCoordinate(coords=( 269.43368493013753, 5.77967824002195, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 191.04664134247093, 160.57232800005821, 124.71248107077699 ))
vP.DatumPointByCoordinate(coords=( 228.97596426435044, 129.06984482197961, 114.60979350699633 ))
vP.DatumPointByCoordinate(coords=( 235.57152538264552, 123.73551643376175, 123.26767577027167 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 191.04664134247093, 160.57232800005821, 124.71248107077699 ))
vP.DatumPointByCoordinate(coords=( 88.01741522207378, 93.73536088691492, 99.59168676123311 ))
vP.DatumPointByCoordinate(coords=( 100.97455266117538, 81.93319796544537, 95.78162423956135 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 88.01741522207378, 93.73536088691492, 99.59168676123311 ))
vP.DatumPointByCoordinate(coords=( 68.35294395645052, 93.60002839641287, 113.31451368932730 ))
vP.DatumPointByCoordinate(coords=( 86.25658236822727, 50.00570229504683, 120.05573045710750 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-32', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-32']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 410.56533356585715, 44.88650450844319, 72.05223967898773 ))
vP.DatumPointByCoordinate(coords=( 399.85695589929867, 32.87033139690689, 67.48083233258002 ))
vP.DatumPointByCoordinate(coords=( 409.71554568342793, 15.32809717679228, 51.01279931900925 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 488.65113801855250, 30.34793826668001, 101.02028944742437 ))
vP.DatumPointByCoordinate(coords=( 479.54259616785185, 128.85060507293707, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 464.35638396524712, 137.00624197912191, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 409.71554568342793, 15.32809717679228, 51.01279931900925 ))
vP.DatumPointByCoordinate(coords=( 407.69305428867733, -0.00000000000000, 50.94815815573406 ))
vP.DatumPointByCoordinate(coords=( 498.44664721887597, -0.00000000000000, 109.84859549549827 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 331.54035293848955, -0.00000000000000, 153.50529511580859 ))
vP.DatumPointByCoordinate(coords=( 313.12559895148968, 0.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 514.46998938463912, 0.00000000000000, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 409.71554568342793, 15.32809717679228, 51.01279931900925 ))
vP.DatumPointByCoordinate(coords=( 399.85695589929867, 32.87033139690689, 67.48083233258002 ))
vP.DatumPointByCoordinate(coords=( 331.54035293848955, -0.00000000000000, 153.50529511580859 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 455.20740236856375, 136.37577864407791, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 313.12559895148968, 0.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 331.54035293848955, -0.00000000000000, 153.50529511580859 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 464.35638396524712, 137.00624197912191, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 455.20740236856375, 136.37577864407791, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 456.56561672258624, 135.31978053492003, 193.79289062439946 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 514.46998938463912, 0.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 313.12559895148968, 0.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 455.20740236856375, 136.37577864407791, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 488.65113801855250, 30.34793826668001, 101.02028944742437 ))
vP.DatumPointByCoordinate(coords=( 498.44664721887597, -0.00000000000000, 109.84859549549827 ))
vP.DatumPointByCoordinate(coords=( 514.46998938463912, 0.00000000000000, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-33', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-33']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 179.84869739046383, 46.18027897541785 ))
vP.DatumPointByCoordinate(coords=( 511.71229281689136, 216.61593336038922, 111.55730423221010 ))
vP.DatumPointByCoordinate(coords=( 482.04225176219848, 148.58058097965895, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 118.96225391083986, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 260.64326061368280, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 282.50893142641553, 100.05659511269569 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 489.74553649436160, 138.47379855252166, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 118.96225391083986, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 125.05484864351186, 91.48686227423764 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 482.04225176219848, 148.58058097965895, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 507.53415868941624, 257.90740074291693, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 260.64326061368280, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 526.09371961841725, 277.92610056537808, 111.00870043584025 ))
vP.DatumPointByCoordinate(coords=( 533.75565801220728, 279.24597321791100, 106.01203622506119 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 282.50893142641553, 100.05659511269569 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 482.04225176219848, 148.58058097965895, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 511.71229281689136, 216.61593336038922, 111.55730423221010 ))
vP.DatumPointByCoordinate(coords=( 526.09371961841725, 277.92610056537808, 111.00870043584025 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 282.50893142641553, 100.05659511269569 ))
vP.DatumPointByCoordinate(coords=( 533.75565801220728, 279.24597321791100, 106.01203622506119 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 206.70544145069479, 50.21116370506773 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 533.75565801220728, 279.24597321791100, 106.01203622506119 ))
vP.DatumPointByCoordinate(coords=( 526.09371961841725, 277.92610056537808, 111.00870043584025 ))
vP.DatumPointByCoordinate(coords=( 511.71229281689136, 216.61593336038922, 111.55730423221010 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-34', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-34']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 0.00000000000000, 217.86831069596252, 103.52888860376889 ))
vP.DatumPointByCoordinate(coords=( 56.76604562883994, 313.99665292665827, 82.54548045069348 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 337.22905436907695, 81.38475309015155 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 0.00000000000000, 362.69025149527937, 108.61523448528696 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 361.27259081055587, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 147.49769555782228, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 56.76604562883994, 313.99665292665827, 82.54548045069348 ))
vP.DatumPointByCoordinate(coords=( 80.05240228059732, 321.04705284937302, 100.75452335445767 ))
vP.DatumPointByCoordinate(coords=( 75.00417322925176, 338.57601143049982, 117.18869801691318 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 0.00000000000000, 362.69025149527937, 108.61523448528696 ))
vP.DatumPointByCoordinate(coords=( 75.00417322925176, 338.57601143049982, 117.18869801691318 ))
vP.DatumPointByCoordinate(coords=( 78.97124126323675, 336.02295286314228, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 78.97124126323675, 336.02295286314228, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 110.36328486810774, 239.00052766720060, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 38.19612060832480, 149.00521675999650, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 110.36328486810774, 239.00052766720060, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 78.97124126323675, 336.02295286314228, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 75.00417322925176, 338.57601143049982, 117.18869801691318 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 56.76604562883994, 313.99665292665827, 82.54548045069348 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 217.86831069596252, 103.52888860376889 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 145.70280161442892, 163.29005256275011 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 38.19612060832480, 149.00521675999650, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 145.70280161442892, 163.29005256275011 ))
vP.DatumPointByCoordinate(coords=( 0.00000000000000, 147.49769555782228, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-35', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-35']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 197.44443520954422, 184.83397929872177, 108.92918786397236 ))
vP.DatumPointByCoordinate(coords=( 198.44642197988122, 184.84006703104578, 108.26323705343299 ))
vP.DatumPointByCoordinate(coords=( 268.20219634913673, 290.78260454581823, 102.59060420064331 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 151.70629670214404, 211.15288734500169, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 152.65015166265385, 193.36029220931468, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 191.04664134247093, 160.57232800005823, 124.71248107077697 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 261.46326718860229, 297.99738250861373, 109.86738632031442 ))
vP.DatumPointByCoordinate(coords=( 299.84224536276128, 336.49197155942562, 151.00578042774001 ))
vP.DatumPointByCoordinate(coords=( 296.01697416666423, 338.59451405226366, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 343.93706948781102, 282.52836735576079, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 317.32781038342210, 316.98788047801827, 131.31128916216304 ))
vP.DatumPointByCoordinate(coords=( 313.45468160836162, 290.47610345675952, 103.68062710931744 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 254.42585829480376, 109.20366409577126, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 152.65015166265385, 193.36029220931468, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 151.70629670214404, 211.15288734500169, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 330.64500374835717, 200.68979068726719, 110.29055547578790 ))
vP.DatumPointByCoordinate(coords=( 240.12952162828370, 131.06205098312029, 112.96363528589650 ))
vP.DatumPointByCoordinate(coords=( 235.57152538264552, 123.73551643376177, 123.26767577027164 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 261.46326718860229, 297.99738250861373, 109.86738632031442 ))
vP.DatumPointByCoordinate(coords=( 268.20219634913673, 290.78260454581823, 102.59060420064331 ))
vP.DatumPointByCoordinate(coords=( 313.45468160836162, 290.47610345675952, 103.68062710931744 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 317.32781038342210, 316.98788047801827, 131.31128916216304 ))
vP.DatumPointByCoordinate(coords=( 343.93706948781102, 282.52836735576079, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 296.01697416666423, 338.59451405226366, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 268.20219634913673, 290.78260454581823, 102.59060420064331 ))
vP.DatumPointByCoordinate(coords=( 198.44642197988122, 184.84006703104578, 108.26323705343299 ))
vP.DatumPointByCoordinate(coords=( 230.74582213651124, 130.44338744813592, 112.78474356679109 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 235.57152538264552, 123.73551643376177, 123.26767577027164 ))
vP.DatumPointByCoordinate(coords=( 228.97596426435047, 129.06984482197964, 114.60979350699630 ))
vP.DatumPointByCoordinate(coords=( 191.04664134247093, 160.57232800005823, 124.71248107077697 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 240.12952162828370, 131.06205098312029, 112.96363528589650 ))
vP.DatumPointByCoordinate(coords=( 230.74582213651124, 130.44338744813592, 112.78474356679109 ))
vP.DatumPointByCoordinate(coords=( 228.97596426435047, 129.06984482197964, 114.60979350699630 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[62], point2=vP.datums[63], point3=vP.datums[64])
vP.DatumAxisByTwoPoint(point1=vP.datums[62], point2=vP.datums[63])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[66],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[66])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 228.97596426435047, 129.06984482197964, 114.60979350699630 ))
vP.DatumPointByCoordinate(coords=( 230.74582213651124, 130.44338744813592, 112.78474356679109 ))
vP.DatumPointByCoordinate(coords=( 198.44642197988122, 184.84006703104578, 108.26323705343299 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[68], point2=vP.datums[69], point3=vP.datums[70])
vP.DatumAxisByTwoPoint(point1=vP.datums[68], point2=vP.datums[69])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[71], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[72],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[71], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[72])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-36', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-36']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 151.70629670214402, 211.15288734500177, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 181.25681599582643, 230.22747341866688, 137.23012227410368 ))
vP.DatumPointByCoordinate(coords=( 82.08525698919257, 320.70846345997990, 99.09475161355840 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 78.97124126323678, 336.02295286314228, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 147.17361507331350, 403.23640510582129, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 292.67010469526809, 367.24268555303217, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 80.05240228059735, 321.04705284937302, 100.75452335445769 ))
vP.DatumPointByCoordinate(coords=( 75.00417322925176, 338.57601143049982, 117.18869801691318 ))
vP.DatumPointByCoordinate(coords=( 78.97124126323678, 336.02295286314228, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 299.84224536276128, 336.49197155942568, 151.00578042774001 ))
vP.DatumPointByCoordinate(coords=( 298.31748454863856, 347.50408870414822, 154.26671940759977 ))
vP.DatumPointByCoordinate(coords=( 205.68230887979112, 344.70473635569005, 90.14580941715013 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 181.25681599582643, 230.22747341866688, 137.23012227410368 ))
vP.DatumPointByCoordinate(coords=( 151.70629670214402, 211.15288734500177, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 296.01697416666423, 338.59451405226372, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 205.68230887979112, 344.70473635569005, 90.14580941715013 ))
vP.DatumPointByCoordinate(coords=( 143.00718007398805, 357.83904465728625, 84.23486340183223 ))
vP.DatumPointByCoordinate(coords=( 82.08525698919257, 320.70846345997990, 99.09475161355840 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 80.05240228059735, 321.04705284937302, 100.75452335445769 ))
vP.DatumPointByCoordinate(coords=( 82.08525698919257, 320.70846345997990, 99.09475161355840 ))
vP.DatumPointByCoordinate(coords=( 143.00718007398805, 357.83904465728625, 84.23486340183223 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 115.49202185219657, 378.37667619719787, 118.47159797898860 ))
vP.DatumPointByCoordinate(coords=( 147.17361507331350, 403.23640510582129, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 78.97124126323678, 336.02295286314228, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 296.01697416666423, 338.59451405226372, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 292.67010469526809, 367.24268555303217, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 298.31748454863856, 347.50408870414822, 154.26671940759977 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 115.49202185219657, 378.37667619719787, 118.47159797898860 ))
vP.DatumPointByCoordinate(coords=( 143.00718007398805, 357.83904465728625, 84.23486340183223 ))
vP.DatumPointByCoordinate(coords=( 205.68230887979112, 344.70473635569005, 90.14580941715013 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-37', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-37']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 299.84224536276128, 336.49197155942568, 151.00578042774001 ))
vP.DatumPointByCoordinate(coords=( 298.31748454863850, 347.50408870414827, 154.26671940759977 ))
vP.DatumPointByCoordinate(coords=( 292.67010469526804, 367.24268555303223, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 343.93706948781107, 282.52836735576079, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 317.32781038342216, 316.98788047801827, 131.31128916216301 ))
vP.DatumPointByCoordinate(coords=( 299.84224536276128, 336.49197155942568, 151.00578042774001 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 292.67010469526804, 367.24268555303223, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 309.63965132805612, 415.79238184552344, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 383.69817113619706, 468.74476006346532, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 398.33623628203298, 455.94407138770987, 142.04799756705839 ))
vP.DatumPointByCoordinate(coords=( 319.92169978010168, 400.11885451946620, 142.65012036099051 ))
vP.DatumPointByCoordinate(coords=( 334.69548266367144, 323.59120602254671, 116.05565785355680 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 451.14416190111052, 470.96598834454858, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 383.69817113619706, 468.74476006346532, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 398.33623628203298, 455.94407138770987, 142.04799756705839 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 476.53135793754427, 438.34798119041784, 119.15881057346272 ))
vP.DatumPointByCoordinate(coords=( 515.13737771530646, 403.76823930080224, 162.21941396201984 ))
vP.DatumPointByCoordinate(coords=( 515.12571476816447, 407.19890454611397, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 383.69817113619706, 468.74476006346532, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 309.63965132805612, 415.79238184552344, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 319.87917071103766, 400.10349855540858, 142.68761249733879 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 498.22794334466317, 275.56819545167383, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 505.30245217312762, 321.72976141638605, 104.00537980423262 ))
vP.DatumPointByCoordinate(coords=( 483.58126917449749, 331.82857003053607, 85.17239863321890 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 515.12571476816447, 407.19890454611397, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 515.13737771530646, 403.76823930080224, 162.21941396201984 ))
vP.DatumPointByCoordinate(coords=( 507.83347514948247, 341.23686958219150, 101.76181632996753 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 298.31748454863850, 347.50408870414827, 154.26671940759977 ))
vP.DatumPointByCoordinate(coords=( 299.84224536276128, 336.49197155942568, 151.00578042774001 ))
vP.DatumPointByCoordinate(coords=( 317.32781038342216, 316.98788047801827, 131.31128916216301 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 309.63965132805612, 415.79238184552344, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 292.67010469526804, 367.24268555303223, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 298.31748454863850, 347.50408870414827, 154.26671940759977 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[62], point2=vP.datums[63], point3=vP.datums[64])
vP.DatumAxisByTwoPoint(point1=vP.datums[62], point2=vP.datums[63])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[66],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[65], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[66])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 505.30245217312762, 321.72976141638605, 104.00537980423262 ))
vP.DatumPointByCoordinate(coords=( 507.83347514948247, 341.23686958219150, 101.76181632996753 ))
vP.DatumPointByCoordinate(coords=( 495.38352751213722, 354.38576920391250, 89.38797911930030 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[68], point2=vP.datums[69], point3=vP.datums[70])
vP.DatumAxisByTwoPoint(point1=vP.datums[68], point2=vP.datums[69])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[71], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[72],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[71], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[72])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 476.53135793754427, 438.34798119041784, 119.15881057346272 ))
vP.DatumPointByCoordinate(coords=( 495.38352751213722, 354.38576920391250, 89.38797911930030 ))
vP.DatumPointByCoordinate(coords=( 507.83347514948247, 341.23686958219150, 101.76181632996753 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[74], point2=vP.datums[75], point3=vP.datums[76])
vP.DatumAxisByTwoPoint(point1=vP.datums[74], point2=vP.datums[75])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[77], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[78],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[77], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[78])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-38', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-38']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 507.83347514948252, 341.23686958219150, 101.76181632996754 ))
vP.DatumPointByCoordinate(coords=( 505.30245217312768, 321.72976141638600, 104.00537980423265 ))
vP.DatumPointByCoordinate(coords=( 520.37129982586191, 292.00693482344161, 105.81942982063870 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 414.78495000213144, 182.17286023220120 ))
vP.DatumPointByCoordinate(coords=( 515.13737771530646, 403.76823930080218, 162.21941396201987 ))
vP.DatumPointByCoordinate(coords=( 507.83347514948252, 341.23686958219150, 101.76181632996754 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 282.50893142641547, 100.05659511269567 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 260.64326061368280, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 416.40433990167514, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 282.50893142641547, 100.05659511269567 ))
vP.DatumPointByCoordinate(coords=( 533.75565801220739, 279.24597321791094, 106.01203622506115 ))
vP.DatumPointByCoordinate(coords=( 526.09371961841737, 277.92610056537808, 111.00870043584028 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 507.53415868941624, 257.90740074291693, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 498.22794334466323, 275.56819545167383, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 515.12571476816447, 407.19890454611397, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 515.12571476816447, 407.19890454611397, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 498.22794334466323, 275.56819545167383, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 505.30245217312768, 321.72976141638600, 104.00537980423265 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 414.78495000213144, 182.17286023220120 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 416.40433990167514, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 515.12571476816447, 407.19890454611397, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 507.53415868941624, 257.90740074291693, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 526.09371961841737, 277.92610056537808, 111.00870043584028 ))
vP.DatumPointByCoordinate(coords=( 520.37129982586191, 292.00693482344161, 105.81942982063870 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 533.75565801220739, 279.24597321791094, 106.01203622506115 ))
vP.DatumPointByCoordinate(coords=( 520.37129982586191, 292.00693482344161, 105.81942982063870 ))
vP.DatumPointByCoordinate(coords=( 526.09371961841737, 277.92610056537808, 111.00870043584028 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-39', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-39']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( -0.00000000000001, 443.72459772869473, 103.48305722416040 ))
vP.DatumPointByCoordinate(coords=( 100.46861047126256, 493.34835366821915, 109.77868906264557 ))
vP.DatumPointByCoordinate(coords=( 124.02726812509621, 517.61896722936149, 142.00664784938181 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 0.00000000000000, 361.27259081055587, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( -0.00000000000001, 362.69025149527943, 108.61523448528696 ))
vP.DatumPointByCoordinate(coords=( -0.00000000000001, 443.72459772869473, 103.48305722416040 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 105.35034717345596, 532.70162533977168, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 147.14990159986743, 495.48831914605364, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 147.17361507331350, 403.23640510582129, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 75.00417322925179, 338.57601143049982, 117.18869801691319 ))
vP.DatumPointByCoordinate(coords=( 115.49202185219659, 378.37667619719781, 118.47159797898861 ))
vP.DatumPointByCoordinate(coords=( 112.69217116366035, 486.83193422543400, 111.33973178910402 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 0.00000000000000, 361.27259081055587, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 78.97124126323678, 336.02295286314228, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 75.00417322925179, 338.57601143049982, 117.18869801691319 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 78.97124126323678, 336.02295286314228, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 147.17361507331350, 403.23640510582129, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 115.49202185219659, 378.37667619719781, 118.47159797898861 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 147.17361507331350, 403.23640510582129, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 147.14990159986743, 495.48831914605364, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 124.57156958297776, 517.13659708255614, 141.92367431021484 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 124.02726812509621, 517.61896722936149, 142.00664784938181 ))
vP.DatumPointByCoordinate(coords=( 124.57156958297776, 517.13659708255614, 141.92367431021484 ))
vP.DatumPointByCoordinate(coords=( 147.14990159986743, 495.48831914605364, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 124.02726812509621, 517.61896722936149, 142.00664784938181 ))
vP.DatumPointByCoordinate(coords=( 100.46861047126256, 493.34835366821915, 109.77868906264557 ))
vP.DatumPointByCoordinate(coords=( 112.69217116366035, 486.83193422543400, 111.33973178910402 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-40', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-40']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 515.13737771530646, 403.76823930080224, 162.21941396201990 ))
vP.DatumPointByCoordinate(coords=( 476.53135793754427, 438.34798119041784, 119.15881057346274 ))
vP.DatumPointByCoordinate(coords=( 460.89235511111929, 454.70220526533359, 127.64131573007879 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 416.40433990167514, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 414.78495000213150, 182.17286023220123 ))
vP.DatumPointByCoordinate(coords=( 515.13737771530646, 403.76823930080224, 162.21941396201990 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 451.14416190111058, 470.96598834454852, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 516.61330489427098, 600.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 600.00000000000000, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 514.68032124523006, 96.42782182332543 ))
vP.DatumPointByCoordinate(coords=( 479.66231459694319, 469.16090031549140, 93.79563957373411 ))
vP.DatumPointByCoordinate(coords=( 476.53135793754427, 438.34798119041784, 119.15881057346274 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 416.40433990167514, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 600.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 600.00000000000000, 138.44778631671718 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 522.43331995855806, 600.00000000000000, 176.60408781943829 ))
vP.DatumPointByCoordinate(coords=( 478.39556165170541, 472.62087754760284, 93.82727857854806 ))
vP.DatumPointByCoordinate(coords=( 600.00000000000000, 549.38841701614717, 96.95073331518765 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 600.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 516.61330489427098, 600.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 522.43331995855806, 600.00000000000000, 176.60408781943829 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 600.00000000000000, 549.38841701614717, 96.95073331518765 ))
vP.DatumPointByCoordinate(coords=( 478.39556165170541, 472.62087754760284, 93.82727857854806 ))
vP.DatumPointByCoordinate(coords=( 478.08911604837607, 472.00995697903181, 93.81311789334109 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 460.89235511111929, 454.70220526533359, 127.64131573007879 ))
vP.DatumPointByCoordinate(coords=( 478.08911604837607, 472.00995697903181, 93.81311789334109 ))
vP.DatumPointByCoordinate(coords=( 478.39556165170541, 472.62087754760284, 93.82727857854806 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[51], point3=vP.datums[52])
vP.DatumAxisByTwoPoint(point1=vP.datums[50], point2=vP.datums[51])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[54],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[53], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[54])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 460.89235511111929, 454.70220526533359, 127.64131573007879 ))
vP.DatumPointByCoordinate(coords=( 476.53135793754427, 438.34798119041784, 119.15881057346274 ))
vP.DatumPointByCoordinate(coords=( 479.66231459694319, 469.16090031549140, 93.79563957373411 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[57], point3=vP.datums[58])
vP.DatumAxisByTwoPoint(point1=vP.datums[56], point2=vP.datums[57])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[60],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[59], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[60])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=(6000)+200)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0,0), point2=(600,600))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-41', type= DEFORMABLE_BODY)
vP=mdb.models['Model-1'].parts['Part-41']
vP.BaseSolidExtrude(depth=200, sketch= mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 220.29249018794016, 569.51253041112466, 92.78888848831858 ))
vP.DatumPointByCoordinate(coords=( 209.14217266824201, 600.00000000000000, 89.30089397152959 ))
vP.DatumPointByCoordinate(coords=( 107.59007792746939, 600.00000000000000, 127.43938346154449 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[3], point3=vP.datums[4])
vP.DatumAxisByTwoPoint(point1=vP.datums[2], point2=vP.datums[3])
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

vP.DatumPointByCoordinate(coords=( 240.08941089378882, 492.12437914915563, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 310.24295649025157, 600.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 244.35615162205747, 600.00000000000000, 99.26689102516153 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[9], point3=vP.datums[10])
vP.DatumAxisByTwoPoint(point1=vP.datums[8], point2=vP.datums[9])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[12],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[11], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[12])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 124.57156958297780, 517.13659708255614, 141.92367431021484 ))
vP.DatumPointByCoordinate(coords=( 147.14990159986746, 495.48831914605364, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 240.08941089378882, 492.12437914915563, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[15], point3=vP.datums[16])
vP.DatumAxisByTwoPoint(point1=vP.datums[14], point2=vP.datums[15])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[18],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[17], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[18])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 147.14990159986746, 495.48831914605364, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 105.35034717345597, 532.70162533977168, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 88.84892104569022, 600.00000000000000, 200.00000000000000 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[21], point3=vP.datums[22])
vP.DatumAxisByTwoPoint(point1=vP.datums[20], point2=vP.datums[21])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[24],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[23], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[24])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 209.14217266824201, 600.00000000000000, 89.30089397152959 ))
vP.DatumPointByCoordinate(coords=( 220.29249018794016, 569.51253041112466, 92.78888848831858 ))
vP.DatumPointByCoordinate(coords=( 244.35615162205747, 600.00000000000000, 99.26689102516153 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[27], point3=vP.datums[28])
vP.DatumAxisByTwoPoint(point1=vP.datums[26], point2=vP.datums[27])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[30],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[29], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[30])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 310.24295649025157, 600.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 88.84892104569022, 600.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 107.59007792746939, 600.00000000000000, 127.43938346154449 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[33], point3=vP.datums[34])
vP.DatumAxisByTwoPoint(point1=vP.datums[32], point2=vP.datums[33])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[36],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[35], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[36])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 88.84892104569022, 600.00000000000000, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 105.35034717345597, 532.70162533977168, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 124.02726812509623, 517.61896722936149, 142.00664784938181 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[39], point3=vP.datums[40])
vP.DatumAxisByTwoPoint(point1=vP.datums[38], point2=vP.datums[39])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[42],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[41], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[42])
del mdb.models['Model-1'].sketches['__profile__']

vP.DatumPointByCoordinate(coords=( 147.14990159986746, 495.48831914605364, 200.00000000000000 ))
vP.DatumPointByCoordinate(coords=( 124.57156958297780, 517.13659708255614, 141.92367431021484 ))
vP.DatumPointByCoordinate(coords=( 124.02726812509623, 517.61896722936149, 142.00664784938181 ))
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[45], point3=vP.datums[46])
vP.DatumAxisByTwoPoint(point1=vP.datums[44], point2=vP.datums[45])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.12, name='__profile__',sheetSize=5.02,
    transform=vP.MakeSketchTransform(sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,
    sketchUpEdge=vP.datums[48],sketchOrientation=RIGHT, origin=(0,0,0)))
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(sheetSize=6000)
vP.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-6000, -6000), point2=(6000, 6000))

vP.CutExtrude(depth=6000, flipExtrudeDirection=OFF,
      sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
      sketchPlane=vP.datums[47], sketchPlaneSide=SIDE1,sketchUpEdge=vP.datums[48])
del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-1-1', 
    part=mdb.models['Model-1'].parts['Part-1'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-2-1', 
    part=mdb.models['Model-1'].parts['Part-2'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-3-1', 
    part=mdb.models['Model-1'].parts['Part-3'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-4-1', 
    part=mdb.models['Model-1'].parts['Part-4'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-5-1', 
    part=mdb.models['Model-1'].parts['Part-5'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-6-1', 
    part=mdb.models['Model-1'].parts['Part-6'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-7-1', 
    part=mdb.models['Model-1'].parts['Part-7'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-8-1', 
    part=mdb.models['Model-1'].parts['Part-8'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-9-1', 
    part=mdb.models['Model-1'].parts['Part-9'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-10-1', 
    part=mdb.models['Model-1'].parts['Part-10'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-11-1', 
    part=mdb.models['Model-1'].parts['Part-11'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-12-1', 
    part=mdb.models['Model-1'].parts['Part-12'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-13-1', 
    part=mdb.models['Model-1'].parts['Part-13'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-14-1', 
    part=mdb.models['Model-1'].parts['Part-14'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-15-1', 
    part=mdb.models['Model-1'].parts['Part-15'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-16-1', 
    part=mdb.models['Model-1'].parts['Part-16'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-17-1', 
    part=mdb.models['Model-1'].parts['Part-17'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-18-1', 
    part=mdb.models['Model-1'].parts['Part-18'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-19-1', 
    part=mdb.models['Model-1'].parts['Part-19'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-20-1', 
    part=mdb.models['Model-1'].parts['Part-20'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-21-1', 
    part=mdb.models['Model-1'].parts['Part-21'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-22-1', 
    part=mdb.models['Model-1'].parts['Part-22'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-23-1', 
    part=mdb.models['Model-1'].parts['Part-23'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-24-1', 
    part=mdb.models['Model-1'].parts['Part-24'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-25-1', 
    part=mdb.models['Model-1'].parts['Part-25'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-26-1', 
    part=mdb.models['Model-1'].parts['Part-26'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-27-1', 
    part=mdb.models['Model-1'].parts['Part-27'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-28-1', 
    part=mdb.models['Model-1'].parts['Part-28'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-29-1', 
    part=mdb.models['Model-1'].parts['Part-29'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-30-1', 
    part=mdb.models['Model-1'].parts['Part-30'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-31-1', 
    part=mdb.models['Model-1'].parts['Part-31'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-32-1', 
    part=mdb.models['Model-1'].parts['Part-32'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-33-1', 
    part=mdb.models['Model-1'].parts['Part-33'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-34-1', 
    part=mdb.models['Model-1'].parts['Part-34'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-35-1', 
    part=mdb.models['Model-1'].parts['Part-35'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-36-1', 
    part=mdb.models['Model-1'].parts['Part-36'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-37-1', 
    part=mdb.models['Model-1'].parts['Part-37'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-38-1', 
    part=mdb.models['Model-1'].parts['Part-38'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-39-1', 
    part=mdb.models['Model-1'].parts['Part-39'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-40-1', 
    part=mdb.models['Model-1'].parts['Part-40'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-41-1', 
    part=mdb.models['Model-1'].parts['Part-41'])
mdb.models['Model-1'].rootAssembly.InstanceFromBooleanMerge(domain=GEOMETRY, instances=(
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-3-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-4-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-5-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-6-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-7-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-8-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-9-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-10-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-11-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-12-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-13-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-14-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-15-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-16-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-17-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-18-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-19-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-20-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-21-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-22-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-23-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-24-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-25-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-26-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-27-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-28-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-29-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-30-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-31-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-32-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-33-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-34-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-35-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-36-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-37-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-38-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-39-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-40-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-41-1']), 
    keepIntersections=ON, name='Part-total', originalInstances=DELETE)
mdb.models['Model-1'].Material(name='M5-554deg')
mdb.models['Model-1'].materials['M5-554deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M5-554deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M5-554deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.758,
		0.471, 0.450, 0.0, 0.0, 0.0, 1.0, 0.0, -0.230,-0.840,0.492,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M5-554deg', name='Section-M5-554', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((538.77612304687500, 1.21550428867340, 21.81731986999512),),)), sectionName='Section-M5-554')

mdb.models['Model-1'].Material(name='M0-512deg')
mdb.models['Model-1'].materials['M0-512deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M0-512deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M0-512deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.910,
		-0.402, -0.102, 0.0, 0.0, 0.0, 1.0, 0.0, 0.399,0.782,0.480,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M0-512deg', name='Section-M0-512', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((156.64411926269531, 136.09474182128906, 22.97905731201172),),)), sectionName='Section-M0-512')

mdb.models['Model-1'].Material(name='M6-124deg')
mdb.models['Model-1'].materials['M6-124deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M6-124deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M6-124deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.725,
		0.687, -0.041, 0.0, 0.0, 0.0, 1.0, 0.0, -0.675,-0.722,-0.153,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M6-124deg', name='Section-M6-124', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((370.09460449218750, 136.41954040527344, 12.60424137115479),),)), sectionName='Section-M6-124')

mdb.models['Model-1'].Material(name='M6-095deg')
mdb.models['Model-1'].materials['M6-095deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M6-095deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M6-095deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.609,
		-0.793, -0.010, 0.0, 0.0, 0.0, 1.0, 0.0, 0.780,0.597,0.187,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M6-095deg', name='Section-M6-095', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((2.76776719093323, 238.15280151367187, 12.26280021667481),),)), sectionName='Section-M6-095')

mdb.models['Model-1'].Material(name='M1-629deg')
mdb.models['Model-1'].materials['M1-629deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M1-629deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M1-629deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.472,
		-0.259, 0.843, 0.0, 0.0, 0.0, 1.0, 0.0, 0.683,-0.497,-0.535,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M1-629deg', name='Section-M1-629', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((268.60006713867187, 203.14697265625000, 29.90346527099609),),)), sectionName='Section-M1-629')

mdb.models['Model-1'].Material(name='M1-736deg')
mdb.models['Model-1'].materials['M1-736deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M1-736deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M1-736deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.645,
		0.055, -0.762, 0.0, 0.0, 0.0, 1.0, 0.0, -0.713,-0.316,-0.626,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M1-736deg', name='Section-M1-736', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((489.51593017578125, 222.57882690429687, 14.96555519104004),),)), sectionName='Section-M1-736')

mdb.models['Model-1'].Material(name='M3-309deg')
mdb.models['Model-1'].materials['M3-309deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M3-309deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M3-309deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.269,
		-0.950, -0.159, 0.0, 0.0, 0.0, 1.0, 0.0, -0.959,0.280,-0.048,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M3-309deg', name='Section-M3-309', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((269.80538940429687, 377.57089233398438, 28.91017723083496),),)), sectionName='Section-M3-309')

mdb.models['Model-1'].Material(name='M2-466deg')
mdb.models['Model-1'].materials['M2-466deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M2-466deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M2-466deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.898,
		-0.432, -0.082, 0.0, 0.0, 0.0, 1.0, 0.0, -0.385,0.683,0.620,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M2-466deg', name='Section-M2-466', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((572.15161132812500, 309.03570556640625, 0.67399317026138),),)), sectionName='Section-M2-466')

mdb.models['Model-1'].Material(name='M5-042deg')
mdb.models['Model-1'].materials['M5-042deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M5-042deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M5-042deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.900,
		-0.086, -0.428, 0.0, 0.0, 0.0, 1.0, 0.0, 0.432,-0.319,-0.844,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M5-042deg', name='Section-M5-042', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((573.18591308593750, 499.38137817382812, 11.52659797668457),),)), sectionName='Section-M5-042')

mdb.models['Model-1'].Material(name='M0-855deg')
mdb.models['Model-1'].materials['M0-855deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M0-855deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M0-855deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.018,
		0.914, -0.405, 0.0, 0.0, 0.0, 1.0, 0.0, -0.712,-0.296,-0.636,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M0-855deg', name='Section-M0-855', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((255.44860839843750, 584.79809570312500, 3.04063129425049),),)), sectionName='Section-M0-855')

mdb.models['Model-1'].Material(name='M1-557deg')
mdb.models['Model-1'].materials['M1-557deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M1-557deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M1-557deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.021,
		0.070, 0.997, 0.0, 0.0, 0.0, 1.0, 0.0, 0.106,-0.992,0.071,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M1-557deg', name='Section-M1-557', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((376.37341308593750, 528.50598144531250, 18.97734451293945),),)), sectionName='Section-M1-557')

mdb.models['Model-1'].Material(name='M4-710deg')
mdb.models['Model-1'].materials['M4-710deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M4-710deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M4-710deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.672,
		-0.036, -0.740, 0.0, 0.0, 0.0, 1.0, 0.0, 0.739,-0.042,0.673,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M4-710deg', name='Section-M4-710', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((47.42376327514648, 11.97438335418701, 36.02491378784180),),)), sectionName='Section-M4-710')

mdb.models['Model-1'].Material(name='M2-608deg')
mdb.models['Model-1'].materials['M2-608deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M2-608deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M2-608deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.896,
		-0.181, -0.404, 0.0, 0.0, 0.0, 1.0, 0.0, -0.320,-0.896,-0.308,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M2-608deg', name='Section-M2-608', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((278.98187255859375, 35.30915451049805, 65.76535797119141),),)), sectionName='Section-M2-608')

mdb.models['Model-1'].Material(name='M1-032deg')
mdb.models['Model-1'].materials['M1-032deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M1-032deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M1-032deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.624,
		0.072, 0.778, 0.0, 0.0, 0.0, 1.0, 0.0, 0.352,-0.863,0.363,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M1-032deg', name='Section-M1-032', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((171.64984130859375, 267.88458251953125, 46.76134872436523),),)), sectionName='Section-M1-032')

mdb.models['Model-1'].Material(name='M5-368deg')
mdb.models['Model-1'].materials['M5-368deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M5-368deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M5-368deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.718,
		0.467, 0.516, 0.0, 0.0, 0.0, 1.0, 0.0, -0.692,-0.400,-0.602,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M5-368deg', name='Section-M5-368', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((389.47628784179687, 397.78250122070312, 37.22938919067383),),)), sectionName='Section-M5-368')

mdb.models['Model-1'].Material(name='M3-380deg')
mdb.models['Model-1'].materials['M3-380deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M3-380deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M3-380deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.848,
		-0.518, -0.113, 0.0, 0.0, 0.0, 1.0, 0.0, -0.489,0.847,-0.207,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M3-380deg', name='Section-M3-380', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((76.83747100830078, 420.48892211914062, 39.36801528930664),),)), sectionName='Section-M3-380')

mdb.models['Model-1'].Material(name='M6-052deg')
mdb.models['Model-1'].materials['M6-052deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M6-052deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M6-052deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.968,
		-0.107, -0.228, 0.0, 0.0, 0.0, 1.0, 0.0, 0.103,0.994,-0.028,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M6-052deg', name='Section-M6-052', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((145.60778808593750, 548.13507080078125, 33.71647262573242),),)), sectionName='Section-M6-052')

mdb.models['Model-1'].Material(name='M5-953deg')
mdb.models['Model-1'].materials['M5-953deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M5-953deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M5-953deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.331,
		0.918, -0.219, 0.0, 0.0, 0.0, 1.0, 0.0, -0.930,0.279,-0.238,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M5-953deg', name='Section-M5-953', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((513.14648437500000, 592.37677001953125, 63.40299987792969),),)), sectionName='Section-M5-953')

mdb.models['Model-1'].Material(name='M6-021deg')
mdb.models['Model-1'].materials['M6-021deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M6-021deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M6-021deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.968,
		0.149, 0.202, 0.0, 0.0, 0.0, 1.0, 0.0, -0.117,0.980,-0.163,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M6-021deg', name='Section-M6-021', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((171.97314453125000, 2.69061613082886, 99.33132934570313),),)), sectionName='Section-M6-021')

mdb.models['Model-1'].Material(name='M2-630deg')
mdb.models['Model-1'].materials['M2-630deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M2-630deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M2-630deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.871,
		0.288, -0.398, 0.0, 0.0, 0.0, 1.0, 0.0, 0.416,-0.864,0.286,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M2-630deg', name='Section-M2-630', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((494.66204833984375, 125.24060058593750, 76.65689849853516),),)), sectionName='Section-M2-630')

mdb.models['Model-1'].Material(name='M0-542deg')
mdb.models['Model-1'].materials['M0-542deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M0-542deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M0-542deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.515,
		0.773, -0.370, 0.0, 0.0, 0.0, 1.0, 0.0, -0.688,0.630,0.359,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M0-542deg', name='Section-M0-542', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((599.73321533203125, 424.34619140625000, 95.45594787597656),),)), sectionName='Section-M0-542')

mdb.models['Model-1'].Material(name='M4-264deg')
mdb.models['Model-1'].materials['M4-264deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M4-264deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M4-264deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.480,
		-0.050, 0.876, 0.0, 0.0, 0.0, 1.0, 0.0, 0.288,0.934,0.212,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M4-264deg', name='Section-M4-264', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((92.61746215820313, 204.83300781250000, 102.68830871582031),),)), sectionName='Section-M4-264')

mdb.models['Model-1'].Material(name='M0-346deg')
mdb.models['Model-1'].materials['M0-346deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M0-346deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M0-346deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.119,
		0.980, -0.157, 0.0, 0.0, 0.0, 1.0, 0.0, -0.951,0.067,-0.301,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M0-346deg', name='Section-M0-346', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((197.60586547851562, 429.62854003906250, 130.94378662109375),),)), sectionName='Section-M0-346')

mdb.models['Model-1'].Material(name='M6-071deg')
mdb.models['Model-1'].materials['M6-071deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M6-071deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M6-071deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.673,
		0.720, 0.169, 0.0, 0.0, 0.0, 1.0, 0.0, -0.711,-0.693,0.124,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M6-071deg', name='Section-M6-071', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((300.63543701171875, 523.50439453125000, 123.65332031250000),),)), sectionName='Section-M6-071')

mdb.models['Model-1'].Material(name='M3-299deg')
mdb.models['Model-1'].materials['M3-299deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M3-299deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M3-299deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.829,
		-0.552, 0.089, 0.0, 0.0, 0.0, 1.0, 0.0, -0.559,0.819,-0.129,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M3-299deg', name='Section-M3-299', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((565.90850830078125, 49.70191574096680, 158.38792419433594),),)), sectionName='Section-M3-299')

mdb.models['Model-1'].Material(name='M2-614deg')
mdb.models['Model-1'].materials['M2-614deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M2-614deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M2-614deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.986,
		0.120, 0.118, 0.0, 0.0, 0.0, 1.0, 0.0, 0.163,0.857,0.489,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M2-614deg', name='Section-M2-614', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((346.00509643554687, 106.99283599853516, 146.38272094726562),),)), sectionName='Section-M2-614')

mdb.models['Model-1'].Material(name='M0-939deg')
mdb.models['Model-1'].materials['M0-939deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M0-939deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M0-939deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.177,
		0.980, -0.094, 0.0, 0.0, 0.0, 1.0, 0.0, -0.570,0.180,0.802,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M0-939deg', name='Section-M0-939', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((419.47723388671875, 240.12480163574219, 139.81022644042969),),)), sectionName='Section-M0-939')

mdb.models['Model-1'].Material(name='M5-853deg')
mdb.models['Model-1'].materials['M5-853deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M5-853deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M5-853deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.448,
		0.797, 0.406, 0.0, 0.0, 0.0, 1.0, 0.0, -0.888,-0.449,-0.098,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M5-853deg', name='Section-M5-853', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((11.72012519836426, 539.83300781250000, 137.84065246582031),),)), sectionName='Section-M5-853')

mdb.models['Model-1'].Material(name='M1-445deg')
mdb.models['Model-1'].materials['M1-445deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M1-445deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M1-445deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.662,
		-0.417, 0.623, 0.0, 0.0, 0.0, 1.0, 0.0, -0.435,-0.463,-0.772,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M1-445deg', name='Section-M1-445', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((417.06094360351562, 574.67700195312500, 141.75794982910156),),)), sectionName='Section-M1-445')

mdb.models['Model-1'].Material(name='M4-527deg')
mdb.models['Model-1'].materials['M4-527deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M4-527deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M4-527deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.832,
		0.286, 0.476, 0.0, 0.0, 0.0, 1.0, 0.0, -0.372,0.349,-0.860,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M4-527deg', name='Section-M4-527', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((21.73064994812012, 25.62931060791016, 192.56602478027344),),)), sectionName='Section-M4-527')

mdb.models['Model-1'].Material(name='M4-888deg')
mdb.models['Model-1'].materials['M4-888deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M4-888deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M4-888deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.282,
		-0.890, -0.359, 0.0, 0.0, 0.0, 1.0, 0.0, 0.072,0.392,-0.917,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M4-888deg', name='Section-M4-888', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((153.32017517089844, 79.03237915039063, 188.43316650390625),),)), sectionName='Section-M4-888')

mdb.models['Model-1'].Material(name='M1-552deg')
mdb.models['Model-1'].materials['M1-552deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M1-552deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M1-552deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.959,
		0.043, 0.279, 0.0, 0.0, 0.0, 1.0, 0.0, -0.279,0.007,0.960,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M1-552deg', name='Section-M1-552', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((435.04391479492187, 14.22859287261963, 181.64755249023437),),)), sectionName='Section-M1-552')

mdb.models['Model-1'].Material(name='M3-583deg')
mdb.models['Model-1'].materials['M3-583deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M3-583deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M3-583deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.026,
		0.962, 0.271, 0.0, 0.0, 0.0, 1.0, 0.0, 0.936,-0.118,0.330,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M3-583deg', name='Section-M3-583', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((592.46899414062500, 199.78804016113281, 166.81468200683594),),)), sectionName='Section-M3-583')

mdb.models['Model-1'].Material(name='M4-323deg')
mdb.models['Model-1'].materials['M4-323deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M4-323deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M4-323deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.794,
		0.213, 0.569, 0.0, 0.0, 0.0, 1.0, 0.0, -0.368,0.576,-0.729,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M4-323deg', name='Section-M4-323', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((12.10984516143799, 269.39199829101563, 180.64750671386719),),)), sectionName='Section-M4-323')

mdb.models['Model-1'].Material(name='M2-069deg')
mdb.models['Model-1'].materials['M2-069deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M2-069deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M2-069deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.618,
		0.410, 0.671, 0.0, 0.0, 0.0, 1.0, 0.0, -0.071,0.821,-0.567,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M2-069deg', name='Section-M2-069', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((264.89962768554687, 213.97216796875000, 186.57174682617187),),)), sectionName='Section-M2-069')

mdb.models['Model-1'].Material(name='M0-503deg')
mdb.models['Model-1'].materials['M0-503deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M0-503deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M0-503deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.670,
		-0.668, -0.324, 0.0, 0.0, 0.0, 1.0, 0.0, 0.741,0.570,0.356,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M0-503deg', name='Section-M0-503', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((170.65614318847656, 320.69036865234375, 174.63388061523438),),)), sectionName='Section-M0-503')

mdb.models['Model-1'].Material(name='M1-568deg')
mdb.models['Model-1'].materials['M1-568deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M1-568deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M1-568deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.119,
		-0.237, -0.964, 0.0, 0.0, 0.0, 1.0, 0.0, -0.425,0.865,-0.265,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M1-568deg', name='Section-M1-568', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((424.44912719726562, 350.34014892578125, 193.17662048339844),),)), sectionName='Section-M1-568')

mdb.models['Model-1'].Material(name='M3-881deg')
mdb.models['Model-1'].materials['M3-881deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M3-881deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M3-881deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.630,
		0.698, -0.340, 0.0, 0.0, 0.0, 1.0, 0.0, 0.442,-0.682,-0.582,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M3-881deg', name='Section-M3-881', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((588.63812255859375, 329.26278686523437, 195.14123535156250),),)), sectionName='Section-M3-881')

mdb.models['Model-1'].Material(name='M4-645deg')
mdb.models['Model-1'].materials['M4-645deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M4-645deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M4-645deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.412,
		-0.191, 0.891, 0.0, 0.0, 0.0, 1.0, 0.0, 0.737,-0.505,-0.449,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M4-645deg', name='Section-M4-645', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((63.33156967163086, 429.59402465820313, 183.13273620605469),),)), sectionName='Section-M4-645')

mdb.models['Model-1'].Material(name='M4-603deg')
mdb.models['Model-1'].materials['M4-603deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M4-603deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M4-603deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.124,
		0.254, 0.959, 0.0, 0.0, 0.0, 1.0, 0.0, 0.736,-0.625,0.260,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M4-603deg', name='Section-M4-603', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((570.46228027343750, 496.84439086914062, 179.91838073730469),),)), sectionName='Section-M4-603')

mdb.models['Model-1'].Material(name='M1-741deg')
mdb.models['Model-1'].materials['M1-741deg'].Depvar(n=145)
mdb.models['Model-1'].materials['M1-741deg'].Density(table=((8.000000e-015,),))
mdb.models['Model-1'].materials['M1-741deg'].UserMaterial(unsymm=ON, mechanicalConstants=(
300000.000, 0.270, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0,1.0,1.0,1.0,1.0,0.0,  0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.849,
		-0.303, 0.433, 0.0, 0.0, 0.0, 1.0, 0.0, 0.338,0.320,0.885,
		0.0,  0.0,  6.000,1.000,0.0, 0.0, 0.0, 0.0, 0.0, 2,   
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 50.000,2.000,800.000,1000.000,
		0.500, 200.000, 5.000, 1000.000, 1.0, 1.0, 2.000, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 
		0.0,  0.0,  1.0, 10.0,1.0e-5,0.0,0.0,0.0, 0.0, 0.0))

mdb.models['Model-1'].HomogeneousSolidSection(material='M1-741deg', name='Section-M1-741', thickness=1.0)
mdb.models['Model-1'].parts['Part-total'].SectionAssignment(region=Region(cells= mdb.models['Model-1'].parts['Part-total'].cells.findAt(((203.29492187500000, 586.80676269531250, 187.32112121582031),),)), sectionName='Section-M1-741')

