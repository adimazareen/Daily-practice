import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

try:
    import mplfinance as mpf
except ImportError:
    %pip install --upgrade mplfinance
    import mplfinance as mpf

# Create a sample financial DataFrame
# This simulates 30 days of stock data
np.random.seed(42)
dates = pd.date_range(start='2025-01-01', periods=30)
data = 100 + (np.random.randn(30) * 3 + np.linspace(0, 15, 30)).cumsum()

# Create Open, High, Low, Close columns
ohlc_data = {
    'Open': data - np.random.uniform(0, 1, 30),
    'High': data + np.random.uniform(0, 2, 30),
    'Low': data - np.random.uniform(0, 2, 30),
    'Close': data + np.random.randn(30) * 0.5
}
df_stocks = pd.DataFrame(ohlc_data, index=dates)

# Plot the candlestick chart using mplfinance
mpf.plot(df_stocks,
         type='candle',
         style='yahoo',
         title='Sample Candlestick Chart',
         ylabel='Price ($)')
