import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
from matplotlib.lines import Line2D
# Example comparing 'viridis' and 'jet'
N = M = 200
X, Y = np.ogrid[0:20:N*1j, 0:20:M*10]
data = np.sin(np.pi * X*2 / 20) * np.cos(np.pi * Y*2 / 20)

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(8, 3))

im1 = ax1.imshow(data, cmap='viridis')
ax1.set_title("Default: 'viridis'")
fig.colorbar(im1, ax=ax1, shrink=0.85)

im2 = ax2.imshow(data, cmap='jet')
ax2.set_title("Classic: 'jet'")
fig.colorbar(im2, ax=ax2, shrink=0.85)

fig.tight_layout()
plt.show()

# Example of a custom colormap on a scatter plot
np.random.seed(52)
x,y,c = zip(*np.random.rand(50,3))
custom_cmap = matplotlib.colors.LinearSegmentedColormap.from_list("custom_cmap", ["red","yellow","green"])
plt.scatter(x, y, c=c, cmap=custom_cmap)
plt.colorbar()
plt.title("Scatter Plot with a Custom Colormap")
plt.show()
