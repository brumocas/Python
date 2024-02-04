# Imports

import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
keras = tf.keras

# Load the dataset
import tensorflow_datasets as tdfs
tdfs.disable_progress_bar()

# split the data manually into 80% training, 10% testing, 10% validation
(raw_train, raw_validation, raw_test), metadata = tdfs.load(
    'cats_vs_dogs' ,
    split=['train[:80%]', 'train[80%:90%]', 'train[90%:]'],
    with_info=True,
    as_supervised=True,
)

get_label_name = metadata.features['label'].int2str # creates a function object that we can use to get labels


# display 2 images from the dataset 
for image, label in raw_train.take(2):
    plt.figure(1)
    plt.imshow(image)
    plt.title(get_label_name(label))   
    #plt.show()


# Data processing 
# because images dont have the same resolution/size

IMG_SIZE = 160 # All images will be resized 160x160

def format_example(image, label):
    """
    returns an image that is reshaped to IMG_SIZE
    """
    image = tf.cast(image, tf.float32)
    image = (image/127.5) - 1
    image = tf.image.resize(image, (IMG_SIZE, IMG_SIZE))
    return image, label

# Now we apply this function to all images using map
train = raw_train.map(format_example)
validation = raw_validation.map(format_example)
test = raw_test.map(format_example)

# display 2 images from the dataset 
for image, label in train.take(2):
    plt.figure(1)
    plt.imshow(image)
    plt.title(get_label_name(label))   
    plt.show()
    
# Lets look at the original shape
for img, label in raw_train.take(2):
    print("Original shape:",img.shape)

# Lets look at the new shape
for img, label in train.take(2):
    print("New shape:",img.shape)




    