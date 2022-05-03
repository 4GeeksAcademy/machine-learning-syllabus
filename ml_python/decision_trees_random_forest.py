# -*- coding: utf-8 -*-
"""decision_trees_random_forest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/138asSVwxeN2kOyvjR60gPpHwAoUmjxEE

# Loading common libraries
"""

import pandas as pd
import numpy as np

# Regression metrics
from sklearn.metrics import mean_squared_error

# Classification metrics
from sklearn.metrics import accuracy_score

"""# Load datasets

## Load datasets for classification
"""

# read the train and test dataset
class_train_data = pd.read_csv('https://raw.githubusercontent.com/vamsivarma/datasets/master/machine_learning/logistic_regression/train.csv')
class_test_data = pd.read_csv('https://raw.githubusercontent.com/vamsivarma/datasets/master/machine_learning/logistic_regression/test.csv')

# shape of the dataset
print('Shape of classification training data :', class_train_data.shape)
print('Shape of classification testing data :', class_test_data.shape)

"""Separating the target variable (or column) which we want to predict using ML algorithms"""

# Now, we need to predict the missing target variable in the test data
# target variable - Survived

# seperate the independent and target variable on training data
class_train_x = class_train_data.drop(columns=['Survived'],axis=1)
class_train_y = class_train_data['Survived']

# seperate the independent and target variable on testing data
class_test_x = class_test_data.drop(columns=['Survived'],axis=1)
class_test_y = class_test_data['Survived']

class_train = pd.DataFrame(columns=['Train'])
class_train['Train'] = class_train_y

class_test = pd.DataFrame(columns=['Test'])
class_test['Test'] = class_test_y

"""## Load datasets for Regression"""

# These datasets are used for following algorithms
# Linear regression

# read the train and test dataset
reg_train_data = pd.read_csv('https://raw.githubusercontent.com/vamsivarma/datasets/master/machine_learning/linear_regression/train.csv')
reg_test_data = pd.read_csv('https://raw.githubusercontent.com/vamsivarma/datasets/master/machine_learning/linear_regression/test.csv')

# shape of the dataset
print('\nShape of regression training data :', reg_train_data.shape)
print('\nShape of regression testing data :', reg_test_data.shape)

"""Separating the target variable (or column) which we want to predict using ML algorithms"""

# Now, we need to predict the missing target variable in the test data
# target variable - Item_Outlet_Sales
# seperate the independent and target variable on training data
reg_train_x = reg_train_data.drop(columns=['Item_Outlet_Sales'], axis=1)
reg_train_y = reg_train_data['Item_Outlet_Sales']

# seperate the independent and target variable on training data
reg_test_x = reg_test_data.drop(columns=['Item_Outlet_Sales'], axis=1)
reg_test_y = reg_test_data['Item_Outlet_Sales']

reg_train = pd.DataFrame(columns=['Train'])
reg_train['Train'] = reg_train_y

reg_test = pd.DataFrame(columns=['Test'])
reg_test['Test'] = reg_test_y

## Data frames for saving prediction of different algorithms
col_list = ['DT', 'RF']

# Classification predictions for train and test set
class_train_pred = pd.DataFrame(columns = col_list)
class_test_pred = pd.DataFrame(columns = col_list)

# Regression predictions for train and test set
reg_train_pred = pd.DataFrame(columns = col_list)
reg_test_pred = pd.DataFrame(columns = col_list)

"""# Decision Tree"""

import sklearn.tree
dir(sklearn.tree)

"""### Classification"""

# importing required libraries
from sklearn.tree import DecisionTreeClassifier

'''
Create the object of the Decision Tree model
You can also add other parameters and test your code here
Some parameters are : max_depth and max_features
Documentation of sklearn DecisionTreeClassifier: 

https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
'''
model = DecisionTreeClassifier()

#print(model)

# fit the model with the training data
model.fit(class_train_x, class_train_y)

#print(dir(model))

# depth of the decision tree
print('Depth of the Decision Tree :', model.tree_.max_depth)

# predict the target on the train dataset
predict_train = model.predict(class_train_x)

# Save predictions
class_train_pred['DT'] = predict_train

# Accuray Score on train dataset
accuracy_train = accuracy_score(class_train_y, predict_train)
print('\nAccuracy for Decision tree on train dataset : ', accuracy_train)

# predict the target on the test dataset
predict_test = model.predict(class_test_x)

# Save predictions
class_test_pred['DT'] = predict_test

# Accuracy Score on test dataset
accuracy_test = accuracy_score(class_test_y, predict_test)
print('\nAccuracy for Decision tree on test dataset : ', accuracy_test)

