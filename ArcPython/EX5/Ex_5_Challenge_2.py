
import arcpy
from arcpy import env
env.workspace = ("G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise 5\EX5")
arcpy.AddXY_management ("hospitals.shp")
