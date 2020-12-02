import math
import saga_api
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import scipy.stats as sst
from scipy.optimize import curve_fit

def Compute_Distance(x1,y1,x2,y2):
	Dist = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))
	return Dist

#############################
##### read Grid ############
############################

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



#############################
##### read shape ############
############################
Shapefile = saga_api.SG_Get_Data_Manager().Add_Shapes("session6/TrackUniSeegrube.shp") #gleichbedeutent mit eine Open befehl
count = Shapefile.Get_Count()

print(count)

PointList =[]
PointNames = []
for i in range(count):
    shape = Shapefile.Get_Shape(i)
    x = shape.Get_Point(0,0).x
    y = shape.Get_Point(0,0).y
    name = shape.asString(0)
    print (x,y,name)

    PointList.append([x,y])
    PointNames.append(name)
PointArray = np.array(PointList)
print(PointArray)

#Shapeout = kompletter Layer
ShapeOut = saga_api.SG_Create_Shapes(saga_api.SHAPE_TYPE_Point, "Track", saga_api.CSG_Table(), saga_api.SG_VERTEX_TYPE_XY)
ShapeOut.Add_Field(saga_api.CSG_String("DistCol"), saga_api.SG_DATATYPE_Float)
ShapeOut.Add_Field(saga_api.CSG_String("AccDistCol"), saga_api.SG_DATATYPE_Float)
ShapeOut.Add_Field(saga_api.CSG_String("Height"), saga_api.SG_DATATYPE_Float)

#exact das gleiche wie Session 4 

# übung5
Data = []

AccDist = 0
for i in range(1,len(PointArray)):
    x2 = PointArray[i,0]
    y2 = PointArray[i,1]
    x1 = PointArray[i-1,0]
    y1 = PointArray[i-1,1]
    Dist = Compute_Distance(x1,y1,x2,y2)
    AccDist += Dist

    gx = int((x2 -LLX)/Cellsize) #Differenz zwsichen wert & lower left corner des GRITS / Cellsize um in der richtigen spalte zu landen # 40 distanz Cellzise 4 --> wert 10
    gy = int((y2 -LLY)/Cellsize)
    Height = float(DTMArray[gy,gx])

    #Data List füllen
    Data.append([AccDist,Height])

Array = np.array(Data)
print(Array)

####################################
######### Scater Plot ##############
####################################

numBins = 100
stats = sst.binned_statistic(Array[:,0], Array[:,1], statistic='mean', bins=numBins, range=None)
stats_altitude = stats[1][0:numBins] #get centre of bin
stats_temp = (stats[0]) #get mean of all samples in bin

plt.plot(Array[:,0], Array[:,1],'r-') #'r." steht für Roter punkt ploten
plt.title("Höhenprofil Plot",fontsize=12)
plt.ylabel('Höhe in m')
plt.xlabel('Entfernung vom Ausgangaspunkt in m')
plt.savefig("session6/hoehenplot.png",dpi=300)
plt.close()