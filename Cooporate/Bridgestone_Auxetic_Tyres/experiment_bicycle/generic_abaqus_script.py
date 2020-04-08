from abaqus import *
from abaqusConstants import *
import __main__
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
import numpy as np

# %% ---------------------------------
def read_files(val_name, read_dir='./', hasStrut=False):
    file_path = read_dir + 'NodePos_' + str(val_name) + '.npy'
    NodePos = np.load(file_path)

    if hasStrut:
        StrutMap = np.load(read_dir + 'StruttedMap.npy')
    else:
        StrutMap = np.load(read_dir + 'StrutlessMap.npy')

    return NodePos, StrutMap

def GetDatumNumber(myF):
    f = myF.name
    mystr = ''
    flag = False
    for n in range(0, len(f)):
        if flag:
            mystr = mystr + f[n]
        else:
            if f[n] == '-':
                flag = True
    P = int(mystr)
    return P

def generate_part(val_name, NodePos, StrutMap):
    ModelName = 'Model-1'
    PartName = 'Part-' + str(val_name)

    p = mdb.models[ModelName].Part(name=PartName, dimensionality=THREE_D, \
        type=DEFORMABLE_BODY)
    p.ReferencePoint(point=(0.0, 0.0, 0.0))
    p = mdb.models[ModelName].parts[PartName]    

    PointD = ()
    FetD = ()

    # Create Datum Points
    for i in range(0, len(NodePos[:, 0])):
        f = p.DatumPointByCoordinate(coords=(NodePos[i, 0], NodePos[i, 1], NodePos[i, 2]))
        FetD = FetD + ((f, ))
        P = GetDatumNumber(f)
        PointD = PointD + ((P + 1, ))

    d = p.datums

    StrutLocs = ()
    for n in range(0, len(StrutMap)):
        # print(n)
        P1 = PointD[int(StrutMap[n, 0])]
        P2 = PointD[int(StrutMap[n, 1])]
        StrutLocs = StrutLocs +  \
            ((d[P1], d[P2]),)

    p.WirePolyLine(points=StrutLocs, mergeWire=OFF, meshable=ON)

read_dir = './x_8/'
val_list = ['0', 'n1', 'p1', 'n2', 'p2', 'n3', 'p3', 'n4', 'p4']

for val_name in val_list:
    NodePos, StrutMap = read_files(val_name, read_dir=read_dir, hasStrut=False)
    generate_part(val_name, NodePos, StrutMap)
