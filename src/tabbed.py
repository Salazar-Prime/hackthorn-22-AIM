import emailing
import streamlit as st
import model
import PIL 
from PIL import Image
import random
import os
from os import listdir
import webbrowser
import pandas as pd
import csv   

replace_gif = False

def start_tabs():
    global replace_gif
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Image Classification", "Image Grid", "Dashboard", "Helpful Links", "CSV View", "Our Team"]) 

    with tab1:
        col11, col12 = st.columns([2,0.9],gap="small")
        with col11:
            placeholder_image = st.empty()
            if replace_gif == False:
                placeholder_image.image("../resources/hemp.jpeg")
        with col12:
            uploaded_file = st.file_uploader("Upload image")
            placeholder_prediction = st.empty()  
            email = st.text_input("Email")
            prediction = model.get_model(uploaded_file)

            if prediction is not None:
                placeholder_prediction.subheader(prediction[0])
                updateImage(placeholder_image, uploaded_file, prediction[2], prediction[1])  
                # emailing.sendEmail(email, prediction[1])   


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
        df = pd.read_csv("sofar.csv")  # read a CSV file inside the 'data" folder next to 'app.py'
        st.title("Data View")  # add a title
        st.write(df)
    with tab6:
        col51, col52, col53 = st.columns([1,1,1],gap="medium")
        with col51:
            st.image("../teamPhotos/aanis.jpeg", caption="Aanis")
            st.text("Co-Founder/CFO")
        with col52:
            st.image("../teamPhotos/aaron.jpg", caption="Aaron")
            st.text("Co-Founder/CEO")
        with col53:
            st.image("../teamPhotos/fabio.jpg", caption="Fabio")
            st.text("Co-Founder/CTO")
        col54, col55, col56 = st.columns([1,1, 1],gap="medium")
        with col54:
            st.image("../teamPhotos/sami.jpg", caption="Sami")
            st.text("Co-Founder/CCO")
        with col55:
            st.image("../teamPhotos/varun.jpeg", caption="Varun", width=210)
            st.text("Co-Founder")
    return [tab1, tab2, tab3, tab4]

def updateImage(placeholder, img, classNo, pred):
    global replace_gif
    replace_gif = True
    placeholder.image(img, use_column_width="always")
    writeImage(img, classNo, pred)

def writeImage(img, classNo, pred):
    img = PIL.Image.open(img)
    # Resize the image for tensorflow predicition
    img = img.resize((500, 500), PIL.Image.ANTIALIAS)
    imageName = random.randint(100000000,999999999)
    img.save("../collection/"+str(classNo)+"/"+str(imageName)+".jpg")
    imName = str(imageName)+".jpg"
    with open("sofar.csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow([imName,pred])



    