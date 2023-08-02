# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

# load data
import pickle

# sidebar for navigate

with st.sidebar:
    selected = option_menu ('Multiple Car Prediction System',
                            
                            ['Car Price Prediction',
                            'Breath Cancer Prediction'],
                            icons = ['car-front','person'],
                            default_index=0
                            )
    
   
if(selected == "Car Price Prediction") :
    
    st.title("Prediction du Prix de voitures en utilisant Le Machine Learning")
    
    st.subheader("Author : Group 1 ")
    
    col1, col2,col3,col4 = st.columns(4)
    
   
    
    with col1:
        Levy = st.number_input('Levy',key=1,min_value = 0)
    
    with col2:
        
        manufacturer = st.text_input('Manufacturer')
    
    with col3:
        
        model = st.text_input('Model')
    
    with col4:
        
        prod_year = st.date_input('Production year')
    
    with col1:
        
        category = st.text_input('Category')
    
    with col2 :
        
        leather_interior = st.selectbox('Leather_interior',('yes','no'))
    
    with col3 :
        
        fuel_type = st.text_input('Fuel type')
    
    with col4:
        
        engine_volume = st.number_input('Engine Volume',key=2,min_value = 0)
    
    with col1 :
        
        mileage = st.number_input('Mileage',key=3,min_value = 0)
    
    with col2 :
        
        cylinder = st.number_input('Cylinder',key=4,min_value = 0)
    
    with col3 :
        
        gear_box_type = st.selectbox('Gear box type',('Automatic', 'Tiptronic', 'Variator', 'Manual'))
        
    with col4:
        
        drive_wheels = st.selectbox('Drive Wheels',('4x4', 'Front', 'Rear'))
    
    with col1 :
        
        doors = st.text_input('Value of Doors')
    
    with col2 :
        
            wheel = st.text_input('Wheel')
    
    with col3 :
        
        color = st.text_input('Color')
    
    with col4 :
        
        airbags = st.number_input('Airbags',key=5,min_value = 0)
    
    with open ("car_price_prediction.pkl","rb") as file :
        price_prediction = pickle.load(file)
        
        my_price = ''
    # button of test
    
    if st.button('Car Price Test'):
        prediction =  price_prediction.predict([[Levy,manufacturer,model,prod_year,category,leather_interior,fuel_type,engine_volume,mileage,cylinder,gear_box_type,drive_wheels,doors,wheel,color,airbags]])
    
        if(prediction[0]>1 and prediction[0]<=9278.965 ):
            st.write("Moins Cher")
        elif (prediction[0]> 9278.965 and prediction[0]<=1.855593e+04):
            st.write("Moyen")
        elif (prediction[0] >1.855593e+04  and prediction[0]<=27834.895):
            st.write("Cher")
        else:
            st.write("Tres Cher")
            
    st.success(my_price)

    
if(selected == 'Breath Cancer Prediction') :
    
    st.title("Prediction du cancer de sein  en utilisant Le Machine Learning")
    


    

    
