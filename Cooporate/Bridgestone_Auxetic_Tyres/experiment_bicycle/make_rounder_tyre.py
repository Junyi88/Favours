import numpy as np


def slice_vals(ds, NodePos, StrutMap):
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

        if nS == 1:
            NewStruts.append([StrutMap[ist, 0], StrutMap[ist, 1]])
        else:
            for ii in range(1, nS):
                tmp = p1 + dxyz * ii
                NewPoints.append(tmp.tolist())

            NewStruts.append([StrutMap[ist, 0], iPoint])
            # iPoint += 1

            for ii in range(1, nS - 1):
                NewStruts.append([iPoint, iPoint + 1])
                iPoint += 1

            NewStruts.append([iPoint, StrutMap[ist, 1]])
            iPoint += 1      

    OutPoints = NodePos.tolist()
    OutPoints.extend(NewPoints)
    OutPoints = np.array(OutPoints, dtype=np.float)
    NewStruts = np.array(NewStruts, dtype=np.int)

    return OutPoints, NewStruts

