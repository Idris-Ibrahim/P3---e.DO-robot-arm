# import matplotlib.pyplot as plt


# # Create a list of numerical data
# data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# data2 = [1, 2, 3, 4, 5, 6, 7]
# # Create a box plot using the boxplot function
# plt.boxplot([data1, data2], vert =False)

# # Add a title and label the axes
# plt.title("Box Plot of Numerical Data")
# plt.xlabel("values")
# plt.ylabel("Data")

# # Display the plot
# plt.show()

import matplotlib.pyplot as plt

# Open the first file in read mode
with open('tests/Mcheck_test.txt', 'r') as file:
  # Read all lines in the file
  lines = file.readlines()

# Create an empty list for the first set of values
Mcheck_results = []

# Iterate over the lines in the file
for line in lines:
  # Strip leading and trailing whitespace from the line
  line = line.strip()
  # Append the value to the list
  Mcheck_results.append(float(line))

# Open the second file in read mode
with open('tests/random_test.txt', 'r') as file:
  # Read all lines in the file
  lines = file.readlines()

# Create an empty list for the second set of values
random_results = []

# Iterate over the lines in the file
for line in lines:
  # Strip leading and trailing whitespace from the line
  line = line.strip()
  # Append the value to the list
  random_results.append(float(line))
  
# Open the second file in read mode
with open('tests/small_test.txt', 'r') as file:
  # Read all lines in the file
  lines = file.readlines()

# Create an empty list for the second set of values
small_results = []

# Iterate over the lines in the file
for line in lines:
  # Strip leading and trailing whitespace from the line
  line = line.strip()
  # Append the value to the list
  small_results.append(float(line))

# Create a boxplot comparing the two sets of values
plt.boxplot([random_results, small_results, Mcheck_results], vert = False, labels= ["Random Algorithm", "Small Algorithm", "Mcheck Algorithm"])
plt.title("Boxplot of algorithm retults")
plt.xlabel("% wasted space per order")
plt.grid()
plt.show()
