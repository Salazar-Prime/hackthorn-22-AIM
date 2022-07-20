import emailing
import streamlit as st
import model
import PIL 
from PIL import Image
import random
import os
from os import listdir
import webbrowser

replace_gif = False

def start_tabs():
    global replace_gif
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Image Classification", "Image Grid", "Dashboard", "Helpful Links", "Our Team"])

    with tab1:
        col11, col12 = st.columns([2,0.9],gap="small")
        with col11:
            placeholder_image = st.empty()
            if replace_gif == False:
                placeholder_image.image("../resources/hemp.gif")
        with col12:
            uploaded_file = st.file_uploader("Upload image")
            placeholder_prediction = st.empty()  
            email = st.text_input("Email")
            prediction = model.get_model(uploaded_file)

            if prediction is not None:
                placeholder_prediction.subheader(prediction[1])
                updateImage(placeholder_image, uploaded_file, prediction[2])  
                emailing.sendEmail(email, prediction[0])   


    with tab2:
        col21, col22 = st.columns([2, 2],gap="small")
        with col21:
            st.header("Class 0 - Drought")
            for im in os.listdir("../collection/0"):
                img = PIL.Image.open("../collection/0/"+im)
                img = img.resize((500, 500), PIL.Image.ANTIALIAS)
                st.image(img)
        with col22:
            st.header("Class 1 - Healthy")
            for im in os.listdir("../collection/1"):
                img = PIL.Image.open("../collection/1/"+im)
                img = img.resize((500, 500), PIL.Image.ANTIALIAS)
                st.image(img)

    with tab3:
        st.header("Dashboard")
        url_gra = "http://ibts-compute.ecn.purdue.edu:3000/d/uxmtKcgVk/asabe_hack?orgId=1"
        st.components.v1.iframe(url_gra, width=None, height=1000, scrolling=True)

    
    with tab4:
        url = 'https://www.streamlit.io/'
        if st.button('Streamlit'):
            webbrowser.open_new_tab(url)

        url = "https://agr.wa.gov/departments/pesticides-and-fertilizers/fertilizers/product-database"
        if st.button('Fertilizer Database'):
            webbrowser.open_new_tab(url)
        url = "https://droughtmonitor.unl.edu/"
        if st.button('Drought Monitor'):
            webbrowser.open_new_tab(url)

        url = "https://weather.com/"
        if st.button('Weather'):
            webbrowser.open_new_tab(url)

    with tab5:
        col51, col52, col53 = st.columns([1,1,1],gap="medium")
        with col51:
            st.image("../teamPhotos/varun.jpeg", caption="Aanis")
            st.text("Likes to Eat Sleep and Repeat")
        with col52:
            st.image("../teamPhotos/varun.jpeg", caption="Aaron")
            st.text("Likes to Eat Sleep and Repeat")
        with col53:
            st.image("../teamPhotos/varun.jpeg", caption="Fabio")
            st.text("Likes to Eat Sleep and Repeat")
        col54, col55, col56 = st.columns([1,1, 1],gap="medium")
        with col54:
            st.image("../teamPhotos/varun.jpeg", caption="Sami")
            st.text("Likes to Eat Sleep and Repeat")
        with col55:
            st.image("../teamPhotos/varun.jpeg", caption="Varun")
            st.text("Likes to Eat Sleep and Repeat")
    return [tab1, tab2, tab3, tab4]

def updateImage(placeholder, img, classNo):
    global replace_gif
    replace_gif = True
    placeholder.image(img, use_column_width="always")
    writeImage(img, classNo)

def writeImage(img, classNo):
    img = PIL.Image.open(img)
    # Resize the image for tensorflow predicition
    img = img.resize((500, 500), PIL.Image.ANTIALIAS)
    imageName = random.randint(100000000,999999999)
    img.save("../collection/"+str(classNo)+"/"+str(imageName)+".jpg")


    