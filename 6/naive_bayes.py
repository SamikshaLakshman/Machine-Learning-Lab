# Naive Bayes Classifier on Titanic Dataset

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import accuracy_score, confusion_matrix


# Load dataset
df = pd.read_csv("titanic.csv")


# Select required columns
df = df[
    [
        'Pclass',
        'Sex',
        'Age',
        'Fare',
        'Survived'
    ]
]


# Handle missing values

df['Age'] = df['Age'].fillna(
    df['Age'].median()
)


# Convert categorical value

df['Sex'] = df['Sex'].map(
    {
        'male':0,
        'female':1
    }
)


# Features and target

X = df.drop(
    'Survived',
    axis=1
)

y = df['Survived']


# Split dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.1,
    random_state=42
)


# Train model

model = GaussianNB()

model.fit(
    X_train,
    y_train
)


# Prediction

y_pred = model.predict(
    X_test
)


print(
    "Accuracy:",
    accuracy_score(
        y_test,
        y_pred
    )
)


print(
    "Confusion Matrix:"
)

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)