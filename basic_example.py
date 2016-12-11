### Straight from https://github.com/fchollet/keras
# with some additional notes and visualization subroutines

# Imports
print("importing packages")
from keras.models import Sequential
from keras.layers import Dense, Activation
import keras.utils.visualize_util as keras_vis

# Use the sequential model to utilize a restricted class of tensor
# representations of multilayer nn's - basically if the matrix is blocked
# we don't need to keep track of all those zeros.
model = Sequential()

# Initialize the simple example network architecture
# By the restrictions of the sequential model, each layer takes input only from
# the previous and pipes output only to the next layer.
# This particular sequential model has 100 input nodes fully connected (Dense)
# to 64 hidden nodes and 10 output nodes.
print("initializing sequential model")
model.add(
        Dense(
            output_dim = 64,
            input_dim = 100
    ))
model.add(
        Activation("relu")
    )
model.add(
        Dense(
            output_dim = 10
    ))
model.add(
        Activation("softmax")
    )

# Visualize the model before we compile it
print("plotting basic model outline")
keras_vis.plot(model, to_file='basic_dot_model.png')

# Compile net
print("compiling the net")
model.compile(
        loss='categorical_crossentropy',
        optimizer='sgd',
        metrics=['accuracy']
    )

# TODO load the MNIST dataset and train the net and visualize
