# -*- coding: utf-8 -*-
"""unsupervised_machine_learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KaC9cFDcPMEQ7RP4nUEw_V3YFp-YzDmx

# **All Common Libraries Imports**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""# **All Scikit-Learn Imports**"""

from sklearn.datasets import load_wine
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA     # Dimensionality Reduction: PCA
from sklearn.cluster import KMeans        # Clustering: K-Means

# Regression metrics
from sklearn.metrics import mean_squared_error

# Classification metrics
from sklearn.metrics import accuracy_score

"""#**K-means**"""

import sklearn.cluster
dir(sklearn.cluster)

help(sklearn.cluster.KMeans)

"""#**Loading data**"""

# Now, we need to divide the training data into differernt clusters
# and predict in which cluster a particular data point belongs.

# read the train and test dataset
train_data = pd.read_csv('https://raw.githubusercontent.com/vamsivarma/datasets/master/machine_learning/kmeans/train.csv')
test_data = pd.read_csv('https://raw.githubusercontent.com/vamsivarma/datasets/master/machine_learning/kmeans/test.csv')

# shape of the dataset
print('Shape of training data :',train_data.shape)
print('Shape of testing data :',test_data.shape)

train_data.head()

test_data.head()

"""#**Clustering Model Definition**"""

'''
Create the object of the K-Means model
You can also add other parameters and test your code here
Some parameters are : n_clusters and max_iter
Documentation of sklearn KMeans: 

https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
 '''

model = KMeans()  

# fit the model with the training data
model.fit(train_data)

# Number of Clusters
print('\nDefault number of Clusters : ',model.n_clusters)

# predict the clusters on the train dataset
predict_train = model.predict(train_data)
print('\nCLusters on train data',predict_train) 

# predict the target on the test dataset
predict_test = model.predict(test_data)
print('Clusters on test data',predict_test)

# Now, we will train a model with n_cluster = 3
model_n3 = KMeans(n_clusters=3)

# fit the model with the training data
model_n3.fit(train_data)

# Number of Clusters
print('\nNumber of Clusters : ',model_n3.n_clusters)

# predict the clusters on the train dataset
predict_train_3 = model_n3.predict(train_data)
print('\nCLusters on train data',predict_train_3) 

# predict the target on the test dataset
predict_test_3 = model_n3.predict(test_data)
print('Clusters on test data',predict_test_3) 

print(predict_test_3)

"""# **Another K-Means Example from Random Data to Visualize Clusters**

# **All Globals**
"""

NPOINTSPERCLUSTER = 200

"""#**Random Data Generation**"""

# Set three centers
center_1 = np.array([0,0])
center_2 = np.array([3,4])
center_3 = np.array([6,1])

# Generate random data around the three centers
data_1 = np.random.randn(NPOINTSPERCLUSTER, 2) + center_1
data_2 = np.random.randn(NPOINTSPERCLUSTER, 2) + center_2
data_3 = np.random.randn(NPOINTSPERCLUSTER, 2) + center_3

data = np.concatenate((data_1, data_2, data_3), axis = 0)
print(data.shape)

data[0:10]

plt.scatter(data[:,0], data[:,1]);

"""#**Clustering Model Definition and Training**

**K-Means Inertia:** Sum of squared distances of samples to their closest cluster center, weighted by the sample weights if provided. Inertia measures how well a dataset was clustered by K-Means. It is calculated by measuring the distance between each data point and its centroid, squaring this distance, and summing these squares across one cluster.
"""

# define the model
model = KMeans(n_clusters = 3)
#model.labels_ = ['dogs', 'cats', 'mouses']

# fit the model on training data
model = model.fit(data)

# press tab to see available methods
#model. #press tab
print(model.cluster_centers_)
print(model.labels_)
print(model.inertia_) # sse

# compare to how data has been generated

"""#**Computing how good the cluster partition is:**

Remember SSE (Sum of Squared Error):
$$
SSE = \sum_{i=1}^N (x_i - C_{(X_i)})^2
$$
where $C_{(X_i)}$ represents the cluster centroid of $X_i$.
"""

def sse(data, clusters, centroids):
    return np.sum(np.square(np.linalg.norm(data - centroids[clusters], axis=1)))

# check inertia is our sse defined function
abs(model.inertia_ - sse(data, model.labels_, model.cluster_centers_)) < 0.01

# apply the fitted model 
# if applied to the same data, we get model.labels_
clusters_sk = model.predict(data)

all(model.labels_ == clusters_sk)

clusters_sk

"""#**Clustering Output Visualization**"""

def plot_clustering(data, clusters, include_centroids = False, centroids = None):
    
    K_ = len(set(clusters))
    
    plt.figure(figsize=(8,4))
    plt.scatter(data[:,0], data[:,1], c=clusters, cmap="plasma", linewidths=0)

    if include_centroids:
        for k in range(K_):
            plt.scatter(centroids[k,0], centroids[k, 1], s=100, marker='D', color='red')
        
    plt.show()

