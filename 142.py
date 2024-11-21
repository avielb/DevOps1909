import matplotlib.pyplot as plt

# Generate data for a diagonal line
x = [0, 1, 2, 5, 5, 5]  # x values
y = [0, 1, 2, 3, 4, 5]  # y values (same as x for a diagonal line)

# Create the plot
plt.figure(figsize=(10, 5))  # Set the figure size
plt.plot(x, y, label='Diagonal Line', color='blue')  # Plot the data

# Add titles and labels
plt.title('Simple Diagonal Line Plot')
plt.xlabel('X values')
plt.ylabel('Y values')

# Add a legend
plt.legend()

# Show grid
plt.grid()

# Show the plot
plt.show()
