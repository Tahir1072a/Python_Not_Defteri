# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 14:27:37 2025

@author: tahir
"""
# uci arşiv.
# https://archive.ics.uci.edu/dataset/45/heart+disease

from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

import pandas as pd

heart_disease = fetch_ucirepo(id=45)

# Missing Value Problem - EDA

df = pd.DataFrame(data=heart_disease.data.features)

df["Target"] = heart_disease.data.targets

# isna() fonksiyonu her bir satır ve sütun için true/false değerleri return eder.
# Eğer ilgili hücre nan değer içeriyorsa o hücre için True return edecektir.
# Birinci any() bize her bir sütun için kontrol yapıp ilgili sütun içinde True olup olmadığını kontrol eder.
# Buradan bir array return edilecektir. Daha sonra ikinci any() ile bu array içerisinde True var mı
# o kontrol edilir. Eğer varsa ilgili Data Frame içinde en az bir tane none değer olduğu anlamına gelmektedir.
if df.isna().any().any():
    df.dropna(inplace=True)

X = df.drop(["Target"],
            axis=1).values  # axis = 1, sütun olarak drop eder. values yaparsak bize numpy array olarak return eder.
y = df["Target"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

log_reg = LogisticRegression(penalty='l2', C=1, solver="lbfgs", max_iter=100)
log_reg.fit(X_train, y_train)

accuracy_score = log_reg.score(X_test, y_test)

print(f"Accuracy Score: {accuracy_score}")