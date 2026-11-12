# Example: Comparing user engagement scores before and after a website redesign
df = pd.DataFrame({
    'Before': [6.5, 5.8],
    'After': [8.2, 6.1]
}, index=['Redesign', 'Control Group'])

# Define the error (e.g., standard deviation)
error = [[0.5, 0.4], [0.3, 0.5]] # Error for Before and After columns

# Plot the grouped bar chart with error bars
ax = df.plot(kind='bar', yerr=error, capsize=4, color=['salmon', 'lightblue'])

ax.set_title('User Engagement Before vs. After Redesign')
ax.set_ylabel('Average Engagement Score')
ax.set_xticklabels(df.index, rotation=0)
plt.show()
