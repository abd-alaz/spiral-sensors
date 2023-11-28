# This code is to build a multi-muscle SPA
# Generated via ABAQUS 2020 
# by Abdullah Al-Azzawi 
# on 26.Nov.2021

# We have made the source codes for the simulations conducted in this study available 
# on our GitHub repository: {https://github.com/abd-alaz/spiral-sensors}. Interested 
# readers can access and download the codes for a closer examination of the implementations
# and methods employed. The codes are open-source and provided under the GNU General 
# Public License v3.0, allowing for academic and non-commercial use.

from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=291.65625, 
    height=188.144424438477)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)


mdb.saveAs(pathName='D:/Abaqus_temp/SPA_multi_3.cae')
#: The model database has been saved to "D:\Abaqus_temp\SPA_multi_4.cae".



# create custom viewport with z-axis verticle
session.View(name='User-1', nearPlane=269.49, farPlane=473.06, width=416.82, 
    height=200.1, projection=PARALLEL, cameraPosition=(210.46, 223.89, 288.82), 
    cameraUpVector=(-0.58355, -0.57336, 0.57509), cameraTarget=(-2.4611, 
    13.051, 75.698), viewOffsetX=0, viewOffsetY=0, autoFit=ON)


#########################################################################
# Define materials ..............................

mdb.models['Model-1'].Material(name='Elasosil_M4601')
mdb.models['Model-1'].materials['Elasosil_M4601'].Density(table=((1.13e-09, ), 
    ))
mdb.models['Model-1'].materials['Elasosil_M4601'].Hyperelastic(
    materialType=ISOTROPIC, testData=OFF, type=YEOH, 
    volumetricResponse=VOLUMETRIC_DATA, table=((0.11, 0.02, 0.0, 0.0, 0.0, 
    0.0), ))

mdb.models['Model-1'].Material(name='SSteel_18/8')
mdb.models['Model-1'].materials['SSteel_18/8'].Density(table=((7.93e-09, ), ))
mdb.models['Model-1'].materials['SSteel_18/8'].Elastic(table=((193000.0, 
    0.305), ))

mdb.models['Model-1'].Material(name='PET_Ortho')
mdb.models['Model-1'].materials['PET_Ortho'].Density(table=((1.35e-09, ), ))
mdb.models['Model-1'].materials['PET_Ortho'].Elastic(type=LAMINA, table=((
    6000.0, 0.001, 0.37, 1.0, 1.0, 1.0), ))

# mdb.models['Model-1'].Material(name='PET')
# mdb.models['Model-1'].materials['PET'].Density(table=((1.35e-09, ), ))
# mdb.models['Model-1'].materials['PET'].Elastic(table=((6000.0, 0.37), ))

# mdb.models['Model-1'].Material(name='Paper')
# mdb.models['Model-1'].materials['Paper'].Density(table=((7.5e-10, ), ))
# mdb.models['Model-1'].materials['Paper'].Elastic(table=((6500.0, 0.2), ))

# mdb.models['Model-1'].Material(name='Nitinol')
# mdb.models['Model-1'].materials['Nitinol'].Density(table=((6.45e-09, ), ))
# mdb.models['Model-1'].materials['Nitinol'].Elastic(table=((70000.0, 0.33), ))

# mdb.models['SPA_Connolly'].Material(name='Nitinol')
# mdb.models['SPA_Connolly'].materials['Nitinol'].SuperElasticity(
    # nonassociated=None, shapeSetField=None, table=((26500.0, 0.3, 0.047, 419.0, 
    # 450.0, 180.0, 140.0, 540.0, 37.0, 7.34, 7.64, 0.0), ))
# mdb.models['SPA_Connolly'].materials['Nitinol'].Elastic(table=((71300.0, 0.3), 
    # ))




#########################################################################
# Define sections ..............................

