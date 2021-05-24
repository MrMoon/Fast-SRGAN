import json
from keras.utils.data_utils import get_file
from tensorflow import keras
import numpy as np
import cv2
import os
from google.colab.patches import cv2_imshow

MODEL_NAME = 'FastSRGAN'
MODEL_URL = 'https://github.com/HasnainRaz/Fast-SRGAN/blob/master/models/generator.h5'

weights_path = get_file(MODEL_NAME , MODEL_URL)
model = keras.load_model(weights_path)
inputs = keras.Input((None , None , 3))
output = model(inputs)
model = keras.models.Model(inputs , outputs)

for image_path in image_paths:

  # Read Image
  low_res = cv2.imread(image_path , 1)

  # Convert to RGB
  low_res = cv2.cvtColor(low_res , cv2.COLOR_BGR2RGB)

  # Rescale to 0-1
  low_res = low_res/255.0

  # Get Super Resolution Image
  super_resolution = model.predict(np.expand_dims(low_res , axis=0))[0]

  # Rescale values in range 0-255
  super_resolution = (((super_resolution + 1) / 2.) * 255).astype(np.uint8)

  # Convert back to BGR for OpenCV
  super_resolution = cv2.cvtColor(super_resolution , cv2.COLOR_RGB2BGR)

  # Show Result
  cv2_imshow(super_resolution)


