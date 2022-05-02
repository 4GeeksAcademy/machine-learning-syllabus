# -*- coding: utf-8 -*-
"""Data_preprocessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rzoUtgJDD0INoS6p-ikWJweSor8Y1P3d

### Loading The Data
"""

# Data manipulation using Numpy and Pandas
import numpy as np 
import pandas as pd

# Data visualization using Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

titanic = pd.read_csv("https://raw.githubusercontent.com/vamsivarma/datasets/master/data_science/pandas/titanic.csv")
covid19 = pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv")
covid19.columns

#X = np.random.random((10,5)) 
#y = np.array(['M','M','F','F','M','F','M','M','F','F','F'])

covid19.head()

titanic.head()

"""### Data Preprocessing

#### Encoding Categorical Features

Now, let us encode all the categorical values in to numerical values for our ML algorithm

Pandas allows for a quick conversion from categorical to numeric columns with its get_dummies method. After this step, we have a clean dataset with strictly numerical columns that we can feed into machine learning models.
"""

titanic = pd.get_dummies(titanic, columns=['pclass', 'sex', 'embarked', 'embark_town', 'class', 'who', 'adult_male', 'alive', 'alone', 'deck'], drop_first=True)

titanic.info()

"""#### As we can observe the columnn age has null values, lets see approaches we can take to handle these null values

### Visualizing null values
"""

sns.heatmap(titanic.isnull()) 
plt.show()

sns.heatmap(covid19.isnull()) 
plt.show()

"""### FILL NAN values in dataset """

# Method 1 - replace null values with 0
# df.fillna(0, inplace=True)

# Method 2 - drop rows with null values
# df.dropna(inplace=True)

# Method 3 - replace null values with the mean of field
#titanic['age'].fillna(titanic['age'].mean(), inplace=True)


# Method 4 - Use predictive filling
# Reference: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html
titanic['age'].interpolate(method='linear', 
                           limit_direction='forward', 
                           axis=0, inplace=True)

"""drop_first = True gets rid of collinearity in the predictor matrix"""

#titanic['age']
titanic.head()

sns.pairplot(covid19)
plt.show()

from sklearn.preprocessing import LabelEncoder
enc = LabelEncoder()
y = enc.fit_transform(y)

"""### Spilling the dataset in to train and test datasets"""

from sklearn.model_selection import train_test_split
X = titanic.drop('survived', axis=1)
y = titanic['survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#print(X_train)

import sklearn
dir(sklearn.preprocessing)

"""#### Standardization"""

X_train

from sklearn.preprocessing import StandardScaler 

scaler = StandardScaler().fit(X_train) 
standardized_X = scaler.transform(X_train) 
standardized_X_test = scaler.transform(X_test)

print(standardized_X.shape)
print(standardized_X.max())
print(standardized_X.min())
print(standardized_X.mean())
print(standardized_X.std())

print(standardized_X_test.shape)
print(standardized_X_test.max())
print(standardized_X_test.min())
print(standardized_X_test.mean())
print(standardized_X_test.std())

dir(np.ndarray)

"""#### Normalization"""

from sklearn.preprocessing import Normalizer 
scaler = Normalizer().fit(X_train) 
normalized_X = scaler.transform(X_train) 
normalized_X_test = scaler.transform(X_test)

print(normalized_X.shape)
print(normalized_X.max())
print(normalized_X.min())
print(normalized_X.mean())
print(normalized_X.std())

print(normalized_X_test.shape)
print(normalized_X_test.max())
print(normalized_X_test.min())
print(normalized_X_test.mean())
print(normalized_X_test.std())

"""#### Binarization"""

from sklearn.preprocessing import Binarizer 

binarizer = Binarizer(threshold=0.0).fit(X) 
binary_X = binarizer.transform(X)

binary_X

"""#### Imputing missing values"""

from sklearn.preprocessing import Imputer
imp = Imputer(missing_values=0, strategy='mean', axis=0)
imp.fit_transform(X_train)

"""#### Generating Polynomial Features

Polynomial features are those features created by raising existing features to an exponent. For example, if a dataset had one input feature X, then a polynomial feature would be the addition of a new feature (column) where values were calculated by squaring the values in X, e.g. X^2. This process can be repeated for each input variable in the dataset, creating a transformed version of each. As such, polynomial features are a type of feature engineering, e.g. the creation of new input features based on the existing features. The “degree” of the polynomial is used to control the number of features added, e.g. a degree of 3 will add two new variables for each input variable. Typically a small degree is used such as 2 or 3. Generally speaking, it is unusual to use d greater than 3 or 4 because for large values of d, the polynomial curve can become overly flexible and can take on some very strange shapes. Linear regression is linear in the model parameters and adding polynomial terms to the model can be an effective way of allowing the model to identify nonlinear patterns. Polynomial regression extends the linear model by adding extra predictors, obtained by raising each of the original predictors to a power. For example, a cubic regression uses three variables, X, X2, and X3, as predictors. This approach provides a simple way to provide a non-linear fit to data.
"""

from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(2)
poly.fit_transform(X)

"""Running the example first reports the raw data with two features (columns) and each feature has the same value, either 2 or 3.

#### Lets see the preprocessed dataset
"""

X_train

X_test

y_train

y_test

"""#### Saving the preprocessed data using pandas"""

X_train.to_csv('data/train.csv', index=False)
X_test.to_csv('data/test.csv', index=False)

y_train.to_csv('data/train_target.csv', index=False)
y_test.to_csv('data/test_target.csv', index=False)

