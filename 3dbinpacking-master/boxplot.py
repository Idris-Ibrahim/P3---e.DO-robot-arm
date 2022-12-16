import matplotlib.pyplot as plt

# Create a list of numerical data
data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data2 = [1, 2, 3, 4, 5, 6, 7]
# Create a box plot using the boxplot function
plt.boxplot([data1, data2], vert =False)

# Add a title and label the axes
plt.title("Box Plot of Numerical Data")
plt.xlabel("values")
plt.ylabel("Data")

# Display the plot
plt.show()