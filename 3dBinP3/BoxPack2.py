from DefineBoxes import DefineBoxes
from DefineItems import DefineItems
import math

BoxList = []
ItemList = []
PackedList = []

DefineBoxes(BoxList)
DefineItems(ItemList)

print("Itemlist Length:", len(ItemList), "Boxlist Length:", len(BoxList))

for i in range(len(BoxList)):
    for j in range(len(ItemList)):

        if ItemList[j].volume > BoxList[i].volume:
            i += 1
        
        if ItemList[j].volume == BoxList[i].volume:
            if ItemList[j].x == BoxList[i].x and ItemList[j].y == BoxList[i].y and ItemList[j].z == BoxList[i].z:
                PackedList.append(f"1 ItemType: {j} is packed in 1 BoxType: {i}")

        elif ItemList[j].volume < BoxList[i].volume:
            print("hard")

if len(PackedList) == 0:
    print("no items could be packed in the given boxes")

else :
    for i in range(len(PackedList)):
        print(PackedList[i])