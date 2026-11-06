# Import necessary libraries
from sklearn.datasets import load_iris  # To load the inbuilt Iris dataset
import pandas as pd                     # For data manipulation and DataFrame
import numpy as np                      # For numerical operations
import matplotlib.pyplot as plt         # For plotting
import seaborn as sns                   # For advanced visualizations
from sklearn.ensemble import RandomForestClassifier  # For feature importance
#This block loads all the Python libraries needed for data loading, exploration, visualization, and modeling.
# Load the inbuilt Iris dataset
iris = load_iris()

# Create a DataFrame from the dataset features
df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add the target (species) as a new column with readable names
df_iris['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Display the first 5 rows of the dataset
print("Iris Dataset (First 5 Rows):")
print(df_iris.head())
#This block loads the Iris dataset, converts it into a readable DataFrame, and shows the first few rows to understand the structure.

# Melt the dataset to long format for easier plotting with seaborn
df_melted = df_iris.melt(id_vars='species', var_name='Feature', value_name='Value')

# Display the melted DataFrame
print("Melted Data (First 5 Rows):")
print(df_melted.head())
#This transforms the wide-format DataFrame into a long-format, which is more suitable for seaborn plots (like violin or boxplots).

# Plot violin plots for each feature by species
plt.figure(figsize=(12, 6))
sns.violinplot(x="Feature", y="Value", hue="species", data=df_melted, palette='muted')
plt.title("Feature Distributions by Iris Species")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#This shows the distribution of each feature for different species using a violin plot. Helps identify which features separate species well.
# Prepare the features (X) and target (y) for the model
X = df_iris[iris.feature_names]
y = df_iris['species']

# Train a Random Forest Classifier to find feature importance
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X, y)
#This block trains a Random Forest model on the Iris dataset to learn which features are most important for classifying the species.

# Extract and sort feature importance values
importances = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf_model.feature_importances_
}).sort_values(by='Importance', ascending=False)

# Plot the feature importances
plt.figure(figsize=(8, 5))
sns.barplot(x='Importance', y='Feature', data=importances, palette='rocket')
plt.title("Feature Importance (Iris Dataset)")
plt.tight_layout()
plt.show()
#This visualizes the importance of each feature as calculated by the Random Forest model. More importance = more predictive power.

# Print the final summary based on the visualizations and model
print("From the violin plots and Random Forest results:")
print("- Petal length and petal width are the most important features for predicting Iris species.")
#This summarizes the learning: Which features matter the most in identifying the flower species.