"""## Regression"""

# importing required libraries
from sklearn.tree import DecisionTreeRegressor

'''
Create the object of the Decision Tree model
You can also add other parameters and test your code here
Some parameters are : max_depth and max_features
Documentation of sklearn DecisionTreeClassifier: 

https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
'''
model = DecisionTreeRegressor()

# fit the model with the training data
model.fit(reg_train_x, reg_train_y)

#print(dir(model))

# depth of the decision tree
print('Depth of the Decision Tree :', model.tree_.max_depth)

# fit the model with the training data
model.fit(reg_train_x, reg_train_y)

# predict the target on the test dataset
predict_train = model.predict(reg_train_x)

# Save predictions
reg_train_pred['DT'] = predict_train

# Root Mean Squared Error on training dataset
rmse_train = mean_squared_error(reg_train_y, predict_train)**(0.5)
print('\nRMSE for Decision tree on train dataset : ', rmse_train)

# predict the target on the testing dataset
predict_test = model.predict(reg_test_x)

# Save predictions
reg_test_pred['DT'] = predict_test

# Root Mean Squared Error on testing dataset
rmse_test = mean_squared_error(reg_test_y, predict_test)**(0.5)
print('\nRMSE for Decision tree on test dataset : ', rmse_test)

"""# Random Forest"""

import sklearn.ensemble
dir(sklearn.ensemble)

help(sklearn.ensemble.RandomForestClassifier)

"""### Classification"""

# importing required libraries
from sklearn.ensemble import RandomForestClassifier

'''
Create the object of the Random Forest model
You can also add other parameters and test your code here
Some parameters are : n_estimators and max_depth
Documentation of sklearn RandomForestClassifier: 

https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
'''

model = RandomForestClassifier()

# fit the model with the training data
model.fit(class_train_x, class_train_y)

# number of trees used
print('Number of Trees used : ', model.n_estimators)

# predict the target on the train dataset
predict_train = model.predict(class_train_x)
#print('\nTarget on train data',predict_train) 

# Save predictions
class_train_pred['RF'] = predict_train

# Accuray Score on train dataset
accuracy_train = accuracy_score(class_train_y, predict_train)
print('\nAccuracy for Random forest on train dataset : ', accuracy_train)

# predict the target on the test dataset
predict_test = model.predict(class_test_x)
#print('\nTarget on test data',predict_test) 

# Save predictions
class_test_pred['RF'] = predict_test

# Accuracy Score on test dataset
accuracy_test = accuracy_score(class_test_y, predict_test)
print('\nAccuracy for Random forest on test dataset : ', accuracy_test)

"""### Regression"""

# importing required libraries
from sklearn.ensemble import RandomForestRegressor

'''
Create the object of the Random Forest model
You can also add other parameters and test your code here
Some parameters are : n_estimators and max_depth
Documentation of sklearn RandomForestRegressor: 

https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html
'''

model = RandomForestRegressor()  

# fit the model with the training data
model.fit(reg_train_x, reg_train_y)

# Number of Neighbors used to predict the target
print('\nNumber of Trees used : ',model.n_estimators)

# predict the target on the train dataset
predict_train = model.predict(reg_train_x)
#print('\nTarget on train data',predict_train) 

# Save predictions
reg_train_pred['RF'] = predict_train


# Root Mean Squared Error on training dataset
rmse_train = mean_squared_error(reg_train_y, predict_train)**(0.5)
print('\nRMSE for Random Forest on train dataset : ', rmse_train)

# predict the target on the testing dataset
predict_test = model.predict(reg_test_x)

# Save predictions
reg_test_pred['RF'] = predict_test

# Root Mean Squared Error on testing dataset
rmse_test = mean_squared_error(reg_test_y, predict_test)**(0.5)
print('\nRMSE for Random Forest on test dataset : ', rmse_test)

class_train_pred.head()

class_test_pred.head()

reg_train_pred.head()

reg_test_pred.head()

# Save original data
class_train.to_csv('class_train.csv', sep='\t', index=False)

class_test.to_csv('class_test.csv', sep='\t', index=False)

reg_train.to_csv('reg_train.csv', sep='\t', index=False)

reg_test.to_csv('reg_test.csv', sep='\t', index=False)

#Export predictions to csv, delimit by tab

class_train_pred.to_csv('class_train_pred.csv', sep='\t', index=False)

class_test_pred.to_csv('class_test_pred.csv', sep='\t', index=False)

reg_train_pred.to_csv('reg_train_pred.csv', sep='\t', index=False)

reg_test_pred.to_csv('reg_test_pred.csv', sep='\t', index=False)