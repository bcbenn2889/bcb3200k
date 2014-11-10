import arcpy
from arcpy import env
env.workspace = "G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise08"
env.overwriteOutput = True
outpath = "G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise08"
fc = "Results/newpolygon.shp"
arcpy.CreateFeatureclass_management("G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise08", fc, "Polygon")
cursor = arcpy.da.InsertCursor(fc, ["SHAPE@"])
array = arcpy.Array()
coordinates =[[0, 0], [0, 1000], [1000, 1000], [1000, 0]]
for x, y in coordinates:
    point = arcpy.Point(x,y)
    array.append(point)
polygon = arcpy.Polygon(array)
cursor.insertRow([polygon])
del cursor