mdb.models['Model-1'].HomogeneousSolidSection(name='Sec-SSteel', 
    material='SSteel_18/8', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(name='Sec-Elastosil', 
    material='Elasosil_M4601', thickness=None)
mdb.models['Model-1'].HomogeneousShellSection(name='Sec-OPET', 
    preIntegrate=OFF, material='PET_Ortho', thicknessType=UNIFORM, 
    thickness=0.1, thicknessField='', nodalThicknessField='', 
    idealization=NO_IDEALIZATION, poissonDefinition=DEFAULT, 
    thicknessModulus=None, temperature=GRADIENT, useDensity=OFF, 
    integrationRule=SIMPSON, numIntPts=5)





#########################################################################
# Define parts ..............................


# Base ...
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(11.0, 0.0))
p = mdb.models['Model-1'].Part(name='Part-Base', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-Base']
p.BaseSolidExtrude(sketch=s, depth=2.0)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-Base']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']


# Top ...
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(11.0, 0.0))
p = mdb.models['Model-1'].Part(name='Part-Top', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-Top']
p.BaseSolidExtrude(sketch=s1, depth=2.0)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-Top']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['Part-Top']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#2 ]', ), )
v1, e, d1 = p.vertices, p.edges, p.datums
p.PartitionFaceByShortestPath(point2=v1[0], faces=pickedFaces, 
    point1=p.InterestingPoint(edge=e[0], rule=MIDDLE))
p = mdb.models['Model-1'].parts['Part-Top']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#5 ]', ), )
v2, e1, d2 = p.vertices, p.edges, p.datums
p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
    edge=e1[1], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[2], 
    rule=MIDDLE))


# Tube ...
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(4.0, 0.0))
s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(2.0, 0.0))
p = mdb.models['Model-1'].Part(name='Part-Tube', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-Tube']
p.BaseSolidExtrude(sketch=s, depth=250.0)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-Tube']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']

# create skin for the tube, to be used for ortho layer ...
p = mdb.models['Model-1'].parts['Part-Tube']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.Skin(faces=faces, name='Skin-1')
mdb.models['Model-1'].parts['Part-Tube'].skins.changeKey(fromName='Skin-1', 
    toName='Skin-Tube')


# Body ...
# create tird of a full body, combining 3 thirds in the assembly
# will generate an edge at the centreline.
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(6.0, 0.0))
s.CircleByCenterPerimeter(center=(-6.0, 0.0), point1=(-10.0, 0.0))
s.CoincidentConstraint(entity1=v[2], entity2=g[2], addUndoState=False)
s.delete(objectList=(g[2], ))
s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(11.0, 0.0))
s.Line(point1=(0.0, 0.0), point2=(11.0, 0.0))
s.HorizontalConstraint(entity=g[5], addUndoState=False)
s.delete(objectList=(g[4], ))
s.radialPattern(geomList=(g[3], g[5]), vertexList=(), number=3, 
    totalAngle=360.0, centerPoint=(0.0, 0.0))
s.delete(objectList=(g[5], g[6], g[8], c[11]))
s.ArcByCenterEnds(center=(0.0, 0.0), point1=(-5.5, 9.52627944162883), point2=(
    -5.5, -9.52627944162882), direction=COUNTERCLOCKWISE)
p = mdb.models['Model-1'].Part(name='Part-Body', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-Body']
p.BaseSolidExtrude(sketch=s, depth=250.0)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-Body']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']





#########################################################################
# Assembly ..............................

