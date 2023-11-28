# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2020 
# Run by Abdullah Al-Azzawi on 30 Sep 2021
#
# We have made the source codes for the simulations conducted in this study available 
# on our GitHub repository: {https://github.com/abd-alaz/spiral-sensors}. Interested 
# readers can access and download the codes for a closer examination of the implementations
# and methods employed. The codes are open-source and provided under the GNU General 
# Public License v3.0, allowing for academic and non-commercial use.
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...

from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=270.0, 
    height=180.0)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
mdb.models.changeKey(fromName='Model-1', toName='SPA_Connolly')
session.viewports['Viewport: 1'].setValues(displayedObject=None)
mdb.saveAs(pathName='D:/Abaqus_temp/SPA_F_Connolly.cae')
#: The model database has been saved to "D:\Abaqus_temp\SPA_F_Connolly.cae".


# Create parts ....................

s = mdb.models['SPA_Connolly'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(6.35, 0.0))
s.offset(distance=2.0, objectList=(g[2], ), side=RIGHT)
p = mdb.models['SPA_Connolly'].Part(name='Tube', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['SPA_Connolly'].parts['Tube']
p.BaseSolidExtrude(sketch=s, depth=165.0)
s.unsetPrimaryObject()
p = mdb.models['SPA_Connolly'].parts['Tube']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['SPA_Connolly'].sketches['__profile__']
s1 = mdb.models['SPA_Connolly'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(8.35, 0.0))
p = mdb.models['SPA_Connolly'].Part(name='Bottom', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['SPA_Connolly'].parts['Bottom']
p.BaseSolidExtrude(sketch=s1, depth=2.0)
s1.unsetPrimaryObject()
p = mdb.models['SPA_Connolly'].parts['Bottom']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['SPA_Connolly'].sketches['__profile__']
p1 = mdb.models['SPA_Connolly'].parts['Bottom']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['SPA_Connolly'].Part(name='Endcap', 
    objectToCopy=mdb.models['SPA_Connolly'].parts['Bottom'])
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)

p = mdb.models['SPA_Connolly'].parts['Endcap']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#2 ]', ), )
v, e, d = p.vertices, p.edges, p.datums
p.PartitionFaceByShortestPath(point1=v[0], faces=pickedFaces, 
    point2=p.InterestingPoint(edge=e[0], rule=MIDDLE))
p = mdb.models['SPA_Connolly'].parts['Endcap']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#5 ]', ), )
v1, e1, d1 = p.vertices, p.edges, p.datums
p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
    edge=e1[2], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[1], 
    rule=MIDDLE))



# Define materials ....................

mdb.models['SPA_Connolly'].Material(name='Elastosil_M4601')
mdb.models['SPA_Connolly'].materials['Elastosil_M4601'].Density(table=((
    1.13e-09, ), ))
mdb.models['SPA_Connolly'].materials['Elastosil_M4601'].Hyperelastic(
    materialType=ISOTROPIC, testData=OFF, type=YEOH, 
    volumetricResponse=VOLUMETRIC_DATA, table=((0.11, 0.02, 0.0, 0.0, 0.0, 
    0.0), ))

mdb.models['SPA_Connolly'].Material(name='PET_Ortho')
mdb.models['SPA_Connolly'].materials['PET_Ortho'].Density(table=((13.5e-10, ), ))
mdb.models['SPA_Connolly'].materials['PET_Ortho'].Elastic(type=LAMINA, 
    table=((6000.0, 0.001, 0.37, 1.0, 1.0, 1.0), ))

# mdb.models['SPA_Connolly'].Material(name='Paper')
# mdb.models['SPA_Connolly'].materials['Paper'].Density(table=((1e-10, ), ))
# mdb.models['SPA_Connolly'].materials['Paper'].Elastic(table=((0.1, 0.0), ))

mdb.models['SPA_Connolly'].Material(name='SSteel')
mdb.models['SPA_Connolly'].materials['SSteel'].Density(table=((7.93e-09, ), ))
mdb.models['SPA_Connolly'].materials['SSteel'].Elastic(table=((193000.0, 
    0.305), ))



# Define sections ....................

mdb.models['SPA_Connolly'].HomogeneousSolidSection(name='Sec-SSteel', 
    material='SSteel', thickness=None)

mdb.models['SPA_Connolly'].HomogeneousSolidSection(name='Sec-Elastosil', 
    material='Elastosil_M4601', thickness=None)

# mdb.models['SPA_Connolly'].HomogeneousShellSection(name='Sec-Paper', 
    # preIntegrate=OFF, material='Paper', thicknessType=UNIFORM, thickness=0.1, 
    # thicknessField='', nodalThicknessField='', idealization=NO_IDEALIZATION, 
    # poissonDefinition=DEFAULT, thicknessModulus=None, temperature=GRADIENT, 
    # useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)

