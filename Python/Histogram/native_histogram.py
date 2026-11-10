# Example of a histogram for a normal distribution
np.random.seed(42)
data = np.random.randn(1000) # Generate 1000 random numbers from a standard normal distribution

plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram of a Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
