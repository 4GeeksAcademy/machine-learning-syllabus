# -*- coding: utf-8 -*-
"""Metrics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10G6MvrlTj-yFPVmkgU6EWihxOTRPg87q

# Evaluate Your Model’s Performance

## Loading common libraries
"""

import pandas as pd
import numpy as np

import sklearn
print(sklearn.__version__)

import sklearn.metrics
dir(sklearn.metrics)

"""# Load datasets

## Load datasets for classification
"""

# read the train and test dataset
class_train_data = pd.read_csv('https://raw.githubusercontent.com/vamsivarma/datasets/master/machine_learning/logistic_regression/train.csv')
class_test_data = pd.read_csv('https://raw.githubusercontent.com/vamsivarma/datasets/master/machine_learning/logistic_regression/test.csv')

class_train_data.head()

"""Separating the target variable (or column) which we want to predict using ML algorithms"""

# Now, we need to predict the missing target variable in the test data
# target variable - Survived

# seperate the independent and target variable on training data
class_train_x = class_train_data.drop(columns=['Survived'],axis=1)
class_train_y = class_train_data['Survived']

# seperate the independent and target variable on testing data
class_test_x = class_test_data.drop(columns=['Survived'],axis=1)
class_test_y = class_test_data['Survived']

"""## Load datasets for Regression"""

# These datasets are used for following algorithms
# Linear regression

# read the train and test dataset
reg_train_data = pd.read_csv('https://raw.githubusercontent.com/vamsivarma/datasets/master/machine_learning/linear_regression/train.csv')
reg_test_data = pd.read_csv('https://raw.githubusercontent.com/vamsivarma/datasets/master/machine_learning/linear_regression/test.csv')

reg_train_data.head()

"""Separating the target variable (or column) which we want to predict using ML algorithms"""

# Now, we need to predict the missing target variable in the test data
# target variable - Item_Outlet_Sales
# seperate the independent and target variable on training data
reg_train_x = reg_train_data.drop(columns=['Item_Outlet_Sales'],axis=1)
reg_train_y = reg_train_data['Item_Outlet_Sales']

# seperate the independent and target variable on training data
reg_test_x = reg_test_data.drop(columns=['Item_Outlet_Sales'],axis=1)
reg_test_y = reg_test_data['Item_Outlet_Sales']

reg_train_y

"""# Linear Regression"""

# importing required libraries for LR
from sklearn.linear_model import LinearRegression

model = LinearRegression()

# fit the model with the training data
model.fit(reg_train_x,reg_train_y)

# predict the target on the test dataset
reg_predict_train = model.predict(reg_train_x) 

print(reg_predict_train)

# predict the target on the testing dataset
reg_predict_test = model.predict(reg_test_x)

"""# Logistic Regression"""

import sklearn.linear_model

help(sklearn.linear_model.LogisticRegression)

# importing required libraries
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

# fit the model with the training data
model.fit(class_train_x, class_train_y)

# predict the target on the train dataset
class_predict_train = model.predict(class_train_x)

# predict the target on the test dataset
class_predict_test = model.predict(class_test_x)

"""# Classification Metrics"""

import sklearn.metrics
dir(sklearn.metrics)

"""##### Accuracy Score"""

from sklearn.metrics import accuracy_score

# For Logistic regression
accuracy_train = accuracy_score(class_train_y, class_predict_train)

# For Logistic regression
accuracy_test = accuracy_score(class_test_y, class_predict_test)

print("Accuracy for train set using Logistic regression: ", accuracy_train)
print("Accuracy for test set using Logistic regression: ", accuracy_test)

"""##### Classification report"""

from sklearn.metrics import classification_report
from sklearn.metrics import f1_score

# For Logistic regression
cr_train = classification_report(class_train_y, class_predict_train)

# For Logistic regression
cr_test = classification_report(class_test_y, class_predict_test)

print("Classification report  for train set using Logistic regression: \n", cr_train)
print("Classification report  for test set using Logistic regression: \n", cr_test)

print(f1_score(class_test_y, class_predict_test))

"""##### Confusion Matrix"""

from sklearn.metrics import confusion_matrix

# For Logistic regression
cm_train = confusion_matrix(class_train_y, class_predict_train)

# For Logistic regression
cm_test = confusion_matrix(class_test_y, class_predict_test)

print("Confusion Matrix for train set using Logistic regression: \n", cm_train)
print("Confusion Matrix for test set using Logistic regression: \n", cm_test)

'''
from sklearn import metrics
import matplotlib.pyplot as plt

disp = metrics.plot_confusion_matrix(model, class_train_x, class_train_y)
disp.figure_.suptitle("Confusion Matrix")
print("Confusion matrix:\n%s" % disp.confusion_matrix)

plt.show()
'''

"""# Regression Metrics

##### Mean Absolute Error
"""

from sklearn.metrics import mean_absolute_error

# For Linear regression
mae_train = mean_absolute_error(reg_train_y, reg_predict_train)

# For Linear regression
mae_test = mean_absolute_error(reg_test_y, reg_predict_test)

print("MAE for train set using Logistic regression: ", mae_train)
print("MAE for test set using Logistic regression: ", mae_test)

i

"""##### Mean Squared Error"""

from sklearn.metrics import mean_squared_error

# For Linear regression
mse_train = mean_squared_error(reg_train_y, reg_predict_train)

# For Linear regression
mse_test = mean_squared_error(reg_test_y, reg_predict_test)

print("RMSE for train set using Linear regression: ", mse_train)
print("RMSE for test set using Linear regression: ", mse_test)

"""##### R2 Score"""

from sklearn.metrics import r2_score

# For Linear regression
r2_train = r2_score(reg_train_y, reg_predict_train)

# For Linear regression
r2_test = r2_score(reg_test_y, reg_predict_test)

print("R2 for train set using Linear regression: ", r2_train)
print("R2 for test set using Linear regression: ", r2_test)

