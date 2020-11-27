import saga_api
import numpy as np
import math

Shapefile = saga_api.SG_Get_Data_Manager().Add_Shapes("Session6/PolygonsIn.shp")
count = Shapefile.Get_Count()

Polygons = []
for i in range(count):
    shape = Shapefile.Get_Shape(i)

    #Get Attributes
    name = shape.asString(0)
    ID = shape.asInt(1)
    Value = shape.asFloat(2)

    Polygon = []
    for ring in range(shape.Get_Part_Count()):
        Ring = []
        for pt in range(shape.Get_Point_Count(ring)):
            x = shape.Get_Point(pt, 0).x
            y = shape.Get_Point(pt, 0).y
            pt = (x,y)
            Ring.append(pt)
        Polygon.append(Ring)
    Polygons.append(Polygon)	

ShapeOut = saga_api.SG_Create_Shapes(saga_api.SHAPE_TYPE_Polygon, "Polygon", saga_api.CSG_Table(), saga_api.SG_VERTEX_TYPE_XY)
ShapeOut.Add_Field(saga_api.CSG_String("ID"), saga_api.SG_DATATYPE_Int)

shapeout = ShapeOut.Add_Shape()
shapeout.Set_Value(0,0)

for Polygon in Polygons:
    ring=0
    for Ring in Polygon:
        for vertex in Ring:
            shapeout.Add_Point(vertex[0],vertex[1],ring)
        ring+=1
ShapeOut.Save('Session6/PolygonsOut.shp')   