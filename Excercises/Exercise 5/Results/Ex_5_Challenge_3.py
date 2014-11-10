import arcpy
from arcpy import env
env.workspace = ("G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise 5\EX5")
arcpy.Dissolve_management ("parks.shp", "dissolved_parks.shp","PARK_TYPE", "", "FALSE")

