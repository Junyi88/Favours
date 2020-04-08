import numpy as np


def get_preset_info():
    NodePoints = np.loadtxt('./ToAbaNodeLoc.csv', dtype=np.int, delimiter=',')
    StrutlessMap = np.loadtxt('./ToAbaNoStrutBeam.csv', dtype=np.int, delimiter=',')
    StruttedMap = np.loadtxt('./ToAbaStrutBeam.csv', dtype=np.int, delimiter=',')

    NodePoints -= 1
    StrutlessMap -= 1
    StruttedMap -= 1
    return NodePoints, StrutlessMap, StruttedMap


def generate_node_positions(H=17.5, h=5.5, L=11.5):
    NodePoints, _, _ = get_preset_info()

    GridX = np.array([-L, -L / 2.0, 0.0, L / 2.0, L])
    GridY = np.array([-L, -L / 2.0, 0.0, L / 2.0, L])
    GridZ = np.array([-(H - h), - H / 2.0, -(H / 2.0 - h),
        (H / 2.0 - h), H / 2.0, (H - h)])


    NodePos = np.zeros([len(NodePoints), 3])

    for i, NodePoint in enumerate(NodePoints):
        NodePos[i, 0] = GridX[NodePoint[0]]
        NodePos[i, 1] = GridY[NodePoint[1]]
        NodePos[i, 2] = GridZ[NodePoint[2]]

    return NodePos


def generate_individual_beams(NodePos, StrutMap):
    nStrut = len(StrutMap)
    Xs = np.zeros([nStrut, 2])
    Ys = np.zeros([nStrut, 2])
    Zs = np.zeros([nStrut, 2])

    for i in range(nStrut):
        for ip in range(2):
            Xs[i, ip] = NodePos[StrutMap[i, ip], 0]
            Ys[i, ip] = NodePos[StrutMap[i, ip], 1]
            Zs[i, ip] = NodePos[StrutMap[i, ip], 2]
    return Xs, Ys, Zs



