# Visualize n-dimensional data using Scatter Plot

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()

# Convert to dataframe
df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

# Scatter plot
plt.scatter(
    df.iloc[:, 0],
    df.iloc[:, 1],
    c=iris.target
)

plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title("Scatter Plot of Iris Dataset")

plt.show()