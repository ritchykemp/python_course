
from osgeo import ogr
import os
import numpy as np
from math import *

# File lesen
driver = ogr.GetDriverByName('ESRI Shapefile') 
datasource = driver.Open("RouteIn.shp", 0)        

layer = datasource.GetLayer()
layer_properties = layer.GetLayerDefn()
field_count = layer_properties.GetFieldCount()

Lines = []
featureCount = layer.GetFeatureCount()
for i in range (layer.GetFeatureCount()):
	Line = []
	feature = layer.GetFeature(i)                              
	geometry = feature.GetGeometryRef()

		# read fields
	for ii in range(field_count):
		fieldName = layer_properties.GetFieldDefn(ii).GetName()
		FieldValue = feature.GetFieldAsString(fieldName)
		
	for i in range(geometry.GetPointCount()):
		x = geometry.GetX(i)                     
		y = geometry.GetY(i)
		pt = (x,y)                      
		Line.append(pt)  
	Lines.append(Line)		
          

layer.ResetReading()                            
datasource.Destroy()

# Neues File schreiben
if os.path.exists('Route.shp'):              
    driver.DeleteDataSource('Route.shp')     
datasourceOut = driver.CreateDataSource('Route.shp') 
layerOut = datasourceOut.CreateLayer('Route',geom_type= ogr.wkbLineString) 
        
featureDefn = layerOut.GetLayerDefn()         
for Line in Lines:
	featureOut = ogr.Feature(featureDefn)
	geom = ogr.Geometry(ogr.wkbLineString) 
	for vertex in Line: 
		geom.AddPoint(vertex[0],vertex[1]) 
	featureOut.SetGeometry(geom)  
	
	layerOut.CreateFeature(featureOut) 
featureOut.Destroy()
datasourceOut.Destroy() 



