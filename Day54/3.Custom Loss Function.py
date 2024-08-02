#Implement a custom loss function in TensorFlow/Keras. 
#Explain the purpose of the loss function and provide an example scenario where it would be useful.

#importing libraries
import tensorflow as tf
from tensorflow.keras.losses import Loss
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# custom loss function
class AsymmetricLoss(Loss):
    def __init__(self, overestimate_penalty=2.0):
        super().__init__()
        self.overestimate_penalty = overestimate_penalty
    
    def call(self, y_true, y_pred):
        error = y_pred - y_true
        loss = tf.where(error > 0, self.overestimate_penalty * tf.square(error), tf.square(error))
        return tf.reduce_mean(loss)

# Creating regression model
model = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),  
    Dense(1) 
])

# Compiling the model with the custom loss function
model.compile(optimizer='adam', loss=AsymmetricLoss())

# sample data for demonstration
import numpy as np
x_train = np.random.rand(100, 10)
y_train = np.random.rand(100, 1)

# Train the model
model.fit(x_train, y_train, epochs=10)
