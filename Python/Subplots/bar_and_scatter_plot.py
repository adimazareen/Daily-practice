import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10) # for reproducibility

# 1. Create a figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 2. First Subplot: Scatter Plot
x_rand = np.random.rand(50)
y_rand = np.random.rand(50)
colors = np.random.rand(50)
axes[0].scatter(x_rand, y_rand, c=colors, cmap='viridis')
axes[0].set_title('Random Scatter Plot')

# 3. Second Subplot: Bar Chart
categories = ['A', 'B', 'C', 'D']
values = [15, 30, 22, 18]
axes[1].bar(categories, values, color='skyblue')
axes[1].set_title('Category Comparison')

# Remove top and right spines from the bar chart
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)

# 4. Display the figure
plt.tight_layout()
plt.show()
