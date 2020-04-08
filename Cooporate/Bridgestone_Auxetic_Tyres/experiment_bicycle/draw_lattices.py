import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from lattice_generator import *


NodePoints, StrutlessMap, StruttedMap = get_preset_info()
NodePos = generate_node_positions(H=17.5, h=5.5, L=11.5)

X0s, Y0s, Z0s = generate_individual_beams(NodePos, StrutlessMap)
X1s, Y1s, Z1s = generate_individual_beams(NodePos, StruttedMap)


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
