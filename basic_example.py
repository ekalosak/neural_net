### Straight from https://github.com/fchollet/keras

from keras.model import Sequential
from keras.layers import Dense, Activation

# Use the sequential model to utilize a restricted class of tensor
# representations of multilayer nn's - basically if the matrix is blocked
# we don't need to keep track of all those zeros.
model = Sequential()

# Initialize the simple example network architecture
model.add(Dense(output_dim=64, input_dim=100))
model.add(Activation("relu"))
model.add(Dense(output_dim=10))
model.add(Activation("softmax"))
