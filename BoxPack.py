from DefineBoxes import DefineBoxes
from DefineItems import DefineItems

ItemList = []
BoxList = []

DefineBoxes()
DefineItems()

print("Itemlist Length:", len(ItemList), "Boxlist Length:", len(BoxList))

#først sammenligner vi item[0] volume og ser om det er mindre en box[0] volume

j = 1
i = 1

if ItemList[j].volume > BoxList[i].volume:
    print("fric")

else : 
    print("yes")