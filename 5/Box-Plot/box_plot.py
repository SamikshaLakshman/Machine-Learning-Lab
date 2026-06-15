# Box Plot using Iris Dataset

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


iris = load_iris()


df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)


plt.boxplot(df)


plt.xticks(
    range(1,len(df.columns)+1),
    df.columns,
    rotation=45
)


plt.title("Box Plot of Iris Dataset")

plt.show()