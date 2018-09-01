from part import * 
from material import * 
from section import * 
from assembly import * 
from step import * 
from interaction import * 
from load import * 
from mesh import * 
from job import * 
from sketch import * 
from visualization import * 
from connectorBehavior import * 
 
# OpenSketch 
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=( 1.0000e+03 )) 
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0000e+00,0.0000e+00), point2=(8.0000e+02,8.0000e+02)) 
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-1', type= DEFORMABLE_BODY) 
vP=mdb.models['Model-1'].parts['Part-1'] 
vP.BaseSolidExtrude(depth=5.0000e+01, sketch= mdb.models['Model-1'].sketches['__profile__']) 
del mdb.models['Model-1'].sketches['__profile__'] 
 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7903e+01, 3.6020e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 9.5425e+01, 3.1267e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.8649e+02, 5.1018e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0743e+02, 1.0647e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.2113e+00, 3.2337e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1804e-01, 3.2774e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6339e+02, 7.9606e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4985e+01, 5.1113e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.9481e+01, 4.6039e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6121e+01, 3.5598e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0526e+02, 3.7225e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 9.6849e+01, 3.7562e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.0518e+02, 4.9975e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6047e+02, 5.0135e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5290e+02, 2.3675e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.0940e+02, 1.7546e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.2008e+02, 1.3300e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.7259e+02, 1.0057e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0436e+02, 4.3490e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.4690e+02, 1.0413e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.4961e+02, 7.5826e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.5345e+02, 8.4543e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.9358e+00, 5.5900e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 9.3540e+01, 5.0426e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2028e+02, 5.1276e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2619e+02, 5.3525e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 9.4821e+01, 5.1388e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 8.5668e+01, 4.5783e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1493e+01, 3.0443e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8261e+02, 4.4034e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.3473e+02, 5.0519e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.2844e+02, 5.5046e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.0959e+01, 3.7013e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.5917e+02, 5.0238e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.0713e+02, 5.0676e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.0220e+02, 5.0652e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.2009e+02, 1.6365e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5478e+02, 2.3666e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.9188e+02, 4.0069e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.6649e+02, 2.7997e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.4632e+02, 8.1731e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.2130e+02, 1.2972e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5011e+02, 1.9411e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1381e+02, 1.1716e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.3480e+02, 9.6915e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.2148e+02, 9.9541e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0424e+02, 1.0928e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6600e+02, 1.1585e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.4146e+01, 3.4876e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9056e+01, 3.5289e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8049e+01, 3.4804e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 8.5872e-01, 1.5445e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4208e+00, 1.3497e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5135e+02, 8.4001e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1036e+02, 1.9496e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5600e+02, 1.3347e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.6237e+02, 1.0348e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 8.2575e+01, 4.9797e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2610e+02, 5.3662e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.2985e+01, 5.1082e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1493e+01, 5.4737e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 8.7605e+01, 4.5839e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4208e+00, 5.5937e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.4867e+01, 3.8185e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0931e+01, 3.6479e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7996e+01, 3.8185e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8280e+02, 4.8991e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0352e+02, 5.6378e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.2123e+02, 5.6657e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1542e+02, 5.5543e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.2019e+01, 3.8068e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.7676e+01, 3.8007e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 9.6957e+01, 3.1358e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3985e+02, 3.6123e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3403e+02, 4.3884e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4048e+01, 3.7813e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.8991e+02, 4.9582e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.8541e+02, 5.2938e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6140e+02, 3.7735e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7246e+02, 3.6142e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3244e+02, 5.1738e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3198e+02, 5.0510e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.5430e+02, 5.1241e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.5195e+02, 4.2102e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.3978e+02, 2.4036e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9328e+02, 5.2381e-01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7565e+02, 4.3115e+00, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.4575e+02, 3.9553e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1851e+02, 1.1935e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1577e+02, 1.4200e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9924e+02, 1.6340e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0781e+02, 1.6487e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6628e+02, 1.4144e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6985e+02, 1.5530e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.5335e+02, 1.5624e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.7859e+01, 3.4305e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9424e+01, 3.3930e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 8.0981e+01, 3.1399e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4485e+01, 3.1043e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9337e+01, 3.0462e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5052e+02, 7.5545e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.4052e+01, 1.3122e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0548e+01, 1.4434e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9442e+02, 8.1543e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0661e+02, 1.6421e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.7736e+02, 1.0947e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5037e+02, 9.1478e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.9228e+02, 1.9551e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0580e+02, 1.5093e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.4240e+02, 1.0732e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4954e+02, 4.6302e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.6005e+02, 6.7484e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.3649e+02, 8.8573e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.7932e+02, 9.1385e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.1174e+02, 9.1947e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0694e+02, 5.5600e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2053e+02, 5.6331e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2775e+02, 5.0829e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1166e+02, 5.4343e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.7982e+01, 5.1335e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6489e+01, 5.4287e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.2329e+01, 5.3940e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 8.4418e+01, 4.5933e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4208e+00, 3.0443e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3268e+00, 3.5851e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0498e+01, 3.0443e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.2535e+02, 2.6441e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.2488e+02, 3.3386e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.0857e+02, 4.6920e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8130e+02, 5.4643e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4635e+02, 5.4737e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1153e+02, 3.6348e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8343e+02, 4.3340e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8043e+02, 5.0538e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.0728e+02, 4.9982e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.8391e+02, 5.0932e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.6589e+02, 5.0366e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.2233e+02, 4.5242e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5184e+02, 3.6085e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.2082e+02, 5.0888e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7949e+02, 5.1522e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6225e+02, 4.9019e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.4688e+02, 4.9594e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.4444e+02, 4.9871e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.4438e+02, 4.9698e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.2851e+02, 4.9544e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.3425e+02, 5.3556e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5946e+02, 5.0388e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.2796e+02, 5.1288e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.5195e+02, 5.2601e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.9019e+02, 5.2057e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6939e+02, 4.2027e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.7192e+02, 1.5380e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.5833e+02, 1.5840e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.7650e+02, 3.9713e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1973e+02, 2.4163e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8974e+02, 2.6825e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6252e+02, 3.3742e+00, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5652e+02, 1.1435e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.2101e+02, 7.8107e+00, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.2832e+02, 2.0620e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0611e+02, 1.3966e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3028e+02, 9.7665e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2494e+02, 1.4500e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7593e+02, 1.4706e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2559e+02, 3.1999e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9993e+02, 1.1003e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8549e+02, 1.5052e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8137e+02, 1.4041e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3450e+02, 1.2053e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.5036e+02, 1.4940e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.3490e+01, 3.4042e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.7445e+01, 2.0464e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2935e+01, 2.8306e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6056e+01, 1.3122e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3253e+02, 7.5545e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3403e+02, 7.6856e+00, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2766e+02, 3.4305e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4141e+02, 6.0611e+00, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.6671e+02, 7.6826e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.6710e+02, 7.8565e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9536e+02, 4.3490e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8730e+02, 4.8353e-01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.6968e+02, 9.4009e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.5535e+02, 9.7477e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.3839e+02, 5.0426e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4710e+02, 8.0606e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.6528e+02, 4.2552e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.2133e+02, 4.6489e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.2684e+02, 8.3043e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6620e+02, 8.0169e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.7033e+02, 8.0419e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.9160e+02, 8.8667e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.0640e+02, 8.8979e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.3939e+02, 4.1334e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.3536e+02, 3.3555e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3591e+02, 5.6606e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0985e+02, 5.4425e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4003e+02, 4.6601e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0554e+02, 4.6133e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2447e+02, 4.6339e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0660e+02, 5.1157e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0953e+02, 5.1191e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.1421e+01, 4.8944e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.3670e+01, 4.5120e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1767e+01, 4.8092e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6309e+01, 5.0257e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3309e+01, 3.5817e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.6472e-01, 3.4989e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.0894e+02, 3.3180e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6320e+02, 2.6525e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.8626e+02, 3.1418e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.5701e+02, 3.2467e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.9676e+02, 3.3386e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.8570e+02, 4.2356e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8645e+02, 4.7548e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1944e+02, 5.0529e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9039e+02, 4.9422e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9080e+02, 4.9838e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.5235e+02, 5.0838e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.5341e+02, 5.6657e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3141e+02, 4.3246e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0414e+02, 3.7431e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.7949e+02, 4.8645e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6263e+02, 5.0219e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.3902e+02, 5.2938e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.3240e+02, 5.1107e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.7379e+02, 5.0882e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.2140e+02, 5.2938e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.1231e+02, 5.1429e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.0574e+02, 5.2984e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0099e+02, 4.8895e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9654e+02, 4.6396e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8287e+02, 4.8458e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9823e+02, 4.0837e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7215e+02, 3.2826e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.4450e+02, 5.2326e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6927e+02, 5.2047e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.5533e+02, 5.4531e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.4942e+02, 5.5937e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.9141e+02, 5.5937e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.7041e+02, 5.5937e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.2628e+02, 5.0847e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.1934e+02, 5.0444e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6733e+02, 5.2741e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.9735e+02, 4.2887e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.2393e+02, 1.8980e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.0350e+02, 2.0929e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.3640e+02, 1.5746e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5543e+02, 2.6338e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.3837e+02, 2.6544e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.2638e+02, 2.4144e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.7548e+02, 2.6253e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.9057e+02, 2.5963e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.1315e+02, 4.1765e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.0692e+02, 3.2833e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.8794e+02, 2.1389e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.1334e+02, 1.8052e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.7343e+02, 2.6638e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3263e+02, 4.6864e+00, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.5250e+02, 3.5617e+00, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6938e+02, 3.5617e+00, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8662e+02, 1.6871e+00, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.4969e+02, 3.0743e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.2664e+02, 3.1680e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2791e+02, 1.5505e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2184e+02, 1.4884e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3206e+02, 1.4444e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4903e+02, 1.5783e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1651e+02, 7.1421e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.7725e+02, 4.6302e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.4519e+02, 8.3230e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.1925e+01, 2.0892e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4144e+02, 1.9511e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6308e+01, 1.5043e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8486e+01, 1.4847e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.4708e+02, 9.4946e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8343e+02, 1.1247e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0002e+02, 1.4425e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9102e+02, 1.5343e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.7837e+02, 1.5840e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1745e+02, 1.3506e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.4753e+02, 1.3938e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8193e+02, 1.6496e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.2711e+02, 1.8940e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1656e+02, 2.0178e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.3817e+02, 1.5821e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4672e+01, 2.1417e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 8.9978e+00, 1.4059e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.5545e+01, 2.4369e+00, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0329e+02, 4.6864e+00, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5090e+02, 4.0303e+00, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1322e+02, 3.3367e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.6612e+01, 2.9608e-01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.1053e+01, 3.1867e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8130e+02, 8.1543e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1345e+02, 1.4959e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9324e+02, 1.1097e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9848e+02, 1.4881e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5918e+02, 6.4860e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5578e+02, 8.2043e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.5385e+02, 2.4847e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1795e+02, 1.7330e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.2938e+02, 1.4528e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.7625e+02, 1.9055e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.6190e+02, 1.8699e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.7128e+02, 9.3540e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.3621e+02, 1.1931e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.8515e+02, 9.1666e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.2769e+02, 1.0395e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.5834e+02, 5.4550e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.5642e+02, 5.3425e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.2346e+02, 9.0541e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5565e+02, 5.2201e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5156e+02, 5.2029e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4772e+02, 5.2863e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 9.7384e+01, 5.4146e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.2423e+01, 4.6433e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.4237e+01, 4.6877e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0339e+01, 5.5440e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.5494e+01, 4.6939e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.7446e+02, 3.4033e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.7258e+02, 3.1961e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6039e+02, 3.3442e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.6687e+02, 4.3827e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5693e+02, 3.3686e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0661e+02, 5.0116e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.2984e+02, 4.3668e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.2544e+02, 4.6500e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.5076e+02, 3.4305e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5337e+02, 4.8139e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.4125e+02, 5.0572e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9330e+02, 5.5543e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0430e+02, 5.5706e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1041e+02, 3.1849e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8746e+02, 4.5739e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5521e+02, 4.5964e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0845e+02, 4.5739e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4341e+02, 4.5045e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2761e+02, 4.0142e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 8.0231e+01, 3.7857e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2810e+02, 3.8066e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3957e+02, 4.1952e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1455e+02, 5.6657e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.4426e+02, 5.1635e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.7275e+02, 5.2872e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1099e+02, 4.4493e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0743e+02, 4.6689e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8062e+02, 3.6460e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.2439e+02, 4.7370e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7049e+02, 4.0556e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8455e+02, 4.1090e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9645e+02, 5.1138e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.1231e+02, 5.5928e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.4568e+02, 5.5384e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.8514e+02, 5.4250e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.7437e+02, 5.3537e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5693e+02, 5.3200e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.7614e+02, 5.1469e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.7008e+02, 5.1582e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6958e+02, 5.4156e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6639e+02, 1.4547e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.0538e+02, 2.4144e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.5139e+02, 2.4444e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.1493e+02, 1.9917e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.3949e+02, 2.6535e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.3284e+02, 2.4407e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6789e+02, 2.4125e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.2430e+02, 3.3723e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.3892e+02, 3.3498e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.3574e+02, 4.2140e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.0266e+02, 4.0715e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.5825e+02, 2.7753e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8524e+02, 2.3479e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4148e+02, 3.4623e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9826e+02, 5.2381e-01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6955e+02, 1.3403e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0262e+02, 1.6485e+00, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.5963e+02, 4.3302e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6638e+02, 3.0555e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3263e+02, 7.6295e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1651e+02, 3.5617e+00, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2691e+02, 1.5006e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6112e+02, 1.4893e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6871e+02, 7.6295e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8652e+02, 7.2545e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9543e+02, 4.3490e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6853e+02, 3.3451e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.2567e+02, 1.6352e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9336e+02, 1.9636e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5352e+02, 2.0751e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.2926e+01, 1.5099e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3151e+02, 9.0541e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.4950e+02, 1.1753e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0395e+02, 2.2617e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4208e+00, 2.0545e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2391e+02, 8.0044e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1172e+02, 1.0998e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 8.6605e+01, 5.4363e+00, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4743e+02, 3.5336e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1847e+02, 1.0498e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.6331e+01, 3.0462e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.3483e+01, 3.1493e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9236e+02, 1.0348e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8889e+02, 1.0676e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8661e+02, 1.0398e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1841e+02, 3.2430e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.6237e+02, 5.2488e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9911e+02, 9.7477e+00, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.3754e+02, 2.4453e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4335e+02, 1.4847e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4879e+02, 1.8202e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.3192e+02, 1.4725e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.8740e+02, 8.1543e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.3229e+02, 1.7752e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.0472e+02, 7.6951e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0127e+02, 7.7419e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.1514e+02, 7.3295e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.3061e+02, 6.7953e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0239e+02, 9.5415e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.7334e+02, 8.2481e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.5629e+02, 8.0419e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1242e+02, 8.1543e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4026e+02, 1.0057e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.5806e+02, 1.4893e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.3884e+02, 7.9013e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.9722e+02, 1.5765e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.9441e+02, 1.6946e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.6535e+02, 9.2416e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3338e+02, 5.3528e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2700e+02, 5.2001e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4256e+02, 5.0529e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.9294e+01, 5.3856e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 8.5827e-01, 4.3499e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4208e+00, 4.7239e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.4982e+00, 4.7239e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1435e+01, 3.5036e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0886e+02, 3.4398e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9386e+02, 3.4192e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.4845e+02, 2.6638e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.8139e+02, 3.3442e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9861e+02, 4.3773e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.6668e+02, 4.8776e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.4700e+02, 4.3881e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.4531e+02, 4.4933e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5377e+02, 4.4112e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1954e+02, 4.7249e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.1391e+02, 4.3012e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.1644e+02, 4.5645e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.4092e+02, 4.2431e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.9434e+02, 5.5037e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0230e+02, 5.5834e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.3537e+02, 4.9638e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.7240e+02, 5.6443e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.6743e+02, 5.1129e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.7934e+02, 5.4718e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2681e+02, 3.6188e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4547e+02, 3.7941e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0589e+02, 3.5601e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.5603e+02, 4.5873e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.8841e+02, 3.2542e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.4998e+02, 3.8194e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.7100e+02, 4.9712e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.3208e+02, 5.2984e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.9947e+02, 5.1232e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.5889e+02, 5.2600e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0434e+02, 5.2629e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8549e+02, 4.9207e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.3489e+02, 3.7679e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1786e+02, 3.7547e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.6535e+02, 4.9263e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9102e+02, 3.6104e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7846e+02, 3.7772e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1436e+02, 5.0829e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7002e+02, 4.6180e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7555e+02, 5.0547e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9486e+02, 5.0529e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6338e+02, 5.2544e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.8183e+02, 5.2613e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.4951e+02, 1.4959e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.5833e+02, 2.7050e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.8495e+02, 2.4107e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.3359e+02, 3.2911e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.4633e+02, 1.6534e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.6837e+02, 2.3544e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.0969e+02, 2.6207e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.5298e+02, 3.2898e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8949e+02, 3.3980e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8606e+02, 3.3770e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.7154e+02, 2.5532e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.9153e+02, 2.8924e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.7034e+02, 2.5344e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0143e+02, 3.1493e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9045e+02, 3.1493e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5971e+02, 3.2617e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9045e+02, 1.3497e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9964e+02, 1.0067e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9345e+02, 1.2147e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4903e+02, 1.4584e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8259e+02, 1.2935e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7265e+02, 1.8840e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6346e+02, 1.8933e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8455e+02, 1.6043e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1867e+02, 1.6474e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0254e+02, 1.6355e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0011e+02, 6.7953e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1643e+02, 3.1493e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8634e+02, 1.8765e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6390e+02, 3.2586e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6693e+02, 3.2177e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7940e+02, 3.2936e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.9106e+01, 2.2064e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 9.2041e+01, 2.2308e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4922e+02, 2.0433e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8592e+01, 1.5124e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9496e+01, 2.0545e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1651e+02, 9.6540e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3434e+02, 1.5895e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3479e+02, 1.3530e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0245e+02, 1.4547e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9936e+02, 1.3356e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.7556e+01, 3.4548e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.8551e+01, 3.0837e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 9.1666e+01, 1.3684e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1935e+02, 3.9741e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8149e+02, 1.4397e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.7830e+02, 4.7426e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.1832e+02, 7.8544e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.6434e+02, 1.4847e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.8234e+02, 1.5146e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.6237e+02, 1.1144e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.4326e+02, 1.4940e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0783e+02, 2.0001e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.8738e+02, 7.9481e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.4128e+02, 1.3056e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0642e+02, 1.1153e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4841e+02, 1.0854e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.3135e+02, 7.9481e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.3154e+02, 4.3302e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.8550e+02, 1.4837e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.1531e+02, 8.5574e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2982e+02, 5.1753e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3307e+02, 5.1740e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6864e+01, 5.0819e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6489e+01, 4.6939e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4208e+00, 3.8241e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.3801e+02, 2.7697e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1640e+02, 4.3771e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.4137e+02, 3.3442e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.7165e+02, 4.7848e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.7615e+02, 4.2440e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.5076e+02, 5.1176e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.6005e+02, 4.8139e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.8600e+02, 5.6293e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5337e+02, 4.7839e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.4750e+02, 4.8076e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0015e+02, 4.7258e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4247e+02, 3.2326e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5746e+02, 4.6289e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0982e+02, 4.1134e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9901e+02, 3.6110e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9270e+02, 3.7266e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0994e+02, 3.7594e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4238e+02, 4.0350e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.7285e+02, 4.5936e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.7587e+02, 4.9737e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.2842e+02, 5.1438e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1924e+02, 5.2657e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8343e+02, 5.2638e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.4989e+02, 4.8710e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0874e+02, 4.5833e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0224e+02, 4.6316e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0837e+02, 3.6048e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.4294e+02, 4.5983e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1145e+02, 4.9938e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.2759e+02, 5.5656e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.3142e+02, 5.6237e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.0640e+02, 2.6094e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.9853e+02, 2.4603e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0080e+02, 2.3891e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1559e+02, 3.7125e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0443e+02, 3.3742e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.6404e+02, 3.8879e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.7428e+02, 2.8456e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0736e+02, 2.7144e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7537e+02, 3.1399e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8165e+02, 1.0367e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1153e+02, 1.4640e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 9.1666e+01, 1.4491e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0067e+02, 1.5127e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6672e+02, 1.6054e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3628e+02, 1.5377e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8746e+02, 1.5996e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8793e+02, 1.4781e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1464e+02, 1.4809e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0161e+02, 1.8868e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1352e+02, 4.0584e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8249e+02, 3.3555e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0151e+02, 3.2336e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3925e+02, 3.3298e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8371e+02, 2.4332e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5793e+02, 3.2514e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0128e+02, 2.4016e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1172e+02, 3.0668e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4959e+02, 2.3394e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3234e+02, 2.3263e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1987e+02, 2.3048e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7696e+02, 2.0001e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7021e+02, 2.0732e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.2583e+02, 2.1411e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 9.4478e+01, 3.1493e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.5545e+01, 1.7434e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.6246e+02, 9.7383e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.6846e+02, 1.3910e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.3247e+02, 8.2387e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0090e+02, 2.2992e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.5887e+02, 1.2250e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.1508e+02, 1.4509e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.1458e+02, 1.4690e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.2733e+02, 1.3391e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.4551e+02, 1.2766e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.7634e+02, 1.1378e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.1486e+02, 1.0207e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1336e+02, 1.0348e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.3379e+02, 1.0985e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.4532e+02, 6.7484e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.7041e+02, 1.4847e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0649e+01, 5.0529e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3271e+00, 4.9960e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6496e+01, 4.3940e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.2338e+02, 2.7341e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.2203e+02, 4.3712e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.7164e+02, 2.7818e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.8813e+02, 3.0368e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.7839e+02, 2.9243e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.7727e+02, 5.0229e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0436e+02, 4.7239e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.3181e+02, 4.5176e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.2029e+02, 5.0229e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.2001e+02, 4.7595e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.2138e+02, 4.6151e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.5749e+02, 4.2693e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.6005e+02, 4.2734e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.5887e+02, 3.4445e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.5887e+02, 5.1241e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.5535e+02, 4.7539e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.8178e+02, 4.5476e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.2626e+02, 4.5758e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.2354e+02, 4.1531e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1801e+02, 3.4698e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1632e+02, 3.3042e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.6132e+02, 5.1729e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9824e+02, 5.0857e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8962e+02, 3.7322e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0499e+02, 3.7604e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.4905e+02, 4.9769e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5755e+02, 4.0631e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9851e+02, 3.2936e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.1757e+02, 5.3856e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.4334e+02, 3.2636e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.4577e+02, 3.3479e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0071e+02, 2.4688e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.8590e+02, 2.5607e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6346e+02, 1.0647e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1472e+02, 1.5634e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 9.7478e+01, 1.4247e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0226e+02, 1.5427e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.7041e+02, 3.2842e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3535e+02, 3.3151e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6402e+02, 2.5982e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1753e+02, 2.9337e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.6482e+01, 1.4547e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9831e+02, 1.4316e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.7060e+02, 1.7255e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1065e+02, 1.8206e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6469e+02, 1.6562e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0104e+02, 8.6511e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.9228e+02, 1.1247e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0127e+02, 4.5552e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.4326e+02, 1.1453e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.6000e+02, 1.1885e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.3146e+02, 1.3338e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.2217e+02, 2.0442e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.3596e+02, 2.0789e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.2636e+02, 4.1428e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.5646e+01, 4.4343e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.6472e+02, 4.2496e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.6650e+02, 4.4758e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.2864e+02, 4.7501e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.4036e+02, 4.8036e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.6005e+02, 2.9693e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.3324e+02, 5.1129e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.6987e+02, 4.7567e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.9734e+02, 4.5739e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3244e+02, 3.4042e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1739e+02, 3.2898e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6825e+02, 4.2759e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8932e+02, 4.5982e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1296e+02, 5.1466e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8906e+02, 4.7539e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8687e+02, 3.5798e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5840e+02, 5.0632e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.5391e+02, 4.2393e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.9994e+02, 5.4193e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.4653e+02, 5.3228e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.2431e+02, 3.2851e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.2590e+02, 2.6141e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.8841e+02, 2.5944e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0333e+02, 2.5494e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.2544e+02, 3.4351e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1126e+02, 3.1680e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6729e+02, 2.3916e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1445e+02, 1.2147e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.4042e+02, 2.1464e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1922e+02, 2.7219e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.8234e+02, 4.3490e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.2827e+02, 1.0853e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.2339e+02, 1.1941e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0633e+02, 1.1547e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0024e+02, 1.5137e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.3080e+02, 2.1511e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1795e+02, 1.1050e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1486e+01, 4.4839e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.3688e+02, 4.2918e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.2402e+02, 4.7248e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.2424e+02, 4.2431e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.9172e+02, 4.2496e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.9977e+02, 5.1279e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.6434e+02, 5.4718e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.4642e+02, 5.2507e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1662e+02, 4.9319e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.3648e+02, 4.8233e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9937e+02, 4.3846e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.1559e+02, 2.4725e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.8035e+02, 2.4838e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.9734e+02, 3.4642e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.7878e+02, 3.4680e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.5325e+02, 3.3161e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8052e+02, 2.5550e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9739e+02, 2.5138e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0994e+02, 2.8109e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3347e+02, 2.6544e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.5475e+02, 1.7462e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.5448e+02, 2.1351e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.6760e+02, 2.1300e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.3575e+02, 4.4736e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.3979e+02, 4.7276e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.3481e+02, 4.8186e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.3850e+02, 4.8370e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.1542e+02, 4.7248e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.8397e+02, 5.1244e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.8253e+02, 4.7558e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.5094e+02, 4.4736e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.1739e+02, 5.1232e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2447e+02, 4.1840e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8165e+02, 3.2223e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.4083e+02, 2.9487e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1341e+02, 9.3540e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1492e+01, 4.4240e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.5085e+02, 4.2421e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0577e+02, 4.2402e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.3380e+02, 3.4389e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.5844e+02, 3.4651e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.1814e+02, 3.4623e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.3451e+02, 4.9629e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9477e+02, 3.5889e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0727e+02, 2.9149e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1314e+02, 2.4932e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4837e+02, 2.6103e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1050e+02, 8.0512e+01, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.1627e+02, 2.2439e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.2152e+02, 2.9515e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.8839e+02, 2.3160e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.8750e+02, 2.3947e+02, 0.0000e+00)) 

