import numpy as np
from lattice_generator import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# 1: Set Width, Other Diameter, Inner Diameter
x_layer = 8

outer_diameter = 647
inner_diameter = 423
width = 215

r_outer = outer_diameter / 2
r_inner = inner_diameter / 2
r_depth = r_outer - r_inner
r_mid = 0.5 * (r_outer + r_inner)

thickness = 0.2 * width / x_layer

# 2: Determine number of cells in total
x_dist = width / x_layer
y_layer_ex = r_depth / x_dist
y_dist = r_depth / y_layer_ex
d_dist = y_dist - x_dist

length_width_ratio = 11.5 / (17.5 - 5.5)
H_h_ratio = 17.5 / 5.5
z_dist_ex = 2.0 * (x_dist) / length_width_ratio

perimeter_mid = 2.0 * np.pi * r_mid
z_layer_ex = perimeter_mid / z_dist_ex

y_layer = int(y_layer_ex)
y_dist = x_dist = r_depth / y_layer

z_layer = int(z_layer_ex)
z_dist = perimeter_mid / z_layer
dtheta = 2.0 * np.pi / z_layer
dtheta_d = dtheta / np.pi * 180.0

# 3: Calculate adjustsments
L = x_dist / 2.0
H = z_dist / (2.0 * (1 - 1.0 / H_h_ratio))
h = H - z_dist / 2.0


NodePoints, StrutlessMap, StruttedMap = get_preset_info()
NodePos = generate_node_positions(H=H, h=h, L=L)

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
ax.set_title('No Strut - Ori')


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
ax.set_title('Strutted - Ori')

# %% ==========================================================
# 4: Perform adjustments
Ny = 0
Rshift = r_mid + Ny * y_dist

theta = (NodePos[:, 2] / z_dist) * dtheta
R = (NodePos[:, 1] / y_dist) * y_dist - Rshift

NodePos_adj = np.copy(NodePos)
NodePos_adj[:, 1] = R * np.cos(theta)
NodePos_adj[:, 2] = R * np.sin(theta)

X0s_adj, Y0s_adj, Z0s_adj = generate_individual_beams(NodePos_adj, StrutlessMap)
X1s_adj, Y1s_adj, Z1s_adj = generate_individual_beams(NodePos_adj, StruttedMap)


# %% ----------------------
fig = plt.figure(11, clear=True)

ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(NodePos_adj[:, 0], NodePos_adj[:, 1], NodePos_adj[:, 2], s=20, c='r')

for i in range(X0s.shape[0]):
    ax.plot3D(X0s_adj[i, :], Y0s_adj[i, :], Z0s_adj[i, :], 'blue', linewidth=2)

for i, pos in enumerate(NodePos_adj):
    ax.text(pos[0], pos[1], pos[2], "{}".format(i), color='red', fontsize=6)

for i in range(len(X0s_adj)):
    ax.text(np.mean(X0s_adj[i, :]), np.mean(Y0s_adj[i, :]), np.mean(Z0s_adj[i, :]), "{}".format(i), color='blue', fontsize=6)

# ax.plot3D([0.0], [0.0], [0.0], 'ks')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('No Strut - Adj')
plt.grid()


fig = plt.figure(12, clear=True)

ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(NodePos_adj[:, 0], NodePos_adj[:, 1], NodePos_adj[:, 2], s=20, c='r')

for i in range(X1s_adj.shape[0]):
    ax.plot3D(X1s_adj[i, :], Y1s_adj[i, :], Z1s_adj[i, :], 'blue', linewidth=2)

for i, pos in enumerate(NodePos_adj):
    ax.text(pos[0], pos[1], pos[2], "{}".format(i), color='red', fontsize=6)

for i in range(len(X1s_adj)):
    ax.text(np.mean(X1s_adj[i, :]), np.mean(Y1s_adj[i, :]), np.mean(Z1s_adj[i, :]), "{}".format(i), color='blue', fontsize=6)

# ax.plot3D([0.0], [0.0], [0.0], 'ks')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Strutted - Adj')
plt.grid()


# 5: Abaqus