a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['Part-Base']
a.Instance(name='Part-Base-1', part=p, dependent=ON)
p = mdb.models['Model-1'].parts['Part-Body']
a.Instance(name='Part-Body-1', part=p, dependent=ON)
p = mdb.models['Model-1'].parts['Part-Top']
a.Instance(name='Part-Top-1', part=p, dependent=ON)
p = mdb.models['Model-1'].parts['Part-Tube']
a.Instance(name='Part-Tube-1', part=p, dependent=ON)
p1 = a.instances['Part-Body-1']
p1.translate(vector=(24.1, 0.0, 0.0))
p1 = a.instances['Part-Top-1']
p1.translate(vector=(38.5, 0.0, 0.0))
p1 = a.instances['Part-Tube-1']
p1.translate(vector=(55.3, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()


# move base to origin ...
a = mdb.models['Model-1'].rootAssembly
a.translate(instanceList=('Part-Base-1', ), vector=(0.0, 0.0, -2.0))
#: The instance Part-Base-1 was translated by 0., 0., -2. with respect to the assembly coordinate system


# Add the body to the base ...
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Part-Body-1'].faces
f2 = a.instances['Part-Base-1'].faces
a.FaceToFace(movablePlane=f1[5], fixedPlane=f2[1], flip=ON, clearance=0.0)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-Body-1'].edges
e2 = a.instances['Part-Base-1'].edges
a.CoincidentPoint(movablePoint=a.instances['Part-Body-1'].InterestingPoint(
    edge=e1[2], rule=MIDDLE), 
    fixedPoint=a.instances['Part-Base-1'].InterestingPoint(edge=e2[0], 
    rule=MIDDLE))
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Part-Body-1'].faces
f2 = a.instances['Part-Base-1'].faces
a.Coaxial(movableAxis=f1[0], fixedAxis=f2[0], flip=OFF)
#: The instance "Part-Body-1" is fully constrained

# add the tube to the body, and make copies ...
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Part-Tube-1'].faces
f2 = a.instances['Part-Body-1'].faces
a.FaceToFace(movablePlane=f1[2], fixedPlane=f2[4], flip=OFF, clearance=0.0)
a = mdb.models['Model-1'].rootAssembly
v11 = a.instances['Part-Tube-1'].vertices
e1 = a.instances['Part-Body-1'].edges
a.CoincidentPoint(movablePoint=v11[0], 
    fixedPoint=a.instances['Part-Body-1'].InterestingPoint(edge=e1[9], 
    rule=MIDDLE))
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Part-Tube-1'].faces
f2 = a.instances['Part-Body-1'].faces
a.Coaxial(movableAxis=f1[1], fixedAxis=f2[3], flip=OFF)
#: The instance "Part-Tube-1" is fully constrained
a = mdb.models['Model-1'].rootAssembly
a.RadialInstancePattern(instanceList=('Part-Body-1', 'Part-Tube-1'), point=(
    0.0, 0.0, 0.0), axis=(0.0, 0.0, 1.0), number=3, totalAngle=360.0)

# Add the top to body ...
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Part-Top-1'].faces
f2 = a.instances['Part-Body-1-rad-3'].faces
a.FaceToFace(movablePlane=f1[5], fixedPlane=f2[4], flip=ON, clearance=0.0)
a = mdb.models['Model-1'].rootAssembly
v11 = a.instances['Part-Top-1'].vertices
v12 = a.instances['Part-Body-1-rad-3'].vertices
a.CoincidentPoint(movablePoint=v11[5], fixedPoint=v12[1])
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Part-Top-1'].faces
f2 = a.instances['Part-Base-1'].faces
a.Coaxial(movableAxis=f1[3], fixedAxis=f2[0], flip=OFF)
#: The instance "Part-Top-1" is fully constrained


# Generate assembly ...
a = mdb.models['Model-1'].rootAssembly
a.InstanceFromBooleanMerge(name='Merged', instances=(
    a.instances['Part-Base-1'], a.instances['Part-Body-1'], 
    a.instances['Part-Top-1'], a.instances['Part-Tube-1'], 
    a.instances['Part-Body-1-rad-2'], a.instances['Part-Body-1-rad-3'], 
    a.instances['Part-Tube-1-rad-2'], a.instances['Part-Tube-1-rad-3'], ), 
    keepIntersections=ON, originalInstances=SUPPRESS, domain=GEOMETRY)



#########################################################################
# Finish the model features ..............................


p = mdb.models['Model-1'].parts['Merged']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])

