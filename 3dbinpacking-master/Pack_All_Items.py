from main import Packer, Bin, Item

packer = Packer()

volumelist = []

packer.add_bin(Bin('Lille kasse', 20, 10, 15, 20))
packer.add_bin(Bin('Stor kasse', 23, 32, 43, 20))
packer.add_bin(Bin('Kæmpe kasse', 50, 50, 70, 20))


packer.add_item(Item('Harddrive', 11.5, 1.5, 8, 1))
packer.add_item(Item('PC Mouse', 7, 4.5, 12, 1))
packer.add_item(Item('KeyBoard', 45, 4, 14, 1))
packer.add_item(Item('Iphone', 8, 1.4, 15, 1))
packer.add_item(Item('Headset', 26, 7, 22, 1))

for bin in packer.bins:
    volumelist.append(bin.get_volume())

for bin in packer.bins:
    index = 0
    bin.format_numbers(bin.number_of_decimals)

    for item in packer.items:
        item.format_numbers(item.number_of_decimals)
        
        # skal gemme alle de kasser der er blevet pakket:    
    BinList = []
            
    packer.bins = sorted(packer.bins, key=lambda bin: bin.get_volume(), reverse=False)
        
    packer.items = sorted(packer.items, key=lambda item: item.get_volume(), reverse=True)
        
    for bin in packer.bins:
        print("--------------------------------------------------------")
        print("-------------------  OPEN NEW BIN  ---------------------")
        print("--------------------------------------------------------\n")
        print("BIN TYPE: ", bin.string(), "\n")
        
        print("FITTED ITEMS:")
        for item in bin.items:
            print("====> ", item.string(), "\n") 
                       
        print("UNFITTED ITEMS:")
        for item in bin.unfitted_items:
            print("====> ", item.string(), "\n")
        
        for item in packer.items:
            packer.pack_to_bin(bin, item)
                #if all items couldn be packed, open new box:
            if len(bin.unfitted_items) == 0:
                    
                # skal pritnte den givne configuration for kassen der kunne holde alle items:
                print("ALL ITEMS FITTED:")
                for item in bin.items:
                    print("====> ", item.string(), "\n")
                    bin.items.clear()
                            
            if len(bin.unfitted_items) > 0:
                    if volumelist[index] * 2 < volumelist[index+1]:
                        break
                    elif volumelist[index] * 2 >= volumelist[index+1]:
                        for item in bin.unfitted_items:
                            item.rotation_type = 0
                            packer.add_item(item)
                            for item in packer.items:
                                packer.pack_to_bin(bin, item)
                        bin.unfitted_item.clear