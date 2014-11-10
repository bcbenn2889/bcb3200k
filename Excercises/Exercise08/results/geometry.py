import arcpy
from arcpy import env
env.workspace = "G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise08"
fc = "rivers.shp"
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@LENGTH"])
length = 0
for row in cursor:
    length = length + row[0]
units = arcpy.Describe(fc).spatialReference.linearUnitName
print str(length) + " " + units