#- Create Datums [1]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4641e+02, 1.0254e+02, 0.0000e+00)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7903e+01, 3.6020e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 9.5425e+01, 3.1267e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.8649e+02, 5.1018e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0743e+02, 1.0647e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.2113e+00, 3.2337e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1804e-01, 3.2774e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6339e+02, 7.9606e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4985e+01, 5.1113e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.9481e+01, 4.6039e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6121e+01, 3.5598e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0526e+02, 3.7225e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 9.6849e+01, 3.7562e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.0518e+02, 4.9975e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6047e+02, 5.0135e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5290e+02, 2.3675e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.0940e+02, 1.7546e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.2008e+02, 1.3300e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.7259e+02, 1.0057e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0436e+02, 4.3490e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.4690e+02, 1.0413e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.4961e+02, 7.5826e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.5345e+02, 8.4543e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.9358e+00, 5.5900e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 9.3540e+01, 5.0426e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2028e+02, 5.1276e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2619e+02, 5.3525e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 9.4821e+01, 5.1388e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 8.5668e+01, 4.5783e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1493e+01, 3.0443e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8261e+02, 4.4034e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.3473e+02, 5.0519e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.2844e+02, 5.5046e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.0959e+01, 3.7013e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.5917e+02, 5.0238e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.0713e+02, 5.0676e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.0220e+02, 5.0652e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.2009e+02, 1.6365e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5478e+02, 2.3666e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.9188e+02, 4.0069e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.6649e+02, 2.7997e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.4632e+02, 8.1731e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.2130e+02, 1.2972e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5011e+02, 1.9411e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1381e+02, 1.1716e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.3480e+02, 9.6915e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.2148e+02, 9.9541e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0424e+02, 1.0928e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6600e+02, 1.1585e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.4146e+01, 3.4876e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9056e+01, 3.5289e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8049e+01, 3.4804e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 8.5872e-01, 1.5445e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4208e+00, 1.3497e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5135e+02, 8.4001e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1036e+02, 1.9496e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5600e+02, 1.3347e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.6237e+02, 1.0348e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 8.2575e+01, 4.9797e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2610e+02, 5.3662e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.2985e+01, 5.1082e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1493e+01, 5.4737e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 8.7605e+01, 4.5839e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4208e+00, 5.5937e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.4867e+01, 3.8185e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0931e+01, 3.6479e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7996e+01, 3.8185e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8280e+02, 4.8991e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0352e+02, 5.6378e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.2123e+02, 5.6657e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1542e+02, 5.5543e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.2019e+01, 3.8068e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.7676e+01, 3.8007e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 9.6957e+01, 3.1358e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3985e+02, 3.6123e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3403e+02, 4.3884e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4048e+01, 3.7813e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.8991e+02, 4.9582e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.8541e+02, 5.2938e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6140e+02, 3.7735e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7246e+02, 3.6142e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3244e+02, 5.1738e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3198e+02, 5.0510e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.5430e+02, 5.1241e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.5195e+02, 4.2102e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.3978e+02, 2.4036e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9328e+02, 5.2381e-01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7565e+02, 4.3115e+00, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.4575e+02, 3.9553e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1851e+02, 1.1935e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1577e+02, 1.4200e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9924e+02, 1.6340e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0781e+02, 1.6487e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6628e+02, 1.4144e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6985e+02, 1.5530e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.5335e+02, 1.5624e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.7859e+01, 3.4305e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9424e+01, 3.3930e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 8.0981e+01, 3.1399e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4485e+01, 3.1043e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9337e+01, 3.0462e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5052e+02, 7.5545e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.4052e+01, 1.3122e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0548e+01, 1.4434e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9442e+02, 8.1543e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0661e+02, 1.6421e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.7736e+02, 1.0947e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5037e+02, 9.1478e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.9228e+02, 1.9551e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0580e+02, 1.5093e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.4240e+02, 1.0732e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4954e+02, 4.6302e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.6005e+02, 6.7484e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.3649e+02, 8.8573e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.7932e+02, 9.1385e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.1174e+02, 9.1947e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0694e+02, 5.5600e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2053e+02, 5.6331e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2775e+02, 5.0829e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1166e+02, 5.4343e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.7982e+01, 5.1335e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6489e+01, 5.4287e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.2329e+01, 5.3940e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 8.4418e+01, 4.5933e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4208e+00, 3.0443e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3268e+00, 3.5851e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0498e+01, 3.0443e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.2535e+02, 2.6441e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.2488e+02, 3.3386e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.0857e+02, 4.6920e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8130e+02, 5.4643e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4635e+02, 5.4737e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1153e+02, 3.6348e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8343e+02, 4.3340e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8043e+02, 5.0538e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.0728e+02, 4.9982e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.8391e+02, 5.0932e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.6589e+02, 5.0366e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.2233e+02, 4.5242e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5184e+02, 3.6085e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.2082e+02, 5.0888e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7949e+02, 5.1522e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6225e+02, 4.9019e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.4688e+02, 4.9594e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.4444e+02, 4.9871e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.4438e+02, 4.9698e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.2851e+02, 4.9544e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.3425e+02, 5.3556e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5946e+02, 5.0388e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.2796e+02, 5.1288e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.5195e+02, 5.2601e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.9019e+02, 5.2057e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6939e+02, 4.2027e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.7192e+02, 1.5380e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.5833e+02, 1.5840e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.7650e+02, 3.9713e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1973e+02, 2.4163e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8974e+02, 2.6825e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6252e+02, 3.3742e+00, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5652e+02, 1.1435e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.2101e+02, 7.8107e+00, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.2832e+02, 2.0620e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0611e+02, 1.3966e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3028e+02, 9.7665e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2494e+02, 1.4500e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7593e+02, 1.4706e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2559e+02, 3.1999e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9993e+02, 1.1003e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8549e+02, 1.5052e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8137e+02, 1.4041e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3450e+02, 1.2053e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.5036e+02, 1.4940e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.3490e+01, 3.4042e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.7445e+01, 2.0464e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2935e+01, 2.8306e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6056e+01, 1.3122e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3253e+02, 7.5545e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3403e+02, 7.6856e+00, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2766e+02, 3.4305e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4141e+02, 6.0611e+00, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.6671e+02, 7.6826e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.6710e+02, 7.8565e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9536e+02, 4.3490e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8730e+02, 4.8353e-01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.6968e+02, 9.4009e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.5535e+02, 9.7477e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.3839e+02, 5.0426e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4710e+02, 8.0606e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.6528e+02, 4.2552e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.2133e+02, 4.6489e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.2684e+02, 8.3043e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6620e+02, 8.0169e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.7033e+02, 8.0419e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.9160e+02, 8.8667e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.0640e+02, 8.8979e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.3939e+02, 4.1334e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.3536e+02, 3.3555e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3591e+02, 5.6606e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0985e+02, 5.4425e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4003e+02, 4.6601e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0554e+02, 4.6133e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2447e+02, 4.6339e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0660e+02, 5.1157e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0953e+02, 5.1191e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.1421e+01, 4.8944e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.3670e+01, 4.5120e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1767e+01, 4.8092e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6309e+01, 5.0257e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3309e+01, 3.5817e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.6472e-01, 3.4989e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.0894e+02, 3.3180e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6320e+02, 2.6525e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.8626e+02, 3.1418e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.5701e+02, 3.2467e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.9676e+02, 3.3386e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.8570e+02, 4.2356e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8645e+02, 4.7548e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1944e+02, 5.0529e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9039e+02, 4.9422e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9080e+02, 4.9838e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.5235e+02, 5.0838e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.5341e+02, 5.6657e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3141e+02, 4.3246e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0414e+02, 3.7431e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.7949e+02, 4.8645e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6263e+02, 5.0219e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.3902e+02, 5.2938e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.3240e+02, 5.1107e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.7379e+02, 5.0882e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.2140e+02, 5.2938e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.1231e+02, 5.1429e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.0574e+02, 5.2984e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0099e+02, 4.8895e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9654e+02, 4.6396e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8287e+02, 4.8458e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9823e+02, 4.0837e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7215e+02, 3.2826e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.4450e+02, 5.2326e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6927e+02, 5.2047e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.5533e+02, 5.4531e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.4942e+02, 5.5937e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.9141e+02, 5.5937e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.7041e+02, 5.5937e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.2628e+02, 5.0847e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.1934e+02, 5.0444e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6733e+02, 5.2741e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.9735e+02, 4.2887e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.2393e+02, 1.8980e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.0350e+02, 2.0929e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.3640e+02, 1.5746e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5543e+02, 2.6338e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.3837e+02, 2.6544e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.2638e+02, 2.4144e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.7548e+02, 2.6253e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.9057e+02, 2.5963e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.1315e+02, 4.1765e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.0692e+02, 3.2833e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.8794e+02, 2.1389e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.1334e+02, 1.8052e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.7343e+02, 2.6638e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3263e+02, 4.6864e+00, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.5250e+02, 3.5617e+00, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6938e+02, 3.5617e+00, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8662e+02, 1.6871e+00, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.4969e+02, 3.0743e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.2664e+02, 3.1680e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2791e+02, 1.5505e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2184e+02, 1.4884e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3206e+02, 1.4444e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4903e+02, 1.5783e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1651e+02, 7.1421e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.7725e+02, 4.6302e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.4519e+02, 8.3230e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.1925e+01, 2.0892e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4144e+02, 1.9511e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6308e+01, 1.5043e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8486e+01, 1.4847e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.4708e+02, 9.4946e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8343e+02, 1.1247e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0002e+02, 1.4425e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9102e+02, 1.5343e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.7837e+02, 1.5840e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1745e+02, 1.3506e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.4753e+02, 1.3938e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8193e+02, 1.6496e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.2711e+02, 1.8940e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1656e+02, 2.0178e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.3817e+02, 1.5821e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4672e+01, 2.1417e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 8.9978e+00, 1.4059e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.5545e+01, 2.4369e+00, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0329e+02, 4.6864e+00, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5090e+02, 4.0303e+00, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1322e+02, 3.3367e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.6612e+01, 2.9608e-01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.1053e+01, 3.1867e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8130e+02, 8.1543e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1345e+02, 1.4959e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9324e+02, 1.1097e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9848e+02, 1.4881e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5918e+02, 6.4860e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5578e+02, 8.2043e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.5385e+02, 2.4847e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1795e+02, 1.7330e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.2938e+02, 1.4528e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.7625e+02, 1.9055e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.6190e+02, 1.8699e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.7128e+02, 9.3540e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.3621e+02, 1.1931e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.8515e+02, 9.1666e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.2769e+02, 1.0395e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.5834e+02, 5.4550e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.5642e+02, 5.3425e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.2346e+02, 9.0541e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5565e+02, 5.2201e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5156e+02, 5.2029e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4772e+02, 5.2863e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 9.7384e+01, 5.4146e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.2423e+01, 4.6433e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.4237e+01, 4.6877e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0339e+01, 5.5440e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.5494e+01, 4.6939e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.7446e+02, 3.4033e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.7258e+02, 3.1961e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6039e+02, 3.3442e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.6687e+02, 4.3827e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5693e+02, 3.3686e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0661e+02, 5.0116e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.2984e+02, 4.3668e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.2544e+02, 4.6500e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.5076e+02, 3.4305e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5337e+02, 4.8139e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.4125e+02, 5.0572e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9330e+02, 5.5543e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0430e+02, 5.5706e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1041e+02, 3.1849e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8746e+02, 4.5739e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5521e+02, 4.5964e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0845e+02, 4.5739e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4341e+02, 4.5045e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2761e+02, 4.0142e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 8.0231e+01, 3.7857e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2810e+02, 3.8066e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3957e+02, 4.1952e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1455e+02, 5.6657e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.4426e+02, 5.1635e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.7275e+02, 5.2872e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1099e+02, 4.4493e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0743e+02, 4.6689e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8062e+02, 3.6460e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.2439e+02, 4.7370e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7049e+02, 4.0556e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8455e+02, 4.1090e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9645e+02, 5.1138e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.1231e+02, 5.5928e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.4568e+02, 5.5384e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.8514e+02, 5.4250e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.7437e+02, 5.3537e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5693e+02, 5.3200e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.7614e+02, 5.1469e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.7008e+02, 5.1582e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6958e+02, 5.4156e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6639e+02, 1.4547e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.0538e+02, 2.4144e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.5139e+02, 2.4444e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.1493e+02, 1.9917e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.3949e+02, 2.6535e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.3284e+02, 2.4407e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6789e+02, 2.4125e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.2430e+02, 3.3723e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.3892e+02, 3.3498e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.3574e+02, 4.2140e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.0266e+02, 4.0715e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.5825e+02, 2.7753e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8524e+02, 2.3479e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4148e+02, 3.4623e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9826e+02, 5.2381e-01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6955e+02, 1.3403e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0262e+02, 1.6485e+00, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.5963e+02, 4.3302e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6638e+02, 3.0555e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3263e+02, 7.6295e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1651e+02, 3.5617e+00, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2691e+02, 1.5006e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6112e+02, 1.4893e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6871e+02, 7.6295e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8652e+02, 7.2545e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9543e+02, 4.3490e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6853e+02, 3.3451e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.2567e+02, 1.6352e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9336e+02, 1.9636e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5352e+02, 2.0751e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.2926e+01, 1.5099e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3151e+02, 9.0541e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.4950e+02, 1.1753e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0395e+02, 2.2617e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4208e+00, 2.0545e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2391e+02, 8.0044e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1172e+02, 1.0998e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 8.6605e+01, 5.4363e+00, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4743e+02, 3.5336e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1847e+02, 1.0498e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.6331e+01, 3.0462e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.3483e+01, 3.1493e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9236e+02, 1.0348e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8889e+02, 1.0676e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8661e+02, 1.0398e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1841e+02, 3.2430e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.6237e+02, 5.2488e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9911e+02, 9.7477e+00, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.3754e+02, 2.4453e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4335e+02, 1.4847e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4879e+02, 1.8202e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.3192e+02, 1.4725e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.8740e+02, 8.1543e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.3229e+02, 1.7752e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.0472e+02, 7.6951e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0127e+02, 7.7419e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.1514e+02, 7.3295e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.3061e+02, 6.7953e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0239e+02, 9.5415e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.7334e+02, 8.2481e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.5629e+02, 8.0419e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1242e+02, 8.1543e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4026e+02, 1.0057e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.5806e+02, 1.4893e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.3884e+02, 7.9013e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.9722e+02, 1.5765e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.9441e+02, 1.6946e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.6535e+02, 9.2416e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3338e+02, 5.3528e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2700e+02, 5.2001e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4256e+02, 5.0529e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.9294e+01, 5.3856e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 8.5827e-01, 4.3499e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4208e+00, 4.7239e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.4982e+00, 4.7239e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1435e+01, 3.5036e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0886e+02, 3.4398e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9386e+02, 3.4192e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.4845e+02, 2.6638e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.8139e+02, 3.3442e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.9861e+02, 4.3773e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.6668e+02, 4.8776e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.4700e+02, 4.3881e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.4531e+02, 4.4933e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5377e+02, 4.4112e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1954e+02, 4.7249e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.1391e+02, 4.3012e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.1644e+02, 4.5645e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.4092e+02, 4.2431e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.9434e+02, 5.5037e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0230e+02, 5.5834e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.3537e+02, 4.9638e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.7240e+02, 5.6443e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.6743e+02, 5.1129e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.7934e+02, 5.4718e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2681e+02, 3.6188e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4547e+02, 3.7941e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0589e+02, 3.5601e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.5603e+02, 4.5873e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.8841e+02, 3.2542e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.4998e+02, 3.8194e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.7100e+02, 4.9712e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.3208e+02, 5.2984e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.9947e+02, 5.1232e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.5889e+02, 5.2600e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0434e+02, 5.2629e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8549e+02, 4.9207e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.3489e+02, 3.7679e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1786e+02, 3.7547e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.6535e+02, 4.9263e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9102e+02, 3.6104e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7846e+02, 3.7772e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1436e+02, 5.0829e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7002e+02, 4.6180e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7555e+02, 5.0547e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9486e+02, 5.0529e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6338e+02, 5.2544e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.8183e+02, 5.2613e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.4951e+02, 1.4959e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.5833e+02, 2.7050e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.8495e+02, 2.4107e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.3359e+02, 3.2911e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.4633e+02, 1.6534e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.6837e+02, 2.3544e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.0969e+02, 2.6207e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.5298e+02, 3.2898e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8949e+02, 3.3980e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8606e+02, 3.3770e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.7154e+02, 2.5532e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.9153e+02, 2.8924e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.7034e+02, 2.5344e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0143e+02, 3.1493e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9045e+02, 3.1493e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5971e+02, 3.2617e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9045e+02, 1.3497e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9964e+02, 1.0067e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9345e+02, 1.2147e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4903e+02, 1.4584e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8259e+02, 1.2935e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7265e+02, 1.8840e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6346e+02, 1.8933e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8455e+02, 1.6043e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1867e+02, 1.6474e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0254e+02, 1.6355e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0011e+02, 6.7953e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1643e+02, 3.1493e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8634e+02, 1.8765e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6390e+02, 3.2586e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6693e+02, 3.2177e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7940e+02, 3.2936e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.9106e+01, 2.2064e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 9.2041e+01, 2.2308e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4922e+02, 2.0433e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8592e+01, 1.5124e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9496e+01, 2.0545e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1651e+02, 9.6540e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3434e+02, 1.5895e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3479e+02, 1.3530e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0245e+02, 1.4547e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9936e+02, 1.3356e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.7556e+01, 3.4548e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.8551e+01, 3.0837e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 9.1666e+01, 1.3684e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1935e+02, 3.9741e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.8149e+02, 1.4397e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.7830e+02, 4.7426e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.1832e+02, 7.8544e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.6434e+02, 1.4847e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.8234e+02, 1.5146e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.6237e+02, 1.1144e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.4326e+02, 1.4940e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0783e+02, 2.0001e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.8738e+02, 7.9481e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.4128e+02, 1.3056e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0642e+02, 1.1153e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.4841e+02, 1.0854e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.3135e+02, 7.9481e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.3154e+02, 4.3302e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.8550e+02, 1.4837e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.1531e+02, 8.5574e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2982e+02, 5.1753e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3307e+02, 5.1740e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6864e+01, 5.0819e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.6489e+01, 4.6939e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4208e+00, 3.8241e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.3801e+02, 2.7697e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1640e+02, 4.3771e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.4137e+02, 3.3442e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.7165e+02, 4.7848e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.7615e+02, 4.2440e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.5076e+02, 5.1176e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.6005e+02, 4.8139e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.8600e+02, 5.6293e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.5337e+02, 4.7839e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.4750e+02, 4.8076e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0015e+02, 4.7258e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4247e+02, 3.2326e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5746e+02, 4.6289e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0982e+02, 4.1134e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9901e+02, 3.6110e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9270e+02, 3.7266e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0994e+02, 3.7594e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4238e+02, 4.0350e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.7285e+02, 4.5936e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.7587e+02, 4.9737e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.2842e+02, 5.1438e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1924e+02, 5.2657e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8343e+02, 5.2638e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.4989e+02, 4.8710e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0874e+02, 4.5833e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0224e+02, 4.6316e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0837e+02, 3.6048e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.4294e+02, 4.5983e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1145e+02, 4.9938e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.2759e+02, 5.5656e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.3142e+02, 5.6237e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.0640e+02, 2.6094e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.9853e+02, 2.4603e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0080e+02, 2.3891e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1559e+02, 3.7125e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0443e+02, 3.3742e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.6404e+02, 3.8879e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.7428e+02, 2.8456e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0736e+02, 2.7144e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7537e+02, 3.1399e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8165e+02, 1.0367e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1153e+02, 1.4640e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 9.1666e+01, 1.4491e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0067e+02, 1.5127e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6672e+02, 1.6054e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3628e+02, 1.5377e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8746e+02, 1.5996e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8793e+02, 1.4781e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1464e+02, 1.4809e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0161e+02, 1.8868e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1352e+02, 4.0584e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8249e+02, 3.3555e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0151e+02, 3.2336e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3925e+02, 3.3298e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8371e+02, 2.4332e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5793e+02, 3.2514e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0128e+02, 2.4016e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1172e+02, 3.0668e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4959e+02, 2.3394e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3234e+02, 2.3263e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1987e+02, 2.3048e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7696e+02, 2.0001e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.7021e+02, 2.0732e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.2583e+02, 2.1411e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 9.4478e+01, 3.1493e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.5545e+01, 1.7434e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.6246e+02, 9.7383e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.6846e+02, 1.3910e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.3247e+02, 8.2387e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0090e+02, 2.2992e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.5887e+02, 1.2250e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.1508e+02, 1.4509e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.1458e+02, 1.4690e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.2733e+02, 1.3391e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.4551e+02, 1.2766e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.7634e+02, 1.1378e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.1486e+02, 1.0207e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1336e+02, 1.0348e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.3379e+02, 1.0985e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.4532e+02, 6.7484e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.7041e+02, 1.4847e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0649e+01, 5.0529e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3271e+00, 4.9960e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6496e+01, 4.3940e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.2338e+02, 2.7341e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.2203e+02, 4.3712e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.7164e+02, 2.7818e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.8813e+02, 3.0368e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.7839e+02, 2.9243e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.7727e+02, 5.0229e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.0436e+02, 4.7239e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.3181e+02, 4.5176e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.2029e+02, 5.0229e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.2001e+02, 4.7595e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.2138e+02, 4.6151e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.5749e+02, 4.2693e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.6005e+02, 4.2734e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.5887e+02, 3.4445e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.5887e+02, 5.1241e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.5535e+02, 4.7539e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.8178e+02, 4.5476e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.2626e+02, 4.5758e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.2354e+02, 4.1531e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1801e+02, 3.4698e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1632e+02, 3.3042e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.6132e+02, 5.1729e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9824e+02, 5.0857e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8962e+02, 3.7322e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.0499e+02, 3.7604e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.4905e+02, 4.9769e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5755e+02, 4.0631e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9851e+02, 3.2936e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.1757e+02, 5.3856e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.4334e+02, 3.2636e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.4577e+02, 3.3479e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0071e+02, 2.4688e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.8590e+02, 2.5607e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6346e+02, 1.0647e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1472e+02, 1.5634e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 9.7478e+01, 1.4247e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.0226e+02, 1.5427e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.7041e+02, 3.2842e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3535e+02, 3.3151e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6402e+02, 2.5982e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1753e+02, 2.9337e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.6482e+01, 1.4547e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9831e+02, 1.4316e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.7060e+02, 1.7255e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1065e+02, 1.8206e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6469e+02, 1.6562e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0104e+02, 8.6511e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.9228e+02, 1.1247e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0127e+02, 4.5552e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.4326e+02, 1.1453e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.6000e+02, 1.1885e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.3146e+02, 1.3338e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.2217e+02, 2.0442e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.3596e+02, 2.0789e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.2636e+02, 4.1428e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.5646e+01, 4.4343e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.6472e+02, 4.2496e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.6650e+02, 4.4758e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.2864e+02, 4.7501e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.4036e+02, 4.8036e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.6005e+02, 2.9693e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.3324e+02, 5.1129e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.6987e+02, 4.7567e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.9734e+02, 4.5739e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.3244e+02, 3.4042e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1739e+02, 3.2898e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.6825e+02, 4.2759e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8932e+02, 4.5982e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1296e+02, 5.1466e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8906e+02, 4.7539e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.8687e+02, 3.5798e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.5840e+02, 5.0632e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.5391e+02, 4.2393e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.9994e+02, 5.4193e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.4653e+02, 5.3228e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.2431e+02, 3.2851e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.2590e+02, 2.6141e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.8841e+02, 2.5944e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0333e+02, 2.5494e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.2544e+02, 3.4351e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1126e+02, 3.1680e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.6729e+02, 2.3916e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1445e+02, 1.2147e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.4042e+02, 2.1464e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1922e+02, 2.7219e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.8234e+02, 4.3490e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.2827e+02, 1.0853e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.2339e+02, 1.1941e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0633e+02, 1.1547e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0024e+02, 1.5137e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.3080e+02, 2.1511e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1795e+02, 1.1050e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.1486e+01, 4.4839e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.3688e+02, 4.2918e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.2402e+02, 4.7248e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.2424e+02, 4.2431e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.9172e+02, 4.2496e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.9977e+02, 5.1279e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.6434e+02, 5.4718e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.4642e+02, 5.2507e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1662e+02, 4.9319e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.3648e+02, 4.8233e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9937e+02, 4.3846e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 4.1559e+02, 2.4725e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.8035e+02, 2.4838e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.9734e+02, 3.4642e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.7878e+02, 3.4680e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.5325e+02, 3.3161e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8052e+02, 2.5550e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.9739e+02, 2.5138e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.0994e+02, 2.8109e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.3347e+02, 2.6544e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.5475e+02, 1.7462e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.5448e+02, 2.1351e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.6760e+02, 2.1300e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.3575e+02, 4.4736e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.3979e+02, 4.7276e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.3481e+02, 4.8186e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 5.3850e+02, 4.8370e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.1542e+02, 4.7248e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.8397e+02, 5.1244e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.8253e+02, 4.7558e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.5094e+02, 4.4736e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.1739e+02, 5.1232e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.2447e+02, 4.1840e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.8165e+02, 3.2223e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.4083e+02, 2.9487e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1341e+02, 9.3540e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.1492e+01, 4.4240e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.5085e+02, 4.2421e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0577e+02, 4.2402e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.3380e+02, 3.4389e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.5844e+02, 3.4651e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.1814e+02, 3.4623e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 3.3451e+02, 4.9629e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.9477e+02, 3.5889e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.0727e+02, 2.9149e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 2.1314e+02, 2.4932e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4837e+02, 2.6103e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.1050e+02, 8.0512e+01, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.1627e+02, 2.2439e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 7.2152e+02, 2.9515e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.8839e+02, 2.3160e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 6.8750e+02, 2.3947e+02, 5.0000e+01)) 

