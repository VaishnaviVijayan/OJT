import numpy as np
import matplotlib.pyplot as plt

# Generate some random data for the scatter plot
np.random.seed(0)
x = np.random.rand(1000)
y = np.random.rand(1000)

# Create a scatter plot
plt.scatter(x, y)

# Add title and labels
plt.title('Scatter Plot with 1000 Dots')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

# Show the plot
plt.show()
