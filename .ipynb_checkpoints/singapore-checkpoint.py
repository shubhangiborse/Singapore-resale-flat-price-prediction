# import necessary libraries
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import os
import pickle


st.set_page_config(page_title='Singapore Flat Resale Price Predictor', layout='wide',
                   initial_sidebar_state='expanded')

st.markdown("<h1 style='text-align: center; color: blue;'>Singapore Flat Resale Price Predicton</h1>",unsafe_allow_html=True)

df=pd.read_csv(r'final.csv')
df=df.drop(['Unnamed: 0'],axis=1) 

tab1,tab2,tab3=st.tabs(['HOME','PREDICTION','PREDICTION AND CONCLUSION'])