#- Create Datums [2]------------------------ 
vP.DatumPointByCoordinate(coords=( 1.4641e+02, 1.0254e+02, 5.0000e+01)) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[87], point2=vP.datums[88], point3=vP.datums[862]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[88], point2=vP.datums[159], point3=vP.datums[863]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[159], point2=vP.datums[293], point3=vP.datums[934]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[293], point2=vP.datums[180], point3=vP.datums[1068]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[180], point2=vP.datums[178], point3=vP.datums[955]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[178], point2=vP.datums[402], point3=vP.datums[953]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[402], point2=vP.datums[399], point3=vP.datums[1177]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[399], point2=vP.datums[292], point3=vP.datums[1174]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[292], point2=vP.datums[400], point3=vP.datums[1067]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[400], point2=vP.datums[291], point3=vP.datums[1175]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[291], point2=vP.datums[295], point3=vP.datums[1066]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[379], point2=vP.datums[383], point3=vP.datums[1154]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[383], point2=vP.datums[161], point3=vP.datums[1158]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[161], point2=vP.datums[261], point3=vP.datums[936]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[261], point2=vP.datums[262], point3=vP.datums[1036]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[262], point2=vP.datums[263], point3=vP.datums[1037]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[263], point2=vP.datums[264], point3=vP.datums[1038]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[264], point2=vP.datums[377], point3=vP.datums[1039]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[180], point2=vP.datums[160], point3=vP.datums[955]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[160], point2=vP.datums[378], point3=vP.datums[935]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[378], point2=vP.datums[497], point3=vP.datums[1153]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[497], point2=vP.datums[163], point3=vP.datums[1272]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[163], point2=vP.datums[90], point3=vP.datums[938]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[90], point2=vP.datums[161], point3=vP.datums[865]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[399], point2=vP.datums[525], point3=vP.datums[1174]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[525], point2=vP.datums[613], point3=vP.datums[1300]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[613], point2=vP.datums[104], point3=vP.datums[1388]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[104], point2=vP.datums[103], point3=vP.datums[879]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[103], point2=vP.datums[176], point3=vP.datums[878]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[176], point2=vP.datums[290], point3=vP.datums[951]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[290], point2=vP.datums[54], point3=vP.datums[1065]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[6], point2=vP.datums[7], point3=vP.datums[781]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[90], point2=vP.datums[162], point3=vP.datums[865]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[162], point2=vP.datums[266], point3=vP.datums[937]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[266], point2=vP.datums[712], point3=vP.datums[1041]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[712], point2=vP.datums[495], point3=vP.datums[1487]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[495], point2=vP.datums[587], point3=vP.datums[1270]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[587], point2=vP.datums[496], point3=vP.datums[1362]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[496], point2=vP.datums[401], point3=vP.datums[1271]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[401], point2=vP.datums[179], point3=vP.datums[1176]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[179], point2=vP.datums[294], point3=vP.datums[954]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[294], point2=vP.datums[612], point3=vP.datums[1069]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[612], point2=vP.datums[404], point3=vP.datums[1387]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[404], point2=vP.datums[403], point3=vP.datums[1179]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[403], point2=vP.datums[296], point3=vP.datums[1178]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[296], point2=vP.datums[101], point3=vP.datums[1071]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[101], point2=vP.datums[175], point3=vP.datums[876]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[175], point2=vP.datums[6], point3=vP.datums[950]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[6], point2=vP.datums[6], point3=vP.datums[781]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[89], point2=vP.datums[265], point3=vP.datums[864]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[265], point2=vP.datums[381], point3=vP.datums[1040]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[381], point2=vP.datums[599], point3=vP.datums[1156]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[599], point2=vP.datums[494], point3=vP.datums[1374]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[494], point2=vP.datums[508], point3=vP.datums[1269]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[508], point2=vP.datums[197], point3=vP.datums[1283]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[197], point2=vP.datums[196], point3=vP.datums[972]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[196], point2=vP.datums[686], point3=vP.datums[971]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[686], point2=vP.datums[598], point3=vP.datums[1461]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[598], point2=vP.datums[388], point3=vP.datums[1373]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[388], point2=vP.datums[272], point3=vP.datums[1163]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[272], point2=vP.datums[380], point3=vP.datums[1047]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[380], point2=vP.datums[89], point3=vP.datums[1155]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[89], point2=vP.datums[89], point3=vP.datums[864]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[184], point2=vP.datums[410], point3=vP.datums[959]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[410], point2=vP.datums[56], point3=vP.datums[1185]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[56], point2=vP.datums[408], point3=vP.datums[831]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[408], point2=vP.datums[526], point3=vP.datums[1183]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[526], point2=vP.datums[540], point3=vP.datums[1301]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[540], point2=vP.datums[112], point3=vP.datums[1315]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[112], point2=vP.datums[189], point3=vP.datums[887]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[189], point2=vP.datums[717], point3=vP.datums[964]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[717], point2=vP.datums[680], point3=vP.datums[1492]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[680], point2=vP.datums[190], point3=vP.datums[1455]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[190], point2=vP.datums[187], point3=vP.datums[965]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[187], point2=vP.datums[313], point3=vP.datums[962]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[313], point2=vP.datums[312], point3=vP.datums[1088]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[526], point3=vP.datums[795]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[113], point2=vP.datums[627], point3=vP.datums[888]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[627], point2=vP.datums[420], point3=vP.datums[1402]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[420], point2=vP.datums[419], point3=vP.datums[1195]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[419], point2=vP.datums[418], point3=vP.datums[1194]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[418], point2=vP.datums[415], point3=vP.datums[1193]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[415], point2=vP.datums[422], point3=vP.datums[1190]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[422], point2=vP.datums[423], point3=vP.datums[1197]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[423], point2=vP.datums[188], point3=vP.datums[1198]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[188], point2=vP.datums[539], point3=vP.datums[963]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[539], point2=vP.datums[424], point3=vP.datums[1314]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[424], point2=vP.datums[105], point3=vP.datums[1199]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[105], point2=vP.datums[297], point3=vP.datums[880]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[297], point2=vP.datums[182], point3=vP.datums[1072]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[182], point2=vP.datums[181], point3=vP.datums[957]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[181], point2=vP.datums[301], point3=vP.datums[956]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[301], point2=vP.datums[409], point3=vP.datums[1076]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[409], point2=vP.datums[528], point3=vP.datums[1184]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[528], point2=vP.datums[183], point3=vP.datums[1303]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[183], point2=vP.datums[20], point3=vP.datums[958]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[20], point2=vP.datums[20], point3=vP.datums[795]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[22], point3=vP.datums[783]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[22], point2=vP.datums[427], point3=vP.datums[797]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[427], point2=vP.datums[191], point3=vP.datums[1202]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[191], point2=vP.datums[542], point3=vP.datums[966]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[542], point2=vP.datums[195], point3=vP.datums[1317]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[195], point2=vP.datums[116], point3=vP.datums[970]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[116], point2=vP.datums[314], point3=vP.datums[891]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[314], point2=vP.datums[114], point3=vP.datums[1089]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[114], point2=vP.datums[23], point3=vP.datums[889]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[23], point2=vP.datums[192], point3=vP.datums[798]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[192], point2=vP.datums[8], point3=vP.datums[967]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[8], point2=vP.datums[8], point3=vP.datums[783]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[42], point2=vP.datums[382], point3=vP.datums[817]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[382], point2=vP.datums[271], point3=vP.datums[1157]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[271], point2=vP.datums[507], point3=vP.datums[1046]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[507], point2=vP.datums[387], point3=vP.datums[1282]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[387], point2=vP.datums[386], point3=vP.datums[1162]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[386], point2=vP.datums[102], point3=vP.datums[1161]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[102], point2=vP.datums[177], point3=vP.datums[877]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[177], point2=vP.datums[398], point3=vP.datums[952]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[398], point2=vP.datums[771], point3=vP.datums[1173]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[771], point2=vP.datums[678], point3=vP.datums[1546]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[678], point2=vP.datums[759], point3=vP.datums[1453]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[759], point2=vP.datums[164], point3=vP.datums[1534]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[164], point2=vP.datums[776], point3=vP.datums[939]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[776], point2=vP.datums[665], point3=vP.datums[1551]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[665], point2=vP.datums[588], point3=vP.datums[1440]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[588], point2=vP.datums[498], point3=vP.datums[1363]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[498], point2=vP.datums[518], point3=vP.datums[1273]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[518], point2=vP.datums[394], point3=vP.datums[1293]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[394], point2=vP.datums[273], point3=vP.datums[1169]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[273], point2=vP.datums[42], point3=vP.datums[1048]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[42], point2=vP.datums[42], point3=vP.datums[817]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[19], point2=vP.datums[407], point3=vP.datums[794]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[407], point2=vP.datums[405], point3=vP.datums[1182]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[405], point2=vP.datums[625], point3=vP.datums[1180]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[625], point2=vP.datums[311], point3=vP.datums[1400]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[311], point2=vP.datums[425], point3=vP.datums[1086]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[425], point2=vP.datums[186], point3=vP.datums[1200]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[186], point2=vP.datums[185], point3=vP.datums[961]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[185], point2=vP.datums[308], point3=vP.datums[960]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[308], point2=vP.datums[310], point3=vP.datums[1083]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[310], point2=vP.datums[421], point3=vP.datums[1085]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[421], point2=vP.datums[624], point3=vP.datums[1196]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[624], point2=vP.datums[718], point3=vP.datums[1399]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[718], point2=vP.datums[681], point3=vP.datums[1493]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[681], point2=vP.datums[682], point3=vP.datums[1456]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[182], point2=vP.datums[302], point3=vP.datums[957]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[302], point2=vP.datums[55], point3=vP.datums[1077]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[55], point2=vP.datums[108], point3=vP.datums[830]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[108], point2=vP.datums[614], point3=vP.datums[883]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[614], point2=vP.datums[19], point3=vP.datums[1389]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[19], point2=vP.datums[19], point3=vP.datums[794]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[618], point2=vP.datums[622], point3=vP.datums[1393]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[622], point2=vP.datums[683], point3=vP.datums[1397]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[683], point2=vP.datums[621], point3=vP.datums[1458]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[621], point2=vP.datums[719], point3=vP.datums[1396]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[719], point2=vP.datums[720], point3=vP.datums[1494]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[720], point2=vP.datums[679], point3=vP.datums[1495]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[679], point2=vP.datums[623], point3=vP.datums[1454]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[623], point2=vP.datums[532], point3=vP.datums[1398]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[532], point2=vP.datums[538], point3=vP.datums[1307]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[538], point2=vP.datums[626], point3=vP.datums[1313]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[626], point2=vP.datums[723], point3=vP.datums[1401]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[723], point2=vP.datums[537], point3=vP.datums[1498]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[537], point2=vP.datums[299], point3=vP.datums[1312]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[299], point2=vP.datums[406], point3=vP.datums[1074]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[406], point2=vP.datums[407], point3=vP.datums[1181]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[185], point2=vP.datums[185], point3=vP.datums[960]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[18], point2=vP.datums[91], point3=vP.datums[793]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[91], point2=vP.datums[280], point3=vP.datums[866]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[280], point2=vP.datums[674], point3=vP.datums[1055]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[674], point2=vP.datums[170], point3=vP.datums[1449]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[170], point2=vP.datums[94], point3=vP.datums[945]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[94], point2=vP.datums[284], point3=vP.datums[869]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[284], point2=vP.datums[520], point3=vP.datums[1059]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[520], point2=vP.datums[283], point3=vP.datums[1295]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[283], point2=vP.datums[522], point3=vP.datums[1058]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[522], point2=vP.datums[501], point3=vP.datums[1297]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[501], point2=vP.datums[499], point3=vP.datums[1276]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[499], point2=vP.datums[714], point3=vP.datums[1274]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[714], point2=vP.datums[171], point3=vP.datums[1489]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[171], point2=vP.datums[395], point3=vP.datums[946]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[395], point2=vP.datums[49], point3=vP.datums[1170]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[49], point2=vP.datums[279], point3=vP.datums[824]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[279], point2=vP.datums[168], point3=vP.datums[1054]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[168], point2=vP.datums[48], point3=vP.datums[943]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[48], point2=vP.datums[45], point3=vP.datums[823]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[45], point2=vP.datums[43], point3=vP.datums[820]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[43], point2=vP.datums[18], point3=vP.datums[818]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[18], point2=vP.datums[18], point3=vP.datums[793]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[21], point2=vP.datums[58], point3=vP.datums[796]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[58], point2=vP.datums[107], point3=vP.datums[833]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[107], point2=vP.datums[299], point3=vP.datums[882]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[621], point2=vP.datums[619], point3=vP.datums[1396]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[619], point2=vP.datums[620], point3=vP.datums[1394]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[620], point2=vP.datums[721], point3=vP.datums[1395]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[721], point2=vP.datums[531], point3=vP.datums[1496]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[531], point2=vP.datums[530], point3=vP.datums[1306]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[530], point2=vP.datums[412], point3=vP.datums[1305]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[412], point2=vP.datums[305], point3=vP.datums[1187]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[305], point2=vP.datums[298], point3=vP.datums[1080]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[298], point2=vP.datums[110], point3=vP.datums[1073]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[110], point2=vP.datums[300], point3=vP.datums[885]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[300], point2=vP.datums[527], point3=vP.datums[1075]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[527], point2=vP.datums[615], point3=vP.datums[1302]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[615], point2=vP.datums[57], point3=vP.datums[1390]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[57], point2=vP.datums[536], point3=vP.datums[832]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[536], point2=vP.datums[309], point3=vP.datums[1311]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[309], point2=vP.datums[111], point3=vP.datums[1084]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[111], point2=vP.datums[21], point3=vP.datums[886]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[21], point2=vP.datums[21], point3=vP.datums[796]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[426], point2=vP.datums[533], point3=vP.datums[1201]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[533], point2=vP.datums[414], point3=vP.datums[1308]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[414], point2=vP.datums[620], point3=vP.datums[1189]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[267], point2=vP.datums[666], point3=vP.datums[1042]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[666], point2=vP.datums[591], point3=vP.datums[1441]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[591], point2=vP.datums[590], point3=vP.datums[1366]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[590], point2=vP.datums[667], point3=vP.datums[1365]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[667], point2=vP.datums[589], point3=vP.datums[1442]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[589], point2=vP.datums[268], point3=vP.datums[1364]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[268], point2=vP.datums[384], point3=vP.datums[1043]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[384], point2=vP.datums[593], point3=vP.datums[1159]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[593], point2=vP.datums[267], point3=vP.datums[1368]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[267], point2=vP.datums[267], point3=vP.datums[1042]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[165], point2=vP.datums[268], point3=vP.datums[940]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[593], point2=vP.datums[270], point3=vP.datums[1368]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[270], point2=vP.datums[592], point3=vP.datums[1045]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[592], point2=vP.datums[504], point3=vP.datums[1367]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[504], point2=vP.datums[594], point3=vP.datums[1279]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[594], point2=vP.datums[668], point3=vP.datums[1369]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[668], point2=vP.datums[596], point3=vP.datums[1443]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[596], point2=vP.datums[521], point3=vP.datums[1371]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[521], point2=vP.datums[595], point3=vP.datums[1296]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[595], point2=vP.datums[166], point3=vP.datums[1370]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[166], point2=vP.datums[385], point3=vP.datums[941]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[385], point2=vP.datums[500], point3=vP.datums[1160]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[500], point2=vP.datums[269], point3=vP.datums[1275]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[269], point2=vP.datums[165], point3=vP.datums[1044]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[165], point2=vP.datums[165], point3=vP.datums[940]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[5], point2=vP.datums[48], point3=vP.datums[780]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[674], point2=vP.datums[169], point3=vP.datums[1449]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[169], point2=vP.datums[95], point3=vP.datums[944]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[95], point2=vP.datums[96], point3=vP.datums[870]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[96], point2=vP.datums[519], point3=vP.datums[871]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[519], point2=vP.datums[505], point3=vP.datums[1294]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[505], point2=vP.datums[506], point3=vP.datums[1280]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[506], point2=vP.datums[594], point3=vP.datums[1281]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[590], point2=vP.datums[673], point3=vP.datums[1365]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[673], point2=vP.datums[277], point3=vP.datums[1448]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[277], point2=vP.datums[393], point3=vP.datums[1052]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[393], point2=vP.datums[516], point3=vP.datums[1168]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[516], point2=vP.datums[276], point3=vP.datums[1291]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[276], point2=vP.datums[53], point3=vP.datums[1051]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[55], point2=vP.datums[616], point3=vP.datums[830]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[616], point2=vP.datums[529], point3=vP.datums[1391]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[529], point2=vP.datums[417], point3=vP.datums[1304]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[417], point2=vP.datums[535], point3=vP.datums[1192]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[535], point2=vP.datums[193], point3=vP.datums[1310]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[193], point2=vP.datums[192], point3=vP.datums[968]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[195], point2=vP.datums[194], point3=vP.datums[970]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[194], point2=vP.datums[115], point3=vP.datums[969]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[115], point2=vP.datums[430], point3=vP.datums[890]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[430], point2=vP.datums[278], point3=vP.datums[1205]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[278], point2=vP.datums[46], point3=vP.datums[1053]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[46], point2=vP.datums[47], point3=vP.datums[821]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[47], point2=vP.datums[5], point3=vP.datums[822]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[5], point2=vP.datums[5], point3=vP.datums[780]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[485], point3=vP.datums[813]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[485], point2=vP.datums[155], point3=vP.datums[1260]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[155], point2=vP.datums[154], point3=vP.datums[930]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[154], point2=vP.datums[363], point3=vP.datums[929]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[363], point2=vP.datums[481], point3=vP.datums[1138]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[481], point2=vP.datums[250], point3=vP.datums[1256]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[250], point2=vP.datums[38], point3=vP.datums[1025]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[38], point2=vP.datums[38], point3=vP.datums[813]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[92], point2=vP.datums[285], point3=vP.datums[867]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[285], point2=vP.datums[675], point3=vP.datums[1060]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[675], point2=vP.datums[744], point3=vP.datums[1450]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[744], point2=vP.datums[677], point3=vP.datums[1519]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[677], point2=vP.datums[282], point3=vP.datums[1452]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[282], point2=vP.datums[281], point3=vP.datums[1057]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[281], point2=vP.datums[92], point3=vP.datums[1056]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[92], point2=vP.datums[92], point3=vP.datums[867]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[503], point3=vP.datums[819]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[503], point2=vP.datums[502], point3=vP.datums[1278]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[502], point2=vP.datums[509], point3=vP.datums[1277]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[509], point2=vP.datums[597], point3=vP.datums[1284]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[597], point2=vP.datums[391], point3=vP.datums[1372]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[391], point2=vP.datums[609], point3=vP.datums[1166]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[609], point2=vP.datums[610], point3=vP.datums[1384]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[610], point2=vP.datums[392], point3=vP.datums[1385]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[392], point2=vP.datums[515], point3=vP.datums[1167]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[515], point2=vP.datums[275], point3=vP.datums[1290]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[275], point2=vP.datums[44], point3=vP.datums[1050]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[44], point2=vP.datums[44], point3=vP.datums[819]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[17], point2=vP.datums[429], point3=vP.datums[792]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[429], point2=vP.datums[428], point3=vP.datums[1204]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[428], point2=vP.datums[541], point3=vP.datums[1203]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[541], point2=vP.datums[628], point3=vP.datums[1316]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[628], point2=vP.datums[172], point3=vP.datums[1403]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[172], point2=vP.datums[288], point3=vP.datums[947]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[288], point2=vP.datums[390], point3=vP.datums[1063]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[390], point2=vP.datums[93], point3=vP.datums[1165]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[93], point2=vP.datums[676], point3=vP.datums[868]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[676], point2=vP.datums[286], point3=vP.datums[1451]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[286], point2=vP.datums[287], point3=vP.datums[1061]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[287], point2=vP.datums[611], point3=vP.datums[1062]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[611], point2=vP.datums[715], point3=vP.datums[1386]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[715], point2=vP.datums[745], point3=vP.datums[1490]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[745], point2=vP.datums[746], point3=vP.datums[1520]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[746], point2=vP.datums[258], point3=vP.datums[1521]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[258], point2=vP.datums[249], point3=vP.datums[1033]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[249], point2=vP.datums[366], point3=vP.datums[1024]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[366], point2=vP.datums[248], point3=vP.datums[1141]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[248], point2=vP.datums[259], point3=vP.datums[1023]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[259], point2=vP.datums[17], point3=vP.datums[1034]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[17], point2=vP.datums[17], point3=vP.datums[792]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[16], point2=vP.datums[86], point3=vP.datums[791]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[86], point2=vP.datums[253], point3=vP.datums[861]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[253], point2=vP.datums[364], point3=vP.datums[1028]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[364], point2=vP.datums[483], point3=vP.datums[1139]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[483], point2=vP.datums[369], point3=vP.datums[1258]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[369], point2=vP.datums[365], point3=vP.datums[1144]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[365], point2=vP.datums[368], point3=vP.datums[1140]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[368], point2=vP.datums[735], point3=vP.datums[1143]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[735], point2=vP.datums[580], point3=vP.datums[1510]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[580], point2=vP.datums[736], point3=vP.datums[1355]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[736], point2=vP.datums[491], point3=vP.datums[1511]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[491], point2=vP.datums[709], point3=vP.datums[1266]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[709], point2=vP.datums[579], point3=vP.datums[1484]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[579], point2=vP.datums[708], point3=vP.datums[1354]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[708], point2=vP.datums[367], point3=vP.datums[1483]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[367], point2=vP.datums[441], point3=vP.datums[1142]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[441], point2=vP.datums[212], point3=vP.datums[1216]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[212], point2=vP.datums[254], point3=vP.datums[987]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[254], point2=vP.datums[255], point3=vP.datums[1029]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[255], point2=vP.datums[487], point3=vP.datums[1030]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[487], point2=vP.datums[128], point3=vP.datums[1262]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[128], point2=vP.datums[252], point3=vP.datums[903]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[252], point2=vP.datums[251], point3=vP.datums[1027]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[251], point2=vP.datums[260], point3=vP.datums[1026]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[260], point2=vP.datums[158], point3=vP.datums[1035]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[158], point2=vP.datums[586], point3=vP.datums[933]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[586], point2=vP.datums[632], point3=vP.datums[1361]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[632], point2=vP.datums[548], point3=vP.datums[1407]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[548], point2=vP.datums[374], point3=vP.datums[1323]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[374], point2=vP.datums[41], point3=vP.datums[1149]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[41], point2=vP.datums[585], point3=vP.datums[816]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[585], point2=vP.datums[492], point3=vP.datums[1360]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[492], point2=vP.datums[768], point3=vP.datums[1267]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[768], point2=vP.datums[773], point3=vP.datums[1543]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[773], point2=vP.datums[758], point3=vP.datums[1548]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[758], point2=vP.datums[692], point3=vP.datums[1533]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[110], point2=vP.datums[106], point3=vP.datums[885]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[106], point2=vP.datums[304], point3=vP.datums[881]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[304], point2=vP.datums[416], point3=vP.datums[1079]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[416], point2=vP.datums[413], point3=vP.datums[1191]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[413], point2=vP.datums[307], point3=vP.datums[1188]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[307], point2=vP.datums[306], point3=vP.datums[1082]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[306], point2=vP.datums[109], point3=vP.datums[1081]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[109], point2=vP.datums[534], point3=vP.datums[884]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[534], point2=vP.datums[684], point3=vP.datums[1309]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[684], point2=vP.datums[685], point3=vP.datums[1459]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[685], point2=vP.datums[722], point3=vP.datums[1460]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[722], point2=vP.datums[772], point3=vP.datums[1497]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[772], point2=vP.datums[617], point3=vP.datums[1547]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[617], point2=vP.datums[774], point3=vP.datums[1392]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[774], point2=vP.datums[775], point3=vP.datums[1549]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[775], point2=vP.datums[663], point3=vP.datums[1550]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[663], point2=vP.datums[710], point3=vP.datums[1438]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[710], point2=vP.datums[664], point3=vP.datums[1485]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[664], point2=vP.datums[493], point3=vP.datums[1439]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[493], point2=vP.datums[303], point3=vP.datums[1268]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[303], point2=vP.datums[411], point3=vP.datums[1078]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[411], point2=vP.datums[157], point3=vP.datums[1186]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[157], point2=vP.datums[581], point3=vP.datums[932]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[581], point2=vP.datums[375], point3=vP.datums[1356]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[375], point2=vP.datums[486], point3=vP.datums[1150]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[486], point2=vP.datums[39], point3=vP.datums[1261]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[39], point2=vP.datums[16], point3=vP.datums[814]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[16], point2=vP.datums[16], point3=vP.datums[791]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[3], point2=vP.datums[99], point3=vP.datums[778]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[99], point2=vP.datums[100], point3=vP.datums[874]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[100], point2=vP.datums[524], point3=vP.datums[875]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[524], point2=vP.datums[30], point3=vP.datums[1299]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[30], point2=vP.datums[127], point3=vP.datums[805]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[127], point2=vP.datums[125], point3=vP.datums[902]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[397], point2=vP.datums[517], point3=vP.datums[1172]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[517], point2=vP.datums[174], point3=vP.datums[1292]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[174], point2=vP.datums[274], point3=vP.datums[949]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[274], point2=vP.datums[289], point3=vP.datums[1049]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[289], point2=vP.datums[513], point3=vP.datums[1064]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[513], point2=vP.datums[514], point3=vP.datums[1288]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[514], point2=vP.datums[396], point3=vP.datums[1289]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[396], point2=vP.datums[608], point3=vP.datums[1171]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[608], point2=vP.datums[607], point3=vP.datums[1383]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[607], point2=vP.datums[606], point3=vP.datums[1382]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[606], point2=vP.datums[713], point3=vP.datums[1381]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[713], point2=vP.datums[602], point3=vP.datums[1488]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[602], point2=vP.datums[604], point3=vP.datums[1377]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[604], point2=vP.datums[769], point3=vP.datums[1379]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[769], point2=vP.datums[741], point3=vP.datums[1544]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[741], point2=vP.datums[740], point3=vP.datums[1516]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[740], point2=vP.datums[671], point3=vP.datums[1515]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[671], point2=vP.datums[770], point3=vP.datums[1446]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[770], point2=vP.datums[743], point3=vP.datums[1545]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[743], point2=vP.datums[716], point3=vP.datums[1518]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[716], point2=vP.datums[742], point3=vP.datums[1491]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[742], point2=vP.datums[672], point3=vP.datums[1517]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[672], point2=vP.datums[605], point3=vP.datums[1447]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[605], point2=vP.datums[74], point3=vP.datums[1380]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[74], point2=vP.datums[3], point3=vP.datums[849]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[3], point2=vP.datums[3], point3=vP.datums[778]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[237], point2=vP.datums[510], point3=vP.datums[1012]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[510], point2=vP.datums[511], point3=vP.datums[1285]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[511], point2=vP.datums[757], point3=vP.datums[1286]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[757], point2=vP.datums[600], point3=vP.datums[1532]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[600], point2=vP.datums[697], point3=vP.datums[1375]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[697], point2=vP.datums[652], point3=vP.datums[1472]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[652], point2=vP.datums[659], point3=vP.datums[1427]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[659], point2=vP.datums[512], point3=vP.datums[1434]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[512], point2=vP.datums[237], point3=vP.datums[1287]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[237], point2=vP.datums[237], point3=vP.datums[1012]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[74], point2=vP.datums[336], point3=vP.datums[849]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[336], point2=vP.datums[167], point3=vP.datums[1111]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[167], point2=vP.datums[559], point3=vP.datums[942]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[559], point2=vP.datums[603], point3=vP.datums[1334]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[603], point2=vP.datums[510], point3=vP.datums[1378]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[697], point2=vP.datums[670], point3=vP.datums[1472]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[670], point2=vP.datums[601], point3=vP.datums[1445]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[601], point2=vP.datums[739], point3=vP.datums[1376]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[739], point2=vP.datums[389], point3=vP.datums[1514]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[389], point2=vP.datums[490], point3=vP.datums[1164]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[490], point2=vP.datums[489], point3=vP.datums[1265]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[489], point2=vP.datums[583], point3=vP.datums[1264]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[583], point2=vP.datums[370], point3=vP.datums[1358]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[370], point2=vP.datums[371], point3=vP.datums[1145]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[371], point2=vP.datums[488], point3=vP.datums[1146]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[488], point2=vP.datums[669], point3=vP.datums[1263]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[669], point2=vP.datums[462], point3=vP.datums[1444]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[462], point2=vP.datums[257], point3=vP.datums[1237]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[257], point2=vP.datums[707], point3=vP.datums[1032]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[707], point2=vP.datums[484], point3=vP.datums[1482]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[484], point2=vP.datums[661], point3=vP.datums[1259]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[661], point2=vP.datums[214], point3=vP.datums[1436]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[214], point2=vP.datums[324], point3=vP.datums[989]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[324], point2=vP.datums[213], point3=vP.datums[1099]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[213], point2=vP.datums[635], point3=vP.datums[988]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[635], point2=vP.datums[636], point3=vP.datums[1410]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[636], point2=vP.datums[634], point3=vP.datums[1411]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[634], point2=vP.datums[482], point3=vP.datums[1409]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[482], point2=vP.datums[441], point3=vP.datums[1257]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[5], point2=vP.datums[5], point3=vP.datums[780]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[484], point2=vP.datums[662], point3=vP.datums[1259]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[662], point2=vP.datums[325], point3=vP.datums[1437]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[325], point2=vP.datums[442], point3=vP.datums[1100]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[442], point2=vP.datums[215], point3=vP.datums[1217]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[215], point2=vP.datums[211], point3=vP.datums[990]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[211], point2=vP.datums[129], point3=vP.datums[986]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[129], point2=vP.datums[550], point3=vP.datums[904]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[550], point2=vP.datums[327], point3=vP.datums[1325]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[327], point2=vP.datums[323], point3=vP.datums[1102]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[323], point2=vP.datums[440], point3=vP.datums[1098]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[440], point2=vP.datums[439], point3=vP.datums[1215]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[439], point2=vP.datums[711], point3=vP.datums[1214]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[711], point2=vP.datums[376], point3=vP.datums[1486]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[376], point2=vP.datums[764], point3=vP.datums[1151]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[764], point2=vP.datums[738], point3=vP.datums[1539]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[738], point2=vP.datums[737], point3=vP.datums[1513]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[737], point2=vP.datums[765], point3=vP.datums[1512]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[765], point2=vP.datums[763], point3=vP.datums[1540]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[763], point2=vP.datums[331], point3=vP.datums[1538]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[331], point2=vP.datums[645], point3=vP.datums[1106]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[41], point2=vP.datums[41], point3=vP.datums[816]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[11], point2=vP.datums[51], point3=vP.datums[786]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[51], point2=vP.datums[50], point3=vP.datums[826]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[50], point2=vP.datums[52], point3=vP.datums[825]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[52], point2=vP.datums[97], point3=vP.datums[827]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[97], point2=vP.datums[98], point3=vP.datums[872]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[98], point2=vP.datums[173], point3=vP.datums[873]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[173], point2=vP.datums[523], point3=vP.datums[948]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[523], point2=vP.datums[438], point3=vP.datums[1298]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[438], point2=vP.datums[210], point3=vP.datums[1213]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[126], point2=vP.datums[209], point3=vP.datums[901]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[209], point2=vP.datums[11], point3=vP.datums[984]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[11], point2=vP.datums[11], point3=vP.datums[786]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[350], point2=vP.datums[702], point3=vP.datums[1125]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[702], point2=vP.datums[767], point3=vP.datums[1477]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[767], point2=vP.datums[574], point3=vP.datums[1542]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[574], point2=vP.datums[582], point3=vP.datums[1349]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[582], point2=vP.datums[471], point3=vP.datums[1357]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[471], point2=vP.datums[656], point3=vP.datums[1246]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[656], point2=vP.datums[655], point3=vP.datums[1431]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[655], point2=vP.datums[350], point3=vP.datums[1430]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[350], point2=vP.datums[350], point3=vP.datums[1125]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[66], point3=vP.datums[777]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[66], point2=vP.datums[34], point3=vP.datums[841]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[34], point2=vP.datums[73], point3=vP.datums[809]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[73], point2=vP.datums[72], point3=vP.datums[848]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[72], point2=vP.datums[77], point3=vP.datums[847]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[77], point2=vP.datums[342], point3=vP.datums[852]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[342], point2=vP.datums[13], point3=vP.datums[1117]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[13], point2=vP.datums[224], point3=vP.datums[788]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[224], point2=vP.datums[12], point3=vP.datums[999]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[12], point2=vP.datums[133], point3=vP.datums[787]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[133], point2=vP.datums[458], point3=vP.datums[908]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[458], point2=vP.datums[75], point3=vP.datums[1233]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[75], point2=vP.datums[140], point3=vP.datums[850]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[140], point2=vP.datums[81], point3=vP.datums[915]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[81], point2=vP.datums[473], point3=vP.datums[856]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[473], point2=vP.datums[562], point3=vP.datums[1248]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[562], point2=vP.datums[460], point3=vP.datums[1337]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[460], point2=vP.datums[651], point3=vP.datums[1235]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[651], point2=vP.datums[696], point3=vP.datums[1426]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[696], point2=vP.datums[601], point3=vP.datums[1471]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[209], point2=vP.datums[2], point3=vP.datums[984]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[2], point3=vP.datums[777]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[562], point2=vP.datums[563], point3=vP.datums[1337]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[563], point2=vP.datums[474], point3=vP.datums[1338]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[474], point2=vP.datums[80], point3=vP.datums[1249]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[80], point2=vP.datums[459], point3=vP.datums[855]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[459], point2=vP.datums[343], point3=vP.datums[1234]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[343], point2=vP.datums[564], point3=vP.datums[1118]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[564], point2=vP.datums[224], point3=vP.datums[1339]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[12], point2=vP.datums[12], point3=vP.datums[787]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[73], point2=vP.datums[65], point3=vP.datums[848]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[65], point2=vP.datums[67], point3=vP.datums[840]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[67], point2=vP.datums[547], point3=vP.datums[842]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[2], point2=vP.datums[2], point3=vP.datums[777]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[31], point2=vP.datums[443], point3=vP.datums[806]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[443], point2=vP.datums[549], point3=vP.datums[1218]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[549], point2=vP.datums[633], point3=vP.datums[1324]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[633], point2=vP.datums[725], point3=vP.datums[1408]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[725], point2=vP.datums[761], point3=vP.datums[1500]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[761], point2=vP.datums[688], point3=vP.datums[1536]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[688], point2=vP.datums[552], point3=vP.datums[1463]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[552], point2=vP.datums[728], point3=vP.datums[1327]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[728], point2=vP.datums[762], point3=vP.datums[1503]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[762], point2=vP.datums[727], point3=vP.datums[1537]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[727], point2=vP.datums[451], point3=vP.datums[1502]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[451], point2=vP.datums[643], point3=vP.datums[1226]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[643], point2=vP.datums[644], point3=vP.datums[1418]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[489], point2=vP.datums[702], point3=vP.datums[1264]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[471], point2=vP.datums[470], point3=vP.datums[1246]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[470], point2=vP.datums[463], point3=vP.datums[1245]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[463], point2=vP.datums[584], point3=vP.datums[1238]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[584], point2=vP.datums[156], point3=vP.datums[1359]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[156], point2=vP.datums[40], point3=vP.datums[931]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[40], point2=vP.datums[373], point3=vP.datums[815]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[373], point2=vP.datums[256], point3=vP.datums[1148]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[256], point2=vP.datums[372], point3=vP.datums[1031]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[372], point2=vP.datums[85], point3=vP.datums[1147]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[85], point2=vP.datums[153], point3=vP.datums[860]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[153], point2=vP.datums[216], point3=vP.datums[928]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[216], point2=vP.datums[247], point3=vP.datums[991]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[247], point2=vP.datums[449], point3=vP.datums[1022]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[449], point2=vP.datums[329], point3=vP.datums[1224]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[329], point2=vP.datums[445], point3=vP.datums[1104]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[445], point2=vP.datums[447], point3=vP.datums[1220]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[447], point2=vP.datums[326], point3=vP.datums[1222]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[326], point2=vP.datums[31], point3=vP.datums[1101]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[31], point2=vP.datums[31], point3=vP.datums[806]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[76], point2=vP.datums[340], point3=vP.datums[851]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[340], point2=vP.datums[338], point3=vP.datums[1115]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[338], point2=vP.datums[560], point3=vP.datums[1113]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[560], point2=vP.datums[476], point3=vP.datums[1335]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[476], point2=vP.datums[337], point3=vP.datums[1251]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[337], point2=vP.datums[339], point3=vP.datums[1112]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[339], point2=vP.datums[649], point3=vP.datums[1114]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[649], point2=vP.datums[575], point3=vP.datums[1424]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[575], point2=vP.datums[461], point3=vP.datums[1350]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[461], point2=vP.datums[566], point3=vP.datums[1236]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[566], point2=vP.datums[699], point3=vP.datums[1341]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[699], point2=vP.datums[234], point3=vP.datums[1474]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[234], point2=vP.datums[573], point3=vP.datums[1009]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[573], point2=vP.datums[572], point3=vP.datums[1348]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[572], point2=vP.datums[139], point3=vP.datums[1347]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[139], point2=vP.datums[348], point3=vP.datums[914]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[348], point2=vP.datums[734], point3=vP.datums[1123]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[734], point2=vP.datums[134], point3=vP.datums[1509]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[134], point2=vP.datums[698], point3=vP.datums[909]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[698], point2=vP.datums[704], point3=vP.datums[1473]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[704], point2=vP.datums[344], point3=vP.datums[1479]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[344], point2=vP.datums[650], point3=vP.datums[1119]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[650], point2=vP.datums[561], point3=vP.datums[1425]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[561], point2=vP.datums[236], point3=vP.datums[1336]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[236], point2=vP.datums[353], point3=vP.datums[1011]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[353], point2=vP.datums[352], point3=vP.datums[1128]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[352], point2=vP.datums[658], point3=vP.datums[1127]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[658], point2=vP.datums[565], point3=vP.datums[1433]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[565], point2=vP.datums[341], point3=vP.datums[1340]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[341], point2=vP.datums[756], point3=vP.datums[1116]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[756], point2=vP.datums[223], point3=vP.datums[1531]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[223], point2=vP.datums[76], point3=vP.datums[998]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[76], point2=vP.datums[76], point3=vP.datums[851]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[10], point2=vP.datums[319], point3=vP.datums[785]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[319], point2=vP.datums[320], point3=vP.datums[1094]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[320], point2=vP.datums[546], point3=vP.datums[1095]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[546], point2=vP.datums[322], point3=vP.datums[1321]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[322], point2=vP.datums[437], point3=vP.datums[1097]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[437], point2=vP.datums[436], point3=vP.datums[1212]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[435], point2=vP.datums[631], point3=vP.datums[1210]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[631], point2=vP.datums[760], point3=vP.datums[1406]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[760], point2=vP.datums[687], point3=vP.datums[1535]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[687], point2=vP.datums[724], point3=vP.datums[1462]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[724], point2=vP.datums[206], point3=vP.datums[1499]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[206], point2=vP.datums[29], point3=vP.datums[981]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[29], point2=vP.datums[124], point3=vP.datums[804]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[124], point2=vP.datums[10], point3=vP.datums[899]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[10], point2=vP.datums[10], point3=vP.datums[785]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[633], point2=vP.datums[747], point3=vP.datums[1408]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[747], point2=vP.datums[754], point3=vP.datums[1522]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[754], point2=vP.datums[689], point3=vP.datums[1529]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[689], point2=vP.datums[648], point3=vP.datums[1464]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[648], point2=vP.datums[695], point3=vP.datums[1423]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[695], point2=vP.datums[642], point3=vP.datums[1470]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[642], point2=vP.datums[330], point3=vP.datums[1417]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[330], point2=vP.datums[726], point3=vP.datums[1105]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[726], point2=vP.datums[751], point3=vP.datums[1501]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[751], point2=vP.datums[558], point3=vP.datums[1526]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[558], point2=vP.datums[753], point3=vP.datums[1333]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[753], point2=vP.datums[694], point3=vP.datums[1528]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[694], point2=vP.datums[647], point3=vP.datums[1469]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[647], point2=vP.datums[748], point3=vP.datums[1422]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[748], point2=vP.datums[448], point3=vP.datums[1523]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[448], point2=vP.datums[638], point3=vP.datums[1223]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[638], point2=vP.datums[217], point3=vP.datums[1413]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[217], point2=vP.datums[551], point3=vP.datums[992]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[551], point2=vP.datums[556], point3=vP.datums[1326]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[556], point2=vP.datums[557], point3=vP.datums[1331]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[557], point2=vP.datums[750], point3=vP.datums[1332]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[750], point2=vP.datums[749], point3=vP.datums[1525]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[749], point2=vP.datums[641], point3=vP.datums[1524]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[641], point2=vP.datums[130], point3=vP.datums[1416]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[130], point2=vP.datums[450], point3=vP.datums[905]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[450], point2=vP.datums[639], point3=vP.datums[1225]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[639], point2=vP.datums[446], point3=vP.datums[1414]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[446], point2=vP.datums[447], point3=vP.datums[1221]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[31], point2=vP.datums[31], point3=vP.datums[806]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[554], point2=vP.datums[691], point3=vP.datums[1329]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[691], point2=vP.datums[690], point3=vP.datums[1466]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[690], point2=vP.datums[726], point3=vP.datums[1465]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[330], point2=vP.datums[330], point3=vP.datums[1105]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[35], point2=vP.datums[138], point3=vP.datums[810]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[138], point2=vP.datums[464], point3=vP.datums[913]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[464], point2=vP.datums[472], point3=vP.datums[1239]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[472], point2=vP.datums[571], point3=vP.datums[1247]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[571], point2=vP.datums[733], point3=vP.datums[1346]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[733], point2=vP.datums[351], point3=vP.datums[1508]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[351], point2=vP.datums[349], point3=vP.datums[1126]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[349], point2=vP.datums[573], point3=vP.datums[1124]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[234], point2=vP.datums[701], point3=vP.datums[1009]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[701], point2=vP.datums[235], point3=vP.datums[1476]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[235], point2=vP.datums[469], point3=vP.datums[1010]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[469], point2=vP.datums[233], point3=vP.datums[1244]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[233], point2=vP.datums[732], point3=vP.datums[1008]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[732], point2=vP.datums[766], point3=vP.datums[1507]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[766], point2=vP.datums[657], point3=vP.datums[1541]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[657], point2=vP.datums[35], point3=vP.datums[1432]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[35], point2=vP.datums[35], point3=vP.datums[810]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[36], point2=vP.datums[244], point3=vP.datums[811]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[244], point2=vP.datums[333], point3=vP.datums[1019]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[333], point2=vP.datums[149], point3=vP.datums[1108]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[149], point2=vP.datums[637], point3=vP.datums[924]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[637], point2=vP.datums[220], point3=vP.datums[1412]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[220], point2=vP.datums[219], point3=vP.datums[995]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[219], point2=vP.datums[68], point3=vP.datums[994]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[68], point2=vP.datums[444], point3=vP.datums[843]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[444], point2=vP.datums[332], point3=vP.datums[1219]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[332], point2=vP.datums[557], point3=vP.datums[1107]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[750], point2=vP.datums[454], point3=vP.datums[1525]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[454], point2=vP.datums[640], point3=vP.datums[1229]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[640], point2=vP.datums[36], point3=vP.datums[1415]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[36], point2=vP.datums[36], point3=vP.datums[811]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[320], point2=vP.datums[207], point3=vP.datums[1095]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[207], point2=vP.datums[205], point3=vP.datums[982]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[205], point2=vP.datums[59], point3=vP.datums[980]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[59], point2=vP.datums[25], point3=vP.datums[834]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[25], point2=vP.datums[203], point3=vP.datums[800]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[203], point2=vP.datums[204], point3=vP.datums[978]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[204], point2=vP.datums[26], point3=vP.datums[979]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[119], point3=vP.datums[801]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[119], point2=vP.datums[433], point3=vP.datums[894]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[433], point2=vP.datums[703], point3=vP.datums[1208]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[703], point2=vP.datums[477], point3=vP.datums[1478]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[477], point2=vP.datums[478], point3=vP.datums[1252]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[478], point2=vP.datums[576], point3=vP.datums[1253]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[576], point2=vP.datums[147], point3=vP.datums[1351]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[147], point2=vP.datums[146], point3=vP.datums[922]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[146], point2=vP.datums[144], point3=vP.datums[921]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[144], point2=vP.datums[143], point3=vP.datums[919]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[143], point2=vP.datums[225], point3=vP.datums[918]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[225], point2=vP.datums[235], point3=vP.datums[1000]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[560], point2=vP.datums[200], point3=vP.datums[1335]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[200], point2=vP.datums[202], point3=vP.datums[975]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[202], point2=vP.datums[201], point3=vP.datums[977]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[201], point2=vP.datums[63], point3=vP.datums[976]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[63], point2=vP.datums[29], point3=vP.datums[838]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[10], point2=vP.datums[10], point3=vP.datums[785]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[9], point2=vP.datums[121], point3=vP.datums[784]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[121], point2=vP.datums[28], point3=vP.datums[896]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[28], point2=vP.datums[203], point3=vP.datums[803]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[630], point2=vP.datums[208], point3=vP.datums[1405]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[208], point2=vP.datums[629], point3=vP.datums[983]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[629], point2=vP.datums[545], point3=vP.datums[1404]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[545], point2=vP.datums[61], point3=vP.datums[1320]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[61], point2=vP.datums[9], point3=vP.datums[836]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[9], point2=vP.datums[9], point3=vP.datums[784]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[78], point3=vP.datums[789]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[78], point2=vP.datums[567], point3=vP.datums[853]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[567], point2=vP.datums[464], point3=vP.datums[1342]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[138], point2=vP.datums[229], point3=vP.datums[913]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[229], point2=vP.datums[137], point3=vP.datums[1004]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[137], point2=vP.datums[466], point3=vP.datums[912]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[466], point2=vP.datums[231], point3=vP.datums[1241]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[231], point2=vP.datums[150], point3=vP.datums[1006]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[150], point2=vP.datums[228], point3=vP.datums[925]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[228], point2=vP.datums[245], point3=vP.datums[1003]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[245], point2=vP.datums[136], point3=vP.datums[1020]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[136], point2=vP.datums[14], point3=vP.datums[911]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[14], point2=vP.datums[14], point3=vP.datums[789]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[4], point2=vP.datums[37], point3=vP.datums[779]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[37], point2=vP.datums[36], point3=vP.datums[812]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[228], point2=vP.datums[84], point3=vP.datums[1003]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[84], point2=vP.datums[361], point3=vP.datums[859]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[361], point2=vP.datums[360], point3=vP.datums[1136]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[360], point2=vP.datums[4], point3=vP.datums[1135]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[4], point2=vP.datums[4], point3=vP.datums[779]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[221], point3=vP.datums[807]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[221], point2=vP.datums[456], point3=vP.datums[996]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[456], point2=vP.datums[752], point3=vP.datums[1231]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[752], point2=vP.datums[729], point3=vP.datums[1527]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[729], point2=vP.datums[755], point3=vP.datums[1504]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[755], point2=vP.datums[693], point3=vP.datums[1530]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[693], point2=vP.datums[553], point3=vP.datums[1468]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[553], point2=vP.datums[646], point3=vP.datums[1328]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[220], point2=vP.datums[328], point3=vP.datums[995]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[328], point2=vP.datums[218], point3=vP.datums[1103]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[218], point2=vP.datums[32], point3=vP.datums[993]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[32], point2=vP.datums[32], point3=vP.datums[807]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[15], point2=vP.datums[145], point3=vP.datums[790]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[145], point2=vP.datums[146], point3=vP.datums[920]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[229], point2=vP.datums[653], point3=vP.datums[1004]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[653], point2=vP.datums[346], point3=vP.datums[1428]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[346], point2=vP.datums[568], point3=vP.datums[1121]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[568], point2=vP.datums[700], point3=vP.datums[1343]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[700], point2=vP.datums[654], point3=vP.datums[1475]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[654], point2=vP.datums[135], point3=vP.datums[1429]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[135], point2=vP.datums[226], point3=vP.datums[910]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[226], point2=vP.datums[15], point3=vP.datums[1001]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[15], point2=vP.datums[15], point3=vP.datums[790]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[145], point2=vP.datums[83], point3=vP.datums[920]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[83], point2=vP.datums[141], point3=vP.datums[858]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[141], point2=vP.datums[475], point3=vP.datums[916]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[475], point2=vP.datums[354], point3=vP.datums[1250]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[354], point2=vP.datums[142], point3=vP.datums[1129]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[142], point2=vP.datums[239], point3=vP.datums[917]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[239], point2=vP.datums[315], point3=vP.datums[1014]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[315], point2=vP.datums[316], point3=vP.datums[1090]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[316], point2=vP.datums[544], point3=vP.datums[1091]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[544], point2=vP.datums[543], point3=vP.datums[1319]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[543], point2=vP.datums[26], point3=vP.datums[1318]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[26], point2=vP.datums[26], point3=vP.datums[801]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[141], point2=vP.datums[82], point3=vP.datums[916]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[82], point2=vP.datums[238], point3=vP.datums[857]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[238], point2=vP.datums[479], point3=vP.datums[1013]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[479], point2=vP.datums[570], point3=vP.datums[1254]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[570], point2=vP.datums[468], point3=vP.datums[1345]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[468], point2=vP.datums[569], point3=vP.datums[1243]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[569], point2=vP.datums[465], point3=vP.datums[1344]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[465], point2=vP.datums[731], point3=vP.datums[1240]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[731], point2=vP.datums[467], point3=vP.datums[1506]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[467], point2=vP.datums[347], point3=vP.datums[1242]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[347], point2=vP.datums[79], point3=vP.datums[1122]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[79], point2=vP.datums[232], point3=vP.datums[854]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[232], point2=vP.datums[230], point3=vP.datums[1007]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[230], point2=vP.datums[227], point3=vP.datums[1005]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[227], point2=vP.datums[151], point3=vP.datums[1002]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[151], point2=vP.datums[246], point3=vP.datums[926]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[246], point2=vP.datums[480], point3=vP.datums[1021]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[480], point2=vP.datums[152], point3=vP.datums[1255]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[152], point2=vP.datums[360], point3=vP.datums[927]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[15], point2=vP.datums[15], point3=vP.datums[790]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[27], point2=vP.datums[432], point3=vP.datums[802]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[432], point2=vP.datums[543], point3=vP.datums[1207]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[315], point2=vP.datums[317], point3=vP.datums[1090]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[317], point2=vP.datums[431], point3=vP.datums[1092]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[431], point2=vP.datums[60], point3=vP.datums[1206]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[60], point2=vP.datums[27], point3=vP.datums[835]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[27], point2=vP.datums[27], point3=vP.datums[802]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[60], point2=vP.datums[120], point3=vP.datums[835]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[120], point2=vP.datums[199], point3=vP.datums[895]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[199], point2=vP.datums[318], point3=vP.datums[974]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[318], point2=vP.datums[434], point3=vP.datums[1093]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[434], point2=vP.datums[123], point3=vP.datums[1209]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[123], point2=vP.datums[122], point3=vP.datums[898]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[122], point2=vP.datums[62], point3=vP.datums[897]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[62], point2=vP.datums[321], point3=vP.datums[837]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[321], point2=vP.datums[24], point3=vP.datums[1096]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[24], point2=vP.datums[64], point3=vP.datums[799]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[9], point2=vP.datums[9], point3=vP.datums[784]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[199], point2=vP.datums[117], point3=vP.datums[974]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[117], point2=vP.datums[118], point3=vP.datums[892]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[118], point2=vP.datums[198], point3=vP.datums[893]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[70], point2=vP.datums[69], point3=vP.datums[845]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[69], point2=vP.datums[335], point3=vP.datums[844]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[335], point2=vP.datums[334], point3=vP.datums[1110]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[334], point2=vP.datums[131], point3=vP.datums[1109]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[131], point2=vP.datums[358], point3=vP.datums[906]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[358], point2=vP.datums[359], point3=vP.datums[1133]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[359], point2=vP.datums[706], point3=vP.datums[1134]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[706], point2=vP.datums[148], point3=vP.datums[1481]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[148], point2=vP.datums[660], point3=vP.datums[923]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[660], point2=vP.datums[705], point3=vP.datums[1435]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[705], point2=vP.datums[357], point3=vP.datums[1480]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[357], point2=vP.datums[362], point3=vP.datums[1132]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[362], point2=vP.datums[240], point3=vP.datums[1137]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[240], point2=vP.datums[356], point3=vP.datums[1015]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[356], point2=vP.datums[577], point3=vP.datums[1131]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[577], point2=vP.datums[355], point3=vP.datums[1352]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[355], point2=vP.datums[242], point3=vP.datums[1130]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[242], point2=vP.datums[243], point3=vP.datums[1017]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[243], point2=vP.datums[241], point3=vP.datums[1018]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[241], point2=vP.datums[578], point3=vP.datums[1016]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[578], point2=vP.datums[345], point3=vP.datums[1353]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[222], point2=vP.datums[455], point3=vP.datums[997]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[455], point2=vP.datums[555], point3=vP.datums[1230]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[555], point2=vP.datums[453], point3=vP.datums[1330]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[453], point2=vP.datums[452], point3=vP.datums[1228]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[452], point2=vP.datums[457], point3=vP.datums[1227]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[457], point2=vP.datums[730], point3=vP.datums[1232]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[730], point2=vP.datums[132], point3=vP.datums[1505]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[132], point2=vP.datums[33], point3=vP.datums[907]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[33], point2=vP.datums[71], point3=vP.datums[808]) 

#- Create Datum Plane ------------------------ 
vP.DatumPlaneByThreePoints( point1=vP.datums[71], point2=vP.datums[335], point3=vP.datums[846]) 
