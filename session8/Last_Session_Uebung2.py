import saga_api
import numpy as np

DSM = saga_api.SG_Get_Data_Manager().Add_Grid("Session7/HoettingDSM.sgrd")

#Metadaten
Cellsize = DSM.Get_Cellsize()
LLX = DSM.Get_XMin()
LLY = DSM.Get_YMin()
NX= DSM.Get_NX()
NY= DSM.Get_NY()
Nodata= DSM.Get_NoData_Value()
print(Nodata)

print("Reading Raster...")
DSMArray = np.empty((NY,NX))
HeightDiffArray = np.empty((NY,NX))

for gy in range(NY):
    for gx in range(NX):

        zDSM= DSM.asFloat(gx, gy)
        DSMArray[gy,gx]=zDSM


#############################################################################
######## All dataset imported ###############################################
#############################################################################
for gy in range(NY):
    for gx in range(NX):
        SearchValue = DSMArray[gy,gx]
        NeighborValues = []
        ##### moving window approach
        for window_gy in range(gy-1,gy+2):
            for window_gx in range(gx-1,gx+2):
                if window_gx >= NX or window_gy >= NY or window_gx < 0 or window_gy < 0:
                    continue
                NeighborValue = DSMArray[window_gy,window_gx]
                DiffHeight = abs(SearchValue - NeighborValue)
                NeighborValues.append(DiffHeight)
        ########### end moving window #########
        SelectedValue = max(NeighborValues)
        HeightDiffArray[gy,gx]=SelectedValue


#############################################################################
######## Output #############################################################
#############################################################################
Out = saga_api.SG_Create_Grid(saga_api.SG_DATATYPE_Float,NX,NY,Cellsize,LLX,LLY,False)
Out.Assign_NoData()

print("Writing Raster...")
for gy in range(NY):
    for gx in range(NX):
        z = HeightDiffArray[gy,gx]
        Out.Set_Value(gx,gy,z)

Out.Save("Session7/HeightDiff.sgrd")