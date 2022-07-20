import streamlit.components.v1 as components

#importing all the helper fxn from helper.py which we will create later
import streamlit as st
import os
import matplotlib.pyplot as plt
import seaborn as sns

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

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import os
import glob
from skimage import io
from matplotlib import pyplot as plt
import numpy as np

from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage import img_as_ubyte, img_as_float
from scipy import ndimage as nd

sns.set_theme(style="darkgrid")
sns.set()

from PIL import Image, ImageDraw
from exif import Image
import exif
import pydeck as pdk
import PIL 

from streamlit_folium import st_folium
from streamlit_folium import folium_static
import folium
import smtplib


######### START ################
import tabbed

# Title
st.title('Drought Classifier')

# add tabs
tabs = tabbed.start_tabs()