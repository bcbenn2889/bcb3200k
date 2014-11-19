import arcpy
import list
arcpy.env.workspace = "G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise12"
fields = list.listfieldnames("streets.shp")
print fields
