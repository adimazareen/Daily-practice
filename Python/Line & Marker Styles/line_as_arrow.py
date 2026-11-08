import matplotlib.pyplot as plt
import numpy as np

# Example demonstrating various line styles
y_base = np.array([1, 2, 3, 2, 1])

plt.plot(y_base, lw=3, ls='--', label="'--' (dashed)")
plt.plot(y_base + 1, lw=3, ls='-.', label="'-.' (dashdot)")
plt.plot(y_base + 2, lw=3, ls=':', label="':' (dotted)")

# Demonstrating dash_capstyle on thick lines
plt.plot(y_base + 3, lw=10, ls='--', dash_capstyle='round', label="capstyle='round'")

plt.title("Line Style Customization")
plt.ylim(0, 5)
plt.legend()
plt.show()
