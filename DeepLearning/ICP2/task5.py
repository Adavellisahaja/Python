from keras import Sequential, Input, Model
from keras.datasets import mnist
import numpy as np
from keras.layers import Dense
from keras.utils import to_categorical
#from keras_applications.inception_resnet_v2 import models

(train_images,train_labels),(test_images, test_labels) = mnist.load_data()

print(train_images.shape[1:])
#process the data
#1. convert each image of shape 28*28 to 784 dimensional which will be fed to the network as a single feature
dimData = np.prod(train_images.shape[1:])
print(dimData)
train_data = train_images.reshape(train_images.shape[0],dimData)
test_data = test_images.reshape(test_images.shape[0],dimData)

#convert data to float and scale values between 0 and 1
train_data = train_data.astype('float')
test_data = test_data.astype('float')
#scale data
train_data /=255.0
test_data /=255.0
#change the labels frominteger to one-hot encoding. to_categorical is doing the same thing as LabelEncoder()
train_labels_one_hot = to_categorical(train_labels)
test_labels_one_hot = to_categorical(test_labels)

#creating network
visible = Input(shape=(dimData,))
hidden = Dense(dimData)(visible)
model = Model(inputs=visible, outputs=hidden)
hidden1 = Dense(512, activation='relu')(visible)
hidden2 = Dense(512, activation='relu')(hidden1)
hidden3 = Dense(512, activation='relu')(hidden2)
output = Dense(10, activation='sigmoid')(hidden3)
model = Model(inputs=visible, outputs=output)

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(train_data, train_labels_one_hot, batch_size=256, epochs=10, verbose=1,
                   validation_data=(test_data, test_labels_one_hot))
