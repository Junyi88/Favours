import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from lattice_generator import *


def set_axes_radius(ax, origin, radius):
    ax.set_xlim3d([origin[0] - radius, origin[0] + radius])
    ax.set_ylim3d([origin[1] - radius, origin[1] + radius])
    ax.set_zlim3d([origin[2] - radius, origin[2] + radius])

def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    '''

    limits = np.array([
        ax.get_xlim3d(),
        ax.get_ylim3d(),
        ax.get_zlim3d(),
    ])

    origin = np.mean(limits, axis=1)
    radius = 0.5 * np.max(np.abs(limits[:, 1] - limits[:, 0]))
    set_axes_radius(ax, origin, radius)


NodePoints, StrutlessMap, StruttedMap = get_preset_info()
NodePos = generate_node_positions(H=17.5, h=5.5, L=11.5)

selected_nodes = np.array([0, 1, 2, 3, 4, 5, 6, 7,
    14, 15, 16, 17, 18, 19,
    20, 21, 22, 23,
    28, 29, 30, 31, 32, 33,
    34, 35], dtype=np.int)

selected_struts = list()
for i in range(len(StrutlessMap)):
    if (StrutlessMap[i, 0] in selected_nodes) and (StrutlessMap[i, 1] in selected_nodes):
        selected_struts.append(i)
selected_struts = np.unique(np.array(selected_struts, dtype=np.int))
StrutlessMap = StrutlessMap[selected_struts, :]

selected_struts = list()
for i in range(len(StruttedMap)):
    if (StruttedMap[i, 0] in selected_nodes) and (StruttedMap[i, 1] in selected_nodes):
        selected_struts.append(i)
selected_struts = np.unique(np.array(selected_struts, dtype=np.int))
StruttedMap = StruttedMap[selected_struts, :]


X0s, Y0s, Z0s = generate_individual_beams(NodePos, StrutlessMap)
X1s, Y1s, Z1s = generate_individual_beams(NodePos, StruttedMap)


# %% ----------------------
fig = plt.figure(1, clear=True)

ax = fig.add_subplot(111, projection='3d')
# ax.set_aspect('equal')
ax.scatter3D(NodePos[selected_nodes, 0], NodePos[selected_nodes, 1], NodePos[selected_nodes, 2], s=20, c='r')

for i in range(X0s.shape[0]):
    ax.plot3D(X0s[i, :], Y0s[i, :], Z0s[i, :], 'blue', linewidth=2)

for i, pos in enumerate(NodePos):
    if i in selected_nodes:
        ax.text(pos[0], pos[1], pos[2], "{}".format(i), color='red', fontsize=6)

for i in range(len(X0s)):
    ax.text(np.mean(X0s[i, :]), np.mean(Y0s[i, :]), np.mean(Z0s[i, :]), "{}".format(i), color='blue', fontsize=6)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('No Strut')
set_axes_equal(ax)

# %% ----------------------
fig = plt.figure(2, clear=True)

ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(NodePos[selected_nodes, 0], NodePos[selected_nodes, 1], NodePos[selected_nodes, 2], s=20, c='r')

for i in range(X1s.shape[0]):
    ax.plot3D(X1s[i, :], Y1s[i, :], Z1s[i, :], 'blue', linewidth=2)

for i, pos in enumerate(NodePos):
    if i in selected_nodes:
        ax.text(pos[0], pos[1], pos[2], "{}".format(i), color='red', fontsize=6)

for i in range(len(X1s)):
    ax.text(np.mean(X1s[i, :]), np.mean(Y1s[i, :]), np.mean(Z1s[i, :]), "{}".format(i), color='blue', fontsize=6)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Strutted')
set_axes_equal(ax)


# 12 is extra strut
# Removed 4, 35, 16, 36, 21, 35, 9, 34
# 23, 19, 24, 17, 22, 18, 20

no_draw_struts = np.array(
    [12, 4, 35, 16, 36, 21, 35, 9, 34, 23, 19, 24, 17, 22, 18, 20], dtype=np.int)


# %% ----------------------
fig = plt.figure(3, clear=True)

ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(NodePos[selected_nodes, 0], NodePos[selected_nodes, 1], NodePos[selected_nodes, 2], s=20, c='r')

for i in range(X1s.shape[0]):
    if i not in no_draw_struts:
        ax.plot3D(X1s[i, :], Y1s[i, :], Z1s[i, :], 'b-', linewidth=2)
    elif i == 12:
        ax.plot3D(X1s[i, :], Y1s[i, :], Z1s[i, :], 'r-', linewidth=2)
    else:
        ax.plot3D(X1s[i, :], Y1s[i, :], Z1s[i, :], 'g-', linewidth=2)


ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
#ax.set_title('Strutted')
set_axes_equal(ax)
