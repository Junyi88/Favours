# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Macro1():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(0.0, 0.0), point2=(-47.5, 25.0))
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.BaseSolidExtrude(sketch=s, depth=20.0)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.rectangle(point1=(0.0, 0.0), point2=(-48.75, 22.5))
    p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-2']
    p.BaseShell(sketch=s1)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-2']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['Part-2']
    f, e, d1 = p.faces, p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=f[0], sketchUpEdge=e[1], 
        sketchPlaneSide=SIDE1, origin=(-24.375, 11.25, 0.0))
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=107.38, gridSpacing=2.68, transform=t)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Part-2']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    s.Line(point1=(-11.39, 11.25), point2=(-16.75, 4.69))
    s.CoincidentConstraint(entity1=v[4], entity2=g[4], addUndoState=False)
    s.Line(point1=(-16.75, 4.69), point2=(2.68, -1.34))
    s.Line(point1=(2.68, -1.34), point2=(-9.73041915893555, -7.88415002822876))
    s.Line(point1=(-9.73041915893555, -7.88415002822876), point2=(10.05, -11.25))
    s.CoincidentConstraint(entity1=v[8], entity2=g[2], addUndoState=False)
    p = mdb.models['Model-1'].parts['Part-2']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    e1, d2 = p.edges, p.datums
    p.PartitionFaceBySketch(sketchUpEdge=e1[1], faces=pickedFaces, sketch=s)
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['Part-2']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#2 ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-1')
    p = mdb.models['Model-1'].parts['Part-2']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#1 ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-2')
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models['Model-1'].parts['Part-2']
    p.seedPart(size=3.6, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Part-2']
    p.generateMesh()
    mdb.meshEditOptions.setValues(enableUndo=True, maxUndoCacheElements=0.5)
    p = mdb.models['Model-1'].parts['Part-2']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#2 ]', ), )
    pickedGeomSourceSide=regionToolset.Region(faces=faces)
    vector =((0.0, 0.0, 0.0), (0.0, 0.0, 2.0))
    p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, 
        extrudeVector=vector, numberOfLayers=2)
    p = mdb.models['Model-1'].parts['Part-2']
    e = p.elements
    elements = e.getSequenceFromMask(mask=('[#0:3 #fffe0000 #ffffffff:2 #1f ]', ), 
        )
    p.Set(elements=elements, name='BottomUpElements-1')
    session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    p1 = mdb.models['Model-1'].parts['Part-2']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['Model-1'].Part(name='Part-2-Copy', 
        objectToCopy=mdb.models['Model-1'].parts['Part-2'])
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p1 = mdb.models['Model-1'].parts['Part-2']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['Model-1'].parts['Part-2']
    p.deleteMesh()
    p = mdb.models['Model-1'].parts['Part-2']
    p.PartFromMesh(name='Part-2-mesh-1', copySets=True)
    p1 = mdb.models['Model-1'].parts['Part-2-mesh-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=60.6475, 
        farPlane=104.05, cameraPosition=(37.5713, 20.0018, -42.9171), 
        cameraUpVector=(-0.616354, 0.763524, -0.192718), cameraTarget=(
        -31.5375, 11.25, 1.00001))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=63.8691, 
        farPlane=100.829, cameraPosition=(22.2615, 4.25858, -60.9525), 
        cameraUpVector=(-0.550876, 0.824656, -0.128364), cameraTarget=(
        -31.5375, 11.25, 1.00001))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=56.8104, 
        farPlane=107.887, cameraPosition=(39.5188, 47.1399, 22.0769), 
        cameraUpVector=(-0.616201, 0.684217, -0.390056), cameraTarget=(
        -31.5375, 11.25, 0.999996))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=64.9566, 
        farPlane=99.7409, cameraPosition=(12.8442, 24.1373, 69.1579), 
        cameraUpVector=(-0.397387, 0.864613, -0.307454), cameraTarget=(
        -31.5375, 11.25, 0.99999))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=68.1298, 
        farPlane=96.5677, cameraPosition=(-6.77482, -7.71076, 77.2143), 
        cameraUpVector=(-0.163813, 0.984541, -0.0620028), cameraTarget=(
        -31.5375, 11.25, 0.99999))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=67.777, 
        farPlane=96.9206, width=86.2589, height=39.5017, cameraPosition=(
        -6.85498, -7.76856, 77.226), cameraTarget=(-31.6177, 11.1922, 1.01165))
    elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, 
        secondOrderAccuracy=OFF, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts['Part-2-mesh-1']
    z1 = p.elements
    elems1 = z1[0:84]
    pickedRegions =(elems1, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON, mesh=OFF)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    mdb.models['Model-1'].Material(name='Material-1')
    mdb.models['Model-1'].materials['Material-1'].Depvar(n=5)
    mdb.models['Model-1'].materials['Material-1'].UserMaterial(
        mechanicalConstants=(1.0, 2.0, 3.0, 4.0, 5.0))
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', 
        material='Material-1', thickness=None)
    p = mdb.models['Model-1'].parts['Part-2-mesh-1']
    e = p.elements
    elements = e.getSequenceFromMask(mask=('[#ffffffff:2 #fffff ]', ), )
    region = p.Set(elements=elements, name='Set-3')
    p = mdb.models['Model-1'].parts['Part-2-mesh-1']
    p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=63.3951, 
        farPlane=101.302, width=150.945, height=68.939, cameraPosition=(
        13.1431, -1.40261, 72.3122), cameraTarget=(-11.6196, 17.5582, 
        -3.90215))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=34.4685, 
        farPlane=89.4925, cameraPosition=(-84.1264, 10.432, 34.4814), 
        cameraUpVector=(0.449011, 0.845171, 0.289957), cameraTarget=(-11.6196, 
        17.5581, -3.90215))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=34.9133, 
        farPlane=87.9627, cameraPosition=(-60.504, -19.2196, 46.3052), 
        cameraUpVector=(-0.029156, 0.955839, 0.292441), cameraTarget=(-19.3825, 
        27.3023, -7.78771))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=33.0321, 
        farPlane=85.5232, cameraPosition=(-48.4892, -37.4443, 30.9343), 
        cameraUpVector=(-0.214185, 0.754974, 0.61979), cameraTarget=(-23.4718, 
        33.5052, -2.55617))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=29.3599, 
        farPlane=81.4712, cameraPosition=(-45.4314, -42.0325, -7.03888), 
        cameraUpVector=(-0.408687, 0.245819, 0.878947), cameraTarget=(-24.6619, 
        35.2909, 12.2231))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=33.4516, 
        farPlane=84.7212, cameraPosition=(-49.3216, -32.4164, 36.7841), 
        cameraUpVector=(-0.183053, 0.859624, 0.477009), cameraTarget=(-22.7712, 
        30.6173, -9.07579))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=45.5565, 
        farPlane=77.808, cameraPosition=(-43.1797, 15.2978, 61.4844), 
        cameraUpVector=(0.0429206, 0.927117, -0.372305), cameraTarget=(
        -25.1893, 11.8322, -18.8003))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=43.0516, 
        farPlane=82.4513, cameraPosition=(-33.284, 51.1008, 49.4876), 
        cameraUpVector=(0.172947, 0.52523, -0.833201), cameraTarget=(-28.5048, 
        -0.163449, -14.7808))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=45.9565, 
        farPlane=79.5463, width=117.85, height=53.8241, cameraPosition=(
        -36.856, 50.4343, 49.7536), cameraTarget=(-32.0768, -0.829977, 
        -14.5148))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=48.3276, 
        farPlane=77.5723, cameraPosition=(-48.2106, 17.0516, 61.4474), 
        cameraUpVector=(0.0961117, 0.908746, -0.406133), cameraTarget=(
        -28.5308, 9.59539, -18.1667))
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p1 = mdb.models['Model-1'].parts['Part-2-Copy']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=77.9878, 
        farPlane=136.929, width=122.124, height=55.9259, cameraPosition=(
        45.9501, 72.4594, 55.5884), cameraTarget=(-16.0908, 10.4184, -6.45255))
    p = mdb.models['Model-1'].parts['Part-2-Copy']
    e = p.elements
    elements = e.getSequenceFromMask(mask=('[#0:3 #fffe0000 #ffffffff:2 #1f ]', ), 
        )
    p.deleteElement(elements=elements, deleteUnreferencedNodes=ON)
    p = mdb.models['Model-1'].parts['Part-2-Copy']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedGeomSourceSide=regionToolset.Region(faces=faces)
    vector =((0.0, 0.0, 0.0), (0.0, 0.0, 2.0))
    p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, 
        extrudeVector=vector, numberOfLayers=2)
    p = mdb.models['Model-1'].parts['Part-2-Copy']
    e = p.elements
    elements = e.getSequenceFromMask(mask=(
        '[#0:3 #fffe0000 #ffffffff:3 #7fffffff ]', ), )
    p.Set(elements=elements, name='BottomUpElements-2')
    p = mdb.models['Model-1'].parts['Part-2-Copy']
    p.deleteMesh()
    p = mdb.models['Model-1'].parts['Part-2-Copy']
    p.PartFromMesh(name='Part-2-Copy-mesh-1', copySets=True)
    p1 = mdb.models['Model-1'].parts['Part-2-Copy-mesh-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    p1 = mdb.models['Model-1'].parts['Part-2-Copy']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['Model-1'].Part(name='Part-2-Copy-Copy', 
        objectToCopy=mdb.models['Model-1'].parts['Part-2-Copy'])
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].parts['Part-2-Copy-Copy']
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Part-2-Copy-mesh-1']
    a.Instance(name='Part-2-Copy-mesh-1-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['Part-2-mesh-1']
    a.Instance(name='Part-2-mesh-1-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=88.1207, 
        farPlane=144.747, width=104.949, height=47.9318, viewOffsetX=16.6935, 
        viewOffsetY=-0.568226)
    a = mdb.models['Model-1'].rootAssembly
    a.InstanceFromBooleanMerge(name='Part-3', instances=(
        a.instances['Part-2-Copy-mesh-1-1'], a.instances['Part-2-mesh-1-1'], ), 
        mergeNodes=ALL, nodeMergingTolerance=1e-06, domain=MESH, 
        originalInstances=SUPPRESS)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=87.2569, 
        farPlane=120.697, width=103.92, height=47.4619, cameraPosition=(
        -8.62317, 54.6412, 94.3401), cameraUpVector=(-0.0555942, 0.751708, 
        -0.657149), cameraTarget=(-28.2474, 11.757, -12.1147), 
        viewOffsetX=16.5299, viewOffsetY=-0.562656)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p1 = mdb.models['Model-1'].parts['Part-3']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    mdb.models['Model-1'].parts['Part-3'].deleteSets(setNames=('Surf-2', 'Surf-1', 
        ))
    p1 = mdb.models['Model-1'].parts['Part-2-mesh-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    del mdb.models['Model-1'].parts['Part-2-mesh-1'].sets['Surf-2']
    p1 = mdb.models['Model-1'].parts['Part-3']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['Model-1'].parts['Part-3']
    e = p.elements
    elements = e.getSequenceFromMask(mask=(
        '[#7c0006 #51d07e00 #f8000c0 #3a0fc000 #a ]', ), )
    p.Set(elements=elements, name='ALL')
    p = mdb.models['Model-1'].parts['Part-3']
    region = p.sets['ALL']
    p = mdb.models['Model-1'].parts['Part-3']
    p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)


