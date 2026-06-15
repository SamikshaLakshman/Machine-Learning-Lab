# PCA and LDA Algorithms

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

from sklearn.decomposition import PCA

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis



iris = load_iris()


X = iris.data

y = iris.target



# PCA

pca = PCA(
    n_components=2
)


X_pca = pca.fit_transform(
    X
)



plt.scatter(
    X_pca[:,0],
    X_pca[:,1],
    c=y
)


plt.xlabel(
    "Principal Component 1"
)


plt.ylabel(
    "Principal Component 2"
)


plt.title(
    "PCA"
)


plt.show()



# LDA


lda = LinearDiscriminantAnalysis(
    n_components=2
)


X_lda = lda.fit_transform(
    X,
    y
)



plt.scatter(
    X_lda[:,0],
    X_lda[:,1],
    c=y
)


plt.xlabel(
    "Linear Discriminant 1"
)


plt.ylabel(
    "Linear Discriminant 2"
)


plt.title(
    "LDA"
)


plt.show()