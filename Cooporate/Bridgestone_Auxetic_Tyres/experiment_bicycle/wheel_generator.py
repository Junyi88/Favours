import numpy as np

def estimate_params_from_x_layer(x_layer, outer_diameter, inner_diameter, width, length_width_ratio=None, H_h_ratio=None):
    r_outer = outer_diameter / 2
    r_inner = inner_diameter / 2 
    r_depth = r_outer - r_inner
    r_mid = 0.5 * (r_outer + r_inner)

    x_dist = width 
    x_dist = width / x_layer
    y_layer_ex = r_depth / x_dist
    y_dist = r_depth / y_layer_ex
    # d_dist = y_dist - x_dist

    if length_width_ratio is None:
        length_width_ratio = 11.5 / (17.5 - 5.5)
    if H_h_ratio is None:
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

    outputs = {
        'L': L, 'H': H, 'h': h,
        'x_layer': x_layer,
        'y_layer': y_layer,
        'z_layer': z_layer,
        'r_outer': r_outer,
        'r_inner': r_inner,
        'r_depth': r_depth,
        'r_mid': r_mid,
        'x_dist': x_dist,
        'y_dist': y_dist,
        'z_dist': z_dist,
        'dtheta': dtheta,
        'dtheta_d': dtheta_d,
        'perimeter_mid': perimeter_mid
    }

    return outputs

def adjust_node_pos(NodePos, r_mid, y_dist, z_dist, dtheta, Ny=0, **kwargs):
    NodePos_adj = np.copy(NodePos)

    Rshift = r_mid + Ny * y_dist
    theta = (NodePos[:, 2] / z_dist) * dtheta
    R = (NodePos[:, 1] / y_dist) * y_dist - Rshift

    NodePos_adj[:, 1] = R * np.cos(theta)
    NodePos_adj[:, 2] = R * np.sin(theta)

    return NodePos_adj
