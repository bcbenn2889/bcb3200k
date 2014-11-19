import arcpy
import random
from arcpy import env
env.overwriteoutput = True
inputfc = "G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise13\points.shp"
outputfc = "G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise13\Results/random.shp"
outcount = 50
desc = arcpy.Describe(inputfc)
inlist = []
randomlist = []
fldname = desc.OIDFieldName
rows = arcpy.SearchCursor(inputfc)
row = rows.next()
while row:
    id = row.getValue(fldname)
    inlist.append(id)
    row = rows.next()
while len(randomlist) < outcount:
    selitem = random.choice(inlist)
    randomlist.append(selitem)
    inlist.remove(selitem)
length = len(str(randomlist))
sqlexp = '"' + fldname + '"' + " in " + "(" + str(randomlist)[1:length - 1] + ")"
arcpy.MakeFeatureLayer_management(inputfc, "selection", sqlexp)
arcpy.CopyFeatures_management("selection", outputfc)
