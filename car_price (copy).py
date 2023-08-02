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
    
    col0,col1, col2,col3,col4 = st.columns(5)
    
    with col0:
        Price = st.number_input('Price',key=0)
    
    
    with col1:
        Levy = st.number_input('Levy',key=1)
    
    with col2:
        
        manufacturer = st.text_input('Manufacturer')
    
    with col3:
        
        model = st.text_input('Model')
    
    with col4:
        
        prod_year = st.number_input('Production year',key=6)
    
    with col0:
        
        category = st.text_input('Category')
    
    with col1 :
        
        leather_interior = st.text_input('Leather_interior')
    
    with col2 :
        
        fuel_type = st.text_input('Fuel type')
    
    with col3:
        
        engine_volume = st.number_input('Engine Volume',key=2)
    
    with col4 :
        
        mileage = st.number_input('Mileage',key=3)
    
    with col0 :
        
        cylinder = st.number_input('Cylinder',key=4)
    
    with col1 :
        
        gear_box_type = st.text_input('Gear box type')
        
    with col2:
        
        drive_wheels = st.text_input('Drive Wheels')
    
    with col3 :
        
        doors = st.text_input('Value of Doors')
    
    with col4 :
        
            wheel = st.text_input('Wheel')
    
    with col0 :
        
        color = st.text_input('Color')
    
    with col1 :
        
        airbags = st.number_input('Airbags',key=5)
    
    with open ("car_price_prediction.pkl","rb") as file :
        price_prediction = pickle.load(file)
        
        my_price = ''
    # button of test
    
    if st.button('Car Price Test'):
        prediction =  price_prediction.predict([[Price,Levy,manufacturer,model,prod_year,category,leather_interior,fuel_type,engine_volume,mileage,cylinder,gear_box_type,drive_wheels,doors,wheel,color,airbags]])
    
        if(prediction[0]>1 and prediction[0]<=9278.965 ):
            print("Moins Cher")
        elif (prediction[0]> 9278.965 and prediction[0]<=1.855593e+04):
            print("Moyen")
        elif (prediction[0] >1.855593e+04  and prediction[0]<=27834.895):
            print("Cher")
        else:
            print("Tres Cher")
            
    st.success(my_price)

    
if(selected == 'Breath Cancer Prediction') :
    
    st.title("Prediction du cancer de sein  en utilisant Le Machine Learning")
    


    

    
