import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise 6\Exercise06"
fieldlist = arcpy.ListFields("cities.shp")
for field in fieldlist:
    print field.name + " " + field.type