def Macro2():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p1 = mdb.models['Model-1'].parts['Part-2-Copy']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['Model-1'].parts['Part-2-Copy']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['Part-2-Copy']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#2 ]', ), )
    pickedGeomSourceSide=regionToolset.Region(faces=faces)
    vector =((0.0, 0.0, 0.0), (0.0, 0.0, 2.0))
    p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, 
        extrudeVector=vector, numberOfLayers=2)
    p = mdb.models['Model-1'].parts['Part-2-Copy']
    e = p.elements
    elements = e.getSequenceFromMask(mask=('[#0:8 #ffffffff:2 #3fffff ]', ), )
    p.Set(elements=elements, name='BottomUpElements-1')


def Macro3():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    p = mdb.models['Model-1'].parts['Part-2-Copy']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedGeomSourceSide=regionToolset.Region(faces=faces)
    vector =((0.0, 0.0, 0.0), (0.0, 0.0, -2.0))
    p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, 
        extrudeVector=vector, numberOfLayers=2)
    p = mdb.models['Model-1'].parts['Part-2-Copy']
    e = p.elements
    elements = e.getSequenceFromMask(mask=('[#0:10 #ffc00000 #ffffffff:4 #f ]', ), 
        )
    p.Set(elements=elements, name='BottomUpElements-3')


