import matplotlib.pyplot as plt
import numpy as np

# Example of applying a style sheet
# Apply the 'fivethirtyeight' style
plt.style.use('fivethirtyeight')

# Create a simple plot
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x) + x/2, label='Series A')
plt.plot(x, np.cos(x) - x/2, label='Series B')

plt.title("Plot with 'fivethirtyeight' Style")
plt.xlabel("X-Value")
plt.ylabel("Y-Value")
plt.legend()
plt.show()

# Reset to default style for any subsequent plots
plt.rcdefaults()
