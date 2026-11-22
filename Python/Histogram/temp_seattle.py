import matplotlib.pyplot as plt
import pandas as pd

# This URL points directly to a raw CSV file from the vega-datasets repository.
url = 'https://raw.githubusercontent.com/vega/vega-datasets/main/data/seattle-weather.csv'

# Use Pandas to read the data and parse the 'date' column
df_weather = pd.read_csv(url, parse_dates=['date'])

# Set the date as the index for easier time-series plotting
df_weather.set_index('date', inplace=True)

# Plot the daily maximum temperature for the whole dataset
plt.figure(figsize=(12, 6))
df_weather['temp_max'].plot(color='crimson')

plt.title('Maximum Daily Temperature in Seattle', fontsize=16)
plt.ylabel('Temperature (°C)')
plt.xlabel('Date')
plt.show()
