# Agglomerative Clustering

from sklearn.datasets import load_iris

from scipy.cluster.hierarchy import linkage, dendrogram

import matplotlib.pyplot as plt



data = load_iris().data[:10]



# Single linkage

plt.figure()

dendrogram(
    linkage(
        data,
        method='single'
    )
)

plt.title(
    "Single Linkage"
)

plt.show()



# Complete linkage


plt.figure()


dendrogram(
    linkage(
        data,
        method='complete'
    )
)


plt.title(
    "Complete Linkage"
)


plt.show()