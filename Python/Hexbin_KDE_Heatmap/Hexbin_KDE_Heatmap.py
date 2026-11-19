import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generate some bivariate normal data (clustered in the center)
np.random.seed(42)
data = pd.DataFrame(np.random.randn(2000, 2), columns=['X', 'Y'])

# Create a 1x2 subplot layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Hexbin plot using Pandas
data.plot(kind='hexbin', x='X', y='Y', gridsize=25, cmap='viridis', ax=ax1)
ax1.set_title('Pandas Hexbin Plot')

# Plot 2: 2D KDE plot using Seaborn
sns.kdeplot(data=data, x='X', y='Y', fill=True, cmap='rocket', ax=ax2)
ax2.set_title('Seaborn 2D KDE Plot')

plt.show()

# Example of a Seaborn Heatmap
correlation_matrix = data.corr()
plt.figure(figsize=(6, 5))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Seaborn Heatmap of a Correlation Matrix')
plt.show()
