import saga_api
import numpy as np

DSM = saga_api.SG_Get_Data_Manager().Add_Grid("session8/DEM.sgrd")

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
AccummulationArray =np.empty((NY,NX))


HeightList =[]
for gy in range(NY):
    for gx in range(NX):

        zDSM= DSM.asFloat(gx, gy)
        DSMArray[gy,gx]=zDSM
        if zDSM == Nodata:
            AccummulationArray[gy,gx]=Nodata
        else:
            AccummulationArray[gy,gx]=1.0
            HeightList.append([zDSM,(gy,gx)])
HeightList.sort(reverse=True)
print(np.array(HeightList))


#############################################################################
######## All dataset imported ###############################################
#############################################################################
for element in HeightList:
    gy,gx=element[1]
    SearchValue = DSMArray[gy,gx]
    if(SearchValue == Nodata):
        continue
    NeighborValues = []

    mindHight = 999999.0
    min_gx =-1
    min_gy =-1
    ##### moving window approach
    for window_gy in range(gy-1,gy+2):
        for window_gx in range(gx-1,gx+2):
            if window_gx >= NX or window_gy >= NY or window_gx < 0 or window_gy < 0:
                continue
            NeighborValue = DSMArray[window_gy,window_gx]
            if NeighborValue == Nodata:
                continue
            DiffHeight = (NeighborValue - SearchValue)

            if DiffHeight < mindHight:
                mindHight =DiffHeight
                #vom niedrigsten wert des Windows wird sich die niedrigste Zelle bemerkt in den vorher definierten Variablen
                min_gx = window_gx 
                min_gy = window_gy

    FlowAccSearchCell = AccummulationArray[gy,gx]
    AccummulationArray[min_gy,min_gx]+=FlowAccSearchCell
            
    ########### end moving window #########
        
        

#############################################################################
######## Output #############################################################
#############################################################################
Out = saga_api.SG_Create_Grid(saga_api.SG_DATATYPE_Float,NX,NY,Cellsize,LLX,LLY,False)
Out.Assign_NoData()

print("Writing Raster...")
for gy in range(NY):
    for gx in range(NX):
        z = AccummulationArray[gy,gx]
        Out.Set_Value(gx,gy,z)
Out.Set_Name(saga_api.CSG_String("FlowAccumulation"))
Out.Save("session8/FlowAccumulation.sgrd")