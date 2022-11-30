#Function definiton:
def DefineItems(ItemList):

    class Item:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
            self.volume = self.x * self.y * self.z
        
        class Rotation : 
            xyz = 0
               

    #Amount of item types:
    ItemTypeAmount = int(input("Amount of item types: "))

    #Insert measurement for each axes for each item:
    for i in range(ItemTypeAmount) :
        x = float(input(f"Item {i} x length: "))
        y = float(input(f"Item {i} y length: "))
        z = float(input(f"Item {i} z length: "))

        ItemList.append(Item(x, y, z))

        i += 1
        ItemAmount -= 1
        print("\n")

    #Sorting all items from biggest to smallest volume (reverse=True)
    ItemList = sorted(ItemList, key=lambda Item: Item.volume, reverse=True)
    
    #Print all the items and the measurement:
    for i in range (0,len(ItemList)):

        print(f"Item {i} measurements:", ItemList[i].x, ItemList[i].y, ItemList[i].z)
        print(f"Item {i} volume: {ItemList[i].volume}\n")