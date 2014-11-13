import arcpy
from arcpy import env
env.workspace = "G:\School\Personal Drive\Fall2014\Python\EX5"
if arcpy.CheckExtension("spatial") == "Available":
    arcpy.CheckOutExtension("spatial")
    out_distance = arcpy.sa.EucDistance("G:/School/Personal Drive/Fall2014/Python/EX5/bike_routes.shp", cell_size = 100)

    out_distance.save("G:/School/Personal Drive/Fall2014/Python/EX5/bike_dist")
    arcpy.CheckInExtension("spatial")
else:
    print "Spatial Analyst license is not available."
