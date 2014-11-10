import arcpy
from arcpy import env
env.workspace ="G:/School/Personal Drive/Fall2014/Python/Excercises/Exercise 6/Results"
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdescribe = arcpy.Describe(fc)
    print fcdescribe.name + " " + "is a" +" " + fcdescribe.dataType
   
