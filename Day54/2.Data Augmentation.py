#Implement data augmentation on a given image dataset using Keras. 
# Show at least three different augmentation techniques and explain how they help improve model performance.

#Importing necessary libraries
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import numpy as np

# Initialize the ImageDataGenerator with augmentation techniques
datagen = ImageDataGenerator(
    rotation_range=40,       
    zoom_range=0.2,          
    horizontal_flip=True,    
    rescale=1./255           
)

# Load a sample image
def load_sample_image(image_path):
    from tensorflow.keras.preprocessing.image import load_img, img_to_array
    img = load_img(image_path, target_size=(150, 150))  # Adjust target size as needed
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)  # Add batch dimension
    return x

# Image path 
image_path = 'test\Yellow_rust010.jpg'

# Loading the image
x = load_sample_image(image_path)

# Create an iterator
aug_iter = datagen.flow(x, batch_size=1)

# Plot augmented images
plt.figure(figsize=(10, 10))

for i in range(9):
    plt.subplot(3, 3, i+1)
    batch = next(aug_iter)
    image = batch[0]  
    plt.imshow(image)
    plt.axis('off')

plt.show()
