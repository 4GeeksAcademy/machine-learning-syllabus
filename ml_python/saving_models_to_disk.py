# -*- coding: utf-8 -*-
"""Saving_models_to_disk.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hns46pPhLCkqYA8wJwmulKs1Mpg5xCpk

## Model persistence

It is possible to save a model in scikit-learn by using Python’s built-in persistence model, pickle:
"""

import sklearn.datasets
dir(sklearn.datasets)

from sklearn import svm
from sklearn import datasets
clf = svm.SVC()
X, y = datasets.load_digits(return_X_y=True)
print(len(X))
clf.fit(X, y)

type(X)
print(X.shape)

"""### Persisting the model using pickle"""

import pickle
file = open("svm_dump.model",'wb')
s = pickle.dump(clf, file)

file = open("svm_dump.model",'rb')
clf2 = pickle.load(file)

clf2.predict(X[0:50])

"""##### In the specific case of scikit-learn, it may be more interesting to use joblib’s replacement for pickle (joblib.dump & joblib.load), which is more efficient on big data but it can only pickle to the disk and not to a string:"""

from joblib import dump, load
dump(clf, 'filename.joblib')

"""##### Later, you can reload the pickled model (possibly in another Python process) with:"""

clf = load('filename.joblib') 
clf.predict(X[0:50])
