import arcpy
from arcpy import env
env.workspace = "G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise08"
fc = "dams.shp"
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@XY"])
for row in cursor:
    x, y = row[0]
print("{0}, {1}".format(x, y))
