from DefineBoxes import DefineBoxes
from DefineItems import DefineItems
import math

BoxList = []
ItemList = []

DefineBoxes(BoxList)
DefineItems(ItemList)

print("Itemlist Length:", len(ItemList), "Boxlist Length:", len(BoxList))

#først sammenligner vi item[0] volume og ser om det er mindre en box[0] volume

for i in range(0,len(BoxList)):
    for j in range(0, len(ItemList)):
        #list of calculations:
        CalList = []
        #Item x to all box axes ratio
        xx = BoxList[i].x / ItemList[j].x
        yx = BoxList[i].y / ItemList[j].x
        zx = BoxList[i].z / ItemList[j].x

        #Item y to all box axes ratio
        xy = BoxList[i].x / ItemList[j].y
        yy = BoxList[i].y / ItemList[j].y
        xy = BoxList[i].z / ItemList[j].y

        #Item z to all box axes ratio
        xz = BoxList[i].x / ItemList[j].z
        yz = BoxList[i].y / ItemList[j].z
        xz = BoxList[i].z / ItemList[j].z

        print(xx, yx, zx, xy, yy, yz, xz, yz, xz)

        CalList.append(xx)
        CalList.append(yx)
        CalList.append(zx)
        CalList.append(xy)
        CalList.append(yy)
        CalList.append(yz)
        CalList.append(zx)
        CalList.append(yz)
        CalList.append(xz)

        #variable for saving lowest wasted space
        LowestWaste1 = CalList[0]

        l = 0

        for l in range (l, len(CalList)):
            if CalList[l]%1 < LowestWaste1%1:
                LowestWaste1 = CalList[l]

            elif CalList[l]%1 == LowestWaste1%1:
                if CalList[l] > LowestWaste1:
                    LowestWaste1 = CalList[l]
        
        print("Mængder pr axe:", math.floor(LowestWaste1), "Waste:", LowestWaste1%1)
