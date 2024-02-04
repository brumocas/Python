# Imports

import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
keras = tf.keras

# Picking a pre-tained model 

IMG_SIZE = 160
IMG_SHAPE = (IMG_SIZE, IMG_SIZE, 3)

# Create the base model from the pre-trained model MobileNet V2
base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE,
                                               include_top=False, # Dont include the classifiers 
                                               weights='imagenet')

os.system("clear")



# Freezing base (This the base of our model, we dont want to change it)

# Dont train the base model
base_model.trainable = False
print(base_model.summary())

# Adding our classifier
global_average_layer = keras.layers.GlobalAveragePooling2D()
prediction_layer = keras.layers.Dense(1)

# Combine layers 
model = tf.keras.Sequential([
    base_model,
    global_average_layer,
    prediction_layer
    ])

print(model.summary())

# Training the model
base_learning_rate = 0.0001
model.compile(optimizer=tf.keras.optimizers.RMSprop(lr=base_learning_rate),
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])

# We can evaluate the model right now to see how it does before training it ono our images 
initial_epochs = 3
validation_steps = 30

loss0, accuracy0 = model.evaluate(validation_batches, steps = validation_steps)
