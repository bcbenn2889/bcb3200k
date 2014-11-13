import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "G:\School\Personal Drive\Fall2014\Python\Python\Data\Exercise09"
if arcpy.CheckExtension("spatial") == "Available":
    arcpy.CheckOutExtension("spatial")
elevraster = arcpy.Raster("elevation")
lcraster = arcpy.Raster("landcover.tif")
slope = Slope(elevraster)
aspect = Aspect(elevraster)
goodslope= ((slope>5)&(slope<20))
goodaspect= ((aspect>150) & (aspect<270))
goodland= ((lcraster == 41) |(lcraster == 42) | (lcraster ==43))
outraster = (goodslope & goodaspect & goodland)
outraster.save("G:\School\Personal Drive\Fall2014\Python\Python\Data\Exercise09\outraster")
arcpy.CheckInExtension("Spatial")
