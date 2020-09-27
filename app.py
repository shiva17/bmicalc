# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 23:16:56 2020

@author: Shivam Kolhe
Project Title: BMI Web App
"""

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image


# Title
html_code = """
        <div style="background-color: #1abc9c; padding:  10px; border-radius: 10px">
          <h1 style="color:white; text-align: center">BMI Calculator</h1>
        </div>
        """
components.html(html_code)


# Set a flag
h_mode = 0


# BMI Image
img = Image.open("bmi.jpg")
st.image(img, width=700)


# Weight in kgs
weight = st.number_input("Enter your weight ...")

# Height
status = st.radio("Select height measurement: ", ('cms', 'meters', 'feet'))
if (status == 'cms'):
    h_mode = 0
    height = st.number_input("centimeters")
    
elif (status == 'meters'):
    h_mode = 1
    height = st.number_input("meters")
    
else:
    h_mode = 2
    height = st.number_input("feet")
    

# Calculate BMI
if(st.button('Calculate BMI')):
    if(h_mode == 0):
        # 1 meter = 100 cms
        bmi = weight / ((height/100) ** 2)
    elif(h_mode == 1):
        bmi = weight / (height ** 2)
    else:
        # 1 meter = 3.28084 feet
        bmi = weight / ((height/3.28084) ** 2)

    bmi = round(bmi, 2)
    
    st.info('Your Body Mass Index is: {}'.format(bmi))
    
    # -----------------------------------------------------------------
    if (bmi < 16):
        st.error("You are Extremely Underweight")
    
    elif (bmi >= 16 and bmi < 18.5):
        st.warning("You are underweight")
    
    elif (bmi >= 18.5 and bmi < 25):
        st.success("You are Healthy")
        st.balloons()
    
    elif (bmi >= 25 and bmi < 30):
        st.warning("You are Overweight")
    
    elif (bmi >=30):
        st.error("You are Extremely Overweight")
    # -----------------------------------------------------------------