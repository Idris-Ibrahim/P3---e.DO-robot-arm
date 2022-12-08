from main import Packer, Bin, Item

packer = Packer()

packer.add_bin(Bin('smallest-envelope', 25, 30, 17, 300))
packer.add_bin(Bin('small-envelope', 30, 40, 20, 300))

packer.add_item(Item('50g [powder 1]', 20, 30, 17, 1))
#packer.add_item(Item('50g [powder 2]', 25, 30, 17, 1))


packer.pack_all_items()
