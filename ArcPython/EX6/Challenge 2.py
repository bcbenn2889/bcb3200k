import arcpy
from arcpy import env
env.workspace = "G:/School/Personal Drive/Fall2014/Python/Excercises/Exercise 6/Results/NM.gdb"
fclist = arcpy.ListFeatureClasses()
arcpy.CreateFileGDB_management("G:/School/Personal Drive/Fall2014/Python/Excercises/Exercise 6/Results/","new.gdb")
for fc in fclist:
    fcdescribe = arcpy.Describe(fc)
    if fcdescribe.shapeType =="Polygon":
        arcpy.Copy_management (fc, "G:/School/Personal Drive/Fall2014/Python/Excercises/Exercise 6/Results/new.gdb/"+fc)
      
