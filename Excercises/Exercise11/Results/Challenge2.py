import arcpy
from arcpy import env
env.workspace = "G:\School\Personal Drive\Fall2014\Python\Python\Data\Exercise09"
raster = "landcover.tif"
desc = arcpy.Describe(raster)
x = desc.meanCellHeight
y = desc.meanCellWidth
spatialref = desc.SpatialReference
units = spatialref.linearUnitName
print "Cells are" + str(x) + " by " + str(y) + " " + units + "."
