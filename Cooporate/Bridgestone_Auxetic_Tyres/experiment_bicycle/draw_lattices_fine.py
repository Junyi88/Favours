import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from lattice_generator import *
from make_rounder_tyre import *

NodePoints, StrutlessMap, StruttedMap = get_preset_info()
NodePos = generate_node_positions(H=17.5, h=5.5, L=11.5)

NodePointsx, StrutlessMapx, StruttedMapx = get_preset_info()
NodePosx = generate_node_positions(H=17.5, h=5.5, L=11.5)

ds = 5
StrutMap = StrutlessMap

nPoints_ori = NodePos.shape[0]
nStruts_ori = StrutMap.shape[0]

iPoint = nPoints_ori
iStrut = nStruts_ori

NewStruts = list()
NewPoints = list()

for ist in range(nStruts_ori):
    p1 = NodePos[StrutMap[ist, 0], :]
    p2 = NodePos[StrutMap[ist, 1], :]
    Ds = p2 - p1
    DS = np.sqrt(np.dot(Ds, Ds))
    nS = np.ceil(DS / ds).astype(np.int)
    dxyz = Ds / nS

    for ii in range(1, nS - 1):
        tmp = p1 + dxyz * ii
        NewPoints.append(tmp.tolist())

    NewStruts.append([StrutMap[ist, 0], iPoint])
    iPoint += 1

    for ii in range(1, nS - 1):
        NewStruts.append([iPoint, iPoint + 1])
        iPoint += 1

    NewStruts.append([iPoint, StrutMap[ist, 1]])        
    iPoint += 1
OutPoints = NodePos.tolist()
OutPoints.extend(NewPoints)
OutPoints = np.array(OutPoints, dtype=np.float)
NewStruts = np.array(NewStruts, dtype=np.int)


# %%
NodePoints, StrutlessMap, StruttedMap = get_preset_info()
NodePos = generate_node_positions(H=17.5, h=5.5, L=11.5)
NodePos, StrutlessMap = slice_vals(5, NodePos, StrutlessMap)
X0s, Y0s, Z0s = generate_individual_beams(NodePos, StrutlessMap)



# %% ----------------------
fig = plt.figure(1, clear=True)

ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(NodePos[:, 0], NodePos[:, 1], NodePos[:, 2], s=20, c='r')

for i in range(X0s.shape[0]):
    ax.plot3D(X0s[i, :], Y0s[i, :], Z0s[i, :], 'blue', linewidth=2)

for i, pos in enumerate(NodePos):
    ax.text(pos[0], pos[1], pos[2], "{}".format(i), color='red', fontsize=6)

for i in range(len(X0s)):
    ax.text(np.mean(X0s[i, :]), np.mean(Y0s[i, :]), np.mean(Z0s[i, :]), "{}".format(i), color='blue', fontsize=6)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('No Strut')


# %% ----------------------
NodePos = generate_node_positions(H=17.5, h=5.5, L=11.5)
NodePos, StruttedMap = slice_vals(5, NodePos, StruttedMap)
X1s, Y1s, Z1s = generate_individual_beams(NodePos, StruttedMap)

fig = plt.figure(2, clear=True)

ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(NodePos[:, 0], NodePos[:, 1], NodePos[:, 2], s=20, c='r')

for i in range(X1s.shape[0]):
    ax.plot3D(X1s[i, :], Y1s[i, :], Z1s[i, :], 'blue', linewidth=2)

for i, pos in enumerate(NodePos):
    ax.text(pos[0], pos[1], pos[2], "{}".format(i), color='red', fontsize=6)

for i in range(len(X1s)):
    ax.text(np.mean(X1s[i, :]), np.mean(Y1s[i, :]), np.mean(Z1s[i, :]), "{}".format(i), color='blue', fontsize=6)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Strutted')
