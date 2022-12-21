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

def add_random(RandomBins, RandomItems):
    
    # ADDING BINS TYPES FOR THE ALGORITHMS DISPOSAL:
    # packer.add_bin(Bin('SMALL BIN', float(25), float(10), float(12), float(10)))
    # packer.add_bin(Bin('DOUBLE - SMALL BIN', float(50), float(20), float(50), float(30)))
    # packer.add_bin(Bin('MEDIUM BIN', float(100), float(50), float(70), float(80)))
    # packer.add_bin(Bin('BIG BIN', float(100), float(100), float(100), float(150)))
    # packer.add_bin(Bin('HUGE BIN', float(100), float(100), float(200), float(200)))
    
    # Random 1-10 types of Bins:
    
    item = random.randrange(1, 40)
    
    # ADDING BINS TO PAKER
    
    packer.add_bin(Bin(f'BIN 1', round(random.uniform(0, 50), 3), round(random.uniform(0, 50), 3), round(random.uniform(0, 50), 3), round(random.uniform(0, 50), 3)))
    packer.add_bin(Bin(f'BIN 2', round(random.uniform(50, 100), 3), round(random.uniform(50, 100), 3), round(random.uniform(50, 100), 3), round(random.uniform(50, 100), 3)))
    packer.add_bin(Bin(f'BIN 3', round(random.uniform(100, 150), 3), round(random.uniform(100, 150), 3), round(random.uniform(100, 150), 3), round(random.uniform(100, 150), 3)))
    packer.add_bin(Bin(f'BIN 4', round(random.uniform(150, 200), 3), round(random.uniform(150, 200), 3), round(random.uniform(150, 200), 3), round(random.uniform(150, 200), 3)))
    packer.add_bin(Bin(f'BIN 5', round(random.uniform(200, 250), 3), round(random.uniform(200, 250), 3), round(random.uniform(200, 250), 3), round(random.uniform(200, 250), 3)))
    

    # ADDING ITEMS TO BE PACKER:
    for i in range(item):
        packer.add_item(Item(f'ITEM {i}', round(random.uniform(25, 100), 3), round(random.uniform(25, 100), 3), round(random.uniform(25, 100), 3), round(random.uniform(0, 5), 3)))
        
    for bin in packer.bins:
        RandomBins.append(bin)
        
    for item in packer.items:
        RandomItems.append(item)
        
def insert_same_random_into_packer(RanBinList = [], RanItemList =[]):
    
    for bin in RanBinList:
        packer.add_bin(bin)

    for item in RanItemList:
        packer.add_item(item)

for j in range(100):
    for i in range(10):
            
        RandomBins = []

        RandomItems = []

        Results_erick_dube = []

        Results_random = []
        
        Results_small = []

        add_random(RandomBins, RandomItems)
        
        print("\n PACK ALL PIVOTING: \n")

        packer.pack_all_items(Results_erick_dube)

        clear_packer(packer) 
        
        insert_same_random_into_packer(RandomBins, RandomItems)
        
        print("\n PACK ALL SMALL: \n")

        packer.pack_all_items_small(Results_random)
        
        clear_packer(packer)
        
        insert_same_random_into_packer(RandomBins, RandomItems)
        
        print("\n PACK ALL RANDOM: \n")

        packer.pack_all_items_random(Results_random)
        
        clear_packer(packer)  
         
# CALLING PACK_ALL_ITEMS FUNCTION ON THE GIVEN ITEMS AND BINS GIVEN:

# list1 = []
# list2 = []

# add()
# print("\n PACK ALL PIVOTING: \n")
# packer.pack_all_items(list1)
# print("\n ^ PACK ALL PIVOTING: ^\n")

# clear_packer(packer)

# # CALLING PACK_ALL_ITEMS_RANDOM FUNCTION ON THE GIVEN ITEMS AND BINS GIVEN:

# add()
# print("\n PACK ALL RANDOM: \n")
# packer.pack_all_items_random(list2)
# print("\n ^ PACK ALL RANDOM: ^\n")

# clear_packer(packer)

# # CALLING PACK_ALL_ITEMS_SMALL FUNCTION ON THE GIVEN ITEMS AND BINS GIVEN:
# add()
# print("\n PACK ALL SMALL BINS: \n")
# packer.pack_all_items_small()
# print("\n ^ PACK ALL SMALL BINS: ^\n")

# clear_packer(packer)