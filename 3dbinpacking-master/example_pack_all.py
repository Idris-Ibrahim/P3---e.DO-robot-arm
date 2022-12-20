from main import Packer, Bin, Item
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


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

    packer.add_item(Item('Fugl', 10, 10, 7, 0.5))
    packer.add_item(Item('Hund', 20, 10, 20, 10))
    packer.add_item(Item('Mus', 8, 5, 12, 0.5))
    packer.add_item(Item('Rat', 8, 5, 12, 3))
    packer.add_item(Item('Turtle', 5, 4, 15, 4))
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


# Define the dimensions of the bins and items
bins = [(10, 10, 12), (20, 10, 12), (30, 15, 20), (50, 30, 40), (100, 50, 100)]
items = [(10, 10, 7), (20, 10, 20), (8, 5, 12), (8, 5, 12), (5, 4, 15), (10, 4, 4)]

# Iterate over the bins
for i, bin in enumerate(bins):
    # Create a figure and an axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the bin as a box
    verts = [
        (0, 0, 0),
        (0, bin[1], 0),
        (bin[0], bin[1], 0),
        (bin[0], 0, 0),
        (0, 0, bin[2]),
        (0, bin[1], bin[2]),
        (bin[0], bin[1], bin[2]),
        (bin[0], 0, bin[2]),
    ]
    ax.add_collection(Poly3DCollection([verts], alpha=.25, facecolor='blue'))

    # Plot the items as boxes inside the bin
    for item in items:
        verts = [
            (0, 0, 0),
            (0, item[1], 0),
            (item[0], item[1], 0),
            (item[0], 0, 0),
            (0, 0, item[2]),
            (0, item[1], item[2]),
            (item[0], item[1], item[2]),
            (item[0], 0, item[2]),
        ]
        ax.add_collection(Poly3DCollection([verts], alpha=.25, facecolor='red'))
        ax.set_xlim(0, bin[0])
        ax.set_ylim(0, bin[1])
        ax.set_zlim(0, bin[2])

    # Show the plot
    plt.show()
