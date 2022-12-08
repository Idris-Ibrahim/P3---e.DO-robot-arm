from main import Packer, Bin, Item

packer = Packer()

packer.add_bin(Bin('small-envelope', 25, 30, 40, 300))

packer.add_item(Item('50g [powder 1]', 25, 30, 17, 1))


packer.pack_all_items()

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