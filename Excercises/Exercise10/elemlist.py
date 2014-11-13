import arcpy
mxd = "G:\School\Personal Drive\Fall2014\Python\Python\Data\Exercise10\Georgia.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)
elemlist = arcpy.mapping.ListLayoutElements(mapdoc)
for elem in elemlist:
    print elem.name + " " + elem.type
del mapdoc
