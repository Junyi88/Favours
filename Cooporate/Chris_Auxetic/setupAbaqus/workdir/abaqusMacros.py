# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def TestBuildWires1():
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
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p.ReferencePoint(point=(0.0, 0.0, 0.0))
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['Part-1']
    p.DatumPointByCoordinate(coords=(1.0, 0.0, 0.0))
    p = mdb.models['Model-1'].parts['Part-1']
    p.DatumPointByCoordinate(coords=(0.0, 1.0, 0.0))
    p = mdb.models['Model-1'].parts['Part-1']
    p.DatumPointByCoordinate(coords=(0.0, 1.0, 1.0))
    p = mdb.models['Model-1'].parts['Part-1']
    d, r = p.datums, p.referencePoints
    p.WirePolyLine(points=((r[1], d[2]), (d[2], d[3]), (d[3], d[4])), 
        mergeType=IMPRINT, meshable=ON)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#7 ]', ), )
    p.Set(edges=edges, name='Wire-1-Set-1')
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.6284, 
        farPlane=7.22801, width=4.32699, height=2.40048, 
        viewOffsetX=-0.0134827, viewOffsetY=-0.0124901)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#6 ]', ), )
    region=p.Set(edges=edges, name='Set-2')
    p = mdb.models['Model-1'].parts['Part-1']
    p.assignBeamSectionOrientation(region=region, method=N1_COSINES, n1=(0.0, 0.0, 
        -1.0))
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#1 ]', ), )
    region=p.Set(edges=edges, name='Set-3')
    p = mdb.models['Model-1'].parts['Part-1']
    p.assignBeamSectionOrientation(region=region, method=N1_COSINES, n1=(0.0, 1.0, 
        -1.0))


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
    p = mdb.models['Model-1'].parts['Part-1']
    e1, d, r = p.edges, p.datums, p.referencePoints
    p.WirePolyLine(points=((p.InterestingPoint(edge=e1[4], rule=MIDDLE), 
        p.InterestingPoint(edge=e1[5], rule=MIDDLE)), (p.InterestingPoint(
        edge=e1[5], rule=MIDDLE), p.InterestingPoint(edge=e1[0], rule=MIDDLE)), 
        (p.InterestingPoint(edge=e1[0], rule=MIDDLE), r[1]), (r[1], 
        p.InterestingPoint(edge=e1[0], rule=MIDDLE)), (p.InterestingPoint(
        edge=e1[0], rule=MIDDLE), d[3])), mergeType=MERGE, meshable=ON)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#19 ]', ), )
    p.Set(edges=edges, name='Wire-3-Set-1')


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
    p = mdb.models['Model-1'].parts['Part-1']
    e, d1, r1 = p.edges, p.datums, p.referencePoints
    p.WirePolyLine(points=((d1[59], d1[47]), (d1[47], d1[31]), (d1[31], d1[61]), (
        d1[61], d1[49]), (d1[61], d1[19])), mergeType=MERGE, meshable=ON)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#1f ]', ), )
    p.Set(edges=edges, name='Wire-1-Set-1')


