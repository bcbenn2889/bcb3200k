import arcpy

Available=[]

if arcpy.CheckExtension("3D") == "Available":
    Available.append("3D")
if arcpy.CheckExtension("Network") == "Available":
    Available.append("Network")
if arcpy.CheckExtension("Spatial") == "Available":
    Available.append("Spatial")
    
else:
    extension_3D = ""
    extension_Network = ""
    extension_Spatial = ""

print "Extensions that are available:" + str(Available)
