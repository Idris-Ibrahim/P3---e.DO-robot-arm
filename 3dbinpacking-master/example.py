from main import Packer, Bin, Item

packer = Packer()


packer.add_bin(Bin('small-envelope', 25, 30, 40, 10))

packer.add_item(Item('50g [powder 1]', 17, 30, 25, 1))
packer.add_item(Item('50g [powder 1]', 17, 30, 25, 1))

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

    print(len(packer.items))