import arcpy
from arcpy import env
env.workspace = "G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise07"
fc = "Results/airports.shp"
cursor = arcpy.da.InsertCursor(fc, "NAME")
cursor.insertRow(["New Airport"])
del cursor
