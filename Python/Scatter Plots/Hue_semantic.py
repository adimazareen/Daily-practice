import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the default Seaborn theme
sns.set_theme(style="darkgrid")

# A scatter plot using a 'hue' semantic to color points
sns.relplot(data=tips, x="total_bill", y="tip", hue="smoker")
