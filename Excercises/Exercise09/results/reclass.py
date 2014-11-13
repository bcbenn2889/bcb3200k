import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "G:\School\Personal Drive\Fall2014\Python\Python\Data\Exercise09"
if arcpy.CheckExtension("spatial") == "Available":
    arcpy.CheckOutExtension("spatial")
    myremap = RemapValue([[41,1], [42,2], [43,3]])
    outreclass = Reclassify("landcover.tif", "VALUE", myremap, "NODATA")
    outreclass.save("lc_recl")
    arcpy.CheckInExtension("spatial")
else:
    print "Spatial Analyst license is not available."