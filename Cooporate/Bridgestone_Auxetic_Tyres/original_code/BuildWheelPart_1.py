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

# --------------------------------------
def ReadMyFiles(hasStrut):
    fileNode = './ToAbaNodeLoc.csv'
    fileStrut = './ToAbaNoStrutBeam.csv'
    fileNoStrut = './ToAbaStrutBeam.csv'
	
    NodePoint = np.loadtxt(fileNode,  \
		dtype='int', delimiter=',')
    if (hasStrut):
        StrutPoint = np.loadtxt(fileStrut,  \
            dtype='int', delimiter=',')	
    else:
        StrutPoint = np.loadtxt(fileNoStrut,  \
            dtype='int', delimiter=',')	
			
    NodePoint = NodePoint - 1
    StrutPoint = StrutPoint - 1
    return NodePoint, StrutPoint

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

# ---------------------------------------
GeoH = 17.5
Geoh = 5.5
GeoL = 10.0
hasStrut = True
ModelName = 'Model-1'
PartName = 'Part-1'

R0 = 205.5
Lz = 2.0 * np.pi * R0 / 100.0
A0 = Lz / (GeoH - Geoh)
GeoH *= A0
Geoh *= A0

PrepX = np.array([-GeoL, -GeoL/2.0, 0.0, GeoL/2.0, GeoL])
PrepY = np.array([-GeoL, -GeoL/2.0, 0.0, GeoL/2.0, GeoL])
PrepZ = np.array([-(GeoH-Geoh), -GeoH/2.0,  -(GeoH/2.0-Geoh), \
    (GeoH/2.0-Geoh), GeoH/2.0, (GeoH-Geoh)])


NodePoint, StrutPoint = ReadMyFiles(hasStrut)


x = np.zeros(NodePoint.shape[0])
y = np.zeros(NodePoint.shape[0])
z = np.zeros(NodePoint.shape[0])
# Create Datum Points
for n in range(0, len(NodePoint)):
    x[n] = PrepX[NodePoint[n, 0]]
    y[n] = PrepY[NodePoint[n, 1]]
    z[n] = PrepZ[NodePoint[n, 2]]

# %% -----------------------------------------------


# %% --------------------------------------------------
Ny = 0

Ly = np.max(y) - np.min(y) 
Rshift = 205.5 + Ny * Ly

X = np.zeros(NodePoint.shape[0])
Y = np.zeros(NodePoint.shape[0])
Z = np.zeros(NodePoint.shape[0])

for i in range(len(X)):
    R = (y[i] / Ly - 0.5) * Ly - Rshift
    theta = 2.0e-2 * np.pi * (z[i] / Lz - 0.5)

    X[i] = x[i]
    Y[i] = R * np.cos(theta)
    Z[i] = R * np.sin(theta)

# %% -------------------------------------------


# %% ===========================================
ModelName = 'Model-1'
PartName = 'Part-0'

p = mdb.models[ModelName].Part(name=PartName, dimensionality=THREE_D, \
    type=DEFORMABLE_BODY)
p.ReferencePoint(point=(0.0, 0.0, 0.0))
p = mdb.models[ModelName].parts[PartName]

PointD = ()
FetD = ()
# Create Datum Points
for i in range(0, len(NodePoint)):
    f = p.DatumPointByCoordinate(coords=(X[i], Y[i], Z[i]))
    FetD=FetD+((f,))
    P = GetDatumNumber(f)
    PointD=PointD+((P+1,))

d = p.datums

StrutLocs = ()
for n in range(0, len(StrutPoint)):
    # print(n)
    P1 = PointD[int(StrutPoint[n,0])]
    P2 = PointD[int(StrutPoint[n,1])]
    StrutLocs = StrutLocs +  \
        ((d[P1],d[P2]),)

p.WirePolyLine(points=StrutLocs, mergeWire=OFF, meshable=ON)
