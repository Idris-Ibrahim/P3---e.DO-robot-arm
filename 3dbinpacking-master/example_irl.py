from main import Packer, Bin, Item

packer = Packer()

# Open the text file in read mode
with open('Measurement.txt', 'r') as f:
  # Read the contents of the file as a string
  numbers_string = f.readline()

# Split the string into a list of strings using a comma as a delimiter
numbers_list = numbers_string.split(',')

# Initialize empty lists for the three numbers
Widths = []
Lengths = []
Heights = []

# Iterate over the list of strings and convert each string to a float
for i, number_string in enumerate(numbers_list):
  number = float(number_string)
  # Append the float to the appropriate list
  if i == 0:
    Widths.append(number)
  elif i == 1:
    Lengths.append(number)
  elif i == 2:
    Heights.append(number)


packer.add_bin(Bin('small-bin', 25, 30, 40, 10))
packer.add_bin(Bin('medium-bin', 50, 30, 40, 10))
packer.add_bin(Bin('big-bin', 80, 50, 60, 10))

for i in range(len(Widths)):
    packer.add_items(f'ITEM {i+1}', Widths[i], Heights[i], Lengths[i], 1)