# partition face to generate path for spiral sensor
p = mdb.models['Model-1'].parts['Merged']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#8000040 ]', ), )
v1, e, d1 = p.vertices, p.edges, p.datums
p.PartitionFaceByShortestPath(point1=v1[14], point2=v1[18], faces=pickedFaces)



# Section assignments (parts)...
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)

# Top ...
p = mdb.models['Model-1'].parts['Merged']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#4 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['Merged']
p.SectionAssignment(region=region, sectionName='Sec-SSteel', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)

# Base ...
p = mdb.models['Model-1'].parts['Merged']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['Merged']
p.SectionAssignment(region=region, sectionName='Sec-SSteel', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)

# Body ...
p = mdb.models['Model-1'].parts['Merged']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#32 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['Merged']
p.SectionAssignment(region=region, sectionName='Sec-Elastosil', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)

# Tubes ...
p = mdb.models['Model-1'].parts['Merged']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#c8 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['Merged']
p.SectionAssignment(region=region, sectionName='Sec-Elastosil', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)


# Section assignments (ortho layer) ... 
# Important to creat a set while assigning the ortho layer, to be used later in mesh
p = mdb.models['Model-1'].parts['Merged']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#4200 #1 ]', ), )
region = p.Set(skinFaces=(('Skin-Tube', faces), ), name='Set-OPET')
p = mdb.models['Model-1'].parts['Merged']
p.SectionAssignment(region=region, sectionName='Sec-OPET', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)



# Create pressure surfaces ...
# Tube1 : between positive x & y axes
# Tube2 : on negative x-axis
# Tube3 : between positive x-axis & negative y-axis


p = mdb.models['Model-1'].parts['Merged']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#10040004 ]', ), )
p.Surface(side1Faces=side1Faces, name='Surf-Tube1')
#: The surface 'Surf-Tube1' has been created (3 faces).

side1Faces = s.getSequenceFromMask(mask=('[#480000 #4 ]', ), )
p.Surface(side1Faces=side1Faces, name='Surf-Tube2')
#: The surface 'Surf-Tube2' has been created (3 faces).

side1Faces = s.getSequenceFromMask(mask=('[#28020 ]', ), )
p.Surface(side1Faces=side1Faces, name='Surf-Tube3')
#: The surface 'Surf-Tube3' has been created (3 faces).




#########################################################################
# Generate mesh ..............................

session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)


# Assign seed size (use 4 mm) ...
p = mdb.models['Model-1'].parts['Merged']
p.seedPart(size=5.0, deviationFactor=0.1, minSizeFactor=0.1)


# Assign mesh control (for parts and ortho layer)...
p = mdb.models['Model-1'].parts['Merged']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#ff ]', ), )
p.setMeshControls(regions=pickedRegions, elemShape=TET, technique=FREE)
elemType1 = mesh.ElemType(elemCode=C3D20R)
elemType2 = mesh.ElemType(elemCode=C3D15)
elemType3 = mesh.ElemType(elemCode=C3D10)
p = mdb.models['Model-1'].parts['Merged']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#ff ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))


# Assign element type (ortho layer) ...
elemType1 = mesh.ElemType(elemCode=S8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=STRI65, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['Merged']
pickedRegions = p.sets['Set-OPET']
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))

