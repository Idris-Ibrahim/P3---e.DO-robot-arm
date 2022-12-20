#Function definiton:
def DefineItems(ItemList):

    class Item:
        def __init__(self, x, y, z, Qty):
            self.x = x
            self.y = y
            self.z = z
            self.Qty = Qty
            self.volume = self.x * self.y * self.z
        
        def rotate_x_y(self) : 
            x = self.x
            y = self.y
            
            self.x = y
            self.y = x
            
        def rotate_x_z(self) : 
            x = self.x
            z = self.z
            
            self.x = z
            self.z = x
               

    #Amount of item types:
    ItemTypeAmount = int(input("Amount of item types: "))

    #Insert measurement for each axes for each item:
    for i in range(ItemTypeAmount) :
        x = float(input(f"Item {i} x length: "))
        y = float(input(f"Item {i} y length: "))
        z = float(input(f"Item {i} z length: "))
        Qty = int(input(f"Quantity of Item {i} to be packed: "))

        ItemList.append(Item(x, y, z, Qty))

        print("\n")

    #Sorting all items from biggest to smallest volume (reverse=True)
    ItemList = sorted(ItemList, key=lambda Item: Item.volume, reverse=True)
    
    #Print all the items and the measurement:
    for i in range (0,len(ItemList)):

        print(f"Item {i} measurements:", ItemList[i].x, ItemList[i].y, ItemList[i].z)
        print(f"Item {i} volume: {ItemList[i].volume}\n")