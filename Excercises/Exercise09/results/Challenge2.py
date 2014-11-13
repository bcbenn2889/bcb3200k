##import arcpy
##from arcpy import env
##out_path = "G:\School\Personal Drive\Fall2014\Python\Python\Data\Exercise09"
##env.workspace = out_path
##rasterlist = arcpy.ListRasters()
##arcpy.CreatePersonalGDB_management(out_path + "/Results", "allrasters.gdb")
##for rasters in rasterlist:
##    desc=arcpy.Describe(rasters)
##    rastername=desc.baseName
##    outraster = out_path + "/Results/allrasters.gdb/" + rastername
##    arcpy.CopyRaster_management(rasters, outraster)
##
import arcpy
from arcpy import env
out_path = "G:\School\Personal Drive\Fall2014\Python\Python\Data\Exercise09"
env.workspace = out_path
rasterlist = arcpy.ListRasters()
arcpy.CreatePersonalGDB_management(out_path + "/Results", "myrasters.gdb")
for raster in rasterlist:
    desc = arcpy.Describe(raster)
    rname = desc.baseName
    outraster = out_path + "/Results/myrasters.gdb/" + rname
    arcpy.CopyRaster_management(raster, outraster)
