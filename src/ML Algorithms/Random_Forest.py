# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 15:49:30 2025

@author: tahir
"""

from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt

oli_faces = fetch_olivetti_faces()

plt.figure()
for i in range(2):
    plt.subplot(1, 2, i + 1)
    plt.imshow(oli_faces.images[i + 10], cmap="gray")  # Grayscale yaptık çünkü görüntümüz zaten renkli değil..
    plt.axis("off")

plt.show()

X = oli_faces.data
y = oli_faces.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

acc_list = []
n_estimators = range(5, 500, 50)
for i, estimator in enumerate(n_estimators):
    rf_clf = RandomForestClassifier(n_estimators=estimator, random_state=42)
    rf_clf.fit(X_train, y_train)

    y_pred = rf_clf.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    acc_list.append(accuracy)

plt.figure(figsize=(10, 6))
plt.scatter(n_estimators, acc_list, c="Green")
plt.title("Random Forest Accuracy vs. Number of Estimators")
plt.xlabel("Number of Estimators")
plt.ylabel("Accuracy Score")
plt.grid(True)
plt.xticks(n_estimators)

plt.show()