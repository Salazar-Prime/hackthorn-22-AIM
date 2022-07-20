import streamlit as st
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models,utils
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from tensorflow.python.keras import utils
import PIL 
from PIL import Image, ImageDraw
import numpy as np

model_path="../model_shrub.h5"


def get_model(uploaded_file):
    # text over upload button "Upload Image"
    if uploaded_file is not None:
        model = load_model(model_path)
        display_image = PIL.Image.open(uploaded_file)

            # # Resize the image for tensorflow predicition
        display_image = display_image.resize((224, 224), PIL.Image.ANTIALIAS)
        img_tensor = tf.keras.preprocessing.image.img_to_array(display_image)
        img_tensor = np.expand_dims(img_tensor, axis=0)
        img_tensor /= 255.
        prediction = model.predict(img_tensor)

        print(prediction)

        if prediction[0][0]>prediction[0][1]:
            predictionFunny = "Poor guy needs some water"
            prediction = "Drought"            
            classNo = 0
        else: 
            predictionFunny = "Healty fella"
            prediction = "Healthy"
            classNo = 1

        
        return [predictionFunny, prediction, classNo]