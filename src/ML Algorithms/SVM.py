# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 19:58:25 2025

@author: tahir
"""

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.svm import SVC

import matplotlib.pyplot as plt

digits = load_digits()

fig, axes = plt.subplots(nrows=2, ncols=5, figsize=(10, 5),
                         subplot_kw={"xticks": [], "yticks": []})

# axes.flat axes'leri tek boyutlu iterable bir arraye dönüştürür.
for idx, ax in enumerate(axes.flat):
    ax.imshow(digits.images[idx], cmap="binary", interpolation="nearest")
    ax.set_title(digits.target[idx])

plt.show()

X = digits.data
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=43)

svm_clf = SVC(kernel="linear", random_state=42)
svm_clf.fit(X_train, y_train)

y_pred = svm_clf.predict(X_test)
accuracy_score = svm_clf.score(X_test, y_test)

print(f"Accuracy Score: {accuracy_score}")

# Ekstra Yöntem - Classification Report

print(classification_report(y_test, y_pred))