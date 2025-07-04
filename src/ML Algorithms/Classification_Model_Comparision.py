# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 10:10:00 2025

@author: tahir
"""
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import ListedColormap

# Make classification ile kendi veri setlerimizi oluşturabiliriz.
from sklearn.datasets import make_classification, make_moons, make_circles
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.inspection import DecisionBoundaryDisplay

# Redundant => Gereksiz / Bilgi içermeyen feature sayısı
# Informative => Bilgilendirici / Bilgi içeren feature sayısı
# Clusters Per Class => Veri kümeleri birbiri içine karışsın mı karışmasın mı...
X, y = make_classification(n_samples=100, n_features=2, n_redundant=0, n_informative=2, n_clusters_per_class=1,
                           random_state=42)
X += 1.2 * np.random.uniform(low=0, high=1, size=X.shape)
Xy = (X, y)

datasets = [Xy,
            make_moons(noise=0.2, random_state=42),
            make_circles(noise=0.1, factor=0.3, random_state=42)]

names = ["Nearest Neighbors", "Linear SVM", "Decision Tree", "Random Forest", "Naive Bayes"]
classifiers = [KNeighborsClassifier(),
               SVC(),
               DecisionTreeClassifier(),
               RandomForestClassifier(),
               GaussianNB()]

fig, axes = plt.subplots(nrows=len(datasets), ncols=len(classifiers) + 1, figsize=(15, 9))

# Renk Haritaları
cm_bright = ListedColormap(["darkred", "darkblue"])

for i, ds in enumerate(datasets):
    X, y = ds

    # Veriyi eğitim ve test olarak ayır
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    ax = axes[i, 0]

    if i == 0:
        ax.set_title("Input Data")

    ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright, edgecolors="k")
    ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, alpha=0.6, edgecolors="k")
    ax.set_xticks(())
    ax.set_yticks(())

    for j, (name, clf) in enumerate(zip(names, classifiers)):

        ax = axes[i, j + 1]

        # Standart Scaler --
        model = make_pipeline(StandardScaler(), clf)
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)  # Accuracy

        # Karar sınırını çiz
        DecisionBoundaryDisplay.from_estimator(
            model, X, cmap=plt.cm.RdBu, ax=ax, alpha=0.8, response_method="predict")

        # Eğitim ve test noktalarını çiz.
        ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright, edgecolors="k")
        ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, edgecolors="k", alpha=0.6)

        ax.set_xticks(())
        ax.set_yticks(())

        if i == 0:
            ax.set_title(name)

        # Skor Bilgisi
        ax.text(
            0.95, 0.05, f"{score:.2f}",
            transform=ax.transAxes,
            fontsize=12,
            horizontalalignment="right",
            verticalalignment="bottom",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1, alpha=0.7)
        )

plt.tight_layout()
plt.show()