mdb.models['SPA_Connolly'].HomogeneousShellSection(name='Sec-PETO', 
    preIntegrate=OFF, material='PET_Ortho', thicknessType=UNIFORM, 
    thickness=0.1, thicknessField='', nodalThicknessField='', 
    idealization=NO_IDEALIZATION, poissonDefinition=DEFAULT, 
    thicknessModulus=None, temperature=GRADIENT, useDensity=OFF, 
    integrationRule=SIMPSON, numIntPts=5)





# Assembly .....................................

a = mdb.models['SPA_Connolly'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['SPA_Connolly'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['SPA_Connolly'].parts['Bottom']
a.Instance(name='Bottom-1', part=p, dependent=ON)
p = mdb.models['SPA_Connolly'].parts['Endcap']
a.Instance(name='Endcap-1', part=p, dependent=ON)
p = mdb.models['SPA_Connolly'].parts['Tube']
a.Instance(name='Tube-1', part=p, dependent=ON)
p = a.instances['Endcap-1']
p.translate(vector=(18.37, 0.0, 0.0))
p = a.instances['Tube-1']
p.translate(vector=(36.74, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a = mdb.models['SPA_Connolly'].rootAssembly
a.rotate(instanceList=('Bottom-1', ), axisPoint=(-8.35, 0.0, 2.0), 
    axisDirection=(16.7, 0.0, 0.0), angle=-90.0)
#: The instance Bottom-1 was rotated by -90. degrees about the axis defined by the point -8.35, 0., 2. and the vector 16.7, 0., 0.
a = mdb.models['SPA_Connolly'].rootAssembly
a.translate(instanceList=('Bottom-1', ), vector=(0.0, 0.0, -2.0))
#: The instance Bottom-1 was translated by 0., 0., -2. with respect to the assembly coordinate system

a = mdb.models['SPA_Connolly'].rootAssembly
f1 = a.instances['Tube-1'].faces
f2 = a.instances['Bottom-1'].faces
a.FaceToFace(movablePlane=f1[3], fixedPlane=f2[1], flip=ON, clearance=0.0)
a = mdb.models['SPA_Connolly'].rootAssembly
v1 = a.instances['Tube-1'].vertices
v2 = a.instances['Bottom-1'].vertices
a.CoincidentPoint(movablePoint=v1[1], fixedPoint=v2[0])
a = mdb.models['SPA_Connolly'].rootAssembly
f1 = a.instances['Tube-1'].faces
f2 = a.instances['Bottom-1'].faces
a.Coaxial(movableAxis=f1[0], fixedAxis=f2[0], flip=OFF)
#: The instance "Tube-1" is fully constrained

a = mdb.models['SPA_Connolly'].rootAssembly
f1 = a.instances['Endcap-1'].faces
f2 = a.instances['Tube-1'].faces
a.FaceToFace(movablePlane=f1[5], fixedPlane=f2[2], flip=ON, clearance=0.0)
a = mdb.models['SPA_Connolly'].rootAssembly
v1 = a.instances['Endcap-1'].vertices
v2 = a.instances['Tube-1'].vertices
a.CoincidentPoint(movablePoint=v1[5], fixedPoint=v2[0])
a = mdb.models['SPA_Connolly'].rootAssembly
f1 = a.instances['Endcap-1'].faces
f2 = a.instances['Tube-1'].faces
a.Coaxial(movableAxis=f1[3], fixedAxis=f2[0], flip=OFF)
#: The instance "Endcap-1" is fully constrained

a = mdb.models['SPA_Connolly'].rootAssembly
a.InstanceFromBooleanMerge(name='Merged', instances=(a.instances['Bottom-1'], 
    a.instances['Endcap-1'], a.instances['Tube-1'], ), keepIntersections=ON, 
    originalInstances=SUPPRESS, domain=GEOMETRY)


# create skin for the tube to apply the ortho layer
p1 = mdb.models['SPA_Connolly'].parts['Merged']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['SPA_Connolly'].parts['Merged']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.Skin(faces=faces, name='SPA_Skin')




# Section assignments ................

p = mdb.models['SPA_Connolly'].parts['Merged']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#2 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['SPA_Connolly'].parts['Merged']
p.SectionAssignment(region=region, sectionName='Sec-SSteel', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)

p = mdb.models['SPA_Connolly'].parts['Merged']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['SPA_Connolly'].parts['Merged']
p.SectionAssignment(region=region, sectionName='Sec-SSteel', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.setValues(activeCutName='Y-Plane', 
    viewCut=ON)

p = mdb.models['SPA_Connolly'].parts['Merged']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#4 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['SPA_Connolly'].parts['Merged']
p.SectionAssignment(region=region, sectionName='Sec-Elastosil', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.setValues(activeCutName='Y-Plane', 
    viewCut=OFF)

p = mdb.models['SPA_Connolly'].parts['Merged']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(skinFaces=(('SPA_Skin', faces), ))
p = mdb.models['SPA_Connolly'].parts['Merged']
p.SectionAssignment(region=region, sectionName='Sec-PETO', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
region=p.Set(skinFaces=(('SPA_Skin', faces), ), name='Set-skin')
mdb.models['SPA_Connolly'].parts['Merged'].sectionAssignments[3].setValues(
    region=region)



# Create step, and apply load ......................

# create surface to apply pressure (i.e. inner surface)
p = mdb.models['SPA_Connolly'].parts['Merged']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#902 ]', ), )
p.Surface(side1Faces=side1Faces, name='Surf-pressure')
#: The surface 'Surf-pressure' has been created (3 faces).

# create a step and apply pressure loading, use damping to enhance convergence
a = mdb.models['SPA_Connolly'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['SPA_Connolly'].StaticStep(name='Step-Pressure', previous='Initial',
    stabilizationMagnitude=0.0002, stabilizationMethod=DISSIPATED_ENERGY_FRACTION, 
    continueDampingFactors=False, initialInc=0.1, maxInc=0.1, nlgeom=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='Step-Pressure')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
a = mdb.models['SPA_Connolly'].rootAssembly
region = a.instances['Merged-1'].surfaces['Surf-pressure']
mdb.models['SPA_Connolly'].Pressure(name='Load-Pressure', 
    createStepName='Step-Pressure', region=region, distributionType=UNIFORM, 
    field='', magnitude=0.06205, amplitude=UNSET)

# # Enhance solver iterations for better accuracy
a = mdb.models['SPA_Connolly'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='Step-Pressure')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['SPA_Connolly'].steps['Step-Pressure'].control.setValues(
    allowPropagation=OFF, resetDefaultValues=OFF, timeIncrementation=(4.0, 8.0, 
    9.0, 50.0, 40.0, 30.0, 12.0, 5.0, 6.0, 3.0, 50.0))


# create boundary conditions (fixed base)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
a = mdb.models['SPA_Connolly'].rootAssembly
f1 = a.instances['Merged-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#1000 ]', ), )
region = regionToolset.Region(faces=faces1)
mdb.models['SPA_Connolly'].EncastreBC(name='BC-FixedBase', 
    createStepName='Initial', region=region, localCsys=None)

# Create boundary condition for the top end to move vertically only (no movement in Z and X)
# with low desnity mesh, the solver generates lateral movement (i.e in x and z )
a1 = mdb.models['SPA_Connolly'].rootAssembly
v1 = a1.instances['Merged-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#20 ]', ), )
region = regionToolset.Region(vertices=verts1)
mdb.models['SPA_Connolly'].DisplacementBC(name='BC-top', 
    createStepName='Initial', region=region, u1=SET, u2=UNSET, u3=SET, 
    ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET, distributionType=UNIFORM, 
    fieldName='', localCsys=None)



# Create mesh ...........................
# using C3D10HS: A 10-node general purpose quadratic tetrahedron 
#                with improved surface stress visualization.
# seed = 2.5 
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p1 = mdb.models['SPA_Connolly'].parts['Merged']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['SPA_Connolly'].parts['Merged']
p.seedPart(size=2.5, deviationFactor=0.1, minSizeFactor=0.1)
# mesh control, element shape = Tet (for solids)
p = mdb.models['SPA_Connolly'].parts['Merged']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#7 ]', ), )
p.setMeshControls(regions=pickedRegions, elemShape=TET, technique=FREE)
elemType1 = mesh.ElemType(elemCode=C3D20R)
elemType2 = mesh.ElemType(elemCode=C3D15)
elemType3 = mesh.ElemType(elemCode=C3D10)
p = mdb.models['SPA_Connolly'].parts['Merged']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#7 ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
# element type = standard, quadratic
elemType1 = mesh.ElemType(elemCode=C3D20R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D15, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D10HS, elemLibrary=STANDARD)
p = mdb.models['SPA_Connolly'].parts['Merged']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#7 ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))


# # mesh control, element shape = Tri (for surfaces)
elemType1 = mesh.ElemType(elemCode=S8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=STRI65, elemLibrary=STANDARD)
p = mdb.models['SPA_Connolly'].parts['Merged']
pickedRegions = p.sets['Set-skin']
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))


# generate mesh ...
p = mdb.models['SPA_Connolly'].parts['Merged']
p.generateMesh()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	




# create job for analysis ...
myJobName = 'Job-spacon'
myModel = 'SPA_Connolly'
jobDescription = ''
myViewport = 'Viewport: 1'

a = mdb.models[myModel].rootAssembly
a.regenerate()
session.viewports[myViewport].setValues(displayedObject=a)
session.viewports[myViewport].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name=myJobName, model=myModel, description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=70, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=8, 
    numDomains=8, numGPUs=2)



