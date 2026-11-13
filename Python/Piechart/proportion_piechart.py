# Data: Website traffic sources for a month
sources = ['Organic Search', 'Direct', 'Referral', 'Social Media', 'Other']
traffic_percent = [45, 25, 15, 10, 5]
explode = (0.1, 0, 0, 0, 0) # Explode the 1st slice (Organic Search)

plt.figure(figsize=(6, 6)) # Ensure the figure is a square
plt.pie(traffic_percent,
        labels=sources,
        explode=explode,
        autopct='%1.1f%%',
        startangle=90, # Rotate the start of the pie
        shadow=True)

plt.title('Website Traffic Sources')
plt.axis('equal') # Ensures the pie is drawn as a circle.
plt.show()
