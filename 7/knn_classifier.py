# KNN Classifier using Euclidean and Manhattan Distance

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score, confusion_matrix



# Load dataset

glass = pd.read_csv(
    "glass.csv"
)


X = glass.drop(
    "Type",
    axis=1
)


y = glass["Type"]



# Train test split 70-30

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)



# Euclidean distance

knn_euclidean = KNeighborsClassifier(
    n_neighbors=3,
    metric='euclidean'
)


knn_euclidean.fit(
    X_train,
    y_train
)


y_pred = knn_euclidean.predict(
    X_test
)


print("Euclidean Distance")

print(
    "Accuracy:",
    accuracy_score(
        y_test,
        y_pred
    )
)


print(
    confusion_matrix(
        y_test,
        y_pred
    )
)



# Manhattan distance


knn_manhattan = KNeighborsClassifier(
    n_neighbors=3,
    metric='manhattan'
)


knn_manhattan.fit(
    X_train,
    y_train
)


y_pred = knn_manhattan.predict(
    X_test
)



print("\nManhattan Distance")


print(
    "Accuracy:",
    accuracy_score(
        y_test,
        y_pred
    )
)


print(
    confusion_matrix(
        y_test,
        y_pred
    )
)