import saga_api
import numpy as np
import math

Shapefile = saga_api.SG_Get_Data_Manager().Add_Shapes("Session6/LineIn.shp")
count = Shapefile.Get_Count()

Lines = []
for i in range(count):
    shape = Shapefile.Get_Shape(i)
    
    #Get Attributes
    name = shape.asString(0)
    ID = shape.asInt(1)
    Value = shape.asFloat(2)

    Line = []
    for pt in range(shape.Get_Point_Count(0)):
        x = shape.Get_Point(pt, 0).x
        y = shape.Get_Point(pt, 0).y
        pt = (x,y)
        Line.append(pt)
    Lines.append(Line)

ShapeOut = saga_api.SG_Create_Shapes(saga_api.SHAPE_TYPE_Line, "Line", saga_api.CSG_Table(), saga_api.SG_VERTEX_TYPE_XY)
ShapeOut.Add_Field(saga_api.CSG_String("ID"), saga_api.SG_DATATYPE_Int)


for Line in Lines:
    shapeout = ShapeOut.Add_Shape()
    shapeout.Set_Value(0,0) # write attribute
    for vertex in Line:
        shapeout.Add_Point(vertex[0],vertex[1],0)
ShapeOut.Save('Session6/LinesOut.shp')   	