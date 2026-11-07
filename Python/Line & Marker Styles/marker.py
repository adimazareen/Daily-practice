import matplotlib.pyplot as plt
import numpy as np

# --- 1. Prepare Data ---
x_data = np.linspace(0, 10, 20)
y1 = x_data
y2 = x_data + 2

# --- 2. Create Plot ---
fig, ax = plt.subplots()
ax.plot(x_data, y1, label='Series 1') # Initial plot of the first series

# --- 3. Customize the Plot ---
# ==> UNCOMMENT the line below to add a second data series.
# ax.plot(x_data, y2, label='Series 2')

# ==> UNCOMMENT the line below to change the style of the first series to a red dashed line.
# ax.plot(x_data, y1, color='red', linestyle='--', label='Series 1')

# ==> UNCOMMENT the line below to add star markers to the second series and remove its line.
# ax.plot(x_data, y2, marker='*', markersize=10, color='green', linestyle='None', label='Series 2')

# ==> UNCOMMENT the line below to add a legend to distinguish the series.
# ax.legend()

# --- 4. Show Plot ---
plt.title("Marker and Line Customization")
plt.show()