# Assign element type (parts) ...
elemType1 = mesh.ElemType(elemCode=C3D20R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D15, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D10HS, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['Merged']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#ff ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
    

# Generate mesh ...
p = mdb.models['Model-1'].parts['Merged']
p.generateMesh()


# Create node set for centreline ...
p = mdb.models['Model-1'].parts['Merged']
n = p.nodes
nodes = n.getSequenceFromMask(mask=(
    '[#80080 #0:6 #fffffc00 #7ffffff #0:235 #20000000 #0:17', 
    ' #40000000 #0:2 #10 #2000000 #0:3 #2000000 #0:8', 
    ' #400 #40008 #2000000 #20000 #10000000 #804 #8000040', 
    ' #800001 #0 #40000000 #0 #10000 #2020 #84000', 
    ' #80000 #800000 #4000 #100 #80000000 #0 #800', 
    ' #40400000 #0:3 #400100 #0:2 #80000 #2000080 #2000000', 
    ' #4000 #40000000 #10000000 #2000 #10000 #400 #0:3', 
    ' #80 #0:13 #80000000 #0:12 #8000000 #0:20 #4', 
    ' #0:15 #40000 #8000 #0:23 #8 ]', ), )
p.Set(nodes=nodes, name='Set-Centreline')
#: The set 'Set-Centreline' has been created (101 nodes).


# Create node set for sensor 1 (straight, on positive x-axis)
p = mdb.models['Model-1'].parts['Merged']
n = p.nodes
nodes = n.getSequenceFromMask(mask=(
    '[#80000400 #0:9 #ffc00000 #ffffffff #7f #0:685 #2', 
    ' #0:5 #202 #0 #4000 #80000000 #0:5 #2', 
    ' #0:10 #800000 #0:2 #100000 #4 #0:5 #100000', 
    ' #0:19 #8000000 #80000000 #0:25 #10000000 #0 #80000', 
    ' #0:3 #400 #0:5 #40000000 #0:5 #200000 #0:2', 
    ' #80000000 #10000 #20 #400 #0:3 #2000000 #80000', 
    ' #0 #40000 #20000 #400 #0 #1 #80000000', 
    ' #0:3 #4000000 #0:4 #8 #0 #8 #0:3', 
    ' #10000000 #20000000 #0 #8000000 #0:2 #20 #0:4', 
    ' #80000 #10401000 #0 #10100001 #0 #408000 #800000', 
    ' #40000 #2000000 #0:6 #4 #0:2 #1000 #0:2', ' #20 ]', ), )
p.Set(nodes=nodes, name='Set-Sen1')
#: The set 'Set-Sen1' has been created (101 nodes).


# Create node set for sensor 2 (straight, between -x & -y)
p = mdb.models['Model-1'].parts['Merged']
n = p.nodes
nodes = n.getSequenceFromMask(mask=(
    '[#20200 #0:4 #ff000000 #ffffffff #1ff #0:230 #20000000', 
    ' #0:5 #80000 #0 #2000000 #0:3 #80 #0:30', 
    ' #200000 #0 #400 #100000 #20 #0:2 #8000', 
    ' #800000 #0 #20000 #40 #20000000 #0 #800000', 
    ' #80 #80000 #400000 #80 #0:2 #1 #8000020', 
    ' #0 #1 #40 #2000 #10 #1000 #0', ' #4000 #8000000 #0 #40 #10000000 #0 #4', 
    ' #0 #4000000 #40000000 #0:5 #1 #0:4 #2000', 
    ' #0:2 #80000 #0:3 #900 #0:7 #40000000 #0:5', 
    ' #40000 #0:4 #40000000 #0:4 #90 #0:2 #100000', 
    ' #2 #0:2 #10000000 #10 #0:27 #800 #0:5', ' #40 #0 #4000 ]', ), )
p.Set(nodes=nodes, name='Set-Sen2')
#: The set 'Set-Sen2' has been created (101 nodes).


# Create node set for sensor 3 (spiral) ...
# nodes to be selected indivisually 
p = mdb.models['Model-1'].parts['Merged']
n = p.nodes
nodes = n.getSequenceFromMask(mask=(
    '[#30400 #0:2 #fffff800 #7 #0:7 #7fffff80 ]', ), )
p.Set(nodes=nodes, name='Set-Sen3')
#: The set 'Set-Sen3' has been created (51 nodes).


# Create node set for top surface, to calculate the actuator angles
# phi, theta, and psi using another code (in Matlab) later
p = mdb.models['Model-1'].parts['Merged']
n = p.nodes
nodes = n.getSequenceFromMask(mask=('[#1c000000 ]', ), )
p.Set(nodes=nodes, name='Set-TopNodes')
#: The set 'Set-TopNodes' has been created (3 nodes).



########################################################################
# Define a reference point (RP), to apply twisting moment
# 3D parts don't have rotational DOF (i.e ur1,ur2 & ur3)
# but reference points do have

# this RP will be constrained (coupling) with the top edge of Elastosil
# part, using (couplingType=DISTRIBUTING)

session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Merged']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Merged']
v, e, d, n = p.vertices, p.edges, p.datums, p.nodes
p.ReferencePoint(point=v[28])
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, interactions=ON, constraints=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
a = mdb.models['Model-1'].rootAssembly
r1 = a.instances['Merged-1'].referencePoints
refPoints1=(r1[22], )
region1=regionToolset.Region(referencePoints=refPoints1)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Merged-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#2000040 #800 ]', ), )
region2=regionToolset.Region(edges=edges1)
mdb.models['Model-1'].Coupling(name='Cons-Coupling', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=DISTRIBUTING, 
    weightingMethod=UNIFORM, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, 
    ur2=ON, ur3=ON)