def Macro4():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    elemType1 = mesh.ElemType(elemCode=C3D20R, elemLibrary=STANDARD)
    elemType2 = mesh.ElemType(elemCode=C3D15, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts['Part-2-Copy']
    z1 = p.elements
    elems1 = z1[1:4]+z1[9:11]+z1[18:25]+z1[32:33]+z1[38:39]+z1[40:47]+z1[52:58]+\
        z1[60:66]+z1[70:73]+z1[78:80]+z1[87:94]+z1[101:102]+z1[107:108]+\
        z1[109:116]+z1[121:127]+z1[129:133]+z1[134:135]+z1[139:140]+\
        z1[141:142]+z1[339:340]+z1[341:342]+z1[343:346]+z1[351:353]+\
        z1[360:367]+z1[373:375]+z1[380:381]+z1[382:389]+z1[394:400]+\
        z1[402:408]+z1[412:415]+z1[420:422]+z1[428:436]+z1[440:441]+\
        z1[442:444]+z1[449:450]+z1[451:458]+z1[463:469]+z1[470:477]+\
        z1[481:482]+z1[483:484]
    pickedRegions =(elems1, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))


def Macro5():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON, mesh=OFF)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=76.0271, 
        farPlane=140.834, cameraPosition=(-128.665, 30.5451, 22.5635), 
        cameraUpVector=(0.52442, 0.847134, 0.0857208), cameraTarget=(-25.2639, 
        11.0216, 0.783684))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=77.1185, 
        farPlane=139.063, cameraPosition=(-122.143, 26.9787, -43.3364), 
        cameraUpVector=(0.303169, 0.837159, 0.45525), cameraTarget=(-25.2054, 
        10.9896, 0.192531))
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-2', 
        material='Material-1', thickness=None)
    p = mdb.models['Model-1'].parts['Part-2-Copy']
    e = p.elements
    elements = e.getSequenceFromMask(mask=('[#0:13 #4000000 ]', ), )
    region = p.Set(elements=elements, name='Set-4')
    p = mdb.models['Model-1'].parts['Part-2-Copy']
    p.SectionAssignment(region=region, sectionName='Section-2', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)


def Macro6():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    a = mdb.models['Model-1'].rootAssembly
    a.regenerate()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB, parallelizationMethodExplicit=DOMAIN, 
        numDomains=1, activateLoadBalancing=False, multiprocessingMode=DEFAULT, 
        numCpus=1, numGPUs=0)
    mdb.jobs['Job-1'].writeInput(consistencyChecking=OFF)


def Macro7():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    mdb.jobs['Job-1'].writeInput(consistencyChecking=OFF)


def Macro8():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    mdb.models['Model-1'].setValues(noPartsInputFile=ON)
    mdb.jobs['Job-1'].writeInput(consistencyChecking=OFF)


