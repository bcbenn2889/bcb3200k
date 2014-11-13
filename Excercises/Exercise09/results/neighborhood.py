import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "G:\School\Personal Drive\Fall2014\Python\Python\Data\Exercise09"
if arcpy.CheckExtension("spatial") == "Available":
    arcpy.CheckOutExtension("spatial")
    mynbr = NbrCircle(3, "CELL")
    outraster = FocalStatistics("landcover.tif", mynbr, "MAJORITY")
    outraster.save("lc_nbr")
    arcpy.CheckInExtension("spatial")
else:
    print "Spatial Analyst license is not available."
