import math
import numpy as np
import saga_api

DSM = saga_api.SG_Get_Data_Manager().Add_Grid("session7/HoettingDSM.sgrd")
###########################################################
############# focal operation ############################
###########################################################


#Metadaten die für ein Grid relevant sind 
# Da metadaten von DTM und DSM identisch sind --> gleiches Grid muss nur einmal ausgelesen werden 
Cellsize = DSM.Get_Cellsize()
LLX = DSM.Get_XMin()
LLY = DSM.Get_YMin()
NX= DSM.Get_NX()
NY= DSM.Get_NY()
Nodata= DSM.Get_NoData_Value()
print(Nodata)


#Downstream vom File to Array
print("Reading Raster...")
DSMArray = np.empty((NY,NX))
HeightDiffArray = np.empty((NY,NX))

for gy in range(NY):
    for gx in range(NX):
        zDSM= DSM.asFloat(gx, gy)
        DSMArray[gy,gx]=zDSM
        

##########################################################################
############## All dataset imported ######################################
##########################################################################


#b) Probiere das ganze mit anderen Fenstergrößen! Was verändert sich?

#schritt für schritt zu jeder Zelle & lese den Höhenwert aus 
for gy in range(NY):
    for gx in range(NX):
        searchValue= DSMArray[gy,gx] #wert der in der Mitte steht 
        NeighborValues =[]
        #Abfrage Aller benachtbaren Pixel um den SearchValue herum 

        ##### moving window approach #####
        # Aufgabe i) für jedes Pixel eine 5*5 Pixelumgebung auswerten 
        for window_gy in range(gy-5,gy+6): #verändern der Fenster größe #je kleiner das Fenster desto feiner ist die Abstufung
            for window_gx in range(gx-5,gx+6): # je größer das Fenster desto "weicher" ist das GRID
                if window_gx >= NX or window_gy >= NY or window_gx < 0 or window_gy < 0:
                    continue
                NeighborValue = DSMArray[window_gy,window_gx]
                DiffHeight = abs(searchValue - NeighborValue)
                NeighborValues.append(DiffHeight)
        #######end moving window approach #######

        #ii) dabei der mittlere Geländehöhenwert berechnet werden und #np.mean
        SelectedValue =np.mean(NeighborValues) 

        # iii) der jeweilige Mittelwert in der zentralen Zelle gespeichert werden.
        HeightDiffArray[gy,gx] =SelectedValue

                


##########################################################################
############## Output ####################################################
##########################################################################

#Upstream
print("Writing Raster ...")
Out = saga_api.SG_Create_Grid(saga_api.SG_DATATYPE_Float,NX,NY,Cellsize,LLX,LLY,False)
Out.Assign_NoData()

for gy in range(NY):
    for gx in range(NX):
        z = HeightDiffArray[gy,gx]
        Out.Set_Value(gx,gy,z)

Out.Save("session7/HeightDiff5x5window.sgrd")
