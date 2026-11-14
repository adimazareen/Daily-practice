import matplotlib.pyplot as plt
import numpy as np

# Example: Plotting a mathematical "rose" curve on a polar chart
theta = np.linspace(0, 2. * np.pi, 1000) # Angle from 0 to 2*pi

# A simple rose curve equation
radius = np.cos(6 * theta)

plt.figure(figsize=(6,6))
ax = plt.subplot(111, projection='polar')
ax.plot(theta, radius, color='purple', linewidth=3)
ax.set_title("Polar Plot of a Rose Curve (r = cos(6θ))")
plt.show()
