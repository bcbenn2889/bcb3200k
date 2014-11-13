import arcpy
from arcpy import env
env.workspace = "G:\School\Personal Drive\Fall2014\Python\EX5"
env.overwriteOutput = True
newclip = arcpy.Clip_analysis("G:/School/Personal Drive/Fall2014/Python/EX5/bike_routes.shp","G:/School/Personal Drive/Fall2014/Python/EX5/parks.shp", "G:/School/Personal Drive/Fall2014/Python/EX5/bike_Clip.shp")
fCount = arcpy.GetCount_management("G:/School/Personal Drive/Fall2014/Python/EX5/bike_Clip.shp")
msgCount=newclip.messageCount
print newclip.getMessage(msgCount-1)


