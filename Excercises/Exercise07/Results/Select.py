import arcpy
from arcpy import env
env.workspace = "G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise07"
infc = "airports.shp"
outfc = "Results/airports_anchorage.shp"
delimitedfield = arcpy.AddFieldDelimiters(infc, "COUNTY")
arcpy.Select_analysis(infc, outfc, delimitedfield + " ='Anchorage Borough'")
