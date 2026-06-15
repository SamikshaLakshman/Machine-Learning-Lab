# Contour Plot using Iris Dataset

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)


plt.tricontourf(
    df.iloc[:,0],
    df.iloc[:,1],
    df.iloc[:,2]
)

plt.colorbar()

plt.title("Contour Plot of Iris Dataset")

plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

plt.show()