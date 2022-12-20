import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
st.set_page_config(
    page_title="Subject"
)

img =Image.open('images/Subject.png')
st.image(img,use_column_width=True)
st.sidebar.header('User Input  Features')
st.title("Subject")
selected_year=st.sidebar.selectbox('Year',list(reversed(range(2019,2021))))
st.markdown( """
    On this page you can see the statistics of each subject and each year by choice
    """
)
@st.cache
def load_data(year):
    path_file='diemthi'+str(year)+'.csv'
    temp=pd.read_csv(path_file)
    df=pd.DataFrame(temp)
    df.drop(df.columns[[0]], axis=1, inplace=True)
    return df
select=load_data(selected_year)
sort_columns=np.array(select.columns)
select_subject=st.sidebar.multiselect('Subject',sort_columns ,sort_columns)
st.write('Data Dimension:' +str(select.shape[0]) + ' row and ' + str(select.shape[1]) + ' columns')
df_exam=select[select_subject]
st.markdown("## Display Data type of DataFrame")

st.dataframe(df_exam)

# st.dataframe(select)