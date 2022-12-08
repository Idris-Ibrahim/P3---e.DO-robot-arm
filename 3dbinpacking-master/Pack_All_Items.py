from main import Packer, Bin, Item

packer = Packer()

<<<<<<< HEAD
# packer.add_bin(Bin('Lille kasse', 10, 10, 10, 20))
packer.add_bin(Bin('Stor kasse', 30, 20, 20, 20))
=======
packer.add_bin(Bin('small-envelope', 25, 30, 40, 300))
>>>>>>> parent of e25011e (Only by adding 1 bin will it work correctly atm)

packer.add_item(Item('50g [powder 1]', 25, 30, 17, 1))
packer.add_item(Item('50g [powder 1]', 25, 30, 17, 1))
packer.add_item(Item('50g [powder 1]', 25, 30, 17, 1))
packer.add_item(Item('50g [powder 1]', 25, 30, 17, 1))
packer.add_item(Item('50g [powder 1]', 25, 30, 17, 1))

packer.pack()

<<<<<<< HEAD
while len(packer.items) > 0:
    
    print("--------------------------------------------------------")
    print("-------------------  OPEN NEW BOX  ---------------------")
    print("--------------------------------------------------------")
    
    packer.pack()
    
    control = 0
    for b in packer.bins:
        control = control + len(b.items)
    
    if control == 0:
        print("no box could contain all kinds of item")
        exit()
   
    for b in packer.bins:
        print("BOX: ", b.string(), "\n")
=======
for b in packer.bins:
    print(":::::::::::", b.string())
>>>>>>> parent of e25011e (Only by adding 1 bin will it work correctly atm)

    print("FITTED ITEMS:")
    for item in b.items:
        print("====> ", item.string())

    print("UNFITTED ITEMS:")
    for item in b.unfitted_items:
        print("====> ", item.string())

    print("***************************************************")
    print("***************************************************")

print("________________________________________________________")
print("________________________________________________________")
print("________________________________________________________")
print("________________________________________________________")

# Deletes all items that has been packed from the bins.items array
packer.items.clear()
for box in packer.bins:
    box.items.clear()

# Adds all the items that couldn fit in the box the the array agian for retry without the fitted items    
for box in packer.bins:
    for item in box.unfitted_items:
        packer.add_item(item)
    box.unfitted_items.clear()
        

<<<<<<< HEAD
    # Adds all the items that couldn fit in the box the the array agian for retry without the fitted items    
    for box in packer.bins:
        for item in box.unfitted_items:
            # Resets rotationtype
            # Rotation type has to be reset: 
            # Otherwise the algorithm will only try for the last rotation type with future boxes
            item.rotation_type = 0
            packer.add_item(item)
            
    box.unfitted_items.clear()
=======
print("________________________________________________________")
print("________________________________________________________")
print("________________________________________________________")
print("________________________________________________________")

packer.pack()

for b in packer.bins:
    print(":::::::::::", b.string())

    print("FITTED ITEMS:")
    for item in b.items:
        print("====> ", item.string())

    print("UNFITTED ITEMS:")
    for item in b.unfitted_items:
        print("====> ", item.string())

    print("***************************************************")
    print("***************************************************")
>>>>>>> parent of e25011e (Only by adding 1 bin will it work correctly atm)
