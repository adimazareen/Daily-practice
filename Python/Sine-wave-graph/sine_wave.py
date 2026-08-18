import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.sin(x)                 # Sine wave

# Create the line graph
plt.figure(figsize=(10, 5))  # Set the size of the figure
plt.plot(x, y, label='Sine Wave', color='blue')  # Plot the line
plt.title('Sine Wave Example')  # Title of the graph
plt.xlabel('X-axis')             # Label for x-axis
plt.ylabel('Y-axis')             # Label for y-axis
plt.axhline(0, color='black',linewidth=0.5, ls='--')  # Horizontal line at y=0
plt.axvline(0, color='black',linewidth=0.5, ls='--')  # Vertical line at x=0
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)  # Add a grid
plt.legend()                     # Show the legend
plt.savefig('sine_wave.png')    # Save the figure
plt.show()                      # Display the graph
