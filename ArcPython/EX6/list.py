
import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "G:/School/Personal Drive/Fall2014/Python/Excercises/Exercise 6/Exercise06"
arcpy.CreateFileGDB_management("G:/School/Personal Drive/Fall2014/Python/Excercises/Exercise 6/Exercise06/Results", "NM.gdb")
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    arcpy.CopyFeatures_management(fc, "G:/School/Personal Drive/Fall2014/Python/Excercises/Exercise 6/Exercise06/Results/NM.gdb/" + fcdesc.basename)
