# Standard imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set default style for a consistent look
plt.style.use('seaborn-v0_8-whitegrid')

# The recommended way: Use plt.subplots() to create a grid of plots
# This creates a 2x2 grid and shares the x-axis among plots in the same column
# and the y-axis among plots in the same row.
fig, axes = plt.subplots(2, 2, figsize=(10, 8), sharex='col', sharey='row')

# The 'axes' object is a 2D NumPy array. We can access each subplot by its index.
x = np.linspace(0, 2 * np.pi, 100)
axes[0, 0].plot(x, np.sin(x), color='b')
axes[0, 0].set_title('sin(x)')

axes[0, 1].plot(x, np.cos(x), color='r')
axes[0, 1].set_title('cos(x)')

axes[1, 0].plot(x, np.tan(x), color='g')
axes[1, 0].set_title('tan(x)')
axes[1, 0].set_ylim(-5, 5) # Limit tan(x) y-axis for better visibility

axes[1, 1].plot(x, np.exp(np.sin(x)), color='purple')
axes[1, 1].set_title('exp(sin(x))')

# Use a single suptitle for the entire figure
fig.suptitle('A Grid of Different Functions', fontsize=16)

# Automatically adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96]) # rect leaves space for the suptitle
plt.show()
