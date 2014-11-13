import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "G:\School\Personal Drive\Fall2014\Python\Python\Data\Exercise09"
if arcpy.CheckExtension("spatial") == "Available":
    arcpy.CheckOutExtension("spatial")
    outraster = arcpy.sa.Slope("elevation", "PERCENT_RISE")
    outraster.save("slope_per")
    arcpy.CheckInExtension("spatial")
else:
    print "Spatial Analyst license is not available."
