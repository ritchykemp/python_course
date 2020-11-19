import math
import mytools
import saga_api
import scipy
import scipy.spatial 
import matplotlib


# open shape file (point)
Shapefile = saga_api.SG_Get_Data_Manager().Add_Shapes("TrackUniSeegrube.shp")

# create empty shape file with 3 attributes (point)
ShapesOut = saga_api.SG_Create_Shapes(saga_api.SHAPE_TYPE_Point, "Output", saga_api.CSG_Table(), saga_api.SG_VERTEX_TYPE_XY)
ShapesOut.Add_Field(saga_api.CSG_String("Z"), saga_api.SG_DATATYPE_Double)
ShapesOut.Add_Field(saga_api.CSG_String("Distance"), saga_api.SG_DATATYPE_Double)
ShapesOut.Add_Field(saga_api.CSG_String("Name"), saga_api.SG_DATATYPE_String)