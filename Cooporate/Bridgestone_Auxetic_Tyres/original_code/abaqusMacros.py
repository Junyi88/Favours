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
    p = mdb.models['Model-1'].parts['Part-1']
    d = p.datums
    p.WirePolyLine(points=((d[47], d[46]), (d[46], d[31])), mergeWire=OFF, 
        meshable=ON)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#3 ]', ), )
    p.Set(edges=edges, name='Wire-1-Set-1')


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
    d1 = p.datums
    p.WirePolyLine(points=((d1[58], d1[61]), (d1[61], d1[60])), mergeWire=ON, 
        meshable=ON)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#c ]', ), )
    p.Set(edges=edges, name='Wire-2-Set-1')


