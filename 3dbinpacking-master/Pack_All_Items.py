from main import Packer, Bin, Item

packer = Packer()

packer.add_bin(Bin('small-envelope', 25, 30, 40, 300))

packer.add_item(Item('50g [powder 1]', 25, 30, 17, 1))
packer.add_item(Item('50g [powder 1]', 25, 30, 17, 1))
packer.add_item(Item('50g [powder 1]', 25, 30, 17, 1))
packer.add_item(Item('50g [powder 1]', 25, 30, 17, 1))
packer.add_item(Item('50g [powder 1]', 25, 30, 17, 1))

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