import matplotlib.pyplot as plt
import numpy as np

# Example of text and annotations
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)

# Add a title with mathematical notation
plt.title(r'Plot of $y = \sin(x)$')

# Add a simple text label
plt.text(3, 0, '<- Simple Text', fontsize=12)

# Add an arrow annotation
peak_x = 1.5 * np.pi
peak_y = np.sin(peak_x)
plt.annotate('A Local Minimum',
             xy=(peak_x, peak_y), # The point to annotate
             xytext=(peak_x, peak_y - 0.7), # The location of the text
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
             ha='center') # Horizontal alignment

plt.show()
