import arcpy
import fileinput
import string
import os
from arcpy import env
env.workspace = "G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise08"
env.overwriteOutput = True
outpath = "G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise08"
newfc = "Results/newpolyline2.shp"
arcpy.CreateFeatureclass_management("G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise08", newfc, "Polyline")
infile = "G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise08\coordinates.txt"
cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
array = arcpy.Array()
for line in fileinput.input(infile):
    ID, X, Y = string.split(line," ")
    array.add(arcpy.Point(X, Y))
cursor.insertRow([arcpy.Polyline(array)])
fileinput.close()
del cursor
