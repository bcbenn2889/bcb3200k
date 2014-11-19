import arcpy
from arcpy import env
env.workspace = "G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise11"
fc = "county.shp"
rows = arcpy.SearchCursor(fc)
fields = arcpy.ListFields(fc)
for field in fields:
    if field.name == "NAME":
        for row in rows:
            print "Name = {0}".format(row.getValue(field.name))
