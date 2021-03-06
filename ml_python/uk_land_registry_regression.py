# -*- coding: utf-8 -*-
"""uk_land_registry_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xgBWiRWu91VVEDKhj5k1KPG-CYjZX0wV

#**Regression Problem**

**Definition**: 

In Supervised Machine Learning there are two main tasks we can address: 

1) **Classification:** this refers to a predictive modeling problem where a class label is predicted for a given example of input data. Examples of classification problems include: Given an example, classify if it is spam or not. Given a handwritten character, classify it as one of the known characters. The outcome is always a **categorical variable. **

2) **Regression:** this is a task for searching the relationship between independent variables (or features) and a dependent variable (or outcome). It's used as a method for predictive modelling in machine learning, in which an algorithm is used to predict **continuous variables.**

#**The Task: From an Interview exercise**

The UK Government’s Land Registry Data is a Dataset with 22 million rows. In order to deal with this enormity of data I decided to apply deep learning models working on GPUs (Graphics Processing Unit). Specifically, I used a mixed neural network adopting convolutional layers and multi-layer perceptron layers with 1 single output. Output neuron has no activation, threshold or something, it is free to supply the estimated price value. 
Furthermore, it can be proven that convolutional (1D or 2D) with regularization techniques are key components in preventing overfitting and reaching better performances. Also, some techniques of regularization can be used to reduce model capacity while maintaining low loss. Hence, I adopted the following regularizations: 

**Dropout**

At each training iteration a dropout layer randomly removes some neurons in the network with a certain probability. This can be seen in a two-pronged way: a) Neurons  become more independent to the weights of the other neurons (less co-adaptivity), therefore the model is more robust in order to generalize on the test set; b) dropout can be proven being a form of averaging multiple models. The “Ensemble” of models shows better performance in most machine learning tasks. 

**Batch Normalization**

Generally, since deep neural networks adopt mini-batch training they require a long tuning of the weight initialization and learning parameters. On one side, the initialization of weights (randomly chosen) are far away from the final learned weights. On the other side, especially with deep networks,  a small perturbation in the initial layers, leads to a large change in the later layers. Batch normalization fosters the reduction of the well-known problem of "internal covariate shift" which causes huge perturbations of gradients and weights . By normalizing the data in each mini-batch, this problem is largely avoided.

**Solution**

In order to implement a fast solution to the problem within the exercise, I made use of python libraries like Keras for the model encoding, Numpy for the arrays processing, pandas for preprocessing and other minor third parts libraries. Keras was configured with TensorFlow in backend to have the fastest possible training. Chosen Neural Network’s topology has a conv layer on the first layer, a dense layer (mlp) on second stage, and a dense layer on the last stage. For every training, 100 epochs were run and instead of doing earlyStopping, i prefered to save the best model within all the epochs, every time, as I noticed there could not be a precise stopping rule for this kind of data.   

**Results**

Because of the inner poor nature of these data attributes and the restrictions from the exercise on the usable attributes (property type, lease duration, location (london – non london) it is very difficult for any predictor forecasting the right price of next purchasing of one property in Uk. Anyway I reached good results by means of this code  

**Future directions**

Future improvements might be: genetic algorithm for hyper-parameter optimization, deeper networks topologies,  integration of this model with other models (grounded on computer vision, natural language processing) able to deal with other information sources: news, sentiments, etc.

#**All Imports**
"""

'''
Created on 21/03/2022

@author: Francesco Pugliese
'''

import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    
import numpy
import os
import sys
import timeit
import platform
import argparse

# Keras imports
import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.optimizers import SGD, RMSprop

"""#**All Initializations**"""

startTime = timeit.default_timer()
OS = platform.system()   # Operating System
os.system('pip install --upgrade --no-cache-dir gdown')

"""#**All Globals**"""

default_config_file = "landregistrymodel.ini"                                         # Default Configuration File
defaultCallbacks = []

"""#**All Utility Functions Definition**"""

def data_download(file_to_download, gdrive_code, OS, uncompress = True):
  if not os.path.exists(file_to_download):
    os.system('gdown --id "'+gdrive_code+'" --output '+file_to_download)
    if OS == "Linux" and uncompress:
        os.system('unzip -o -n "./'+file_to_download+'" -d "./"')
    return True
  else: 
    return None

