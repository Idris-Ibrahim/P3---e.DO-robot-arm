from DefineBoxes import DefineBoxes
from DefineItems import DefineItems
import math

BoxList = []
ItemList = []
CurrentBox = []
PackedList = []

DefineBoxes(BoxList)
DefineItems(ItemList)

print("Itemlist Length:", len(ItemList), "Boxlist Length:", len(BoxList))

for i in range(len(BoxList)):
    for j in range(len(ItemList)):
        if ItemList[j].volume > BoxList[i].volume:
           i += 1
        else :
            print("lort")
            
        


if len(PackedList) == 0:
    print("no items could be packed in the given boxes")

else :
    for i in range(len(PackedList)):
        print(PackedList[i])