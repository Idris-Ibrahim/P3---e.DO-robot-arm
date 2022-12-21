from main import Packer, Bin, Item

packer = Packer()

# Open the text file in read mode
with open('Measurements.txt', 'r') as f:
  # Initialize empty lists for the three numbers
  Widths = []
  Heights = []
  Lengths = []

  # Read each line of the file
  for line in f:
    # Split the line into a list of strings using two commas as a delimiter
    numbers_list = line.split(',')

    # Iterate over the list of strings and convert each string to a float
    for i, number_string in enumerate(numbers_list):
      number = float(number_string)
      # Append the float to the appropriate list
      if i == 0:
        Widths.append(number)
      elif i == 1:
        Heights.append(number)
      elif i == 2:
        Lengths.append(number)


packer.add_bin(Bin('small-bin', 15, 10, 10, 10))
packer.add_bin(Bin('medium-bin', 20, 10, 20, 10))
packer.add_bin(Bin('big-bin', 10, 20, 30, 10))

for i in range(len(Widths)):
    packer.add_item(Item(f'ITEM {i+1}', Widths[i], Heights[i], Lengths[i], 1))

packer.pack_all_items_Nodoc()