# A script to read the Abaqus/CAE Visualization module tutorial
# output database and read displacement data from the node at
# the center of the hemispherical punch.

# Generated via ABAQUS 2020 
# by Abdullah Al-Azzawi 
# on 26.Nov.2021

# We have made the source codes for the simulations conducted in this study available 
# on our GitHub repository: {https://github.com/abd-alaz/spiral-sensors}. Interested 
# readers can access and download the codes for a closer examination of the implementations
# and methods employed. The codes are open-source and provided under the GNU General 
# Public License v3.0, allowing for academic and non-commercial use.

print ' ----------------------------------------------------'
print 'A script to read the Abaqus/CAE Visualization data'
print ' ----------------------------------------------------'

from abaqusConstants import *
from odbAccess import *

import numpy as np              # to work with float arrays
import scipy.io                 # to export variables to matlab


# each soft sensor is represented as an Edge with node sets
# to get the initial location (x,y,z) of each node, use model database (mdb)
# to get the deformation results (ux,uy,uz) for each node, use output database (odb)

# Also, to calculate top surface rotation, 3 nodes were selected in 'Set-topNodes'
# the code will extract their intial location (x,y,z), and displacement (U1,U2,U3)
# for all time frames.

# ----------------------------------------------

mdl = 'Model-1'             # model name
minst = 'Merged-1'          # model instance
mnst1 = 'Set-Sen1'          # model node set for sensor 1
mnst2 = 'Set-Sen2'          # model node set for sensor 2
mnst3 = 'Set-Sen3'          # model node set for sensor 3
mnstt = 'Set-TopNodes'      # model node set for top surface nodes
mnstc = 'Set-Centreline'    # model node set for centreline

# Create variables that refer to each node set in the mdb.
# Each set is associated with the part instance 'Merged-1'.
Sen1_M = mdb.models[mdl].rootAssembly.instances[minst].sets[mnst1].nodes
Sen2_M = mdb.models[mdl].rootAssembly.instances[minst].sets[mnst2].nodes
Sen3_M = mdb.models[mdl].rootAssembly.instances[minst].sets[mnst3].nodes
tpnd_M = mdb.models[mdl].rootAssembly.instances[minst].sets[mnstt].nodes
ctln_M = mdb.models[mdl].rootAssembly.instances[minst].sets[mnstc].nodes

# define 2D float arrays to hold the node labels and x,y,z locations 
Sen1_Loc = np.zeros((len(Sen1_M),4))   # 4 colmuns: label, x, y, z
Sen2_Loc = np.zeros((len(Sen2_M),4))
Sen3_Loc = np.zeros((len(Sen3_M),4))
tpnd_Loc = np.zeros((len(tpnd_M),4))
ctln_Loc = np.zeros((len(ctln_M),4))


# extract data

for idx, val in enumerate(Sen1_M):   # get both index and value
    Sen1_Loc[idx,0] = val.label                  # node ID
    Sen1_Loc[idx,1] = val.coordinates[0]         # x-location
    Sen1_Loc[idx,2] = val.coordinates[1]         # y-location
    Sen1_Loc[idx,3] = val.coordinates[2]         # z-location

for idx, val in enumerate(Sen2_M):   # get both index and value
    Sen2_Loc[idx,0] = val.label                  # node ID
    Sen2_Loc[idx,1] = val.coordinates[0]         # x-location
    Sen2_Loc[idx,2] = val.coordinates[1]         # y-location
    Sen2_Loc[idx,3] = val.coordinates[2]         # z-location

for idx, val in enumerate(Sen3_M):   # get both index and value
    Sen3_Loc[idx,0] = val.label                  # node ID
    Sen3_Loc[idx,1] = val.coordinates[0]         # x-location
    Sen3_Loc[idx,2] = val.coordinates[1]         # y-location
    Sen3_Loc[idx,3] = val.coordinates[2]         # z-location

for idx, val in enumerate(tpnd_M):   # get both index and value
    tpnd_Loc[idx,0] = val.label                  # node ID
    tpnd_Loc[idx,1] = val.coordinates[0]         # x-location
    tpnd_Loc[idx,2] = val.coordinates[1]         # y-location
    tpnd_Loc[idx,3] = val.coordinates[2]         # z-location

