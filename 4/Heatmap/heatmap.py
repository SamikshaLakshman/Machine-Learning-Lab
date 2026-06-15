# Heatmap using Iris Dataset

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)


plt.imshow(
    df.corr(),
    cmap="coolwarm"
)

plt.colorbar()

plt.title("Heatmap of Iris Dataset")

plt.show()