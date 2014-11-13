import arcpy
from arcpy import env
env.workspace = "G:\School\Personal Drive\Fall2014\Python\Python\Data\Exercise09"
rasterlist = arcpy.ListRasters()
for raster in rasterlist:
    print raster
