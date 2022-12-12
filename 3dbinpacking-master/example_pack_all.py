from main import Packer, Bin, Item

#if items have same dimentions and max weight, they must have different names

# DEN HOPPER PT ALTID TIL DEN STØRSTE KASSE OG PAKKER DEM I DEN

# KAN MULIGVIS VÆRE AT DEN PRINTER FORKERT KASSE NAVN TIL DE GIVNE ITEMS

packer = Packer()

packer.add_bin(Bin('SMALL BIN', 10, 10, 12, 10))

packer.add_bin(Bin('DOUBLE - SMALL BIN', 20, 10, 12, 30))

packer.add_bin(Bin('MEDIUM BIN', 30, 15, 20, 80))

packer.add_bin(Bin('BIG BIN', 50, 30, 40, 150))

packer.add_bin(Bin('HUGE BIN', 100, 200, 200, 200))


packer.add_item(Item('Fugl', 10, 10, 7, 0.5))

packer.add_item(Item('Fugl', 10, 10, 7, 0.5))

packer.add_item(Item('Hund', 20, 10, 20, 10))

packer.add_item(Item('Mus', 8, 5, 12, 0.5))

packer.add_item(Item('Rat', 8, 5, 12, 3))

packer.add_item(Item('Turtle', 5, 4, 15, 4))

packer.add_item(Item('Anaconda', 10, 4, 4, 2))

# packer.add_item(Item('Elefant', 100, 100, 200, 150))

packer.pack_all_items()
