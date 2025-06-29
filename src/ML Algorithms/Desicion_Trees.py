from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix

import matplotlib.pyplot as plt

iris = load_iris()

X = iris.data  # features
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Eğitim - Hyperparameter Ayarı
tree_clf = DecisionTreeClassifier(criterion="gini", max_depth=6,
                                  random_state=42)  # Criterion = entropy/gini olarak kullanıyoruz.
tree_clf.fit(X_train, y_train)

# DT Evaluation
y_pred = tree_clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

# Tree Görselleştirme

plt.figure(figsize=(15, 10))
# Ağacı çizmek için plot_tree özel fonksiyonu kullanılır.
# Filled parametresi node'ların içini renkli renkli doldurmayı sağlar.

plot_tree(tree_clf, filled=True, feature_names=iris.feature_names, class_names=list(iris.target_names))

plt.show()

feature_importances = tree_clf.feature_importances_
feature_names = iris.feature_names

feature_importance_sorted = sorted(zip(feature_importances, feature_names), reverse=True)

for importance, feature_name in feature_importance_sorted:
    print(f"{feature_name}: {importance}")

# %%
# Feature Selection - Feature Engineering

# Bu kod
# Eğer sadece iki özelliğe baksaydık, karar ağacı çiçekleri nasıl sınıflandırırdı?"
# sorusunun cevabını 6 farklı senaryo için çizer.

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.inspection import DecisionBoundaryDisplay

import numpy as np
import matplotlib.pyplot as plt

# veri seti inceleme
iris = load_iris()

n_classes = 3
plot_colors = "ryb"

# Burada ikili feature seçimi yaparak eğitim gerçekleştireceğiz

for pairidx, pair in enumerate([[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]):

    X = iris.data[:, pair]
    y = iris.target

    clf = DecisionTreeClassifier().fit(X, y)

    # subplot parametreleri satır-sütun sayısı ve grafik numarasını belirler.
    ax = plt.subplot(2, 3, pairidx + 1)  # Grafik numarası 1'den başlar.
    plt.tight_layout(h_pad=0.5, w_pad=0.5, pad=2.5)  # Horizontal anf vertical padding...
    # Arka plandaki renklerin birbirine değdiği yerleri çizer.
    DecisionBoundaryDisplay.from_estimator(clf, X,
                                           cmap=plt.cm.RdYlBu,
                                           response_method='predict',
                                           ax=ax,
                                           xlabel=iris.feature_names[pair[0]],
                                           ylabel=iris.feature_names[pair[1]])

    for i, color in zip(range(n_classes), plot_colors):
        idx = np.where(y == i)
        # (Fancy Indexing), X arrayi içinden, yine bir array vererek indeksleneiblir.
        plt.scatter(X[idx, 0], X[idx, 1], c=color, label=iris.target_names[i], cmap=plt.cm.RdYlBu, edgecolors='black')

    plt.legend()































