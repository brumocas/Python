import tensorflow as tf

from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

import os

os.system("clear")

# LOAD AND SLPIT DATASET
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# NORMALIZE PIXEL VALUES TO BE BETWEEN 0 AND 1
train_images, test_images = train_images / 255.0, test_images / 255.0


# Working with small datasets 
# When we have a small amout of training data we can increase it by rotating/scalling the images from the set

# Getting from 1 one image 4 different ones /Image Augmentation

from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

# creates a data generator object that transforms images
datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# pick an image to transform
test_img = train_images[10]
img = image.img_to_array(test_img) # convert image to numpy array
# print(img.shape)
img = img.reshape((1,) + img.shape) # reshape image
# print(img.shape)

i = 0

for batch in datagen.flow(img, save_prefix='test', save_format='jpeg'): # this loop runs forever until we break, saving images to current directory
    plt.figure(1)
    plot = plt.imshow(image.img_to_array(batch[0]))
    i += 1
    plt.show()
    if i > 4:
        break



