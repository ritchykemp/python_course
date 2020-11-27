
from osgeo import ogr
import os
Polygons = [] 


# File lesen
driver = ogr.GetDriverByName('ESRI Shapefile')
datasource = driver.Open("Session6/Houses.shp", 0)
layer = datasource.GetLayer()

layer = datasource.GetLayer()
layer_properties = layer.GetLayerDefn()
field_count = layer_properties.GetFieldCount()

i = 0
featureCount = layer.GetFeatureCount()
for i in range (layer.GetFeatureCount()):
	Polygon = []

	feature = layer.GetFeature(i)
	geometry = feature.GetGeometryRef()

	# read fields
	for ii in range(field_count):
		fieldName = layer_properties.GetFieldDefn(ii).GetName()
		FieldValue = feature.GetFieldAsString(fieldName)

	for ring in range(geometry.GetGeometryCount()):
		this_ring = geometry.GetGeometryRef(ring)
		Ring = []

		for i in range(this_ring.GetPointCount()): 
			x = this_ring.GetX(i)
			y = this_ring.GetY(i)
			pt = (x,y)
			Ring.append(pt)
		Polygon.append(Ring)
	Polygons.append(Polygon)


layer.ResetReading()
datasource.Destroy()

# Neues File schreiben
if os.path.exists('HousesOut.shp'): # hier
    driver.DeleteDataSource('HousesOut.shp')
datasourceOut = driver.CreateDataSource('HousesOut.shp')
layerOut = datasourceOut.CreateLayer('HousesOut',geom_type= ogr.wkbPolygon)

featureDefn = layerOut.GetLayerDefn()
for Polygon in Polygons:
	featureOut = ogr.Feature(featureDefn)
	geom = ogr.Geometry(ogr.wkbPolygon)
	
	for Ring in Polygon:
		ring = ogr.Geometry(ogr.wkbLinearRing)
		for vertex in Ring:
			ring.AddPoint(vertex[0],vertex[1])
		geom.AddGeometry(ring)
	featureOut.SetGeometry(geom)
	layerOut.CreateFeature(featureOut)
	
featureOut.Destroy()
datasourceOut.Destroy()



