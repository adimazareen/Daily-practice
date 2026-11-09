# Example of customizing plot spines
y = [0, 1, 4, 9, 16]
plt.plot(y)

# Get the current axes
ax = plt.gca()

# Make the top and right spines invisible
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Make the left and bottom spines thicker and change their color
ax.spines['left'].set_linewidth(4)
ax.spines['left'].set_color('green')
ax.spines['bottom'].set_linewidth(2)
ax.spines['bottom'].set_color('darkblue')

plt.title("Plot with Customized Spines")
plt.show()
