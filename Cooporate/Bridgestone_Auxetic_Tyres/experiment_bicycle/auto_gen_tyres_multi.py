import numpy as np
from lattice_generator import *
from wheel_generator import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import os

# %% --------------------------------------
x_layer = 2

outer_diameter = 647
inner_diameter = 423
width = 215

has_additional_struts = True

# %% --------------------
wheel_params = estimate_params_from_x_layer(x_layer, outer_diameter, inner_diameter, width)

NodePoints, StrutlessMap, StruttedMap = get_preset_info()
NodePos_ref = generate_node_positions(H=wheel_params['H'], h=wheel_params['h'], L=wheel_params['L'])

if has_additional_struts:
    StrutMap = StruttedMap
else:
    StrutMap = StrutlessMap

nExtend = int(wheel_params['y_layer'] / 2) + 1

# %%--------------------
out_dir = './ignoreDir/x_{}/'.format(x_layer)
if not os.path.isdir(out_dir):
    os.makedirs(out_dir) 

np.save(os.path.join(out_dir, "StrutlessMap.npy"), StrutlessMap)
np.save(os.path.join(out_dir, "StruttedMap.npy"), StruttedMap)

# %% -----------------------------------
fig = plt.figure(1, clear=True)
ax = fig.add_subplot(111, projection='3d')

NodePos = adjust_node_pos(NodePos_ref, Ny=0,
    r_mid=wheel_params['r_mid'], y_dist=wheel_params['y_dist'],
    z_dist=wheel_params['z_dist'], dtheta=wheel_params['dtheta'])
Xs, Ys, Zs = generate_individual_beams(NodePos, StrutMap)

ax.scatter3D(NodePos[:, 0], NodePos[:, 1], NodePos[:, 2], s=20, c='k')
for i in range(Xs.shape[0]):
    ax.plot3D(Xs[i, :], Ys[i, :], Zs[i, :], 'black', linewidth=2)

out_path = os.path.join(out_dir, "X_0.npy")
np.save(out_path, Xs)
out_path = os.path.join(out_dir, "Y_0.npy")
np.save(out_path, Ys)
out_path = os.path.join(out_dir, "Z_0.npy")
np.save(out_path, Zs)
out_path = os.path.join(out_dir, "NodePos_0.npy")
np.save(out_path, NodePos)

for i_ext in range(1, nExtend):
    NodePos = adjust_node_pos(NodePos_ref, Ny=i_ext,
        r_mid=wheel_params['r_mid'], y_dist=wheel_params['y_dist'],
        z_dist=wheel_params['z_dist'], dtheta=wheel_params['dtheta'])
    Xs, Ys, Zs = generate_individual_beams(NodePos, StrutMap)

    ax.scatter3D(NodePos[:, 0], NodePos[:, 1], NodePos[:, 2], s=20, c='b')
    for i in range(Xs.shape[0]):
        ax.plot3D(Xs[i, :], Ys[i, :], Zs[i, :], 'blue', linewidth=2)

    out_path = os.path.join(out_dir, "X_p{}.npy".format(i_ext))
    np.save(out_path, Xs)
    out_path = os.path.join(out_dir, "Y_p{}.npy".format(i_ext))
    np.save(out_path, Ys)
    out_path = os.path.join(out_dir, "Z_p{}.npy".format(i_ext))
    np.save(out_path, Zs)
    out_path = os.path.join(out_dir, "NodePos_p{}.npy".format(i_ext))
    np.save(out_path, NodePos)


    #
    NodePos = adjust_node_pos(NodePos_ref, Ny=-i_ext,
        r_mid=wheel_params['r_mid'], y_dist=wheel_params['y_dist'],
        z_dist=wheel_params['z_dist'], dtheta=wheel_params['dtheta'])
    Xs, Ys, Zs = generate_individual_beams(NodePos, StrutMap)

    ax.scatter3D(NodePos[:, 0], NodePos[:, 1], NodePos[:, 2], s=20, c='r')
    for i in range(Xs.shape[0]):
        ax.plot3D(Xs[i, :], Ys[i, :], Zs[i, :], 'red', linewidth=2)

    out_path = os.path.join(out_dir, "X_n{}.npy".format(i_ext))
    np.save(out_path, Xs)
    out_path = os.path.join(out_dir, "Y_n{}.npy".format(i_ext))
    np.save(out_path, Ys)
    out_path = os.path.join(out_dir, "Z_n{}.npy".format(i_ext))
    np.save(out_path, Zs)
    out_path = os.path.join(out_dir, "NodePos_n{}.npy".format(i_ext))
    np.save(out_path, NodePos)



# for i, pos in enumerate(NodePos):
#     ax.text(pos[0], pos[1], pos[2], "{}".format(i), color='red', fontsize=6)

# for i in range(len(Xs)):
#     ax.text(np.mean(Xs[i, :]), np.mean(Ys[i, :]), np.mean(Zs[i, :]), "{}".format(i), color='blue', fontsize=6)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Strut positions')




