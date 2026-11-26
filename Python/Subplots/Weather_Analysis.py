import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. URL is already defined in a previous cell, as is the DataFrame `df_weather`
df_weather = 'https://raw.githubusercontent.com/vega/vega-datasets/main/data/seattle-weather.csv'

# 2. Create a 2x1 grid of subplots that share the same x-axis
fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# 3. First Subplot: Minimum Temperature
axes[0].plot(df_weather.index, df_weather['temp_min'], color='deepskyblue')
axes[0].set_title('Minimum Daily Temperature')
axes[0].set_ylabel('Temp (°C)')

# 4. Second Subplot: Wind Speed
axes[1].plot(df_weather.index, df_weather['wind'], color='slategray')
axes[1].set_title('Average Daily Wind Speed')
axes[1].set_ylabel('Speed (m/s)')

# 5. Add a main title for the entire figure
fig.suptitle('Seattle Weather Metrics', fontsize=16)

# 6. Display the final figure
plt.tight_layout(rect=[0, 0, 1, 0.96]) # Adjust layout
plt.show()
