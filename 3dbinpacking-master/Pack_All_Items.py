from main import Packer, Bin, Item


packer = Packer()

checklist = []
packedItems= []


packer.add_bin(Bin('Lille kasse', 20, 10, 15, 20))
packer.add_bin(Bin('Stor kasse', 23, 32, 43, 20))


packer.add_item(Item('Harddrive', 11.5, 1.5, 8, 1))
packer.add_item(Item('PC Mouse', 7, 4.5, 12, 1))
packer.add_item(Item('KeyBoard', 45, 4, 14, 1))
packer.add_item(Item('Iphone', 8, 1.4, 15, 1))
packer.add_item(Item('Headset', 26, 7, 22, 1))

for b in packer.bins:
    print("BOX: ", b.string(), "\n")
    while len(packer.items) > 0:
        
        print("--------------------------------------------------------")
        print("-------------------  OPEN NEW BOX  ---------------------")
        print("--------------------------------------------------------\n")
        
        packer.pack()
        
        control = 0
        for b in packer.bins:
            control = control + len(b.items)
        
        if control == 0:
            print("No box could contain all kinds of item \n")
            print("UNPACKABLE ITEMS:")
            for b in packer.bins:
                for items in b.unfitted_items:
                    print("====> ", item.string(), "\n")
            exit()

        print("FITTED ITEMS:")
        for item in b.items:
            print("====> ", item.string(), "\n")

        print("UNFITTED ITEMS:")
        for item in b.unfitted_items:
            print("====> ", item.string(), "\n")
            
        #Iratible variable for counting empty space in the box    
        TotalVolume = 0
        for item in b.items:
            ItemVolume = item.get_volume()
            TotalVolume += ItemVolume
            
        BinVolume = b.get_volume()  
        EmptySpace = BinVolume - TotalVolume
        print("UNUSED VOLUME:")
        print("====> ", EmptySpace, "\n")
                
        # Deletes all items that has been packed from the bins.items array
        packer.items.clear()
        
        for box in packer.bins:
            packedItems.append(box.items)
        
        b.items.clear()
             

        # Adds all the items that couldn fit in the box the the array agian for retry without the fitted items    
        for box in packer.bins:
            for item in box.unfitted_items:
                #checks if item has already been re-added to items to be packed
                if item not in checklist:        
                    # Resets rotationtype
                    # Rotation type has to be reset: 
                    # Otherwise the algorithm will only try for the last rotation type with future boxes
                    item.rotation_type = 0
                    packer.add_item(item)
                    checklist.append(item)
        
        box.unfitted_items.clear   
    checklist.clear
    
    