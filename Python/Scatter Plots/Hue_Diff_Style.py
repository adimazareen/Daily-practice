import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the default Seaborn theme
sns.set_theme(style="darkgrid")

# Using hue and style to represent two different variables
sns.relplot(
    data=tips,
    x="total_bill", y="tip", hue="smoker", style="time",)
