import math
import numpy as np
import saga_api

##########################
### locale operationen ###
##########################
#local weil pixel immer an der gleichen stelle liegen

NIR = saga_api.SG_Get_Data_Manager().Add_Grid("session7/NIR_8B.sgrd")
Red = saga_api.SG_Get_Data_Manager().Add_Grid("session7/Red_4B.sgrd")
Green = saga_api.SG_Get_Data_Manager().Add_Grid("session7/Green_3B.sgrd")
SWIR = saga_api.SG_Get_Data_Manager().Add_Grid("session7/SWIR_11B.sgrd")

#Metadaten die für ein Grid relevant sind 
# Da metadaten von NIR und Red identisch sind --> gleiches Grid muss nur einmal ausgelesen werden 
Cellsize = NIR.Get_Cellsize()
LLX = NIR.Get_XMin()
LLY = NIR.Get_YMin()
NX= NIR.Get_NX()
NY= NIR.Get_NY()
Nodata= NIR.Get_NoData_Value()
print(Nodata)

#Downstream vom File to Array
print("Reading Raster...")
NIRArray = np.empty((NY,NX))
RedArray = np.empty((NY,NX))
GreenArray = np.empty((NY,NX))
SWIRArray = np.empty((NY,NX))

NDVI = np.empty((NY,NX))
NDSI = np.empty((NY,NX))
for gy in range(NY):
    for gx in range(NX):
        zNIR= NIR.asFloat(gx, gy) # Beim Array erst Zeilen dann Spalten
        zRed= Red.asFloat(gx, gy)
        NIRArray[gy,gx]=zNIR #Beim Grid erst Spalten dann Zeilen
        RedArray[gy,gx]=zRed
        if (zNIR+zRed) == 0:
            continue
        else:
            NDVI[gy,gx] = (zNIR-zRed)/(zNIR+zRed) 

        zGreen = Green.asFloat(gx, gy)
        zSWIR = SWIR.asFloat(gx, gy)
        GreenArray[gy,gx] =zGreen
        RedArray[gy,gx]= zSWIR

        NDSI[gy,gx] = (zGreen-zSWIR)/(zGreen+zSWIR)

        
print(NDVI)
##########################################################################
############## All dataset imported ######################################
##########################################################################


# von numpy 
# nRed = RedArray - DTMArray #es bleibt nur noch die Höhe der Objekte übrig 

##########################################################################
############## Output ####################################################
##########################################################################

#Upstream
print("Writing Raster ...")
Out_NDVI = saga_api.SG_Create_Grid(saga_api.SG_DATATYPE_Float,NX,NY,Cellsize,LLX,LLY,False)
Out_NDVI.Assign_NoData()
Out_NDSi = saga_api.SG_Create_Grid(saga_api.SG_DATATYPE_Float,NX,NY,Cellsize,LLX,LLY,False)
Out_NDSi.Assign_NoData()

for gy in range(NY):
    for gx in range(NX):
        z = NDVI[gy,gx]
        y = NDSI[gy,gx]
        Out_NDVI.Set_Value(gx,gy,z)
        Out_NDSi.Set_Value(gx,gy,y)

Out_NDVI.Save("session7/NDVI.sgrd")
Out_NDSi.Save("session7/NDSI.sgrd")
