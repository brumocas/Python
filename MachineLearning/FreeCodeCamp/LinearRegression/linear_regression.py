from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib

import tensorflow.compat.v2.feature_column as fc

import tensorflow as tf

import os

# clear the console content
os.system("clear")


# Load dataset
dftrain = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv") # training data
dfeval = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/eval.csv") # testing data

# Prints the first 5 values from the dataframe
print(dftrain.head())

# Remove 'survived' column and stored it in the new variable
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')
print(y_train.head())

# Acessec specific row 
print(dftrain.loc[0], y_train.loc[0])

# Stats about the csv file
print(dftrain.describe())

# Look at the shape
print()
print(dftrain.shape)

# Making graphs from the file

dftrain.age.hist(bins = 20)
plt.show()

dftrain.sex.value_counts().plot(kind = 'barh')
plt.show()

dftrain['class'].value_counts().plot(kind = 'barh')
plt.show()

pd.concat([dftrain, y_train], axis = 1).groupby('sex').survived.mean().plot(kind='barh').set_xlabel('% survive')
plt.show()
