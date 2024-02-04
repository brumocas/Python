from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf

import pandas as pd 

import os

CSV_COLUMN_NAMES = ['SepalLenght','SepalWidth','PetalLenght','PetalWidth','Species']
SPECIES = ['Setosa','Versicolor','Virginica']

train_path = "https://storage.googleapis.com/download.tensorflow.org/data/iris_training.csv"
test_path = "https://storage.googleapis.com/download.tensorflow.org/data/iris_test.csv"

train_path = tf.keras.utils.get_file("iris_training.csv",train_path)
test_path = tf.keras.utils.get_file("iris_test.csv",test_path)

os.system('clear')

train = pd.read_csv(train_path, names = CSV_COLUMN_NAMES, header=0)
test = pd.read_csv(test_path, names = CSV_COLUMN_NAMES, header=0)
# Here we use keras (a module inside TenserFlow) to grab our datasets and read them into a pandas DataFrame

y_train = train.pop('Species')
y_test = test.pop('Species')

print(train.head())
print(y_train.head())
print('Shape:',train.shape)


def input_fn(features, labels, training=True, batch_size=256):
    # Convert the inputs to a Dataset
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))
    
    # Shuffle and repeat it you are in a training model
    if training:
        dataset = dataset.shuffle(1000).repeat()
    
    return dataset.batch(batch_size)

my_feature_columns = []

for key in train.keys():
    my_feature_columns.append(tf.feature_column.numeric_column(key=key))

# Building the model 

# Build a DNN with 2 hidden layers with 30 and 10 hidden nodes each
classifier = tf.estimator.DNNClassifier(
    feature_columns=my_feature_columns,
    # Two hidden layers of 30 and 10 respetively
    hidden_units=[30,10],
    # The model must choose between 3 classes
    n_classes=3)

# Training the model 

classifier.train(input_fn=lambda: input_fn(train, y_train, training =True), steps=5000)

eval_result = classifier.evaluate(input_fn=lambda: input_fn(test, y_test, training =False)) 

os.system("clear")

print('Test set accuracy :{accuracy:0.3f}'.format(**eval_result))

# Making a prediction
def input_fn_p(features, batch_size=256):
    # Convert the inputs to a Dataset without labels
    dataset = tf.data.Dataset.from_tensor_slices(features)
    return dataset.batch(batch_size)

features = ['SepalLenght','SepalWidth','PetalLenght','PetalWidth']
predict = {}

print("Please type numeric values as prompted.")
for feature in features:
    valid = True
    while valid:
        val = input(feature + ": ")
        if not val.isdigit(): valid = False
    
    predict[feature] = [float(val)]

predictions = classifier.predict(input_fn=lambda: input_fn_p(predict))
for pred_dict in predictions:
    print(pred_dict)
    class_id = pred_dict['class_ids'][0]
    probability = pred_dict['probabilities'][class_id]
    
    print('Predictions is "{}" ({:.1f}%)'.format(SPECIES[class_id], 100 * probability))
    
# Here is some example input and expected classes you can try above
expected = ['Setosa','Versicolor','Verginica']
predict_x = {
    'SepalLenght':[5.1, 5.9, 6.9],  
    'SepalWidth' :[3.3, 3.0, 3.1],
    'PetalLenght':[1.7, 4.2, 5.4],
    'PetalWidth' :[0.5, 1.5, 2.1]
}
