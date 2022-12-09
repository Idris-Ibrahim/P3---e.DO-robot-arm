from main import Packer, Bin, Item

packer = Packer()

packer.add_bin(Bin('SMALL BIN', 10, 10, 12, 300))

packer.add_bin(Bin('BIG BIN', 100, 300, 300, 300))


packer.add_item(Item('Fugl', 10, 10, 7, 1))

packer.add_item(Item('Mus', 8, 10, 12, 1))

packer.add_item(Item('Elefant', 50, 100, 200, 1))

packer.pack_all_items()
