from main import Packer, Bin, Item

packer = Packer()

packer.add_bin(Bin('small-envelope', 100, 110, 120, 300))

packer.add_item(Item('50g [powder 1]', 25, 30, 17, 1))
packer.add_item(Item('50g [powder 2]', 25, 30, 17, 1))


packer.pack_all_items()
