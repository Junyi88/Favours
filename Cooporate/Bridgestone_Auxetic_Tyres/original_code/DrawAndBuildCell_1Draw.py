import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

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

PointD = ()
FetD = ()

x = np.zeros(NodePoint.shape[0])
y = np.zeros(NodePoint.shape[0])
z = np.zeros(NodePoint.shape[0])
# Create Datum Points
for n in range(0, len(NodePoint)):
    x[n] = PrepX[NodePoint[n, 0]]
    y[n] = PrepY[NodePoint[n, 1]]
    z[n] = PrepZ[NodePoint[n, 2]]

# %%
fig = plt.figure(1, clear=True)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='red')
for i in range(len(x)):
    ax.text(x[i], y[i], z[i], "{}".format(i+1), color='red')
for i in range(0, len(StrutPoint)):
    P1 = int(StrutPoint[i, 0])
    P2 = int(StrutPoint[i, 1])
    pp = [P1, P2]
    ax.plot(x[pp], y[pp], z[pp], 'b-')    

#ax.set_aspect('equal')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# %% --------------------------------------------------
Rshift = 205.5
Ly = np.max(y) - np.min(y) 

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
fig = plt.figure(2, clear=True)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, c='red')
for i in range(len(X)):
    ax.text(X[i], Y[i], Z[i], "{}".format(i+1), color='red')
for i in range(0, len(StrutPoint)):
    P1 = int(StrutPoint[i, 0])
    P2 = int(StrutPoint[i, 1])
    pp = [P1, P2]
    ax.plot(X[pp], Y[pp], Z[pp], 'b-')    

#ax.set_aspect('equal')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
