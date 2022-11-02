def DefineItems():

    #defining the list of items and the objekt for an item
    ItemList = []

    class Item:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

    #Amount of item types:
    ItemAmount = int(input("Amount of item types: "))

    #insert measurement for each axes for each item:
    i = 0
    while ItemAmount > 0 :
        x = float(input(f"Box {i} x length: "))
        y = float(input(f"Box {i} y length: "))
        z = float(input(f"Box {i} z length: "))

        ItemList.append(Item(x, y, z))

        i += 1
        ItemAmount -= 1
        print("\n")
    
    #print all the items and the measurement:
    for i in range (0,len(ItemList)):

        print(f"Item {i}:", ItemList[i].x, ItemList[i].y, ItemList[i].z)
        print(f"Item {i} volume: {ItemList[i].x * ItemList[i].y * ItemList[i].z }")

#Run function:
DefineItems()