#########################################################################
# Generate Solver step, loads, and BC ........................


# Create step ...
# It looks like damping is causing staibility issues
# No damping provides better solution.
session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticStep(name='Step-Pressure', previous='Initial', 
    initialInc=0.05, maxInc=0.05, nlgeom=ON)
# mdb.models['Model-1'].StaticStep(name='Step-Pressure', previous='Initial', 
    # stabilizationMagnitude=0.0002, 
    # stabilizationMethod=DISSIPATED_ENERGY_FRACTION, 
    # continueDampingFactors=False, adaptiveDampingRatio=0.05, initialInc=0.05, 
    # maxInc=0.05, nlgeom=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='Step-Pressure')

# Enhance step solver (adding more iterations) ...
mdb.models['Model-1'].steps['Step-Pressure'].control.setValues(
    allowPropagation=OFF, resetDefaultValues=OFF, timeIncrementation=(4.0, 8.0, 
    9.0, 50.0, 40.0, 30.0, 12.0, 5.0, 6.0, 3.0, 50.0))

# Apply BC (Fixed base) ...
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Merged-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#0 #40 ]', ), )
region = regionToolset.Region(faces=faces1)
mdb.models['Model-1'].EncastreBC(name='BC-FixedBase', 
    createStepName='Step-Pressure', region=region, localCsys=None)


# Define pressure load (on tube 1, 2 & 3 respectively) ...
# this load will generate bending in XZ plane (no rotation)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['Merged-1'].surfaces['Surf-Tube1']
mdb.models['Model-1'].Pressure(name='Load-Press1', 
    createStepName='Step-Pressure', region=region, distributionType=UNIFORM, 
    field='', magnitude=0.05, amplitude=UNSET)

a = mdb.models['Model-1'].rootAssembly
region = a.instances['Merged-1'].surfaces['Surf-Tube2']
mdb.models['Model-1'].Pressure(name='Load-Press2', 
    createStepName='Step-Pressure', region=region, distributionType=UNIFORM, 
    field='', magnitude=0.2, amplitude=UNSET)

a = mdb.models['Model-1'].rootAssembly
region = a.instances['Merged-1'].surfaces['Surf-Tube3']
mdb.models['Model-1'].Pressure(name='Load-Press3', 
    createStepName='Step-Pressure', region=region, distributionType=UNIFORM, 
    field='', magnitude=0.05, amplitude=UNSET)


# Define twisting moment on RP (around z axis)
# let the moment direction follow the RP rotation
a = mdb.models['Model-1'].rootAssembly
r1 = a.instances['Merged-1'].referencePoints
refPoints1=(r1[22], )
region = regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].Moment(name='Load-Moment', 
    createStepName='Step-Pressure', region=region, cm3=5.0, 
    distributionType=UNIFORM, field='', localCsys=None, follower=ON)



#########################################################################
# Generate job ........................

a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='Job-SPA_3', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=70, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=8, 
    numDomains=8, numGPUs=2)


session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)