"""#**Dataset and all Libs download**"""

out = data_download("./pp-2020_2021.zip", "1NSiYUM1gK65cXS9eHGEdFaZ7dY9wU1bj", OS)
out = data_download("./uk_lr_regression_libs.zip", "190uP4CEAd5Tvf351S-p6iAR4mfwyxufB", OS)

"""#**All Program Imports**"""

from uk_lr_regression_libs.Models.landregistryneuralmodel import LandRegistryNeuralModel
from uk_lr_regression_libs.Preprocessing.preprocessing import LandRegistryPreoprocessing
from uk_lr_regression_libs.Settings.settings import SetParameters

"""#**All Program Functions Definition**"""

def create_model(input_dim = 1, output_size = 1, optimizer='sgd', initMode = 'normal', activation = 'relu', neurons1 = 60, neurons2 = 200):
    modelSummary = True
    
    # Build the Land Registry Model 
    neuralLandRegistryNeuralModel = LandRegistryNeuralModel.build(input_dim = input_dim, output_size = output_size, summary = modelSummary, neurons1 = neurons1, neurons2 = neurons2)  
    
    # Compile the Land Registry Model
    neuralLandRegistryNeuralModel.compile(loss="mean_squared_error", optimizer=optimizer)
    
    return neuralLandRegistryNeuralModel

"""#**Program Configuration**"""

config_file = default_config_file
if config_file is None: 
    config_file = default_config_file                                                # Default Configuration File

## Configuration of the File Parser
# Read the Configuration File
set_parameters = SetParameters("/content/uk_lr_regression_libs/Conf", config_file, OS) 

par = set_parameters.read_config_file()
# Set initial seed for reproducibility
numpy.random.seed(par.seed)

"""#**Data Preprocessing**"""

# Preprocess Land Registry Data
lrp = LandRegistryPreoprocessing(par.demoOnSubset)			 # Test the program on a smaller Dataset - True or Full Dataset - False	
datasets = lrp.loadLandRegistryData(dataPath=par.datasetPath, dataFile = par.datasetFile, fieldSeparator = par.fieldSeparator, normalizeX=par.normalizeX, normalizeY=par.normalizeY, demoOnSubset = par.demoOnSubset)

trainsetX, trainsetY = datasets[0]
testsetX, testsetY = datasets[1]
dataXMax, dataYMax = datasets[2]

trainsetX == numpy.asarray(trainsetX).astype('float32')
testsetX == numpy.asarray(testsetX).astype('float32')
trainsetY_tensor = tf.convert_to_tensor(trainsetY, dtype=tf.float32) 
testsetY_tensor = tf.convert_to_tensor(testsetY, dtype=tf.float32) 
trainsetX_tensor = tf.convert_to_tensor(trainsetX, dtype=tf.float32) 
testsetX_tensor = tf.convert_to_tensor(testsetX, dtype=tf.float32) 

# Compute the number of batches per dataset
nTrainBatches = trainsetX.shape[0] // par.batchSize
nTestBatches = testsetX.shape[0] // par.batchSize

print ('\n\nBatch size: %i\n' % par.batchSize)

print ('Number of training batches: %i' % nTrainBatches)
  
print ('\nTraining set values size (X): %i x %i' % (trainsetX.shape[0], trainsetX.shape[1]))
print ('Training set target vector size (Y): %i x 1' % trainsetY.shape[0])
print ('Sum of train set values (X): %.2f' % trainsetX.sum());
print ('Sum of train set target (Y): %i' % trainsetY.sum());

print ('Number of test batches: %i' % nTestBatches)
print ('\nTest set values size (X): %i x %i' % (testsetX.shape[0], testsetX.shape[1]))
print ('Test set target vector size (Y): %i x 1' % testsetY.shape[0])
print ('Sum of test set values (X): %.2f' % testsetX.sum());
print ('Sum of test set target (Y): %i' % testsetY.sum());

print(trainsetX[0:10])
print(type(trainsetX))
print(trainsetY[0:10])
print(testsetX[0:10])
print(testsetY[0:10])

