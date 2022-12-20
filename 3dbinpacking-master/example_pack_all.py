from main import Packer, Bin, Item

# IMPORTING THE PACKER OBJECT
packer = Packer()


# FUNCTION FOR CLEARING ALL DATA IN PAKCER OBJECT
def clear_packer(pack):
    pack.bins.clear()
    pack.items.clear()
    pack.unfit_items.clear
    pack.total_items = 0

# FUNCTION FOR ADDING ALL DATA TO THE PACKER OBJECT
def add():
    
    # ADDING BINS TYPES FOR THE ALGORITHMS DISPOSAL:

    packer.add_bin(Bin('SMALL BIN', 10, 10, 12, 10))
    packer.add_bin(Bin('DOUBLE - SMALL BIN', 20, 10, 12, 30))
    packer.add_bin(Bin('MEDIUM BIN', 30, 15, 20, 80))
    packer.add_bin(Bin('BIG BIN', 50, 30, 40, 150))
    packer.add_bin(Bin('HUGE BIN', 100, 50, 100, 200))

    # ADDING ITEMS TO BE PACKED:

    packer.add_item(Item('Fugl', 10, 10, 7, 1))
    packer.add_item(Item('Hund', 20, 10, 20, 10))
    packer.add_item(Item('Mus', 8, 5, 12, 3))
    packer.add_item(Item('Rotte', 8, 5, 12, 3))
    packer.add_item(Item('Skildpade', 5, 4, 15, 40))
    packer.add_item(Item('Anaconda', 10, 4, 4, 2))

# CALLING PACK_ALL_ITEMS FUNCTION ON THE GIVEN ITEMS AND BINS GIVEN:

add()
print("\n PACK ALL PIVOTING: \n")
packer.pack_all_items()
print("\n ^ PACK ALL PIVOTING: ^\n")

clear_packer(packer)

# CALLING PACK_ALL_ITEMS_RANDOM FUNCTION ON THE GIVEN ITEMS AND BINS GIVEN:

add()
print("\n PACK ALL RANDOM: \n")
packer.pack_all_items_random()
print("\n ^ PACK ALL RANDOM: ^\n")