import arcpy
from arcpy import env
env.workspace = "G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise07"
sql1 = " \"FEATURE\"='Airport'"
sql2 = " \"FEATURE\"='Seaplane Base'"
arcpy.Select_analysis("airports.shp", "Results/airports_finalbuffer.shp",sql1)
arcpy.Select_analysis("airports.shp", "Results/seaports.shp", sql2)
arcpy.Buffer_analysis("Results/airports_finalbuffer.shp", "Results/airports_buffers.shp", "15000 METERS")
arcpy.Buffer_analysis("Results/seaports.shp", "Results/seaports_buffers.shp", "7500 METERS")

