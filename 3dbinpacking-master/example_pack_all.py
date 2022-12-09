from main import Packer, Bin, Item

packer = Packer()

packer.add_bin(Bin('SMALL BIN', 10, 10, 15, 300))

packer.add_bin(Bin('BIG BIN', 100, 100, 150, 300))


packer.add_item(Item('Fugl', 10, 10, 7, 1))

packer.add_item(Item('Mus', 8, 10, 12, 1))

packer.pack_all_items()
