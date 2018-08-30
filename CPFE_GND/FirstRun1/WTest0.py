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
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=( 2.0000e+02 )) 
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0000e+00,0.0000e+00), point2=(5.0000e+00,5.0000e+00)) 
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-1', type= DEFORMABLE_BODY) 
vP=mdb.models['Model-1'].parts['Part-1'] 
vP.BaseSolidExtrude(depth=1.0000e+00, sketch= mdb.models['Model-1'].sketches['__profile__']) 
del mdb.models['Model-1'].sketches['__profile__'] 
 
