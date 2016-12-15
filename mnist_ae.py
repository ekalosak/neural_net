### Author: Eric Kalosa-Kenyon
### Date: Dec 14, 2016
# using code from https://github.com/fchollet/keras
# Autoencoder for MNIST data

# Imports
print("importing packages")
from keras.models import Sequential
from keras.layers import Dense, Activation
import keras.utils.visualize_util as keras_vis
from mnist import MNIST
import pdb
import numpy as np
from matplotlib import pyplot as plt

# Configure script
print("configuring script")
EXMNISTIMG = './example_mnist.png'
MNISTDATA = '/Users/eric/Projects/neural_net/python-mnist/data'
GRAPHOUT = './basic_dot_model.png'

# Use the sequential model to utilize a restricted class of tensor
# representations of multilayer nn's - basically if the matrix is blocked
# we don't need to keep track of all those zeros.
model = Sequential()

# Initialize the simple example network architecture
# By the restrictions of the sequential model, each layer takes input only from
# the previous and pipes output only to the next layer.
# This particular sequential model has 784 input nodes fully connected (Dense)
# to 64 hidden nodes and 10 output nodes.
print("initializing sequential model")
model.add(Dense(output_dim = 100, input_dim = 784))
model.add(Activation("relu"))
model.add(Dense(output_dim = 64))
model.add(Activation("relu"))
model.add(Dense(output_dim = 10))
model.add(Activation("softmax"))

# Visualize the model before we compile it
print("plotting basic model outline to {}".format(GRAPHOUT))
keras_vis.plot(model, to_file = GRAPHOUT)

# Compile net
print("compiling the net")
model.compile(
        loss='categorical_crossentropy',
        optimizer='sgd',
        metrics=['accuracy']
    )

# Load the MNIST dataset
print("loading MNIST data")
mndata = MNIST(MNISTDATA)
mndata.load_training()
mndata.load_testing()
print("MNIST data loaded")
# type(mndata.train_images[0]) is 'list' with len = 784 = 28*28
# np.array(mndata.train_images[0]).reshape([28, 28])

# Write a training image to disk so we can see it
print("writing ex training image to {}".format(EXMNISTIMG))
fig = plt.figure()
imgplot = plt.imshow(np.array(mndata.train_images[0]).reshape([28, 28]))
imgplot.set_cmap('gray')
plt.savefig(EXMNISTIMG)

# Train autoencoder to store all 10 digits.
# Note that this is a prior on the network architecture - we know we need 10
# deep nodes.
