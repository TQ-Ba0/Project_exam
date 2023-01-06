import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
st.set_page_config(
    page_title="Point"
)
#Introduction
st.title("Point range")
st.markdown( """
    On this page you can see spectrum and comments of each range point and in year by choice.
    """
)
Point = {'1':"One",'2':"Two",'3':"Three",'4':"Four",'5':"Five",'6':"Six",'7':"Seven",'8':"Eight",'9':"Nine","10":'Ten'}
# @st.cache
def load_data(year):
    path_file='diemthi'+str(year)+'.csv'
    temp = pd.read_csv(path_file)
    df = pd.DataFrame(temp)
    df.drop(df.columns[[0]], axis=1, inplace=True)
    return df.round(2)

#sidebar
st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year',list(reversed(range(2019,2021))))
select_point = st.slider(
    'Select a range of point',
    0.0, 10.0,(2.0,3.0))
st.write('Point in range:', select_point)
df = load_data(selected_year)
st.markdown("# Our Data Set")