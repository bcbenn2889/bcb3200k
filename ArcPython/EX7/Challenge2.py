import arcpy
from arcpy import env
env.workspace = "G:\School\Personal Drive\Fall2014\Python\Excercises\Exercise07"
fc = "roads.shp"
arcpy.AddField_management(fc, "FERRY", "TEXT", "", "", 20)
cursor = arcpy.da.UpdateCursor(fc, ["FEATURE", "FERRY"])
for row in cursor:
    if row[0] == "Ferry Crossing":
        row[1] == "YES"
    else:
        row[1] == "NO"
    cursor.updateRow(row)
