import tensorflow as tf

from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

import os

os.system("clear")

# LOAD AND SLPIT DATASET
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# NORMALIZE PIXEL VALUES TO BE BETWEEN 0 AND 1
train_images, test_images = train_images / 255.0, test_images / 255.0

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# Lets look at one image
IMG_INDEX = 80

#plt.imshow(train_images[IMG_INDEX], cmap=plt.cm.binary)
#plt.xlabel(class_names[train_labels[IMG_INDEX][0]])
#plt.show()

# CNN architecture
model = models.Sequential()
model.add(layers.Conv2D(32, (3,3), activation = 'relu', input_shape = (32, 32, 3)))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64, (3,3), activation = 'relu'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64, (3,3), activation = 'relu'))
#model.summary() # let's have a look at our model so far

# Adding Dense Layers
model.add(layers.Flatten())
model.add(layers.Dense(64, activation = 'relu'))
model.add(layers.Dense(10)) # amount of classes for this problem

model.summary() # let's have a look at our model so far

# Training model

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs = 1,
                    validation_data=(test_images, test_labels))

# Evaluating the model
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose = 2)
print(test_acc)
