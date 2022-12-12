from main import Packer, Bin, Item

#if items have same dimentions and max weight, they must have different names

# DEN HOPPER PT ALTID TIL DEN STØRSTE KASSE OG PAKKER DEM I DEN

# KAN MULIGVIS VÆRE AT DEN PRINTER FORKERT KASSE NAVN TIL DE GIVNE ITEMS

packer = Packer()

packer.add_bin(Bin('SMALL BIN', 10, 10, 12, 300))

packer.add_bin(Bin('BIG BIN', 100, 100, 100, 300))

packer.add_bin(Bin('BIGGEST BIN', 100, 100, 200, 300))


packer.add_item(Item('Fugl', 10, 10, 7, 1))

#packer.add_item(Item('Hund', 20, 10, 20, 1))

packer.add_item(Item('Mus', 8, 5, 12, 1))

#packer.add_item(Item('Rat', 8, 5, 12, 1))

#packer.add_item(Item('Elefant', 100, 100, 200, 1))

packer.pack_all_items()
