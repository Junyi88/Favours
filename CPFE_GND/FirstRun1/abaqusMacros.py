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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=10.7615, 
        farPlane=18.0132, width=9.90734, height=4.99087, viewOffsetX=-0.082446, 
        viewOffsetY=-0.000656337)
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    d1 = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d1[5], cells=pickedCells)
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#2 ]', ), )
    d2 = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d2[5], cells=pickedCells)


