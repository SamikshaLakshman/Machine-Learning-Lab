# Visualize n-dimensional data using 3D Surface Plot

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


# Create 3D surface plot
ax = plt.axes(projection='3d')

ax.plot_trisurf(
    df.iloc[:, 0],
    df.iloc[:, 1],
    df.iloc[:, 2]
)

ax.set_xlabel(iris.feature_names[0])
ax.set_ylabel(iris.feature_names[1])
ax.set_zlabel(iris.feature_names[2])

plt.title("3D Surface Plot of Iris Dataset")

plt.show()