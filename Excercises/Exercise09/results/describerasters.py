import arcpy
from arcpy import env
env.workspace = "G:\School\Personal Drive\Fall2014\Python\Python\Data\Exercise09"
rasterband = "tm.img/Layer_1"
desc = arcpy.Describe(rasterband)
x = desc.meanCellHeight
y = desc.meanCellWidth
spatialref = desc.spatialReference
units = spatialref.angularUnitName
print "The raster resolution of Band 1 is " + str(x) + " by " + str(y)
+ " " + units + "."
