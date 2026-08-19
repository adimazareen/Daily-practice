import matplotlib.pyplot as plt
import numpy as np

# Data for the bar graph
x = np.array(['Apple', 'Facefool', 'Microsoft', 'OpenAI', 'Netflix'])
y = np.array([10, 15, 25, 30, 20])

colors = np.array(['red', 'blue', 'green', 'black', 'yellow'])

plt.bar(x, y, color=colors, width=0.5)

plt.title("Bar Graph of Companies")
plt.xlabel("Companies")
plt.ylabel("Values")

plt.show()
