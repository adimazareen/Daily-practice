from matplotlib.ticker import MultipleLocator, NullLocator
import matplotlib.pyplot as plt
import numpy as np

# Data that grows exponentially
x = np.linspace(1, 10, 100)
y = np.exp(x)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Linear Scale
ax1.plot(x, y)
ax1.set_title('Linear Scale')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis')

# Plot 2: Logarithmic Scale
ax2.plot(x, y)
ax2.set_yscale('log') # Set y-axis to a logarithmic scale
ax2.set_title('Logarithmic Scale')
ax2.set_xlabel('X-axis')

# Customize the ticks on the log plot's x-axis
ax2.xaxis.set_major_locator(MultipleLocator(2)) # Major ticks every 2 units
ax2.xaxis.set_minor_locator(MultipleLocator(0.5)) # Minor ticks every 0.5 units

plt.show()
