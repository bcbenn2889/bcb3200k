import arcpy
from arcpy import env
env.workspace = "G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise08"
fc = "rivers.shp"
cursor = arcpy.da.SearchCursor(fc, (["OID@", "SHAPE@"]))
for row in cursor:
    print("Feature {0}: ".format(row[0]))
for point in row[1].getPart(0):
    print("{0}, {1}".format(point.X, point.Y))
 
