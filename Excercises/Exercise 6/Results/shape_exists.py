import arcpy
from arcpy import env
env.workspace = "G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise 6\Exercise06"
if arcpy.Exists("cities.shp"):
    arcpy.CopyFeatures_management("cities.shp", "results/cities_copy.shp")
    