# Training Algorithms 
#opt = SGD(lr=par.learningRate)                                 # Stochastic Gradient Descent Training Algorithm
opt = RMSprop(lr=par.learningRate)                              # Stochastic Gradient Descent Training Algorithm

# CallBacks definition 
checkPoint=ModelCheckpoint(os.path.join("./",par.modelsPath)+"/"+par.modelFile, monitor='val_loss', verbose=1, save_best_only=True, mode='min')

print ('\n')

input_dim = trainsetX.shape[1]
neuralLandRegistryNeuralModel = create_model(input_dim, par.output_size, opt, 'normal', par.activation, par.neurons1, par.neurons2)                             # Returns the model created                        
print ('\n\n')

if par.saveBestModel == True:
    defaultCallbacks = defaultCallbacks+[checkPoint]

# Fit the Land Registry Model 
history = neuralLandRegistryNeuralModel.fit(trainsetX_tensor, trainsetY_tensor, validation_split = 0.3, epochs=par.epochsNumber, batch_size=par.batchSize, shuffle = False, verbose=2)

print ('\n\nPredicting on %i properties of 2021...\n' % (par.numberOfPropertiesToTest))

predictions = neuralLandRegistryNeuralModel.predict(testsetX, batch_size = par.batchSize, verbose = 1)   # as the Batch Size might be greater than numberOfPropertiesToTest we test on the whole Test Set

if par.saveBestModel == True:
    bestNeuralLandRegistryNeuralModel = LandRegistryNeuralModel.build(input_dim = input_dim, output_size = par.output_size, summary = False, neurons1 = par.neurons1, neurons2 = par.neurons2)  
    bestNeuralLandRegistryNeuralModel.load_weights(os.path.join("./",par.modelsPath)+"/"+par.modelFile)       
    bestNeuralLandRegistryNeuralModel.compile(loss="mean_squared_error", optimizer=opt)
    bestPredictions = bestNeuralLandRegistryNeuralModel.predict(testsetX, batch_size = par.batchSize, verbose = 1)   # as the Batch Size might be greater than numberOfPropertiesToTest we test on the whole Test Set

if par.printTestModel == True: 
  logfile = open(os.path.join("./",par.logPath)+"/"+par.logFile, "w")

  numpy.set_printoptions(precision = par.logPrecision, suppress = True)
  print ("\n\n\nLast Model: Real Price and Predicted Price : \n") 
  print ("\n\n\nLast Model: Real Price and Predicted Price : \n", file = logfile) 
  
  # Denormalize outputs
  if par.normalizeY == True:
      testsetY = testsetY * dataYMax
      predictions = predictions * dataYMax
      if par.saveBestModel == True:
          bestPredictions = bestPredictions * dataYMax
  
  for i in range(par.numberOfPropertiesToTest):
      print ("%i: RT %i - PT %i" % (i, testsetY[i,], numpy.round(predictions[i,], par.logPrecision)))
      print ("%i: RT %i - PT %i" % (i, testsetY[i,], numpy.round(predictions[i,], par.logPrecision)), file = logfile)

  if par.saveBestModel == True:
      print ("\n\n\nBest Model: Real Price and Predicted Price : \n") 
      print ("\n\n\nBest Model: Real Price and Predicted Price : \n", file = logfile) 
      for i in range(par.numberOfPropertiesToTest):
          print ("%i: RT %i - PT %i" % (i, testsetY[i,], numpy.round(bestPredictions[i,], par.logPrecision)))
          print ("%i: RT %i - PT %i" % (i, testsetY[i,], numpy.round(bestPredictions[i,], par.logPrecision)), file = logfile)

  logfile.close()

endTime = timeit.default_timer()
print ('\nTotal time: %.2f minutes' % ((endTime - startTime) / 60.))



"""# **Homeworks**

0) Make this code run

1) Write the same regression code for the dataset Boston Housing Price regression of keras: 
https://keras.io/api/datasets/boston_housing/

Hint: rewrite the preprocessing function

2) Write a more complex model with Conv1D as feature extractors

3) Plot the history and predictions
"""

