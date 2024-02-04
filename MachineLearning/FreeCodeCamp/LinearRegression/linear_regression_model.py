from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib

import tensorflow.compat.v2.feature_column as fc

import tensorflow as tf

import os

import csv

# clear the console content
os.system("clear")

# Load dataset
dftrain = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv") # training data
dfeval = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/eval.csv") # testing data

# Remove 'survived' column and stored it in the new variable
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')

CAREGORICAL_COLUMNS = ['sex','n_siblings_spouses','parch','class','deck','embark_town','alone']

NUMERICAL_COLUMNS = ['age','fare']

feature_columns = []

for feature_name in CAREGORICAL_COLUMNS:
    vocabulary = dftrain[feature_name].unique() # gets a list of all unique values from given feature column
    feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary))

for feature_name in NUMERICAL_COLUMNS:
    feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))


# The training process for linear regression model

def make_input_fn(data_df, label_df, num_epochs=10, shuffle=True, batch_size=32):
    def input_function(): # inner function, this will be returned
        ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df)) # create tf.data.Dataset with data and its label
        if shuffle:
            ds = ds.shuffle(1000) # randomize order of data
        ds = ds.batch(batch_size).repeat(num_epochs) # split dataset into batches of 32 repeat the process for number of epochs
        return ds # return a batch from the dataset 
    return input_function # return a function object for use

train_input_fn = make_input_fn(dftrain, y_train) # here we will call the input function that was returned to us to get a dataset object we can feed to the model 
eval_input_fn = make_input_fn(dfeval, y_eval, num_epochs=1, shuffle=False)

# creating the model
linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns)

# Training the model
linear_est.train(train_input_fn) # train
result = linear_est.evaluate(eval_input_fn) # get model metric/stats by testing on testing data

acc = result['accuracy'] # Model overall accuracy

# making a prediction
result = list(linear_est.predict(eval_input_fn))

os.system("clear") # clear the console content

print('Model accuracy:',acc) # the result variable is simply  a dict of stats  about or model

# One example
print(dfeval.loc[20])
print('Survived:',y_eval.loc[20])
print('Probability of surviving:',result[20]['probabilities'][1]) # probability of not surviving is [0] and [1] is the probability of surviving


# Write to csv file to evaluate results
with open('test_results.csv',mode='w',newline='') as csv_file:
    csv_columns = ['probability','survived','sex','age','n_siblings_spouses','parch','fare','class','deck','embark_town','alone']
    writer = csv.DictWriter(csv_file, fieldnames=csv_columns)

    # Write the header
    writer.writeheader()

    for row in range(len(dfeval)):
        writer.writerow({'probability':result[row]['probabilities'][1]*100, 'survived':y_eval.loc[row],
                         'sex':dfeval.loc[row]['sex'], 'age':dfeval.loc[row]['age'], 'n_siblings_spouses':dfeval.loc[row]['n_siblings_spouses'],
                         'parch':dfeval.loc[row]['parch'], 'fare':dfeval.loc[row]['fare'], 'class':dfeval.loc[row]['class'],
                         'deck':dfeval.loc[row]['deck'], 'embark_town':dfeval.loc[row]['embark_town'], 'alone':dfeval.loc[row]['alone']})

