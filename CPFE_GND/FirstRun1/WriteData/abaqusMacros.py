# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Macro1x():
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
    p = mdb.models['Model-1'].parts['Part-Base']
    f, e, d = p.faces, p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=f[0], sketchUpEdge=e[1], 
        sketchPlaneSide=SIDE1, origin=(380.0, 250.0, 0.0))
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=1819.45, gridSpacing=45.48, transform=t)
    g, v, d1, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Part-Base']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    s.Line(point1=(-204.092041015625, 250.0), point2=(-352.47, 79.59))
    s.CoincidentConstraint(entity1=v[4], entity2=g[4], addUndoState=False)
    s.Line(point1=(-352.47, 79.59), point2=(-256.494866617024, -3.9766592644155))
    s.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
    s.Line(point1=(-256.494866617024, -3.9766592644155), point2=(-380.0, -79.59))
    s.CoincidentConstraint(entity1=v[7], entity2=g[5], addUndoState=False)
    s.Line(point1=(443.43, 90.96), point2=(238.77, 90.96))
    s.HorizontalConstraint(entity=g[9], addUndoState=False)
    s.Line(point1=(238.77, 90.96), point2=(238.77, -102.33))
    s.VerticalConstraint(entity=g[10], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
    s.Line(point1=(238.77, -102.33), point2=(238.77, -260.493621826172))
    s.VerticalConstraint(entity=g[11], addUndoState=False)
    s.ParallelConstraint(entity1=g[10], entity2=g[11], addUndoState=False)
    p = mdb.models['Model-1'].parts['Part-Base']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    e1, d2 = p.edges, p.datums
    p.PartitionFaceBySketch(sketchUpEdge=e1[1], faces=pickedFaces, sketch=s)
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['Part-Base']
    f1, e, d = p.faces, p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=f1[1], sketchUpEdge=e[4], 
        sketchPlaneSide=SIDE1, origin=(361.421271, 251.868316, 0.0))
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=1819.45, gridSpacing=45.48, transform=t)
    g, v, d1, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Part-Base']
    p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
    s1.Line(point1=(-68.22, 79.59), point2=(-102.33, 0.0))
    s1.Line(point1=(-102.33, 0.0), point2=(-56.85, -68.22))
    s1.Line(point1=(-56.85, -68.22), point2=(68.22, -79.59))
    s1.Line(point1=(68.22, -79.59), point2=(125.07, 11.37))
    s1.Line(point1=(125.07, 11.37), point2=(48.7742385789752, 59.0548508875072))
    s1.PerpendicularConstraint(entity1=g[25], entity2=g[26], addUndoState=False)
    s1.Line(point1=(48.7742385789752, 59.0548508875072), point2=(-68.22, 79.59))
    p = mdb.models['Model-1'].parts['Part-Base']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#2 ]', ), )
    e1, d2 = p.edges, p.datums
    p.PartitionFaceBySketch(sketchUpEdge=e1[4], faces=pickedFaces, sketch=s1)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']


def ToMesh():
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
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p1 = mdb.models['Model-1'].parts['Part-Base']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['Model-1'].parts['Part-Base']
    p.seedPart(size=5.0, deviationFactor=0.1, minSizeFactor=0.1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1632.06, 
        farPlane=1879.52, width=1374.27, height=717.921, viewOffsetX=185.351, 
        viewOffsetY=-86.7868)
    p = mdb.models['Model-1'].parts['Part-Base']
    f = p.faces
    pickedRegions = f.getSequenceFromMask(mask=('[#ffffffff #3ff ]', ), )
    p.setMeshControls(regions=pickedRegions, elemShape=QUAD)
    p = mdb.models['Model-1'].parts['Part-Base']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1638.57, 
        farPlane=1873.01, width=1302.27, height=680.309, viewOffsetX=195.513, 
        viewOffsetY=-236.135)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1652.16, 
        farPlane=1859.41, width=1027.74, height=535.558, viewOffsetX=43.5414, 
        viewOffsetY=-64.4567)
    p = mdb.models['Model-1'].parts['Part-Base']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#10000 ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-1')
    p = mdb.models['Model-1'].parts['Part-Base']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#20 ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-2')


def deletemesh():
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
    mdb.meshEditOptions.setValues(enableUndo=True, maxUndoCacheElements=0.5)
    p = mdb.models['Model-1'].parts['Part-Base']
    e = p.elementFaces
    pickedElemFacesSourceSide = e.getSequenceFromMask(mask=(
        '[#0:3 #1000000 #10101 #1 #0:344 #100 #1', 
        ' #0 #1000000 #0 #1:2 #10000 #0:18 #1000000', 
        ' #1 #0:56 #1010100 #1010101 #10100 #0:2 #10100', 
        ' #0:12 #1000000 #0:2 #1 #0 #10000 #0', 
        ' #1 #0 #10100 #10000 #0:2 #1000000:3 #0', 
        ' #10000 #1000001 #0:5 #10100 ]', ), )
    vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0))
    p.generateBottomUpExtrudedMesh(elemFacesSourceSide=pickedElemFacesSourceSide, 
        extrudeVector=vector, numberOfLayers=1, extendElementSets=True)
    p = mdb.models['Model-1'].parts['Part-Base']
    e = p.elements
    elements = e.getSequenceFromMask(mask=('[#0:65 #ffffffff #7f ]', ), )
    p.Set(elements=elements, name='BottomUpElements-2')
    p = mdb.models['Model-1'].parts['Part-Base']
    p.deleteMesh()


def hghg():
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
    pass


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
    p = mdb.models['Model-1'].parts['Part-Base']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['Part-Base']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#10000000 ]', ), )
    pickedGeomSourceSide=regionToolset.Region(faces=faces)
    vector =((0.0, 0.0, 0.0), (0.0, 0.0, 10.0))
    p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, 
        extrudeVector=vector, numberOfLayers=1, extendElementSets=True)
    p = mdb.models['Model-1'].parts['Part-Base']
    e = p.elements
    elements = e.getSequenceFromMask(mask=('[#0:66 #ffffff80 #ffffffff #1fffff ]', 
        ), )
    p.Set(elements=elements, name='BottomUpElements-1')


