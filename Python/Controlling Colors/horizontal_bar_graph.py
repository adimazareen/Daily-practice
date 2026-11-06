import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
from matplotlib.lines import Line2D
# Example demonstrating various color specifications
plt.figure(figsize=(10, 2))
plt.plot([0, 1], [0, 0], color='r', linewidth=4, label="'r' (red)")
plt.plot([0, 1], [1, 1], color='C1', linewidth=4, label="'C1' (default cycle orange)")
plt.plot([0, 1], [2, 2], color='limegreen', linewidth=4, label="'limegreen' (HTML name)")
plt.plot([0, 1], [3, 3], color='#FF6347', linewidth=4, label="'#FF6347' (Hex code)")
plt.plot([0, 1], [4, 4], color=(0.2, 0.4, 0.6, 0.8), linewidth=4, label="RGBA tuple")
plt.plot([0, 1], [5, 5], color='0.5', linewidth=4, label="'0.5' (Grayscale)")

plt.title("Examples of Color Specifications")
plt.ylim(-1, 6)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()
