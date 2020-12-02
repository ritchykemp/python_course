import saga_api
import numpy as np

Grid = saga_api.SG_Get_Data_Manager().Add_Grid("session6/DTM_Innsbruck.sgrd")

#Metadaten die für ein Grid relevant sind 
Cellsize = Grid.Get_Cellsize()
LLX = Grid.Get_XMin()
LLY = Grid.Get_YMin()
NX= Grid.Get_NX()
NY= Grid.Get_NY()
Nodata= Grid.Get_NoData_Value()
print(Nodata)

#Downstream vom File to Array
print("Reading Raster...")
DTMArray = np.empty((NY,NX))
for gy in range(NY):
    for gx in range(NX):
        z= Grid.asFloat(gx, gy) # Beim Array erst Zeilen dann Spalten
        DTMArray[gy,gx]=z #Beim Grid erst Spalten dann Zeilen

#ab hier könnte man das numpy array verändern, analysieren ...
#z.b. Werte um 1000m erhöhen
DTMArray[:,2] = DTMArray[:,2] + 1000
print(DTMArray)
#Upstream
print("Writing Raster ...")
GridOut = saga_api.SG_Create_Grid(saga_api.SG_DATATYPE_Float,NX,NY,Cellsize,LLX,LLY,False)
GridOut.Assign_NoData()

for gy in range(NY):
    for gx in range(NX):
        z = DTMArray[gy,gx]
        GridOut.Set_Value(gx,gy,z)

GridOut.Save("session6/Grid_Out.shp")

