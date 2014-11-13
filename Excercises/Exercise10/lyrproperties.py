import arcpy
mxd = "G:\School\Personal Drive\Fall2014\Python\Python\Data\Exercise10\Austin_TX.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)
lyrlist = arcpy.mapping.ListLayers(mapdoc)
for lyr in lyrlist:
    if lyr.name == "parks":
        print lyr.name
        lyr.visible = True
        lyr.showLabels = True
mapdoc.save()
del mapdoc
del lyrlist
