import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

import os

os.system("clear")

fashion_mnist = keras.datasets.fashion_mnist # load dataset 

(train_images, train_labels),(test_images, test_labels) = fashion_mnist.load_data() # split into testing and training

# print(train_images.shape) # 60000 images of resolution 28x28 pixels, total of 784 pixels in an image

# print(train_images[0][23][23]) # lets have a look to one pixel

# print(train_images[0:]) # lets have a look to one image

# print(train_labels[0:10]) # lets have a look to the first 10 training labels

 
class_names = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']

# plot some images examples
#plt.figure()
#plt.imshow(train_images[1])
#plt.colorbar()
#plt.grid(False)
#plt.show()

# Data Processing / Normalize the data
train_images = train_images / 255.0
test_images = test_images / 255.0
 
# Building the model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)), # input layer (1)
    keras.layers.Dense(128, activation='relu'), # hidden layer (2)
    keras.layers.Dense(10, activation='softmax') # output layer (3) 10 is the number of class to predict
])

# Compile the model 
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Training and testing the model 
model.fit(train_images, train_labels, epochs=1)

# Evaluate the model 
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=1)
print('Test accuracy:', test_acc) # Example of overfitting, memorises the training data


# Making predictions
"""
image_index = 100
predictions = model.predict(test_images)
print(class_names[np.argmax(predictions[image_index])])

# plot to confirm the prediction
plt.figure()
plt.imshow(test_images[image_index])
plt.colorbar()
plt.grid(False)
plt.show()
"""

COLOR = 'white'
plt.rcParams['text.color'] = COLOR
plt.rcParams['axes.labelcolor'] = COLOR

def predict(model, image, correct_label):
    class_names = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']
    prediction = model.predict(np.array([image]))
    predicted_class = class_names[np.argmax(prediction)]
    
    show_image(image, class_names[correct_label], predicted_class)
    
def show_image(img, label, guess):
    plt.figure()
    plt.imshow(img, cmap=plt.cm.binary)
    print("Expected "+ label)
    print("Guess: "+ guess)
    plt.colorbar()
    plt.grid(False)
    plt.show()
    
def get_number():
    while True:
        num = input("Pick a number: ")
        if num.isdigit():
            num = int(num)
            if 0 <= num <= 10000:
                return int(num)
        else:
            print("Try again...")
            
            
num = get_number()
image = test_images[num]
label = test_labels[num]
predict(model, image, label)