for idx, val in enumerate(ctln_M):   # get both index and value
    ctln_Loc[idx,0] = val.label                  # node ID
    ctln_Loc[idx,1] = val.coordinates[0]         # x-location
    ctln_Loc[idx,2] = val.coordinates[1]         # y-location
    ctln_Loc[idx,3] = val.coordinates[2]         # z-location





# ----------------------------------------------

# odb = openOdb(path='D:/Abaqus_temp/Job-1.odb',readOnly=TRUE)

odbName = 'Job-SPA_3.odb'
stpName = 'Step-Pressure'   # odb step
oinst = 'MERGED-1'          # odb instance
onst1 = 'SET-SEN1'          # odb node set for sensor 1
onst2 = 'SET-SEN2'          # odb node set for sensor 2
onst3 = 'SET-SEN3'          # odb node set for sensor 3
onstt = 'SET-TOPNODES'      # odb node set for top surface nodes
onstc = 'SET-CENTRELINE'    # odb node set for centreline

odb = session.odbs[odbName]		# handle for odb object 

# Create variables that refers to each node set in the odb.
# The set is associated with the part instance 'MERGED-1'.
Sen1_O = odb.rootAssembly.instances[oinst].nodeSets[onst1]
Sen2_O = odb.rootAssembly.instances[oinst].nodeSets[onst2]
Sen3_O = odb.rootAssembly.instances[oinst].nodeSets[onst3]
tpnd_O = odb.rootAssembly.instances[oinst].nodeSets[onstt]
ctln_O = odb.rootAssembly.instances[oinst].nodeSets[onstc]

# creat a vector for all frames in the selected step
allfrms = odb.steps[stpName].frames	

# define 3D float arrays to hold the node results for each sets
# first dim size = node counts,
# second dim size = time increments
# third dim for node labels, time, and displacement values (U1,U2,U3) 
Sen1_Rst = np.zeros((len(Sen1_M),len(allfrms),5))
Sen2_Rst = np.zeros((len(Sen2_M),len(allfrms),5))
Sen3_Rst = np.zeros((len(Sen3_M),len(allfrms),5))
tpnd_Rst = np.zeros((len(tpnd_M),len(allfrms),5))
ctln_Rst = np.zeros((len(ctln_M),len(allfrms),5))



# create a loop to read results from all frames
for frm in allfrms:


    # Create a variable that refers to the displacement 'U'
    # in the current frame for 'SET-1' node set
    # same variable will be used for each set to
    # extract field output values for each node
    
    # for sensor 1 ...
    displ = frm.fieldOutputs['U'].getSubset(region=Sen1_O)
        
    for idx, val in enumerate(displ.values):
        
       Sen1_Rst[idx,frm.frameId,0] = val.nodeLabel      # node ID
       Sen1_Rst[idx,frm.frameId,1] = frm.frameValue     # current time
       Sen1_Rst[idx,frm.frameId,2] = val.data[0]        # U1 displacement
       Sen1_Rst[idx,frm.frameId,3] = val.data[1]        # U2 displacement
       Sen1_Rst[idx,frm.frameId,4] = val.data[2]        # U3 displacement
    
    
    # for sensor 2 ...
    displ = frm.fieldOutputs['U'].getSubset(region=Sen2_O)
        
    for idx, val in enumerate(displ.values):
        
       Sen2_Rst[idx,frm.frameId,0] = val.nodeLabel      # node ID
       Sen2_Rst[idx,frm.frameId,1] = frm.frameValue     # current time
       Sen2_Rst[idx,frm.frameId,2] = val.data[0]        # U1 displacement
       Sen2_Rst[idx,frm.frameId,3] = val.data[1]        # U2 displacement
       Sen2_Rst[idx,frm.frameId,4] = val.data[2]        # U3 displacement
    
    
    # for sensor 3 ...
    displ = frm.fieldOutputs['U'].getSubset(region=Sen3_O)
        
    for idx, val in enumerate(displ.values):
        
       Sen3_Rst[idx,frm.frameId,0] = val.nodeLabel      # node ID
       Sen3_Rst[idx,frm.frameId,1] = frm.frameValue     # current time
       Sen3_Rst[idx,frm.frameId,2] = val.data[0]        # U1 displacement
       Sen3_Rst[idx,frm.frameId,3] = val.data[1]        # U2 displacement
       Sen3_Rst[idx,frm.frameId,4] = val.data[2]        # U3 displacement
    
    
    # for top nodes ...
    displ = frm.fieldOutputs['U'].getSubset(region=tpnd_O)
        
    for idx, val in enumerate(displ.values):
        
       tpnd_Rst[idx,frm.frameId,0] = val.nodeLabel      # node ID
       tpnd_Rst[idx,frm.frameId,1] = frm.frameValue     # current time
       tpnd_Rst[idx,frm.frameId,2] = val.data[0]        # U1 displacement
       tpnd_Rst[idx,frm.frameId,3] = val.data[1]        # U2 displacement
       tpnd_Rst[idx,frm.frameId,4] = val.data[2]        # U3 displacement
    
    
    # for centreline ...
    displ = frm.fieldOutputs['U'].getSubset(region=ctln_O)
        
    for idx, val in enumerate(displ.values):
        
       ctln_Rst[idx,frm.frameId,0] = val.nodeLabel      # node ID
       ctln_Rst[idx,frm.frameId,1] = frm.frameValue     # current time
       ctln_Rst[idx,frm.frameId,2] = val.data[0]        # U1 displacement
       ctln_Rst[idx,frm.frameId,3] = val.data[1]        # U2 displacement
       ctln_Rst[idx,frm.frameId,4] = val.data[2]        # U3 displacement
    
    





