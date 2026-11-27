import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the default Seaborn theme
sns.set_theme(style="darkgrid")

# Load the "tips" dataset
tips = sns.load_dataset("tips")

# Create a basic scatter plot
sns.relplot(data=tips, x="total_bill", y="tip")
