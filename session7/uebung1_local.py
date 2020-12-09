import math
import numpy as np
import saga_api

##########################
### locale operationen ###
##########################
#local weil pixel immer an der gleichen stelle liegen

DTM = saga_api.SG_Get_Data_Manager().Add_Grid("session7/HoettingDTM.sgrd")
DSM = saga_api.SG_Get_Data_Manager().Add_Grid("session7/HoettingDSM.sgrd")

#Metadaten die für ein Grid relevant sind 
# Da metadaten von DTM und DSM identisch sind --> gleiches Grid muss nur einmal ausgelesen werden 
Cellsize = DTM.Get_Cellsize()
LLX = DTM.Get_XMin()
LLY = DTM.Get_YMin()
NX= DTM.Get_NX()
NY= DTM.Get_NY()
Nodata= DTM.Get_NoData_Value()
print(Nodata)

#Downstream vom File to Array
print("Reading Raster...")
DTMArray = np.empty((NY,NX))
DSMArray = np.empty((NY,NX))
Mask = np.empty((NY,NX))
for gy in range(NY):
    for gx in range(NX):
        zDTM= DTM.asFloat(gx, gy) # Beim Array erst Zeilen dann Spalten
        zDSM= DSM.asFloat(gx, gy)
        DTMArray[gy,gx]=zDTM #Beim Grid erst Spalten dann Zeilen
        DTMArray[gy,gx]=zDSM
        if (zDSM-zDTM) > 5:
            Mask[gy,gx]=Nodata
        else:
            Mask[gy,gx]=1
        #nDSM[gy,gx]=zDSM-zDTM

##########################################################################
############## All dataset imported ######################################
##########################################################################


# von numpy 
# nDSM = DSMArray - DTMArray #es bleibt nur noch die Höhe der Objekte übrig 

##########################################################################
############## Output ####################################################
##########################################################################

#Upstream
print("Writing Raster ...")
Out = saga_api.SG_Create_Grid(saga_api.SG_DATATYPE_Float,NX,NY,Cellsize,LLX,LLY,False)
Out.Assign_NoData()

for gy in range(NY):
    for gx in range(NX):
        z = Mask[gy,gx]
        Out.Set_Value(gx,gy,z)

Out.Save("session7/Mask.sgrd")
