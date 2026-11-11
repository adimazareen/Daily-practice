import matplotlib.pyplot as plt
import pandas as pd

# Example of a bar plot using Pandas for controlled ordering
# Data: Fictional monthly active users for different social media platforms
platforms = ['SocialApp', 'ConnectMe', 'ShareIt', 'LinkUp']
users_in_millions = [2900, 2100, 1500, 900]

# Create a Pandas DataFrame to maintain order
df = pd.DataFrame({'Platform': platforms, 'Users': users_in_millions})

# Use Pandas plotting
ax = df.plot(kind='bar', x='Platform', y='Users', legend=False, color='cornflowerblue')

# Set labels and title
ax.set_title('Monthly Active Users by Platform')
ax.set_xlabel('Platform')
ax.set_ylabel('Users (in Millions)')
ax.set_xticklabels(df['Platform'], rotation=0) # Keep labels horizontal

plt.show()
