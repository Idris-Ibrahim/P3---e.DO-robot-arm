from DefineBoxes import DefineBoxes
from DefineItems import DefineItems

BoxList = []
ItemList = []

DefineBoxes(BoxList)
DefineItems(ItemList)

print("Itemlist Length:", len(ItemList), "Boxlist Length:", len(BoxList))

#først sammenligner vi item[0] volume og ser om det er mindre en box[0] volume

j = 0
i = 0

if ItemList[j].volume > BoxList[i].volume:
    print("fric")

else : 
    print("yes")