plot_clustering(data, clusters_sk, include_centroids = True, centroids = model.cluster_centers_)
#plot_clustering(data, clusters_sk)

"""# **PCA (Principle Component Analysis)**

For dimentionality reduction

# **Data Download for Regression and PCA**
"""

# These datasets are used for following algorithms
# Linear regression

# read the train and test dataset
reg_train_data = pd.read_csv('https://raw.githubusercontent.com/vamsivarma/datasets/master/machine_learning/linear_regression/train.csv')
reg_test_data = pd.read_csv('https://raw.githubusercontent.com/vamsivarma/datasets/master/machine_learning/linear_regression/test.csv')

# shape of the dataset
print('\nShape of regression training data :', reg_train_data.shape)
print('\nShape of regression testing data :', reg_test_data.shape)

"""#**Regression Data Preparation**"""

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

"""#**Regression Model Definition and Training**"""

print('\nTraining model with {} dimensions.'.format(reg_train_x.shape[1]))

# create object of model
model = LinearRegression()

# fit the model with the training data
model.fit(reg_train_x, reg_train_y)

# predict the target on the train dataset
predict_train = model.predict(reg_train_x)

# Accuray Score on train dataset
rmse_train = mean_squared_error(reg_train_y, predict_train)**(0.5)
print('\nRMSE on train dataset without PCA : ', rmse_train)

# predict the target on the test dataset
predict_test = model.predict(reg_test_x)

# Accuracy Score on test dataset
rmse_test = mean_squared_error(reg_test_y, predict_test)**(0.5)
print('\nRMSE on test dataset without PCA : ', rmse_test)

"""#**Dimensionality Reduction Model Definition and Training**"""

# create the object of the PCA (Principal Component Analysis) model
# reduce the dimensions of the data to 10
'''
You can also add other parameters and test your code here
Some parameters are : svd_solver, iterated_power
Documentation of sklearn PCA:

https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
'''
model_pca = PCA(n_components=10)

new_train = model_pca.fit_transform(reg_train_x)
new_test  = model_pca.fit_transform(reg_test_x)

print('\nTraining model with {} dimensions.'.format(new_train.shape[1]))

# create object of model
model_new = LinearRegression()

# fit the model with the training data
model_new.fit(new_train,reg_train_y)

# predict the target on the new train dataset
predict_train_pca = model_new.predict(new_train)

# Accuray Score on train dataset
rmse_train_pca = mean_squared_error(reg_train_y,predict_train_pca)**(0.5)
print('\nRMSE on new train dataset using PCA : ', rmse_train_pca)

# predict the target on the new test dataset
predict_test_pca = model_new.predict(new_test)

# Accuracy Score on test dataset
rmse_test_pca = mean_squared_error(reg_test_y,predict_test_pca)**(0.5)
print('\nRMSE on new test dataset using PCA : ', rmse_test_pca)

print(reg_train_x.shape)
print(reg_test_x.shape)
print(new_train.shape)
print(new_test.shape)

"""# **Another PCA to Visualize Dimensional Reduction**"""

wine = load_wine()
data = pd.DataFrame(data=wine.data, columns=wine.feature_names)

type(data)

data.shape

data.head()

"""#**Data Standardization**

**preprocessing.scale:** for better results in PCA it is better to Standardize a dataset (we can do along any axis with scikit-learn). This function center to the mean and component wise scale to unit variance.

**Standardization** of datasets is a common requirement for many machine learning estimators implemented in scikit-learn; they might behave badly if the individual features do not more or less look like standard normally distributed data: Gaussian with zero mean and unit variance.

In practice we often ignore the shape of the distribution and just transform the data to center it by removing the mean value of each feature, then scale it by dividing non-constant features by their standard deviation.

For instance, many elements used in the objective function of a learning algorithm (such as the RBF kernel of Support Vector Machines or the l1 and l2 regularizers of linear models) assume that all features are centered around zero and have variance in the same order. If a feature has a variance that is orders of magnitude larger than others, it might dominate the objective function and make the estimator unable to learn from other features correctly as expected.
"""

data_norm = preprocessing.scale(data, axis=0)

# check
print(np.mean(data_norm, axis=0))

print(np.std(data_norm, axis=0))

pca_model = PCA()
data_pca_sklearn = pca_model.fit_transform(data_norm)

print('Default number of components: {}'.format(pca_model.n_components_))
print(pca_model.explained_variance_)
print(pca_model.explained_variance_ratio_)
print(np.cumsum(pca_model.explained_variance_ratio_))

pca_model = PCA(n_components = 2)
data_pca_sklearn = pca_model.fit_transform(data_norm)

print(pca_model.explained_variance_)
print(pca_model.explained_variance_ratio_)
print(np.cumsum(pca_model.explained_variance_ratio_))

print(data_pca_sklearn)

"""#**PCA Output Visualization**"""

plt.scatter(data_pca_sklearn[:,0], data_pca_sklearn[:,1], cmap="plasma", linewidths=0);