from main import Packer, Bin, Item
import random
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
    packer.add_item(Item('Tiger', 20, 10, 23, 10))
    packer.add_item(Item('Kat', 10, 5, 10, 13))
    packer.add_item(Item('Orangotang', 15, 12, 14, 20))
    packer.add_item(Item('Flagermus', 14, 5, 12, 2))
    packer.add_item(Item('Nisse', 20, 10, 17, 50))
    packer.add_item(Item('Mulvarp', 17, 13, 18, 7))
    packer.add_item(Item('Bi', 1, 1, 1, 0.001))

def add_random(RandomBins = [], RandomItems = []):
    
    # ADDING BINS TYPES FOR THE ALGORITHMS DISPOSAL:
    # packer.add_bin(Bin('SMALL BIN', float(25), float(10), float(12), float(10)))
    # packer.add_bin(Bin('DOUBLE - SMALL BIN', float(50), float(20), float(50), float(30)))
    # packer.add_bin(Bin('MEDIUM BIN', float(100), float(50), float(70), float(80)))
    # packer.add_bin(Bin('BIG BIN', float(100), float(100), float(100), float(150)))
    # packer.add_bin(Bin('HUGE BIN', float(100), float(100), float(200), float(200)))
    
    # Random 5 types of Bins:
    
    packer.add_bin(Bin('BIN 1', random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 200)))
    packer.add_bin(Bin('BIN 2', random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 200)))
    packer.add_bin(Bin('BIN 3', random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 200)))
    packer.add_bin(Bin('BIN 4', random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 200)))
    packer.add_bin(Bin('BIN 5', random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 200)))

    # ADDING ITEMS TO BE PACKED:

    packer.add_item(Item('ITEM 1', random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 12.5)))
    packer.add_item(Item('ITEM 2', random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 12.5)))
    packer.add_item(Item('ITEM 3', random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 12.5)))
    packer.add_item(Item('ITEM 4', random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 12.5)))
    packer.add_item(Item('ITEM 5', random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 12.5)))
    packer.add_item(Item('ITEM 6', random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 12.5)))
    packer.add_item(Item('ITEM 7', random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 12.5)))
    packer.add_item(Item('ITEM 8', random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 12.5)))
    packer.add_item(Item('ITEM 9', random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 12.5)))
    packer.add_item(Item('ITEM 10', random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 12.5)))
    packer.add_item(Item('ITEM 11', random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 12.5)))
    packer.add_item(Item('ITEM 12', random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 12.5)))
    
    for bin in packer.bins:
        RandomBins.append(bin)
        
    for item in packer.items:
        RandomItems.append(item)
        
def insert_same_random_into_packer(RanBinList = [], RanItemList =[]):
    
    for bin in RanBinList:
        packer.add_bin(bin)

    for item in RanItemList:
        packer.add_item(item)
    

RandomBins = []

RandomItems = []

add_random(RandomBins, RandomItems)

packer.pack_all_items()

clear_packer(packer)

insert_same_random_into_packer(RandomItems, RandomBins)

packer.pack_all_items_random()

# # CALLING PACK_ALL_ITEMS FUNCTION ON THE GIVEN ITEMS AND BINS GIVEN:
# add()
# print("\n PACK ALL PIVOTING: \n")
# packer.pack_all_items()
# print("\n ^ PACK ALL PIVOTING: ^\n")

# clear_packer(packer)

# # CALLING PACK_ALL_ITEMS_RANDOM FUNCTION ON THE GIVEN ITEMS AND BINS GIVEN:

# add()
# print("\n PACK ALL RANDOM: \n")
# packer.pack_all_items_random()
# print("\n ^ PACK ALL RANDOM: ^\n")