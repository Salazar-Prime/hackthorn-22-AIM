import cv2
import os
import numpy as np
import pickle
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models,utils
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from tensorflow.python.keras import utils
from exif import Image


# loading the feature extractor model
model = load_model('model_shrub.h5')

# Predict
def predictor(img_path): # here image is file name 
    img = load_img(img_path, target_size=(224,224))
    img = img_to_array(img)
    img = np.expand_dims(img,axis = 0)
    prediction = model.predict(img)*100
    print(prediction)
    return(prediction)
