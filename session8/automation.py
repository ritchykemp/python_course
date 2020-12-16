import saga_api
import numpy as np

import sys, os

#########################################
saga_api.SG_Set_History_Depth(0)
saga_api.SG_UI_Msg_Lock(True)
if os.name == 'nt':    # Windows
    #os.environ['PATH'] = os.environ['PATH'] + ';' + os.environ['SAGA'] + str('/dll')
    saga_api.SG_Get_Tool_Library_Manager().Add_Directory(str('C:/PythonSAGA/SAGA/tools'), False)
else:                  # Linux
    os.environ['SAGA_MLB'] = '/usr/local/lib'
    #saga_api.SG_Get_Tool_Library_Manager().Add_Directory(os.environ['SAGA_MLB'], False)
    saga_api.SG_Get_Tool_Library_Manager().Add_Directory(str('/usr/local/lib'), False)        # Or set the Tool directory like this!
saga_api.SG_UI_Msg_Lock(False)

print('Python - Version ' + sys.version)
print(saga_api.SAGA_API_Get_Version())
print('number of loaded libraries: ' + str(saga_api.SG_Get_Tool_Library_Manager().Get_Count()))
print()


def Create_NonGreenPatches(Red,Nir, Count):

    #######################################
    ####### Step 1 ########################
    #######################################
    Tool = saga_api.SG_Get_Tool_Library_Manager().Create_Tool(str('grid_calculus'), 1)  # Calls a tool instance
    Parm = Tool.Get_Parameters()        # Gets the Parameters of a Tool Object

    # Parameters are set here:
    Parm('FORMULA'      ).Set_Value(str('ifelse(or(g1=0,g2=0), 1, (g1 - g2) / (g1 + g2))'))
    Parm('NAME').Set_Value(str("NDVI"))
    Parm('FNAME').Set_Value(False)
    Parm('USE_NODATA').Set_Value(False)
    Parm('TYPE').Set_Value(7)           # Datatype : int this case float
    Parm('GRIDS').asGridList().Add_Item(Nir)
    Parm('GRIDS').asGridList().Add_Item(Red)
    
    if Tool.Execute() == False:         # Executes the Tool
        print('Error: executing tool [' + Tool.Get_Name().c_str() + ']')
        saga_api.SG_Get_Tool_Library_Manager().Delete_Tool(Tool)
        return(False)
    Parm = Tool.Get_Parameters()
    Grid = Parm('RESULT').asGrid()
    Grid.Set_Name(saga_api.CSG_String('NDVI'))
    saga_api.SG_Get_Tool_Library_Manager().Delete_Tool(Tool)

    #######################################
    ####### Step 2 ########################
    #######################################
    Tool = saga_api.SG_Get_Tool_Library_Manager().Create_Tool(str('grid_tools'), 15)  # Calls a tool instance
    Parm = Tool.Get_Parameters()        # Gets the Parameters of a Tool Object
    Parm('INPUT').Set_Value(Grid)
    Parm('METHOD').Set_Value(0) 
    Parm('OLD').Set_Value(0.3) 
    Parm('NEW').Set_Value(-99999) 
    Parm('SOPERATOR').Set_Value(4)
    Parm('NODATAOPT').Set_Value(False)
    Parm('OTHEROPT').Set_Value(True)
    Parm('OTHERS').Set_Value(1)
    Parm('RESULT_TYPE').Set_Value(9)
    Parm('RESULT_NODATA_CHOICE').Set_Value(0)
    if Tool.Execute() == False:         # Executes the Tool
        print('Error: executing tool [' + Tool.Get_Name().c_str() + ']')
        saga_api.SG_Get_Tool_Library_Manager().Delete_Tool(Tool)
        return(False)
    Parm = Tool.Get_Parameters()
    GridMasked=Parm('RESULT').asGrid()
    GridMasked.Set_Name(saga_api.CSG_String('Mask'))
    saga_api.SG_Get_Tool_Library_Manager().Delete_Tool(Tool)

    #######################################
    ####### Step 3 ########################
    #######################################
    Tool = saga_api.SG_Get_Tool_Library_Manager().Create_Tool(str('shapes_grid'), 6)  # Calls a tool instance
    Parm = Tool.Get_Parameters()        # Gets the Parameters of a Tool Object
    Parm('GRID').Set_Value(GridMasked)
    Parm('CLASS_ALL').Set_Value(0)
    Parm('CLASS_ID').Set_Value(1)
    Parm('SPLIT').Set_Value(0)
    Parm('ALLVERTICES').Set_Value(False)
    
    if Tool.Execute() == False:         # Executes the Tool
        print('Error: executing tool [' + Tool.Get_Name().c_str() + ']')
        Polygons = False
        saga_api.SG_Get_Tool_Library_Manager().Delete_Tool(Tool)
        return(Polygons)
    
    Parm = Tool.Get_Parameters()
    Polygons = Parm('POLYGONS').asShapes()
    saga_api.SG_Get_Tool_Library_Manager().Delete_Tool(Tool)
    return Polygons

##############################################################
######### MAIN CODE ##########################################
##############################################################


NIRPath = str("session8/sentinel_NirChannel/")
RedPath = str("session8/sentinel_RedChannel/")

OutPath = str("session8/sentinel_Polygons/")
if not os.path.exists(OutPath):
    os.makedirs(OutPath)
#count = 0
#OutPolygons = Create_NonGreenPatches(RED,NIR,count)
#OutPolygons.Save("session8/PolygonTest.shp")

Count=0
for dataset in os.listdir(NIRPath):
    name, ext = os.path.splitext(dataset)
    if(ext == str(".sgrd")):
        print(NIRPath+dataset)
        Nir = saga_api.SG_Get_Data_Manager().Add_Grid(str(NIRPath+dataset))
        Red = saga_api.SG_Get_Data_Manager().Add_Grid(str(RedPath+dataset))
        Nir.Set_Name(saga_api.CSG_String('NIR'))
        Red.Set_Name(saga_api.CSG_String('Red'))
        
        print("Loaded")
        Polygons = Create_NonGreenPatches(Red,Nir, Count)
        if(Polygons != False):
            Polygons.Save(OutPath+name+".shp")
        print(saga_api.SG_Get_Data_Manager().Get_Summary().c_str())
        saga_api.SG_Get_Data_Manager().Delete_All()
        Count+=1
        
        
