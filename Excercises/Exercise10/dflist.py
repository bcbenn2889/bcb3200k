import arcpy
mxd = "G:\School\Personal Drive\Fall2014\Python\Python\Data\Exercise10\Austin_TX.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)
listdf = arcpy.mapping.ListDataFrames(mapdoc)
for df in listdf:
    print df.name
del mapdoc
del listdf
