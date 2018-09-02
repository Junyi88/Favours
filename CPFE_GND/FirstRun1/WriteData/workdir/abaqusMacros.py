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
    s.rectangle(point1=(0.0, 0.0), point2=(-32.5, -18.75))
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.BaseShell(sketch=s)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['Part-1']
    f, e, d1 = p.faces, p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=f[0], sketchUpEdge=e[3], 
        sketchPlaneSide=SIDE1, origin=(-16.25, -9.375, 0.0))
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=75.04, gridSpacing=1.87, transform=t)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Part-1']
    p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
    s1.Line(point1=(-7.21787071228027, 9.375), point2=(-8.415, 4.675))
    s1.CoincidentConstraint(entity1=v[4], entity2=g[2], addUndoState=False)
    s1.Line(point1=(-8.415, 4.675), point2=(-16.25, 2.3375))
    s1.CoincidentConstraint(entity1=v[6], entity2=g[3], addUndoState=False)
    s1.Line(point1=(2.805, 9.375), point2=(0.935, 2.805))
    s1.CoincidentConstraint(entity1=v[7], entity2=g[2], addUndoState=False)
    s1.Line(point1=(0.935, 2.805), point2=(-8.415, 4.675))
    s1.Line(point1=(-8.415, 4.675), point2=(-8.415, -4.67500000004657))
    s1.VerticalConstraint(entity=g[10], addUndoState=False)
    s1.Line(point1=(-8.415, -4.67500000004657), point2=(0.935, 2.805))
    s1.Line(point1=(0.935, 2.805), point2=(0.935, -9.375))
    s1.VerticalConstraint(entity=g[12], addUndoState=False)
    s1.CoincidentConstraint(entity1=v[10], entity2=g[4], addUndoState=False)
    s1.Line(point1=(0.935, -9.375), point2=(-8.415, -4.67500000004657))
    s1.Line(point1=(-8.415, -4.67500000004657), point2=(-16.25, -9.375))
    p = mdb.models['Model-1'].parts['Part-1']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    e1, d2 = p.edges, p.datums
    p.PartitionFaceBySketch(sketchUpEdge=e1[3], faces=pickedFaces, sketch=s1)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['Part-1']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#1 ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-1')
    p = mdb.models['Model-1'].parts['Part-1']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#4 ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-2')
    p = mdb.models['Model-1'].parts['Part-1']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#2 ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-3')
    p = mdb.models['Model-1'].parts['Part-1']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#10 ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-4')
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models['Model-1'].parts['Part-1']
    p.seedPart(size=1.9, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Part-1']
    p.generateMesh()
    mdb.meshEditOptions.setValues(enableUndo=True, maxUndoCacheElements=0.5)
    p = mdb.models['Model-1'].parts['Part-1']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedGeomSourceSide=regionToolset.Region(faces=faces)
    vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0))
    p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, 
        extrudeVector=vector, numberOfLayers=5)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.elements
    elements = e.getSequenceFromMask(mask=('[#0:6 #ffffffe0 #ffffffff:2 #1ff ]', ), 
        )
    p.Set(elements=elements, name='BottomUpElements-1')


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
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(0.0, 0.0), point2=(-27.5, -15.0))
    p = mdb.models['Model-1'].Part(name='Part-3', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-3']
    p.BaseShell(sketch=s)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-3']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['Part-3']
    f, e, d1 = p.faces, p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=f[0], sketchUpEdge=e[3], 
        sketchPlaneSide=SIDE1, origin=(-13.75, -7.5, 0.0))
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=62.64, gridSpacing=1.56, transform=t)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Part-3']
    p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
    s1.Spot(point=(-5.85, -1.56))
    s1.Spot(point=(-2.34, 3.51))
    s1.Spot(point=(-7.8, 7.5))
    s1.CoincidentConstraint(entity1=v[6], entity2=g[2], addUndoState=False)
    s1.Spot(point=(-9.75, -7.5))
    s1.CoincidentConstraint(entity1=v[7], entity2=g[4], addUndoState=False)
    s1.Spot(point=(-3.12, -7.5))
    s1.CoincidentConstraint(entity1=v[8], entity2=g[4], addUndoState=False)
    s1.Line(point1=(-7.8, 7.5), point2=(-9.75, -7.5))
    s1.Line(point1=(-9.75, -7.5), point2=(-3.12, -7.5))
    s1.HorizontalConstraint(entity=g[7], addUndoState=False)
    s1.Line(point1=(-3.12, -7.5), point2=(-5.85, -1.56))
    s1.Line(point1=(-5.85, -1.56), point2=(-2.34, 3.51))
    s1.Line(point1=(-2.34, 3.51), point2=(-7.8, 7.5))
    p = mdb.models['Model-1'].parts['Part-3']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    e1, d2 = p.edges, p.datums
    p.PartitionFaceBySketch(sketchUpEdge=e1[3], faces=pickedFaces, sketch=s1)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']


