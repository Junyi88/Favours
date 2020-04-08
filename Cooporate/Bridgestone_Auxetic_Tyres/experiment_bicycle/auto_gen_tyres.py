import numpy as np
from lattice_generator import *
from wheel_generator import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# %% --------------------------------------
x_layer = 8

outer_diameter = 647
inner_diameter = 423
width = 215

has_additional_struts = False

# %% --------------------
wheel_params = estimate_params_from_x_layer(x_layer, outer_diameter, inner_diameter, width)

NodePoints, StrutlessMap, StruttedMap = get_preset_info()
NodePos_ref = generate_node_positions(H=wheel_params['H'], h=wheel_params['h'], L=wheel_params['L'])
NodePos = adjust_node_pos(NodePos_ref, Ny=0,
    r_mid=wheel_params['r_mid'], y_dist=wheel_params['y_dist'],
    z_dist=wheel_params['z_dist'], dtheta=wheel_params['dtheta'])

if has_additional_struts:
    StrutMap = StruttedMap
else:
    StrutMap = StrutlessMap

Xs, Ys, Zs = generate_individual_beams(NodePos, StrutMap)


fig = plt.figure(1, clear=True)
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(NodePos[:, 0], NodePos[:, 1], NodePos[:, 2], s=20, c='r')

for i in range(Xs.shape[0]):
    ax.plot3D(Xs[i, :], Ys[i, :], Zs[i, :], 'blue', linewidth=2)

for i, pos in enumerate(NodePos):
    ax.text(pos[0], pos[1], pos[2], "{}".format(i), color='red', fontsize=6)

for i in range(len(Xs)):
    ax.text(np.mean(Xs[i, :]), np.mean(Ys[i, :]), np.mean(Zs[i, :]), "{}".format(i), color='blue', fontsize=6)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Strut positions')




