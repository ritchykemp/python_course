import saga_api
import numpy as np
import math

##################################################
##### Übung 6 shapefile verändern ###############
##################################################

Shapefile = saga_api.SG_Get_Data_Manager().Add_Shapes("session6/Borders.shp")
count = Shapefile.Get_Count()

Lines =[]
for i in range(count):
    shape = Shapefile.Get_Shape(i)
    Line = []
    for pt in range(shape.Get_Point_Count(0)):
        x = shape.Get_Point(pt, 0).x
        y = shape.Get_Point(pt, 0).y
        pt = [x,y]
        Line.append(pt)
    Lines.append(Line)	

######################################################
########### All dataset imported #####################
######################################################


#######################################################
########## Output #####################################
#######################################################

ShapeOut = saga_api.SG_Create_Shapes(saga_api.SHAPE_TYPE_Polygon, "Tirol", saga_api.CSG_Table(), saga_api.SG_VERTEX_TYPE_XY)
ShapeOut.Add_Field(saga_api.CSG_String("ID"), saga_api.SG_DATATYPE_Int)

shapeout = ShapeOut.Add_Shape()
shapeout.Set_Value(0,0)
ring = 0

for border in Lines:
    print (border)
    for vertex in border:
        shapeout.Add_Point(vertex[0],vertex[1],ring)
    ring +=1
#sind mehrere Ringe in einem Polygon werden diese als Loch verrechnet 

ShapeOut.Save('session6/Tirol.shp')  