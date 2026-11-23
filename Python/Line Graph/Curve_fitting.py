import matplotlib.pyplot as plt
import numpy as np

#Sample data: Monthly active users over 12 months
months = np.arange(1, 13)
users = np.array([100, 120, 150, 190, 240, 300, 350, 410, 480, 560, 650, 750])

# Fit a 2nd degree polynomial (a quadratic curve) to the data
coeffs = np.polyfit(months, users, 2)
p = np.poly1d(coeffs)

# Define our future timeline for extrapolation (next 6 months)
future_months = np.arange(1, 19)

# Plot the original data, the fitted curve, and the extrapolation
plt.figure(figsize=(10, 6))
plt.plot(months, users, 'o', ms=8, label='Actual Monthly Users')
plt.plot(future_months, p(future_months), '--', lw=2, color='darkorange', label='Fitted & Extrapolated Trend')

plt.title('User Growth and Extrapolation')
plt.xlabel('Month')
plt.ylabel('Active Users')
plt.xticks(future_months)
plt.legend()
plt.show()
