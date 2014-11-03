import arcpy
from arcpy import env
env.workspace = "G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise07"
fc = "airports.shp"
cursor = arcpy.da.SearchCursor(fc, ["NAME"])
for row in cursor:
    print "Airport name = {0}".format(row[0])
