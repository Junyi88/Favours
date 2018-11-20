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
from regionToolset import * 
import regionToolset 
import mesh 
 
# Completed Preamble 

 
# Make Parts ------------------ 

 
# Generating Grain 5 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((1.1731e+02, 2.9420e+01, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-5', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-5'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-5', material='Material-5', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-5'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-5') 
p.SectionAssignment(region=region, sectionName='Section-5', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 6 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((2.9545e+02, 3.9355e+01, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-6', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-6'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-6', material='Material-6', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-6'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-6') 
p.SectionAssignment(region=region, sectionName='Section-6', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 7 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((6.6738e+02, 3.4796e+01, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-7', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-7'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-7', material='Material-7', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-7'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-7') 
p.SectionAssignment(region=region, sectionName='Section-7', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 8 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((6.5114e+02, 6.5157e+01, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-8', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-8'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-8', material='Material-8', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-8'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-8') 
p.SectionAssignment(region=region, sectionName='Section-8', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 9 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((4.3726e+02, 8.6622e+01, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-9', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-9'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-9', material='Material-9', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-9'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-9') 
p.SectionAssignment(region=region, sectionName='Section-9', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 10 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((1.7436e+02, 8.8258e+01, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-10', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-10'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-10', material='Material-10', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-10'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-10') 
p.SectionAssignment(region=region, sectionName='Section-10', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 11 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((6.5256e+02, 9.1973e+01, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-11', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-11'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-11', material='Material-11', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-11'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-11') 
p.SectionAssignment(region=region, sectionName='Section-11', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 12 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((6.6936e+02, 1.1146e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-12', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-12'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-12', material='Material-12', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-12'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-12') 
p.SectionAssignment(region=region, sectionName='Section-12', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 13 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((2.6099e+02, 1.3030e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-13', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-13'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-13', material='Material-13', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-13'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-13') 
p.SectionAssignment(region=region, sectionName='Section-13', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 14 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((6.2863e+02, 1.2922e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-14', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-14'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-14', material='Material-14', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-14'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-14') 
p.SectionAssignment(region=region, sectionName='Section-14', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 16 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((1.1614e+02, 1.5212e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-16', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-16'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-16', material='Material-16', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-16'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-16') 
p.SectionAssignment(region=region, sectionName='Section-16', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 17 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((1.7026e+02, 1.5306e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-17', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-17'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-17', material='Material-17', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-17'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-17') 
p.SectionAssignment(region=region, sectionName='Section-17', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 18 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((2.8665e+02, 8.6384e+01, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-18', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-18'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-18', material='Material-18', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-18'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-18') 
p.SectionAssignment(region=region, sectionName='Section-18', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 19 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((4.5182e+02, 1.5849e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-19', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-19'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-19', material='Material-19', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-19'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-19') 
p.SectionAssignment(region=region, sectionName='Section-19', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 20 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((2.7955e+02, 1.6696e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-20', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-20'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-20', material='Material-20', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-20'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-20') 
p.SectionAssignment(region=region, sectionName='Section-20', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 21 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((1.7142e+02, 1.9836e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-21', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-21'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-21', material='Material-21', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-21'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-21') 
p.SectionAssignment(region=region, sectionName='Section-21', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 22 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((3.6632e+02, 1.8602e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-22', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-22'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-22', material='Material-22', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-22'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-22') 
p.SectionAssignment(region=region, sectionName='Section-22', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 23 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((6.0900e+02, 2.3187e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-23', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-23'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-23', material='Material-23', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-23'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-23') 
p.SectionAssignment(region=region, sectionName='Section-23', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 24 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((9.8008e+01, 2.5889e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-24', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-24'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-24', material='Material-24', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-24'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-24') 
p.SectionAssignment(region=region, sectionName='Section-24', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 25 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((1.9038e+02, 3.2815e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-25', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-25'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-25', material='Material-25', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-25'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-25') 
p.SectionAssignment(region=region, sectionName='Section-25', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 26 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((3.7003e+02, 2.1241e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-26', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-26'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-26', material='Material-26', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-26'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-26') 
p.SectionAssignment(region=region, sectionName='Section-26', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 27 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((5.7859e+02, 3.0959e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-27', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-27'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-27', material='Material-27', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-27'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-27') 
p.SectionAssignment(region=region, sectionName='Section-27', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 28 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((3.5969e+01, 3.5076e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-28', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-28'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-28', material='Material-28', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-28'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-28') 
p.SectionAssignment(region=region, sectionName='Section-28', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 29 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((3.0105e+02, 3.6969e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-29', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-29'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-29', material='Material-29', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-29'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-29') 
p.SectionAssignment(region=region, sectionName='Section-29', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 30 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((9.9775e+01, 3.4520e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-30', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-30'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-30', material='Material-30', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-30'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-30') 
p.SectionAssignment(region=region, sectionName='Section-30', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 31 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((1.5318e+02, 3.7150e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-31', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-31'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-31', material='Material-31', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-31'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-31') 
p.SectionAssignment(region=region, sectionName='Section-31', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 32 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((2.5019e+01, 3.7356e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-32', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-32'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-32', material='Material-32', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-32'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-32') 
p.SectionAssignment(region=region, sectionName='Section-32', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 33 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((5.2454e+02, 3.8023e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-33', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-33'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-33', material='Material-33', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-33'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-33') 
p.SectionAssignment(region=region, sectionName='Section-33', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 34 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((2.1906e+02, 4.3820e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-34', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-34'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-34', material='Material-34', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-34'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-34') 
p.SectionAssignment(region=region, sectionName='Section-34', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 35 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((4.1661e+01, 4.5688e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-35', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-35'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-35', material='Material-35', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-35'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-35') 
p.SectionAssignment(region=region, sectionName='Section-35', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 36 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((6.1457e+02, 4.6400e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-36', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-36'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-36', material='Material-36', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-36'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-36') 
p.SectionAssignment(region=region, sectionName='Section-36', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 37 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((6.8585e+02, 4.4677e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-37', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-37'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-37', material='Material-37', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-37'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-37') 
p.SectionAssignment(region=region, sectionName='Section-37', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 38 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((3.2764e+02, 4.8878e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-38', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-38'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-38', material='Material-38', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-38'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-38') 
p.SectionAssignment(region=region, sectionName='Section-38', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 39 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((5.5295e+02, 4.9916e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-39', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-39'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-39', material='Material-39', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-39'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-39') 
p.SectionAssignment(region=region, sectionName='Section-39', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 40 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((1.7460e+02, 4.8184e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-40', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-40'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-40', material='Material-40', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-40'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-40') 
p.SectionAssignment(region=region, sectionName='Section-40', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 41 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((5.4379e+01, 4.9742e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-41', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-41'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-41', material='Material-41', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-41'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-41') 
p.SectionAssignment(region=region, sectionName='Section-41', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 42 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((4.0148e+02, 5.0737e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-42', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-42'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-42', material='Material-42', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-42'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-42') 
p.SectionAssignment(region=region, sectionName='Section-42', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 43 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((2.7777e+02, 4.2761e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-43', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-43'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-43', material='Material-43', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-43'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-43') 
p.SectionAssignment(region=region, sectionName='Section-43', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 44 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((6.5114e+02, 4.9253e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-44', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-44'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-44', material='Material-44', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-44'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-44') 
p.SectionAssignment(region=region, sectionName='Section-44', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 45 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((3.1186e+02, 5.0391e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-45', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-45'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-45', material='Material-45', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-45'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-45') 
p.SectionAssignment(region=region, sectionName='Section-45', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 46 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((1.8383e+02, 5.1051e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-46', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-46'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-46', material='Material-46', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-46'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-46') 
p.SectionAssignment(region=region, sectionName='Section-46', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 47 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((3.5787e+02, 5.1875e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-47', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-47'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-47', material='Material-47', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-47'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-47') 
p.SectionAssignment(region=region, sectionName='Section-47', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 48 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((1.4075e+02, 5.2356e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-48', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-48'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-48', material='Material-48', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-48'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-48') 
p.SectionAssignment(region=region, sectionName='Section-48', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 49 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((6.2611e+01, 5.1914e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-49', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-49'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-49', material='Material-49', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-49'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-49') 
p.SectionAssignment(region=region, sectionName='Section-49', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 

 
# Generating Grain 53 ---------------------- 
p = mdb.models['Model-1'].Part(name='Part-Temp', objectToCopy=mdb.models['Model-1'].parts['Part-Base']) 
p = mdb.models['Model-1'].parts['Part-Temp'] 
f = p.faces 
faces = f.findAt(((4.5459e+02, 5.2153e+02, 0.0), ),) 
pickedGeomSourceSide=regionToolset.Region(faces=faces) 
vector =((0.0, 0.0, 0.0), (0.0, 0.0, 1.0000e+01)) 
p.generateBottomUpExtrudedMesh(geometrySourceSide=pickedGeomSourceSide, extrudeVector=vector, numberOfLayers=5) 
p.deleteMesh() 
p = mdb.models['Model-1'].parts['Part-Temp'] 
p.PartFromMesh(name='Grain-53', copySets=True) 
del mdb.models['Model-1'].parts['Part-Temp'] 
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT) 
p = mdb.models['Model-1'].parts['Grain-53'] 
elems1 = p.elements 
pickedRegions =(elems1, ) 
p.setElementType(regions=pickedRegions, elemTypes=(elemType1,)) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-53', material='Material-53', thickness=None) 
p = mdb.models['Model-1'].parts['Grain-53'] 
e = p.elements 
elements = e.getByBoundingBox(xMin=-5.0000e+00 , yMin=1.5000e+01 , xMax=7.2000e+02 , yMax=5.3500e+02 ) 
region = p.Set(elements=elements, name='Set-El-53') 
p.SectionAssignment(region=region, sectionName='Section-53', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION) 
 

 
# Add Materials------------------ 

 
# Generating Grain 1 ---------------------- 
mdb.models['Model-1'].Material(name='Material-1') 
mdb.models['Model-1'].materials['Material-1'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-1'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	7.25724173e-01, -5.01546758e-01, 4.70930222e-01,
	-3.41932655e-01, -8.56922973e-01, -3.85700763e-01,
	5.96997893e-01, 1.18885946e-01, -7.93384930e-01))
 
# Generating Grain 2 ---------------------- 
mdb.models['Model-1'].Material(name='Material-2') 
mdb.models['Model-1'].materials['Material-2'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-2'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	7.65171298e-01, -4.83468437e-01, 4.25171912e-01,
	-3.26685838e-01, -8.60607748e-01, -3.90679751e-01,
	5.54787570e-01, 1.60039290e-01, -8.16454639e-01))
 
# Generating Grain 3 ---------------------- 
mdb.models['Model-1'].Material(name='Material-3') 
mdb.models['Model-1'].materials['Material-3'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-3'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	8.50329684e-01, 2.61304063e-01, 4.56792749e-01,
	-8.18106975e-02, -7.91822521e-01, 6.05247144e-01,
	5.19852323e-01, -5.52030146e-01, -6.51932727e-01))
 
# Generating Grain 4 ---------------------- 
mdb.models['Model-1'].Material(name='Material-4') 
mdb.models['Model-1'].materials['Material-4'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-4'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	7.28808300e-01, 3.71465876e-01, -5.75196978e-01,
	1.82845347e-01, -9.15126980e-01, -3.59319062e-01,
	-6.59853044e-01, 1.56702624e-01, -7.34872946e-01))
 
# Generating Grain 5 ---------------------- 
mdb.models['Model-1'].Material(name='Material-5') 
mdb.models['Model-1'].materials['Material-5'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-5'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	7.88336802e-01, -5.06625210e-01, -3.49078764e-01,
	-1.29345610e-01, -6.91178034e-01, 7.11015217e-01,
	-6.01493807e-01, -5.15367656e-01, -6.10410828e-01))
 
# Generating Grain 6 ---------------------- 
mdb.models['Model-1'].Material(name='Material-6') 
mdb.models['Model-1'].materials['Material-6'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-6'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	7.73825180e-01, 2.97888948e-01, -5.58978322e-01,
	-1.13062648e-01, -8.03369891e-01, -5.84648318e-01,
	-6.23226626e-01, 5.15615160e-01, -5.87987737e-01))
 
# Generating Grain 7 ---------------------- 
mdb.models['Model-1'].Material(name='Material-7') 
mdb.models['Model-1'].materials['Material-7'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-7'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.13146598e-01, -3.65388740e-01, 1.80705170e-01,
	-3.19259245e-01, -9.16698612e-01, -2.40285640e-01,
	2.53449846e-01, 1.61724219e-01, -9.53733953e-01))
 
# Generating Grain 8 ---------------------- 
mdb.models['Model-1'].Material(name='Material-8') 
mdb.models['Model-1'].materials['Material-8'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-8'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	7.23048145e-01, 4.08078963e-01, 5.57380426e-01,
	3.16242387e-01, -9.12887774e-01, 2.58121416e-01,
	6.14159696e-01, -1.03668945e-02, -7.89113677e-01))
 
# Generating Grain 9 ---------------------- 
mdb.models['Model-1'].Material(name='Material-9') 
mdb.models['Model-1'].materials['Material-9'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-9'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	8.03432323e-01, -4.76151603e-01, -3.57457905e-01,
	-4.17325856e-01, -8.78564969e-01, 2.32298784e-01,
	-4.24659431e-01, -3.74599254e-02, -9.04577869e-01))
 
# Generating Grain 10 ---------------------- 
mdb.models['Model-1'].Material(name='Material-10') 
mdb.models['Model-1'].materials['Material-10'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-10'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.38491283e-01, -3.16425589e-01, -1.38235159e-01,
	-2.36232139e-01, -8.80340906e-01, 4.11332306e-01,
	-2.51850132e-01, -3.53376197e-01, -9.00942159e-01))
 
# Generating Grain 11 ---------------------- 
mdb.models['Model-1'].Material(name='Material-11') 
mdb.models['Model-1'].materials['Material-11'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-11'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	5.33593117e-01, -5.50206250e-01, -6.42301695e-01,
	-6.75076151e-01, -7.34568252e-01, 6.84227609e-02,
	-5.09461064e-01, 3.97092642e-01, -7.63391681e-01))
 
# Generating Grain 12 ---------------------- 
mdb.models['Model-1'].Material(name='Material-12') 
mdb.models['Model-1'].materials['Material-12'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-12'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	8.36069798e-01, 2.03472600e-01, -5.09496020e-01,
	1.89073353e-01, -9.78651963e-01, -8.05704804e-02,
	-5.15013165e-01, -2.89695756e-02, -8.56692595e-01))
 
# Generating Grain 13 ---------------------- 
mdb.models['Model-1'].Material(name='Material-13') 
mdb.models['Model-1'].materials['Material-13'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-13'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	8.98089835e-01, 2.26692526e-01, -3.76888773e-01,
	1.23310276e-01, -9.52345770e-01, -2.78984067e-01,
	-4.22172032e-01, 2.04078496e-01, -8.83245573e-01))
 
# Generating Grain 14 ---------------------- 
mdb.models['Model-1'].Material(name='Material-14') 
mdb.models['Model-1'].materials['Material-14'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-14'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	7.53860262e-01, -4.84934596e-01, -4.43320588e-01,
	-5.57385481e-01, -8.29254146e-01, -4.07306601e-02,
	-3.47873730e-01, 2.77805685e-01, -8.95437250e-01))
 
# Generating Grain 15 ---------------------- 
mdb.models['Model-1'].Material(name='Material-15') 
mdb.models['Model-1'].materials['Material-15'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-15'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.19927254e-01, -2.08226362e-01, -3.32228278e-01,
	-1.79555347e-01, -9.76985287e-01, 1.15150447e-01,
	-3.48559498e-01, -4.62766707e-02, -9.36143550e-01))
 
# Generating Grain 16 ---------------------- 
mdb.models['Model-1'].Material(name='Material-16') 
mdb.models['Model-1'].materials['Material-16'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-16'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	8.15700257e-01, 6.10388789e-02, -5.75245465e-01,
	3.34177835e-02, -9.97728989e-01, -5.84817549e-02,
	-5.77508738e-01, 2.84801541e-02, -8.15887577e-01))
 
# Generating Grain 17 ---------------------- 
mdb.models['Model-1'].Material(name='Material-17') 
mdb.models['Model-1'].materials['Material-17'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-17'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	7.48275810e-01, -5.23219974e-01, 4.07828605e-01,
	-3.03729820e-01, -8.16754876e-01, -4.90570757e-01,
	5.89772421e-01, 2.43212522e-01, -7.70075426e-01))
 
# Generating Grain 18 ---------------------- 
mdb.models['Model-1'].Material(name='Material-18') 
mdb.models['Model-1'].materials['Material-18'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-18'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.90841018e-01, -1.81652998e-02, 1.33806197e-01,
	-3.54347159e-02, -9.91161954e-01, 1.27837248e-01,
	1.30301409e-01, -1.31407774e-01, -9.82727602e-01))
 
# Generating Grain 19 ---------------------- 
mdb.models['Model-1'].Material(name='Material-19') 
mdb.models['Model-1'].materials['Material-19'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-19'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	8.27364905e-01, -2.55765438e-01, -5.00051352e-01,
	-2.55823178e-01, -9.64193939e-01, 6.98895542e-02,
	-5.00021815e-01, 7.01005615e-02, -8.63170954e-01))
 
# Generating Grain 20 ---------------------- 
mdb.models['Model-1'].Material(name='Material-20') 
mdb.models['Model-1'].materials['Material-20'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-20'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	6.35860126e-01, -5.36521438e-01, -5.54821275e-01,
	-4.20107600e-01, -8.43637906e-01, 3.34342173e-01,
	-6.47450002e-01, 2.04897778e-02, -7.61832438e-01))
 
# Generating Grain 21 ---------------------- 
mdb.models['Model-1'].Material(name='Material-21') 
mdb.models['Model-1'].materials['Material-21'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-21'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	7.42365285e-01, 1.16696929e-01, -6.59754204e-01,
	5.71989247e-02, -9.92158314e-01, -1.11131285e-01,
	-6.67549299e-01, 4.47627773e-02, -7.43218829e-01))
 
# Generating Grain 22 ---------------------- 
mdb.models['Model-1'].Material(name='Material-22') 
mdb.models['Model-1'].materials['Material-22'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-22'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.51133820e-01, -3.08378249e-01, 1.57261378e-02,
	-2.08375879e-01, -6.78613182e-01, -7.04317856e-01,
	2.27868272e-01, 6.66623585e-01, -7.09710537e-01))
 
# Generating Grain 23 ---------------------- 
mdb.models['Model-1'].Material(name='Material-23') 
mdb.models['Model-1'].materials['Material-23'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-23'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.37755116e-01, -1.95763524e-01, 2.86865795e-01,
	-1.58952951e-01, -9.76332524e-01, -1.46658659e-01,
	3.08786821e-01, 9.19317434e-02, -9.46678009e-01))
 
# Generating Grain 24 ---------------------- 
mdb.models['Model-1'].Material(name='Material-24') 
mdb.models['Model-1'].materials['Material-24'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-24'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	8.15925282e-01, 3.66559315e-01, -4.47102005e-01,
	2.60369261e-01, -9.23430954e-01, -2.81927511e-01,
	-5.16210987e-01, 1.13620165e-01, -8.48891439e-01))
 
# Generating Grain 25 ---------------------- 
mdb.models['Model-1'].Material(name='Material-25') 
mdb.models['Model-1'].materials['Material-25'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-25'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.55860990e-01, -2.88797835e-01, 5.40886069e-02,
	-1.93034748e-01, -7.56038233e-01, -6.25414884e-01,
	2.21511519e-01, 5.87368710e-01, -7.78415471e-01))
 
# Generating Grain 26 ---------------------- 
mdb.models['Model-1'].Material(name='Material-26') 
mdb.models['Model-1'].materials['Material-26'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-26'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	7.94688533e-01, -2.35681981e-01, -5.59396227e-01,
	-1.81465681e-01, -9.71645579e-01, 1.51575315e-01,
	-5.79258442e-01, -1.89439472e-02, -8.14923791e-01))
 
# Generating Grain 27 ---------------------- 
mdb.models['Model-1'].Material(name='Material-27') 
mdb.models['Model-1'].materials['Material-27'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-27'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.85140360e-01, -7.93572876e-02, -1.52318390e-01,
	-1.12732468e-01, -9.67845696e-01, -2.24869070e-01,
	-1.29575699e-01, 2.38698825e-01, -9.62410001e-01))
 
# Generating Grain 28 ---------------------- 
mdb.models['Model-1'].Material(name='Material-28') 
mdb.models['Model-1'].materials['Material-28'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-28'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	6.81230850e-01, -3.44536276e-01, -6.45925138e-01,
	-2.41431255e-01, -9.38700253e-01, 2.46074754e-01,
	-6.91111770e-01, -1.16871969e-02, -7.22653396e-01))
 
# Generating Grain 29 ---------------------- 
mdb.models['Model-1'].Material(name='Material-29') 
mdb.models['Model-1'].materials['Material-29'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-29'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	8.27337461e-01, -5.38144376e-01, 1.60976258e-01,
	-4.22850083e-01, -7.85338404e-01, -4.52151965e-01,
	3.69743874e-01, 3.06013434e-01, -8.77294275e-01))
 
# Generating Grain 30 ---------------------- 
mdb.models['Model-1'].Material(name='Material-30') 
mdb.models['Model-1'].materials['Material-30'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-30'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	7.08139592e-01, 2.90828811e-01, 6.43394841e-01,
	1.73947664e-01, -9.55003337e-01, 2.40230801e-01,
	6.84310258e-01, -5.81999116e-02, -7.26864665e-01))
 
# Generating Grain 31 ---------------------- 
mdb.models['Model-1'].Material(name='Material-31') 
mdb.models['Model-1'].materials['Material-31'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-31'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.71754711e-01, 2.04768495e-01, -1.17314301e-01,
	1.81050742e-01, -9.65733932e-01, -1.85953225e-01,
	-1.51371763e-01, 1.59461081e-01, -9.75529986e-01))
 
# Generating Grain 32 ---------------------- 
mdb.models['Model-1'].Material(name='Material-32') 
mdb.models['Model-1'].materials['Material-32'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-32'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	8.14198819e-01, -4.99010061e-01, 2.96764624e-01,
	-4.61282760e-01, -8.66391389e-01, -1.91269905e-01,
	3.52559922e-01, 1.88393255e-02, -9.35599584e-01))
 
# Generating Grain 33 ---------------------- 
mdb.models['Model-1'].Material(name='Material-33') 
mdb.models['Model-1'].materials['Material-33'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-33'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	7.33809009e-01, 4.27772818e-01, 5.27763920e-01,
	3.71530055e-01, -9.03086616e-01, 2.15406551e-01,
	5.68761600e-01, 3.80128901e-02, -8.21623553e-01))
 
# Generating Grain 34 ---------------------- 
mdb.models['Model-1'].Material(name='Material-34') 
mdb.models['Model-1'].materials['Material-34'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-34'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.83301572e-01, -1.60750519e-01, -8.53070255e-02,
	-1.77429889e-01, -9.51047820e-01, -2.53034936e-01,
	-4.04555633e-02, 2.63945666e-01, -9.63688763e-01))
 
# Generating Grain 35 ---------------------- 
mdb.models['Model-1'].Material(name='Material-35') 
mdb.models['Model-1'].materials['Material-35'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-35'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.92641640e-01, -1.20132873e-01, -1.51877640e-02,
	-1.09990459e-01, -8.42082109e-01, -5.28014981e-01,
	5.06426122e-02, 5.25800166e-01, -8.49099235e-01))
 
# Generating Grain 36 ---------------------- 
mdb.models['Model-1'].Material(name='Material-36') 
mdb.models['Model-1'].materials['Material-36'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-36'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.76177292e-01, 1.22195424e-01, -1.79293537e-01,
	8.00415095e-03, -8.46053145e-01, -5.33038468e-01,
	-2.16826723e-01, 5.18904956e-01, -8.26875939e-01))
 
# Generating Grain 37 ---------------------- 
mdb.models['Model-1'].Material(name='Material-37') 
mdb.models['Model-1'].materials['Material-37'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-37'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.07758859e-01, -4.19275355e-01, 1.34918653e-02,
	-3.99040964e-01, -8.72976199e-01, -2.80497531e-01,
	1.29383779e-01, 2.49240312e-01, -9.59759920e-01))
 
# Generating Grain 38 ---------------------- 
mdb.models['Model-1'].Material(name='Material-38') 
mdb.models['Model-1'].materials['Material-38'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-38'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	6.03157718e-01, 4.59547825e-01, 6.51932944e-01,
	5.97892729e-01, -8.01489128e-01, 1.18094539e-02,
	5.27944176e-01, 3.82663004e-01, -7.58184656e-01))
 
# Generating Grain 39 ---------------------- 
mdb.models['Model-1'].Material(name='Material-39') 
mdb.models['Model-1'].materials['Material-39'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-39'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	6.98275349e-01, -3.57819867e-01, -6.19981032e-01,
	-4.20898797e-01, -9.05797974e-01, 4.87260984e-02,
	-5.79012729e-01, 2.26925037e-01, -7.83102348e-01))
 
# Generating Grain 40 ---------------------- 
mdb.models['Model-1'].Material(name='Material-40') 
mdb.models['Model-1'].materials['Material-40'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-40'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.94289324e-01, 3.55456947e-02, 1.00624272e-01,
	4.25316523e-02, -9.96767810e-01, -6.81541681e-02,
	9.78764482e-02, 7.20446782e-02, -9.92587409e-01))
 
# Generating Grain 41 ---------------------- 
mdb.models['Model-1'].Material(name='Material-41') 
mdb.models['Model-1'].materials['Material-41'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-41'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	8.38131761e-01, -4.03561888e-01, 3.66978139e-01,
	-3.02748241e-01, -9.03802762e-01, -3.02463337e-01,
	4.53738531e-01, 1.42402143e-01, -8.79683452e-01))
 
# Generating Grain 42 ---------------------- 
mdb.models['Model-1'].Material(name='Material-42') 
mdb.models['Model-1'].materials['Material-42'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-42'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.87082724e-01, 9.44359012e-02, -1.29420076e-01,
	2.61877365e-02, -8.92048069e-01, -4.51181166e-01,
	-1.58056629e-01, 4.41963916e-01, -8.82998301e-01))
 
# Generating Grain 43 ---------------------- 
mdb.models['Model-1'].Material(name='Material-43') 
mdb.models['Model-1'].materials['Material-43'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-43'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.00623173e-01, 3.79804580e-01, 2.11249573e-01,
	3.87522888e-01, -9.21845137e-01, 5.24929506e-03,
	1.96733098e-01, 7.71364079e-02, -9.77418059e-01))
 
# Generating Grain 44 ---------------------- 
mdb.models['Model-1'].Material(name='Material-44') 
mdb.models['Model-1'].materials['Material-44'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-44'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	8.02928138e-01, 2.86436492e-01, -5.22743284e-01,
	1.62726479e-01, -9.48994634e-01, -2.70054211e-01,
	-5.73433952e-01, 1.31769951e-01, -8.08585297e-01))
 
# Generating Grain 45 ---------------------- 
mdb.models['Model-1'].Material(name='Material-45') 
mdb.models['Model-1'].materials['Material-45'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-45'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.98492308e-01, -5.37337686e-02, 1.12157893e-02,
	-5.46226289e-02, -9.92844474e-01, 1.06189539e-01,
	5.42957031e-03, -1.06642074e-01, -9.94282650e-01))
 
# Generating Grain 46 ---------------------- 
mdb.models['Model-1'].Material(name='Material-46') 
mdb.models['Model-1'].materials['Material-46'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-46'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.25269260e-01, 2.33010980e-01, 2.99303659e-01,
	1.77243587e-01, -9.63224584e-01, 2.01948288e-01,
	3.35352811e-01, -1.33806889e-01, -9.32541800e-01))
 
# Generating Grain 47 ---------------------- 
mdb.models['Model-1'].Material(name='Material-47') 
mdb.models['Model-1'].materials['Material-47'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-47'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	6.57754335e-01, 4.00899629e-01, 6.37682305e-01,
	4.93267502e-01, -8.69065864e-01, 3.75725406e-02,
	5.69250741e-01, 2.89834456e-01, -7.69382598e-01))
 
# Generating Grain 48 ---------------------- 
mdb.models['Model-1'].Material(name='Material-48') 
mdb.models['Model-1'].materials['Material-48'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-48'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.73014114e-01, 2.21802201e-01, -6.36185367e-02,
	2.28747906e-01, -9.63404965e-01, 1.39732850e-01,
	-3.02973605e-02, -1.50514642e-01, -9.88143417e-01))
 
# Generating Grain 49 ---------------------- 
mdb.models['Model-1'].Material(name='Material-49') 
mdb.models['Model-1'].materials['Material-49'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-49'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.47756881e-01, -3.18940495e-01, 5.81858100e-03,
	-3.17484677e-01, -9.44888950e-01, -7.99271660e-02,
	3.09899228e-02, 7.39042112e-02, -9.96783724e-01))
 
# Generating Grain 50 ---------------------- 
mdb.models['Model-1'].Material(name='Material-50') 
mdb.models['Model-1'].materials['Material-50'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-50'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	6.61137457e-01, 4.03892945e-01, -6.32271898e-01,
	2.87242849e-01, -9.14785580e-01, -2.84005087e-01,
	-6.93100865e-01, 6.15081975e-03, -7.20814371e-01))
 
# Generating Grain 51 ---------------------- 
mdb.models['Model-1'].Material(name='Material-51') 
mdb.models['Model-1'].materials['Material-51'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-51'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.74310843e-01, -2.18950780e-01, -5.27156171e-02,
	-2.24976393e-01, -9.35671398e-01, -2.71854112e-01,
	1.01981747e-02, 2.76730179e-01, -9.60893545e-01))
 
# Generating Grain 52 ---------------------- 
mdb.models['Model-1'].Material(name='Material-52') 
mdb.models['Model-1'].materials['Material-52'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-52'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.69299211e-01, -2.37791565e-01, -6.25636648e-02,
	-1.95170337e-01, -8.98822300e-01, 3.92462752e-01,
	-1.49557949e-01, -3.68203265e-01, -9.17637606e-01))
 
# Generating Grain 53 ---------------------- 
mdb.models['Model-1'].Material(name='Material-53') 
mdb.models['Model-1'].materials['Material-53'].Depvar(n=89)
mdb.models['Model-1'].materials['Material-53'].UserMaterial(
	mechanicalConstants=(2.0000e+00,
	9.48434362e-01, -3.05850768e-01, -8.32320140e-02,
	-2.89958112e-01, -9.43231962e-01, 1.61980736e-01,
	-1.28049028e-01, -1.29494298e-01, -9.83277516e-01)) 

 
# Assembly------------------ 

 
# Adding Grain 5 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-5'] 
a.Instance(name='Grain-5-1', part=p, dependent=ON) 

 
# Adding Grain 6 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-6'] 
a.Instance(name='Grain-6-1', part=p, dependent=ON) 

 
# Adding Grain 7 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-7'] 
a.Instance(name='Grain-7-1', part=p, dependent=ON) 

 
# Adding Grain 8 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-8'] 
a.Instance(name='Grain-8-1', part=p, dependent=ON) 

 
# Adding Grain 9 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-9'] 
a.Instance(name='Grain-9-1', part=p, dependent=ON) 

 
# Adding Grain 10 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-10'] 
a.Instance(name='Grain-10-1', part=p, dependent=ON) 

 
# Adding Grain 11 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-11'] 
a.Instance(name='Grain-11-1', part=p, dependent=ON) 

 
# Adding Grain 12 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-12'] 
a.Instance(name='Grain-12-1', part=p, dependent=ON) 

 
# Adding Grain 13 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-13'] 
a.Instance(name='Grain-13-1', part=p, dependent=ON) 

 
# Adding Grain 14 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-14'] 
a.Instance(name='Grain-14-1', part=p, dependent=ON) 

 
# Adding Grain 16 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-16'] 
a.Instance(name='Grain-16-1', part=p, dependent=ON) 

 
# Adding Grain 17 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-17'] 
a.Instance(name='Grain-17-1', part=p, dependent=ON) 

 
# Adding Grain 18 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-18'] 
a.Instance(name='Grain-18-1', part=p, dependent=ON) 

 
# Adding Grain 19 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-19'] 
a.Instance(name='Grain-19-1', part=p, dependent=ON) 

 
# Adding Grain 20 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-20'] 
a.Instance(name='Grain-20-1', part=p, dependent=ON) 

 
# Adding Grain 21 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-21'] 
a.Instance(name='Grain-21-1', part=p, dependent=ON) 

 
# Adding Grain 22 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-22'] 
a.Instance(name='Grain-22-1', part=p, dependent=ON) 

 
# Adding Grain 23 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-23'] 
a.Instance(name='Grain-23-1', part=p, dependent=ON) 

 
# Adding Grain 24 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-24'] 
a.Instance(name='Grain-24-1', part=p, dependent=ON) 

 
# Adding Grain 25 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-25'] 
a.Instance(name='Grain-25-1', part=p, dependent=ON) 

 
# Adding Grain 26 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-26'] 
a.Instance(name='Grain-26-1', part=p, dependent=ON) 

 
# Adding Grain 27 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-27'] 
a.Instance(name='Grain-27-1', part=p, dependent=ON) 

 
# Adding Grain 28 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-28'] 
a.Instance(name='Grain-28-1', part=p, dependent=ON) 

 
# Adding Grain 29 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-29'] 
a.Instance(name='Grain-29-1', part=p, dependent=ON) 

 
# Adding Grain 30 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-30'] 
a.Instance(name='Grain-30-1', part=p, dependent=ON) 

 
# Adding Grain 31 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-31'] 
a.Instance(name='Grain-31-1', part=p, dependent=ON) 

 
# Adding Grain 32 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-32'] 
a.Instance(name='Grain-32-1', part=p, dependent=ON) 

 
# Adding Grain 33 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-33'] 
a.Instance(name='Grain-33-1', part=p, dependent=ON) 

 
# Adding Grain 34 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-34'] 
a.Instance(name='Grain-34-1', part=p, dependent=ON) 

 
# Adding Grain 35 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-35'] 
a.Instance(name='Grain-35-1', part=p, dependent=ON) 

 
# Adding Grain 36 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-36'] 
a.Instance(name='Grain-36-1', part=p, dependent=ON) 

 
# Adding Grain 37 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-37'] 
a.Instance(name='Grain-37-1', part=p, dependent=ON) 

 
# Adding Grain 38 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-38'] 
a.Instance(name='Grain-38-1', part=p, dependent=ON) 

 
# Adding Grain 39 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-39'] 
a.Instance(name='Grain-39-1', part=p, dependent=ON) 

 
# Adding Grain 40 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-40'] 
a.Instance(name='Grain-40-1', part=p, dependent=ON) 

 
# Adding Grain 41 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-41'] 
a.Instance(name='Grain-41-1', part=p, dependent=ON) 

 
# Adding Grain 42 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-42'] 
a.Instance(name='Grain-42-1', part=p, dependent=ON) 

 
# Adding Grain 43 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-43'] 
a.Instance(name='Grain-43-1', part=p, dependent=ON) 

 
# Adding Grain 44 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-44'] 
a.Instance(name='Grain-44-1', part=p, dependent=ON) 

 
# Adding Grain 45 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-45'] 
a.Instance(name='Grain-45-1', part=p, dependent=ON) 

 
# Adding Grain 46 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-46'] 
a.Instance(name='Grain-46-1', part=p, dependent=ON) 

 
# Adding Grain 47 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-47'] 
a.Instance(name='Grain-47-1', part=p, dependent=ON) 

 
# Adding Grain 48 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-48'] 
a.Instance(name='Grain-48-1', part=p, dependent=ON) 

 
# Adding Grain 49 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-49'] 
a.Instance(name='Grain-49-1', part=p, dependent=ON) 

 
# Adding Grain 53 ---------------------- 
a = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Grain-53'] 
a.Instance(name='Grain-53-1', part=p, dependent=ON) 

 
# Combine Stuff ---------------------- 
a.InstanceFromBooleanMerge(name='Poly-Grain', instances=(
	a.instances['Grain-5-1'],
	a.instances['Grain-6-1'],
	a.instances['Grain-7-1'],
	a.instances['Grain-8-1'],
	a.instances['Grain-9-1'],
	a.instances['Grain-10-1'],
	a.instances['Grain-11-1'],
	a.instances['Grain-12-1'],
	a.instances['Grain-13-1'],
	a.instances['Grain-14-1'],
	a.instances['Grain-16-1'],
	a.instances['Grain-17-1'],
	a.instances['Grain-18-1'],
	a.instances['Grain-19-1'],
	a.instances['Grain-20-1'],
	a.instances['Grain-21-1'],
	a.instances['Grain-22-1'],
	a.instances['Grain-23-1'],
	a.instances['Grain-24-1'],
	a.instances['Grain-25-1'],
	a.instances['Grain-26-1'],
	a.instances['Grain-27-1'],
	a.instances['Grain-28-1'],
	a.instances['Grain-29-1'],
	a.instances['Grain-30-1'],
	a.instances['Grain-31-1'],
	a.instances['Grain-32-1'],
	a.instances['Grain-33-1'],
	a.instances['Grain-34-1'],
	a.instances['Grain-35-1'],
	a.instances['Grain-36-1'],
	a.instances['Grain-37-1'],
	a.instances['Grain-38-1'],
	a.instances['Grain-39-1'],
	a.instances['Grain-40-1'],
	a.instances['Grain-41-1'],
	a.instances['Grain-42-1'],
	a.instances['Grain-43-1'],
	a.instances['Grain-44-1'],
	a.instances['Grain-45-1'],
	a.instances['Grain-46-1'],
	a.instances['Grain-47-1'],
	a.instances['Grain-48-1'],
	a.instances['Grain-49-1'],
	a.instances['Grain-53-1'],
	),mergeNodes=ALL, nodeMergingTolerance=1e-06, domain=MESH,
	originalInstances=SUPPRESS)

 
# Write Output ---------------------- 
mdb.models['Model-1'].setValues(noPartsInputFile=ON)
a = mdb.models['Model-1'].rootAssembly 
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
mdb.Job(name='ExtractForPoints-1', model='Model-1', description='', type=ANALYSIS,
	atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
	memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
	explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
	modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
	scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1,
	numGPUs=0) 

mdb.jobs['ExtractForPoints-1'].writeInput(consistencyChecking=OFF) 

 
