import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(170, 10, 250)  # Mean=170, Std Dev=10, 250 data points

plt.hist(data, bins=10, color='blue', edgecolor='black')

plt.title("Histogram of Random Data")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()
