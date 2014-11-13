import arcpy
from arcpy import env
env.workspace = "G:\School\Personal Drive\Fall2014\Python\EX5"
in_features = "parks.shp"
out_featureclass = "G:/School/Personal Drive/Fall2014/Python/EX5/parks_centroid.shp"
if arcpy.ProductInfo() == "ArcInfo":
    arcpy.FeatureToPoint_management(in_features, out_featureclass)
else:
    print "An ArcInfo license is not available."