# export data to matalb variable (.mat)

scipy.io.savemat('SPA_multi3_results.mat', 
    dict(Sen1_Loc = Sen1_Loc, Sen2_Loc = Sen2_Loc, Sen3_Loc = Sen3_Loc,
    TopNodes_Loc = tpnd_Loc, CntrLn_Loc = ctln_Loc,
    Sen1_Rst = Sen1_Rst, Sen2_Rst = Sen2_Rst, Sen3_Rst = Sen3_Rst,
    TopNodes_Rst = tpnd_Rst, CntrLn_Rst = ctln_Rst,    
    totFrames = len(allfrms)))


print 'Data export has completed successfully'
print ' ----------------------------------------------------'




# # Create a variable that refers to the
# # last frame of the selected step.
# lastFrame = odb.steps['Step-Pressure'].frames[-1]

# # Create a variable that refers to the displacement of the
# # node set in the last frame of the first step.
# centerDisplacement = displacement.getSubset(region=EdgeNd_O)


# pp = []

# # Finally, print some field output data from each node
# # in the node set (a single node in this example).
# for v in centerDisplacement.values:
    # # print 'Position = ', v.position,'Type = ',v.type
    # # print 'Node label = ', v.nodeLabel
    # # print 'X displacement = ', v.data[0]
    # # print 'Y displacement = ', v.data[1]
    # # print 'Z displacement = ', v.data[2]
    # # print 'Displacement magnitude =', v.magnitude
    
    # pp.append(v.nodeLabel)

# # odb.close()



# with open('readme.txt', 'w') as f:
    # # writing first line 
    # f.write('nodeID, x0,y0,z0,dx,dy,dz')
    # for line in lines:
        # f.write(line)
        # f.write('\n')

    
    # f.close()
    











# pp are sorted based on ID, should be sorted based on location
# best approach will be using initial 'height' location which is y-axis
 
# session.Path(name='Path-1', type=NODE_LIST, expression=(('Merged-1', (pp)), ))





# The resulting output is
# Position = NODAL Type = VECTOR
# Node label = 1000
# X displacement = -8.29017850095e-34
# Y displacement = -76.4554519653
# Displacement magnitude = 76.4554519653




# print 'Node = %d U[x] = %6.4f, U[y] = %6.4f' % (v.nodeLabel, v.data[0], v.data[1])
# the result is
# Node = 3 U[x] = -0.0000, U[y] = -64.6314